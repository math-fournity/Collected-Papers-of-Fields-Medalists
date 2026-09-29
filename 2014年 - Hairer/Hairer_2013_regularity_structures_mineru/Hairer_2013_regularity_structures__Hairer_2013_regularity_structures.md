# A theory of regularity structures

February 18, 2014

## M. Hairer

Mathematics Department, University of Warwick

Email: M.Hairer@Warwick.ac.uk

## Abstract

We introduce a new notion of “regularity structure” that provides an algebraic framework allowing to describe functions and / or distributions via a kind of “jet” or local Taylor expansion around each point. The main novel idea is to replace the classical polynomial model which is suitable for describing smooth functions by arbitrary models that are purpose-built for the problem at hand. In particular, this allows to describe the local behaviour not only of functions but also of large classes of distributions.

We then build a calculus allowing to perform the various operations (multiplication, composition with smooth functions, integration against singular kernels) necessary to formulate fixed point equations for a very large class of semilinear PDEs driven by some very singular (typically random) input. This allows, for the first time, to give a mathematically rigorous meaning to many interesting stochastic PDEs arising in physics. The theory comes with convergence results that allow to interpret the solutions obtained in this way as limits of classical solutions to regularised problems, possibly modified by the addition of diverging counterterms. These counterterms arise naturally through the action of a “renormalisation group” which is defined canonically in terms of the regularity structure associated to the given class of PDEs.

Our theory also allows to easily recover many existing results on singular stochastic PDEs (KPZ equation, stochastic quantisation equations, Burgers-type equations) and to understand them as particular instances of a unified framework. One surprising insight is that in all of these instances local solutions are actually “smooth” in the sense that they can be approximated locally to arbitrarily high degree as linear combinations of a fixed family of random functions / distributions that play the role of “polynomials” in the theory.

As an example of a novel application, we solve the long-standing problem of building a natural Markov process that is symmetric with respect to the (finite volume) measure describing the$\Phi _ { 3 } ^ { \bar { 4 } }$Euclidean quantum field theory. It is natural to conjecture that the Markov process built in this way describes the Glauber dynamic of 3-dimensional ferromagnets near their critical temperature.

Keywords: Stochastic PDEs, Renormalisation, Wick products, quantum field theory MSC class: 60H15, 81S20, 82C28

## Contents

1 Introduction 3
1.1 Some examples of interesting stochastic PDEs ..... 5
1.2 On regularity structures ..... 7

1.3 Main results: abstract theory . 8   
1.4 On renormalisation procedures . 11   
1.5 Main results: applications . 12   
1.6 Alternative theories . 15   
1.7 Notations . 18   
2 Abstract regularity structures 18   
2.1 Basic properties of regularity structures . 21   
2.2 The polynomial regularity structure . 21   
2.3 Models for regularity structures . 25   
2.4 Automorphisms of regularity structures . 28   
3 Modelled distributions 29   
3.1 Elements of wavelet analysis . 33   
3.2 A convergence criterion in $\mathcal{C}_s^\alpha$ . 35   
3.3 The reconstruction theorem for distributions . 39   
3.4 The reconstruction theorem for functions . 43   
3.5 Consequences of the reconstruction theorem . 44   
3.6 Symmetries . 46   
4 Multiplication 48   
4.1 Classical multiplication . 54   
4.2 Composition with smooth functions . 55   
4.3 Relation to Hopf algebras . 57   
4.4 Rough paths . 59   
5 Integration against singular kernels 62   
5.1 Proof of the extension theorem . 69   
5.2 Multi-level Schauder estimate . 77   
5.3 The symmetric case . 82   
5.4 Differentiation . 83   
6 Singular modelled distributions 84   
6.1 Reconstruction theorem . 88   
6.2 Multiplication . 91   
6.3 Composition with smooth functions . 93   
6.4 Differentiation . 95   
6.5 Integration against singular kernels . 95   
7 Solutions to semilinear (S)PDEs 98   
7.1 Short-time behaviour of convolution kernels . 99   
7.2 The effect of the initial condition . 103   
7.3 A general fixed point map . 106   
8 Regularity structures for semilinear (S)PDEs 111   
8.1 General algebraic structure . 114   
8.2 Realisations of the general algebraic structure . 125   
8.3 Renormalisation group associated to the general algebraic structure . 128   
9 Two concrete renormalisation procedures 136   
9.1 Renormalisation group for (PAMg) . 136   
9.2 Renormalisation group for the dynamical $\Phi_3^4$ model . 137   
9.3 Renormalised equations for (PAMg) . 138   
9.4 Solution theory for the dynamical $\Phi_3^4$ model . 142

10 Homogeneous Gaussian models 147  
10.1 Wiener chaos decomposition ..... 148  
10.2 Gaussian models for regularity structures ..... 150  
10.3 Functions with prescribed singularities ..... 154  
10.4 Wick renormalisation and the continuous parabolic Anderson model ..... 159  
10.5 The dynamical $\Phi_3^4$ model ..... 165  
A A generalised Taylor formula 172  
B Symbolic index 174

## 1 Introduction

The purpose of this article is to develop a general theory allowing to formulate, solve and analyse solutions to semilinear stochastic partial differential equations of the type

$$
\mathcal {L} u = F (u, \xi),\tag{1.1}
$$

where$\mathcal { L }$is a (typically parabolic but possibly elliptic) differential operator,$\xi$is a (typically very irregular) random input, and$F$is some nonlinearity. The nonlinearity$F$ does not necessarily need to be local, and it is also allowed to depend on some partial derivatives of$u ,$as long as these are of strictly lower order than${ \mathcal { L } } .$One example of random input that is of particular interest in many situations arising from the large-scale behaviour of some physical microscopic model is that of white noise (either space-time or just in space), but let us stress immediately that Gaussianity is not essential to the theory, although it simplifies certain arguments. Furthermore, we will assume that$F$ depends on$\xi$in an affine way, although this could in principle be relaxed to some polynomial dependencies.

Our main assumption will be that the equation described by (1.1) is locally subcritical (see Assumption 8.3 below). Roughly speaking, this means that if one rescales (1.1) in a way that keeps both$\mathcal { L } u$and$\xi$invariant then, at small scales, all nonlinear terms formally disappear. A “na¨ıve” approach to such a problem is to consider a sequence of regularised problems given by

$$
\mathcal {L} u _ {\varepsilon} = F (u _ {\varepsilon}, \xi_ {\varepsilon}),\tag{1.2}
$$

where$\xi _ { \varepsilon }$is some smoothened version of$\boldsymbol { \xi }$(obtained for example by convolution with a smooth mollifier), and to show that$u _ { \varepsilon }$converges to some limit u which is independent of the choice of mollifier.

This approach does in general fail, even under the assumption of local subcriticality. Indeed, consider the KPZ equation on the line [KPZ86], which is the stochastic PDE formally given by

$$
\partial_ {t} h = \partial_ {x} ^ {2} h + (\partial_ {x} h) ^ {2} + \xi ,\tag{1.3}
$$

where$\xi$denotes space-time white noise. This is indeed of the form (1.1) with${ \mathcal { L } } =$ $\partial _ { t } - \partial _ { x } ^ { 2 }$and$F ( h , \xi ) = ( \partial _ { x } h ) ^ { 2 } + \xi$and it is precisely this kind of problem that we have in mind. Furthermore, if we zoom into the small scales by writing$h ( x , t ) =$ $\delta ^ { - 1 / 2 } h ( \delta x , \delta ^ { 2 } t )$and$\tilde { \xi } ( x , t ) = \delta ^ { 3 / 2 } \xi ( \delta x , \delta ^ { 2 } t )$for some small parameter$\delta ,$then we have that on the one hand$\xi$equals$\xi$in distribution, and on the other hand$\tilde { h }$solves

$$
\partial_ {t} \tilde {h} = \partial_ {x} ^ {2} \tilde {h} + \delta^ {1 / 2} (\partial_ {x} \tilde {h}) ^ {2} + \tilde {\xi}.
$$

As$\delta  0$(which corresponds to probing solutions at very small scales), we see that, at least at a formal level, the nonlinearity vanishes and we simply recover the stochastic heat equation. This shows that the KPZ equation is indeed locally subcritical in dimension 1. On the other hand, if we simply replace$\xi$by$\xi _ { \varepsilon }$in (1.3) and try to take the limit $\varepsilon  0 .$, solutions diverge due to the ill-posedness of the term$( \partial _ { x } h ) ^ { 2 }$

However, in this case, it is possible to devise a suitable renormalisation procedure [BG97, Hai13], which essentially amounts to subtracting a very large constant to the right hand side of a regularised version of (1.3). This then ensures that the corresponding sequence of solutions converges to a finite limit. The purpose of this article is to build a general framework that goes far beyond the example of the KPZ equation and allows to provide a robust notion of solution to a very large class of locally subcritical stochastic PDEs that are classically ill-posed.

Remark 1.1 In the language of quantum field theory (QFT), equations that are subcritical in the way just described give rise to “superrenormalisable” theories. One major difference between the results presented in this article and most of the literature on quantum field theory is that the approach explored here is truly non-perturbative and therefore allows one to deal also with some non-polynomial equations like (PAMg) or (KPZ) below. We furthermore consider parabolic problems, where we need to deal with the problem of initial conditions and local (rather than global) solutions. Nevertheless, the mathematical analysis of QFT was one of the main inspirations in the development of the techniques and notations presented in Sections 8 and 10.

Conceptually, the approach developed in this article for formulating and solving problems of the type (1.1) consists of three steps.

1. In an algebraic step, one first builds a “regularity structure”, which is sufficiently rich to be able to describe the fixed point problem associated to (1.1). Essentially, a regularity structure is a vector space that allows to describe the coefficients in a kind of “Taylor expansion” of the solution around any point in space-time. The twist is that the “model” for the Taylor expansion does not only consist of polynomials, but can in general contain other functions and / or distributions built from multilinear expressions involving ξ.

2. In an analytical step, one solves the fixed point problem formulated in the algebraic step. This allows to build an “abstract” solution map to (1.1). In a way, this is a closure procedure: the abstract solution map essentially describes all “reasonable” limits that can be obtained when solving (1.1) for sequences of regular driving noises that converge to something very rough.

3. In a final probabilistic step, one builds a “model” corresponding to the Gaussian process ξ we are really interested in. In this step, one typically has to choose a renormalisation procedure allowing to make sense of finitely many products of distributions that have no classical meaning. Although there is some freedom involved, there usually is a canonical model, which is “almost unique” in the sense that it is naturally parametrized by elements in some finite-dimensional Lie group, which has an interpretation as a “renormalisation group” for (1.1).

We will see that there is a very general theory that allows to build a “black box”, which performs the first two steps for a very large class of stochastic PDEs. For the last step, we do not have a completely general theory at the moment, but we have a general methodology, as well as a general toolbox, which seem to be very useful in practice.

## 1.1 Some examples of interesting stochastic PDEs

Some examples of physically relevant equations that in principle fall into the category of problems amenable to analysis via the techniques developed in this article include:

The stochastic quantisation of$\Phi ^ { 4 }$quantum field theory in dimension 3. This formally corresponds to the equation

$$
\partial_ {t} \Phi = \Delta \Phi - \Phi^ {3} + \xi ,\tag{\((\Phi^{4})\}
$$

where$\xi$denotes space-time white noise and the spatial variable takes values in the 3-dimensional torus, see [PW81]. Formally, the invariant measure of$( \Phi ^ { 4 } )$(or rather a suitably renormalised version of it) is the measure on Schwartz distributions associated to Bosonic Euclidean quantum field theory in 3 space-time dimensions. The construction of this measure was one of the major achievements of the programme of constructive quantum field theory, see the articles [Gli68, EO71, GJ73, FO76, Fel74], as well as the monograph [GJ87] and the references therein.

In two spatial dimensions, this problem was previously treated in [AR91, DPD03]. It has also been argued more recently in [ALZ06] that even though it is formally symmetric, the 3-dimensional version of this model is not amenable to analysis via Dirichlet forms. In dimension$^ { 4 , }$the model$( \Phi ^ { 4 } )$becomes critical and one does not expect to be able to give it any non-trivial (i.e. non-Gaussian in this case) meaning as a random field for$d \geq 4 ,$, see for example [Fr¨o82, Aiz82, KE83].

Another reason why$( \Phi ^ { 4 } )$is a very interesting equation to consider is that it is related to the behaviour of the 3D Ising model under Glauber dynamic near its critical temperature. For example, it was shown in [BPRS93] that the one-dimensional version of this equation describes the Glauber dynamic of an Ising chain with a Kac-type interaction at criticality. In [GLP99], it is argued that the same should hold true in higher dimensions and an argument is given that relates the renormalisation procedure required to make sense of$( \Phi ^ { 4 } )$to the precise choice of length scale as a function of the distance from criticality.

The continuous parabolic Anderson model

$$
\partial_ {t} u = \Delta u + \xi u,\tag{PAM}
$$

where$\xi$denotes spatial white noise that is constant in time. For smooth noise, this problem has been treated extensively in [CM94]. While the problem with ξ given by spatial white noise is well-posed in dimension 1 (and a good approximation theory exists, see [IPP08]), it becomes ill-posed already in dimension 2. One does however expect this problem to be renormalisable with the help of the techniques presented here in spatial dimensions 2 and 3. Again, dimension 4 is critical and one does not expect any continuous version of the model for$d \geq 4$

KPZ-type equations of the form

$$
\partial_ {t} h = \partial_ {x} ^ {2} h + g _ {1} (h) (\partial_ {x} h) ^ {2} + g _ {2} (h) \partial_ {x} h + g _ {3} (h) + g _ {4} (h) \xi ,\tag{KPZ}
$$

where$\xi$denotes space-time white noise and the$g _ { i }$are smooth functions. While the classical KPZ equation can be made sense of via the Cole-Hopf transform [Col51, Hop50, BG97], this trick fails in the more general situation given above or in the case of a system of coupled KPZ equations, which arises naturally in the study of chains of nonlinearly interacting oscillators [BGJ13].

A more robust concept of solution for the KPZ equation where$g _ { 4 } = g _ { 1 } = 1$and $g _ { 2 } = g _ { 3 } = 0$, as well as for a number of other equations belonging to the class (KPZ) was given recently in the series of articles [Hai12, Hai11, HW13, Hai13], using ideas from the theory of rough paths that eventually lead to the development of the theory presented here. The more general class of equations (KPZ) is of particular interest since it is formally invariant under changes of coordinates and would therefore be a good candidate for describing a natural “free evolution” for loops on a manifold, which generalises the stochastic heat equation. See [Fun92] for a previous attempt in this direction and [BGJ12] for some closely related work.

The Navier-Stokes equations with very singular forcing

$$
\partial_ {t} v = \Delta v - P (v \cdot \nabla) v + \xi ,\tag{SNS}
$$

where$P$is Leray’s projection onto the space of divergence-free vector fields. If we take$\xi$to have the regularity of space-time white noise, (SNS) is already classically ill-posed in dimension 2, although one can circumvent this problem, see [AC90, DPD02, AF04]. However, it turns out that the actual critical dimension is 4 again, so that we can hope to make sense of (SNS) in a suitably renormalised sense in dimension 3 and construct local solutions there.

One common feature of all of these problems is that they involve products between terms that are too irregular for such a product to make sense as a continuous bilinear form defined on some suitable function space. Indeed, denoting by$\mathcal { C ^ { \alpha } }$for$\alpha < 0$the Besov space$B _ { \infty , \infty } ^ { \alpha } ,$it is well-known that, for non-integer values of α and$\beta ,$the map $( u , v ) \mapsto u v$is well defined from$\mathcal { C } ^ { \alpha } \times \mathcal { C } ^ { \beta }$into some space of Schwartz distributions if and only if$\alpha + \beta > 0$(see for example [BCD11]), which is quite easily seen to be violated in all of these examples.

In the case of second-order parabolic equations, it is straightforward to verify (see also Section 6 below) that, for fixed time, the solutions to the linear equation

$$
\partial_ {t} X = \Delta X + \xi ,
$$

belong to$\mathcal { C ^ { \alpha } }$for$\begin{array} { r } { \alpha < 1 - \frac { d } { 2 } } \end{array}$when$\xi$is space-time white noise and$\begin{array} { r } { \alpha < 2 - \frac { d } { 2 } } \end{array}$when $\xi$is purely spatial white noise. As a consequence, one expects Φ to take values in$\mathcal { C ^ { \alpha } }$ with α$< - 1 / 2$, so that$\Phi ^ { 3 }$is ill-defined. In the case of (PAM), one expects u to take values in$\mathcal { C ^ { \alpha } }$with$\alpha < 2 - d / 2$, so that the product$u \xi$is well-posed only for$d < 2 .$. As in the case of$( \Phi ^ { 4 } )$, dimension 2 is “borderline” with the appearance of logarithmic divergencies, while dimension 3 sees the appearance of algebraic divergencies and logarithmic subdivergencies. Note also that, since$\xi$is white noise in space, there is no theory of stochastic integration available to make sense of the product$u \xi ,$, unlike in the case when$\xi$is space-time white noise. (See however [GIP12] for a very recent article solving this particular problem in dimension 2.) Finally, one expects the function h in (KPZ) to take values in$\mathcal { C ^ { \alpha } }$for$\alpha < \frac { 1 } { 2 }$, so that all the terms appearing in (KPZ) are ill-posed, except for the term involving$g _ { 3 }$

Historically, such situations have been dealt with by replacing the products in question by their Wick ordering with respect to the Gaussian structure given by the solution to the linear problem$\mathcal { L } u = \xi ,$, see for example [JLM85, AR91, DPD02, DPD03, DPDT07] and references therein. In many of the problems mentioned above, such a technique is bound to fail due to the presence of additional subdivergencies. Furthermore, we would like to be able to consider terms like$g _ { 1 } ( h ) ( \partial _ { x } h ) ^ { 2 }$in (KPZ) where g<sub>1</sub> is an arbitrary smooth function, so that it is not clear at all what a Wick ordering would mean. Over the past few years, it has transpired that the theory of controlled rough paths [Lyo98, Gub04, Gub10] could be used in certain situations to provide a meaning to the ill-posed nonlinearities arising in a class of Burgers-type equations [HV11, Hai11, HW13, HMW12], as well as in the KPZ equation [Hai13]. That theory however is intrinsically a one-dimensional theory, which is why it has so far only been successfully applied to stochastic evolution equations with one spatial dimension.

In general, the theory of rough paths and its variants do however allow to deal with processes taking values in an infinite-dimensional space. It has therefore been applied successfully to stochastic PDEs driven by signals that are very rough in time (i.e. rougher than white noise), but at the expense of requiring additional spatial regularity [GT10, CFO11, Tei11].

One very recent attempt to use related ideas in higher dimensions was made in [GIP12] by using a novel theory of “controlled distributions”. With the help of this theory, which relies heavily on the use of Bony’s paraproduct, the authors can treat for example (PAM) (as well as some nonlinear variant thereof) in dimension$d = 2$. The present article can be viewed as a far-reaching generalisation of related ideas, in a way which will become clearer in Section 2 below.

## 1.2 On regularity structures

The main idea developed in the present work is that of describing the “regularity” of a function or distribution in a way that is adapted to the problem at hand. Traditionally, the regularity of a function is measured by its proximity to polynomials. Indeed, we say that a function u :$\mathbf R ^ { d } \to \mathbf R$is of class$\mathcal { C ^ { \alpha } }$with$\alpha > 0 \mathrm { i f } .$, for every point$\boldsymbol { x } \in \mathbf { R } ^ { d }$, it is possible to find a polynomial$P _ { x }$such that

$$
\left| f (y) - P _ {x} (y) \right| \lesssim | x - y | ^ {\alpha}.
$$

What is so special about polynomials? For one, they have very nice algebraic properties: products of polynomials are again polynomials, and so are their translates and derivatives. Furthermore, a monomial is a homogeneous function: it behaves at the origin in a self-similar way under rescalings. The latter property however does rely on the choice of a base point: the polynomial$y \mapsto ( y - x ) ^ { k }$is homogeneous of degree k when viewed around x, but it is made up from a sum of monomials with different homogeneities when viewed around the origin.

In all of the examples considered in the previous subsection, solutions are expected to be extremely irregular (at least in the classical sense!), so that polynomials alone are a very poor model for trying to describe them. However, because of local subcriticality, one expects the solutions to look at smallest scales like solutions to the corresponding linear problems, so we are in situations where it might be possible to make a good “guess” for a much more adequate model allowing to describe the small-scale structure of solutions.

Remark 1.2 In the particular case of functions of one variable, this point of view has been advocated by Gubinelli in [Gub04, Gub10] (and to some extent by Davie in [Dav08]) as a way of interpreting Lyons’s theory of rough paths. (See also [LQ02, LCL07, FV10b] for some recent monographs surveying that theory.) That theory does however rely very strongly on the notion of “increments” which is very onedimensional in nature and forces one to work with functions, rather than general distributions. In a more subtle way, it also relies on the fact that one-dimensional integration can be viewed as convolution with the Heaviside function, which is locally constant away from 0, another typically one-dimensional feature.

This line of reasoning is the motivation behind the introduction of the main novel abstract structure proposed in this work, which is that of a “regularity structure”. The precise definition will be given in Definition 2.1 below, but the basic idea is to fix a finite family of functions (or distributions!) that will play the role of polynomials. Typically, this family contains all polynomials, but it may contain more than that. A simple way of formalising this is that one fixes some abstract vector space$T$where each basis vector represents one of these distributions. A “Taylor expansion$" ( \mathrm { o r } \ \mathrm { " } \mathrm { j e t } ^ { \ \prime \ } )$is then described by an element$a \in T$which, via some “model” Π :$T  S ^ { \prime } ( { \bf R } ^ { d } )$, one can interpret as determining some distribution Πa$\mathbf { \eta } _ { \mathbf { \eta } ^ { \prime } } \in \mathcal { S } ^ { \prime } ( \mathbf { R } ^ { d } )$. In the case of polynomials, $T$would be the space of abstract polynomials in d commuting indeterminates and Π would be the map that realises such an abstract polynomial as an actual function on$\mathbf { R } ^ { d }$

As in the case of polynomials, different distributions have different homogeneities (but these can now be arbitrary real numbers!), so we have a splitting of$T$into “homogeneous subspace$\because T _ { \alpha }$. Again, as in the case of polynomials, the homogeneity of an element a describes the behaviour of Πa around some base point, say the origin 0. Since we want to be able to place this base point at an arbitrary location we also postulate that one has a family of invertible linear maps$F _ { x } \colon T  T$such that if$a \in T _ { \alpha }$ then$\Pi F _ { x } a$exhibits behaviour “of order$\alpha ^ { \prime \prime }$(this will be made precise below in the case of distribution) near the point x. In this sense, the map$\Pi _ { x } = \Pi \circ F _ { x }$plays the role of the “polynomials based at$x '$, while the map$\Gamma _ { x y } = F _ { x } ^ { - 1 } \circ F _ { y }$plays the role of a “translation operator” that allows to rewrite a “jet based at$y '$into a “jet based at$x '$

We will endow the space of all models (Π, F) as above with a topology that enforces the correct behaviour of$\Pi _ { x }$near each point$x ,$and furthermore enforces some natural notion of regularity of the map$x \mapsto F _ { x }$. The important remark is that although this turns the space of models into a complete metric space, it does not turn it into a linear (Banach) space! It is the intrinsic nonlinearity of this space which allows to encode the subtle cancellations that one needs to be able to keep track of in order to treat the examples mentioned in Section 1.1. Note that the algebraic structure arising in the theory of rough paths (truncated tensor algebra, together with its group-like elements) can be viewed as one particular example of an abstract regularity structure. The space of rough paths with prescribed H¨older regularity is then precisely the corresponding space of models. See Section 4.4 for a more detailed description of this correspondence.

## 1.3 Main results: abstract theory

Let us now expose some of the main abstract results obtained in this article. Unfortunately, since the precise set-up requires a number of rather lengthy definitions, we cannot give precise statements here. However, we would like to provide the reader with a flavour of the theory and refer to the main text for more details.

One of the main novel definitions consists in spaces$\mathcal { D } ^ { \gamma }$and$\mathcal { D } _ { \alpha } ^ { \gamma }$(see Definition 3.1 and Remark 3.5 below) which are the equivalent in our framework to the usual spaces $\mathcal { C } ^ { \gamma }$. They are given in terms of a “local Taylor expansion of order$\gamma ^ { \ast }$at every point, together with suitable regularity assumption. Here, the index$\gamma$measures the order of the expansion, while the index α (if present) denotes the lowest homogeneity of the different terms appearing in the expansion. In the case of regular Taylor expansions, the term with the lowest homogeneity is always the constant term, so one has$\alpha = 0$ However, since we allow elements of negative homogeneity, one can have$\alpha \leq 0$ in general. Unlike the case of regular Taylor expansions where the first term always consists of the value of the function itself, we are here in a situation where, due to the fact that our “model” might contain elements that are distributions, it is not clear at all whether these “jets” can actually be patched together to represent an actual distribution. The reconstruction theorem, Theorem 3.10 below, states that this is always the case as soon as$\gamma > 0$. Loosely speaking, it states the following, where we again write$\mathcal { C ^ { \alpha } }$for the Besov space$B _ { \infty , \infty } ^ { \alpha }$. (Note that with this notation$\mathcal { C } ^ { 0 }$really denotes the space$L ^ { \infty }$ $\mathcal { C } ^ { 1 }$the space of Lipschitz continuous functions, etc. This is consistent with the usual notation for non-integer values of α.)

Theorem 1.3 (Reconstruction) For every$\gamma > 0$and$\alpha \leq 0 ,$, there exists a unique continuous linear map$\mathcal { R } \colon \mathcal { D } _ { \alpha } ^ { \gamma }  \mathcal { C } ^ { \alpha } ( \mathbf { R } ^ { d } )$with the property that, in a neighbourhood of size ε around any x$\mathbf { \Psi } : \in \mathbf { R } ^ { d } , \mathcal { R } f$is approximated by$\Pi _ { x } f ( x )$, the jet described by f(x), up to an error oforder$\varepsilon ^ { \gamma }$

The reconstruction theorem shows that elements$f \in \mathcal { D } ^ { \gamma }$uniquely describe distributions that are modelled locally on the distributions described by$\Pi _ { x } f ( x )$. We therefore call such an element$f \mathrm { ~ a ~ } ^ { \ast }$“modelled distribution”. At this stage, the theory is purely descriptive: given a model of a regularity structure, it allows to describe a large class of functions and$/ \mathrm { o r }$distributions that “locally look like” linear combinations of the elements in the model. We now argue that it is possible to construct a whole calculus that makes the theory operational, and in particular sufficiently rich to allow to formulate and solve large classes of semilinear PDEs.

One of the most important and non-trivial operations required for this is multiplication. Indeed, one of the much lamented drawbacks of the classical theory of Schwartz distributions is that there is no canonical way of multiplying them [Sch54]. As a matter of fact, it is in general not even possible to multiply a distribution with a continuous function, unless the said function has sufficient regularity.

The way we use here to circumvent this problem is to postulate the values of the products between elements of our model. If the regularity structure is sufficiently large to also contain all of these products (or at least sufficiently many of them in a sense to be made precise), then one can simply perform a pointwise multiplication of the jets of two modelled distributions at each point. Our main result in this respect is that, under some very natural structural assumptions, such a product is again a modelled distribution. The following is a loose statement of this result, the precise formulation of which is given in Theorem 4.7 below.

Theorem 1.4 (Multiplication) Let ⋆ be a suitable product on T and let$f _ { 1 } \in \mathcal { D } _ { \alpha 1 } ^ { \gamma _ { 1 } }$and $f _ { 2 } \in \mathcal { D } _ { \alpha _ { 2 } } ^ { \gamma _ { 2 } }$with$\gamma _ { i } > 0$. Set$\alpha = \alpha _ { 1 } + \alpha _ { 2 }$and$\gamma = ( \gamma _ { 1 } + \alpha _ { 2 } ) \wedge ( \gamma _ { 2 } + \alpha _ { 1 } )$. Then, the pointwise product$f _ { 1 } \star f _ { 2 }$belongs to$\mathcal { D } _ { \alpha } ^ { \gamma }$

In the case of$f \in \mathcal { D } _ { 0 } ^ { \gamma }$, all terms in the local expansion have positive homogeneity, so that$\mathcal { R } f$is actually a function. It is then of course possible to compose this function with any smooth function$g .$The non-trivial fact is that the new function obtained in this way does also have a local “Taylor expansion” around every point which is typically of the same order as for the original function$f .$. The reason why this statement is not trivial is that the function$\mathcal { R } f$does in general not possess much “classical” regularity, so that$\mathcal { R } f$typically does not belong to$\mathcal { C } ^ { \gamma }$. Our precise result is the content of Theorem 4.16 below, which can be stated loosely as follows.

Theorem 1.5 (Smooth functions) Let$g \colon \mathbf { R }  \mathbf { R }$be a smooth function and consider a regularity structure endowed with a product ⋆ satisfying suitable compatibility assumptions. Then,$f o r \gamma > 0$, one can build a map$\mathcal { G } \colon \mathcal { D } _ { 0 } ^ { \gamma }  \mathcal { D } _ { 0 } ^ { \gamma }$such that the identity $( \mathcal { R } \mathcal { G } ( f ) ) ( x ) = g \big ( ( \mathcal { R } f ) ( x ) \big )$holdsfor every$\boldsymbol { x } \in \mathbf { R } ^ { d }$

The final ingredient that is required in any general solution theory for semilinear PDEs consists in some regularity improvement arising from the linear part of the equation. One of the most powerful class of such statements is given by the Schauder estimates. In the case of convolution with the Green’s function G of the Laplacian, the Schauder estimates state that if$f \in \mathcal { C } ^ { \alpha }$, then$G * f \in { \mathcal { C } } ^ { \alpha + 2 }$, unless$\alpha + 2 \in \mathbf { N } .$. (In which case some additional logarithms appear in the modulus of continuity of$G * f . )$ One of the main reasons why the theory developed in this article is useful is that such an estimate still holds when$f \in \mathcal { D } ^ { \alpha }$. This is highly non-trivial since it involves “guessing” an expansion for the local behaviour of$G * \mathcal { R } f$up to sufficiently high order. Somewhat surprisingly, it turns out that even though the convolution with G is not a local operator at all, its action on the local expansion of a function is local, except for those coefficients that correspond to the usual polynomials.

One way of stating our result is the following, which will be reformulated more precisely in Theorem 5.12 below.

Theorem 1.6 (Multi-level Schauder estimate) Let$K \colon \mathbf { R } ^ { d } \setminus \{ 0 \}  \mathbf { R }$be a smooth kernel with a singularity of order$\beta - d$at the origin for some$\beta > 0$. Then, under certain natural assumptions on the regularity structure and the model realising it, and provided that$\gamma + \beta \not \in \mathbf { N } ,$, one can construct for$\gamma > 0$a linear operator$K _ { \gamma } \colon D _ { \alpha } ^ { \gamma } \to$ $\mathcal { D } _ { ( \alpha + \beta ) \wedge 0 } ^ { \gamma + \beta }$such that the identity

$$
\mathcal {R K} _ {\gamma} f = K * \mathcal {R} f,
$$

holds for every$f \in \mathcal { D } _ { \alpha } ^ { \gamma }$. Here, denotes the usual convolution between two functions / distributions.

We call this a “multi-level” Schauder estimate because it is a statement not just about f itself but about every “layer” appearing in its local expansion.

Remark 1.7 The precise formulation of the multi-level Schauder estimate allows to specify a non-uniform scaling of$\mathbf { R } ^ { d }$. This is very useful for example when considering the heat kernel which scales differently in space and in time. In this case, Theorem 1.6 still holds, but all regularity statements have to be interpreted in a suitable sense. See Sections 2.3 and 5 below for more details.

At this stage, we appear to possibly rely very strongly on the various still unspecified structural assumptions that are required of the regularity structure and of the model realising it. The reason why, at least to some extent, this can be “brushed under the rug” without misleading the reader is the following result, which is a synthesis of Proposition 4.11 and Theorem 5.14 below.

Theorem 1.8 (Extension theorem) It is always possible to extend a given regularity structure in such a way that the assumptions implicit in the statements ofTheorems 1.4–1.6 do hold.

Loosely speaking, the idea is then to start with the “canonical” regularity structure corresponding to classical Taylor expansions and to enlarge it by successively applying the extension theorem, until it is large enough to allow a closed formulation of the problem one wishes to study as a fixed point map.

## 1.4 On renormalisation procedures

The main problem with the strategy outlined above is that while the extension of an abstract regularity structure given by Theorem 1.8 is actually very explicit and rather canonical, the corresponding extension of the model (Π, F) is unique (and continuous) only in the case of the multi-level Schauder theorem and the composition by smooth functions, but not in the case of multiplication when some of the homogeneities are strictly negative. This is a reflection of the fact that multiplication between distributions and functions that are too rough simply cannot be defined in any canonical way [Sch54]. Different non-canonical choices of product then yield truly different solutions, so one might think that the theory is useless at selecting one “natural” solution process.

If the driving noise$\xi$in any of the equations from Section 1.1 is replaced by a smooth approximation$\xi ^ { ( \varepsilon ) }$, then the associated model for the corresponding regularity structure also consists of smooth functions. In this case, there is of course no problem in multiplying these functions, and one obtains a canonical sequence of models $( \Pi ^ { ( \varepsilon ) } , F ^ { ( \varepsilon ) } )$realising our regularity structure. (See Section 8.2 for details of this construction.) At fixed$\varepsilon ,$our theory then simply yields some very local description of the corresponding classical solutions. In some special cases, the sequence$( \Pi ^ { ( \varepsilon ) } , F ^ { ( \varepsilon ) } )$converges to a limit that is independent of the regularisation procedure for a relatively large class of such regularisations. In particular, due to the symmetry of finite-dimensional control systems under time reversal, this is often the case in the classical theory of rough paths, see [Lyo98, CQ02, FV10a].

One important feature of the regularity structures arising naturally in the context of solving semilinear PDEs is that they come with a natural finite-dimensional group R of transformations that act on the space of models. In some examples (we will treat the case of$( \Phi ^ { 4 } )$with$d = 3$in Section 10.5 and a generalisation of (PAM) with$d = 2$ in Section$1 0 . 4 )$, one can explicitly exhibit a subgroup$\Re _ { 0 }$of R and a sequence of elements$M _ { \varepsilon } \in \Re _ { 0 }$such that the “renormalised” sequence$M _ { \varepsilon } ( \Pi ^ { \left( \varepsilon \right) } , F ^ { \left( \varepsilon \right) } )$converges to a finite limiting model$( { \hat { \Pi } } , { \hat { F } } )$. In such a case, the set of possible limits is parametrised by elements of$\Re _ { 0 }$, which in our setting is always just a finite-dimensional nilpotent Lie group. In the two cases mentioned above, one can furthermore reinterpret solutions corresponding to the “renormalised” model$M _ { \varepsilon } ( \Pi ^ { \left( \varepsilon \right) } , F ^ { \left( \varepsilon \right) } )$as solutions corresponding to the “bare” model$( \Pi ^ { ( \varepsilon ) } , F ^ { ( \varepsilon ) } )$, but for a modified equation.

In this sense, R (or a subgroup thereof) has an interpretation as a renormalisation group acting on some space of formal equations, which is a very common viewpoint in the physics literature. (See for example [Del04] for a short introduction.) This thus allows to usually reinterpret the objects constructed by our theory as limits of solutions to equations that are modified by the addition of finitely many diverging counterterms. In the case of (PAM) with$d = 2 .$, the corresponding renormalisation procedure is essentially a type of Wick ordering and therefore yields the appearance of counterterms that are very similar in nature to those arising in the Itˆo-Stratonovich conversion formula for regular SDEs. (But with the crucial difference that they diverge logarithmically instead of being constant!) In the case of$( \Phi ^ { 4 } )$with$d = 3$, the situation is much more delicate because of the appearance of a logarithmic subdivergence “below” the leading order divergence that cannot be dealt with by a Wick-type renormalisation. For the invariant (Gibbs) measure corresponding to$( \Phi ^ { 4 } )$, this fact is well-known and had previously been observed in the context of constructive Euclidean QFT in [Gli68, Fel74, FO76].

Remark 1.9 Symmetries typically play an important role in the analysis of the renormalisation group R. Indeed, if the equation under consideration exhibits some symmetry, at least at a formal level, then it is natural to approximate it by regularised versions with the same symmetry. This then often places some natural restrictions on$\Re _ { 0 } \subset \Re$ ensuring that the renormalised version of the equation is still symmetric. For example, in the case of the KPZ equation, it was already remarked in [Hai13] that regularisation via a non-symmetric mollifier can cause the appearance in the limiting solution of an additional transport term, thus breaking the invariance under left / right reflection. In Section 1.5.1 below, we will consider a class of equations which, via the chain rule, is formally invariant under composition by diffeomorphisms. This “symmetry” again imposes a restriction on$\Re _ { 0 }$ensuring that the renormalised equations again satisfy the chain rule.

Remark 1.10 If an equation needs to be renormalised in order to have a finite limit, it typically yields a whole family of limits parametrised by R (or rather$\Re _ { 0 }$in the presence of symmetries). Indeed, if$M _ { \varepsilon } ( \Pi ^ { \left( \varepsilon \right) } , F ^ { \left( \varepsilon \right) } )$converges to a finite limit and M is any fixed element of$\Re _ { 0 }$, then$M M _ { \varepsilon } ( \Pi ^ { \left( \varepsilon \right) } , \boldsymbol { F } ^ { \left( \varepsilon \right) } )$obviously also converges to a finite limit. At first sight, this might look like a serious shortcoming of the theory: our equations still aren’t well-posed after all! It turns out that this state of affairs is actually very natural. Even the very well-understood situation of one-dimensional SDEs of the type

$$
d x = f (x) d t + \sigma (x) d W (t),\tag{1.4}
$$

exhibits this phenomena: solutions are different whether we interpret the stochastic integral as an Itˆo integral, a Stratonovich integral, etc. In this particular case, one would have$\Re \approx \mathbf { R }$endowed with addition as its group structure and the action of R onto the space of equations is given by$M _ { c } ( f , \sigma ) = ( f , \sigma + c \sigma \sigma ^ { \prime } )$, where$M _ { c } \in \Re$is the group element corresponding to the real constant c. Switching between the Itˆo and Stratonovich formulations is indeed a transformation of this type with$c \in \{ \pm \frac { 1 } { 2 } \}$

If the equation is driven by more than one Brownian motion, our renormalisation group increases in size: one now has a choice of stochastic integral for each of the integrals appearing in the equation. On symmetry grounds however, we would of course work with the subgroup$\Re _ { 0 } \subset \Re$which corresponds to the same choice for each. If we additionally exploit the fact that the class of equations (1.4) is formally invariant under the action of the group of diffeomorphisms of R (via the chain rule), then we could reduce$\Re _ { 0 }$further by postulating that the renormalised solutions should also transform under the classical chain rule. This would then reduce$\Re _ { 0 }$to the trivial group, thus leading to a “canonical” choice (the Stratonovich integral). In this particular case, we could of course also have imposed instead that the integral$\textstyle \int W d W$has no component Rin the 0th Wiener chaos, thus leading to Wick renormalisation with the Itˆo integral as a second “canonical” choice.

## 1.5 Main results: applications

We now show what kind of convergence results can be obtained by concretely applying the theory developed in this article to two examples of stochastic PDEs that cannot be interpreted by any classical means. The precise type of convergence will be detailed in the main body of the article, but it is essentially a convergence in probability on spaces of continuous trajectories with values in$\mathcal { C ^ { \alpha } }$for a suitable (possibly negative) value of α. A slight technical difficulty arises due to the fact that the limit processes do not necessarily have global solutions, but could exhibit blow-ups in finite time. In such a case, we know that the blow-up time is almost surely strictly positive and we have convergence “up to the blow-up time”.

## 1.5.1 Generalisation of the parabolic Anderson model

First, we consider the following generalisation of (PAM):

$$
\partial_ {t} u = \Delta u + f _ {i j} (u) \partial_ {i} u \partial_ {j} u + g (u) \xi , \qquad u (0) = u _ {0},\tag{PAMg}
$$

where$f$and$g$are smooth function and summation of the indices i and$j$is implicit. Here,$\xi$denotes spatial white noise. This notation is of course only formal since neither the product$g ( u ) \xi$, nor the product$\partial _ { i } u \partial _ { i } u$make any sense classically. Here, we view u as a function of time$t \geq 0$and of$x \in \mathbf { T } ^ { 2 }$, the two-dimensional torus.

It is then natural to replace$\xi$by a smooth approximation$\xi _ { \varepsilon }$which is given by the convolution of$\xi$with a rescaled mollifier$\varrho .$Denote by$u _ { \varepsilon }$the solution to the equation

$$
\partial_ {t} u _ {\varepsilon} = \Delta u _ {\varepsilon} + f _ {i j} (u _ {\varepsilon}) \left(\partial_ {i} u _ {\varepsilon} \partial_ {j} u _ {\varepsilon} - \delta_ {i j} C _ {\varepsilon} g ^ {2} (u _ {\varepsilon})\right) + g (u _ {\varepsilon}) (\xi_ {\varepsilon} - 2 C _ {\varepsilon} g ^ {\prime} (u _ {\varepsilon}))\tag{1.5}
$$

again with initial condition$u _ { 0 }$. Then, we have the following result:

Theorem 1.11 Let$\alpha \in ( \textstyle { \frac { 1 } { 2 } } , 1 )$. There exists a choice of constants$C _ { \varepsilon }$such that, for every initial condition$u _ { 0 } \in \mathcal { C } ^ { \alpha } ( \mathbf { T } ^ { 2 } )$, the sequence of solutions$u _ { \varepsilon }$to (1.5) converges to a limit u. Furthermore, there is an explicit constant$K _ { \varrho }$depending on ̺ such that if one sets$\begin{array} { r } { C _ { \varepsilon } = - \frac { 1 } { \pi } \log \varepsilon + K _ { \varrho } , } \end{array}$, then the limit obtained in this way is independent ofthe choice ofmollifier ̺.

Proof. This is a combination of Corollary 9.3 (well-posedness of the abstract formulation of the equation), Theorem 10.19 (convergence of the renormalised models to a limiting model) and Proposition 9.4 (identification of the renormalised solutions with (1.5)). The explicit value of the constant$C _ { \varepsilon }$is given in (10.32).□

Remark 1.12 In the case$f = 0$, this result has recently been obtained by different (though related in spirit) techniques in [GIP12].

Remark 1.13 Since solutions might blow up in finite time, the notion of convergence considered here is to fix some large cut-off$L > 0$and terminal time$T$and to stop the solutions$u _ { \varepsilon }$as soon as$\| u _ { \varepsilon } ( t ) \| _ { \alpha } \geq L$, and similarly for the limiting process$u .$The convergence is then convergence in probability in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( [ 0 , T ] \times \mathbf { T } ^ { 2 } )$for the stopped process. Here elements in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$are$\alpha \cdot$-H¨older continuous in space and$\textstyle { \frac { \alpha } { 2 } }$-H¨older continuous in time, see Definition 2.14 below.

Remark 1.14 It is lengthy but straightforward to verify that the additional diverging terms in the renormalised equation (1.5) are precisely such that if ψ :$\textbf { R }  \textbf { R }$is a smooth diffeomorphism, then$v _ { \varepsilon } \ { \stackrel { \mathrm { d e f } } { = } } \ \psi ( u _ { \varepsilon } )$solves again an equation of the type (1.5). Furthermore, this equation is precisely the renormalised version of the equation that one obtains by just formally applying the chain rule to (PAMg)! This gives a rigorous justification of the chain rule for (PAMg). In the case (KPZ), one expects a similar phenomenon, which would then allow to interpret the Cole-Hopf transform rigorously as a particular case of a general change of variables formula.

## 1.5.2 The dynamical$\Phi _ { 3 } ^ { 4 }$model

A similar convergence result can be obtained for$( \Phi ^ { 4 } )$. This time, the renormalised equation takes the form

$$
\partial_ {t} u _ {\varepsilon} = \Delta u _ {\varepsilon} + C _ {\varepsilon} u _ {\varepsilon} - u _ {\varepsilon} ^ {3} + \xi_ {\varepsilon},\tag{1.6}
$$

where$u _ { \varepsilon }$is a function of time$t \geq 0$and space$x \in \mathbf { T } ^ { 3 }$, the three-dimensional torus. It turns out that the simplest class of approximating noise is to consider a space-time mollifier$\varrho ( { x } , t )$and to set$\xi _ { \varepsilon } \ { \overset { \underset { \mathrm { d e f } } { } } { = } } \ \xi \ * \ \varrho _ { \varepsilon }$, where$\varrho _ { \varepsilon }$is the rescaled mollifier given by $\varrho _ { \varepsilon } ( x , t ) = \varepsilon ^ { - 5 } \varrho ( x / \varepsilon , t / \varepsilon ^ { 2 } )$

With this notation, we then have the following convergence result, which is the content of Section 10.5 below.

Theorem 1.15 Let$\alpha \in ( - \frac { 2 } { 3 } , - \frac { 1 } { 2 } )$. There exists a choice of constants$C _ { \varepsilon }$such that, for every initial condition$u _ { 0 } \in \mathcal { C } ^ { \alpha } ( \mathbf { \bar { T } } ^ { 3 } )$, the sequence of solutions$u _ { \varepsilon }$converges to a limit u. Furthermore,$i f C _ { \varepsilon }$are chosen suitably, then this limit is again independent of the choice of mollifier ϕ.

Proof. This time, the statement is a consequence of Proposition 9.8 (well-posedness of the abstract formulation), Theorem 10.22 (convergence of the renormalised models) and Proposition 9.10 (identification of renormalised solutions with (1.6)).□

Remark 1.16 It turns out that the limiting solution u is almost surely a continuous function in time with values in$\mathcal { C } ^ { \alpha } ( \mathbf { T } ^ { 3 } )$. The notion of convergence is then as in Remark 1.13. Here, we wrote again$\mathcal { C ^ { \alpha } }$as a shorthand for the Besov space$B _ { \infty , \infty } ^ { \alpha }$

Remark 1.17 As already noted in [Fel74] (but for a slightly different regularisation procedure, which is more natural for the static version of the model considered there), the correct choice of constants$C _ { \varepsilon }$is of the form

$$
C _ {\varepsilon} = \frac {C _ {1}}{\varepsilon} + C _ {2} \log \varepsilon + C _ {3},
$$

where$C _ { 1 }$and$C _ { 3 }$depend on the choice of$\varrho$in a way that is explicitly computable, and the constant$C _ { 2 }$is independent of the choice of$\varrho .$It is the presence of this additional logarithmic divergence that makes the analysis of$( \Phi ^ { 4 } )$highly non-trivial. In particular, it was recently remarked in [ALZ06] that this seems to rule out the use of Dirichlet form techniques for interpreting$( \Phi ^ { 4 } )$

Remark 1.18 Again, we do not claim that the solutions constructed here are global. Indeed, the convergence holds in the space$\mathcal { C } ( [ 0 , T ] , \mathcal { C } ^ { \alpha } )$, but only up to some possibly finite explosion time. It is very likely that one can show that the solutions are global for almost every choice of initial condition, where “almost every” refers to the measure built in [Fel74]. This is because that measure is expected to be invariant for the limiting process constructed in Theorem 1.15.

## 1.5.3 General methodology

Our methodology for proving the kind of convergence results mentioned above is the following. First, given a locally subcritical SPDE of the type (1.2), we build a regularity structure$\mathcal { T } _ { F }$which takes into account the structure of the nonlinearity$F$(as well as the regularity index of the driving noise and the local scaling properties of the linear operator$\mathcal { L } )$, together with a class$\mathcal { M } _ { F }$of “admissible models” on$\mathcal { T } _ { F }$which are defined using the abstract properties of$\mathcal { T } _ { F }$and the Green’s function of${ \mathcal { L } } .$The general construction of such a structure is performed in Section 8. We then also build a natural “lift map”$Z \colon { \mathcal { C } } ( \mathbf { R } ^ { d } ) \to { \mathcal { M } } _ { F }$(see Section 8.2), where d is the dimension of the underlying space-time, as well as an abstract solution map$S \colon { \mathcal { C } } ^ { \alpha } \times { \mathcal { M } } _ { F } \to { \mathcal { D } } ^ { \gamma }$, with the property that${ \mathcal R S } \big ( u _ { 0 } , Z ( \xi _ { \varepsilon } ) \big )$yields the classical (local) solution to (1.2) with initial condition$u _ { 0 }$and noise$\xi _ { \varepsilon }$. Here,$\mathcal { R }$is the “reconstruction operator” already mentioned earlier. A general result showing that$\boldsymbol { \mathcal { S } }$can be built for “most” subcritical semilinear evolution problems is provided in Section 7. This relies fundamentally on the multi-level Schauder estimate of Section 5, as well as the results of Section 6 dealing with singular modelled distributions, which is required in order to deal with the behaviour near time 0.

The main feature of this construction is that both the abstract solution map$\boldsymbol { \mathcal { S } }$and the reconstruction operator  are continuous. In most cases of interest they are even locally Lipschitz continuous in a suitable sense. Note that we made a rather serious abuse of notation here, since the very definition of the space$\mathcal { D } ^ { \gamma }$does actually depend on the particular model$Z ( \xi _ { \varepsilon } ) !$This will not bother us unduly since one could very easily remedy this by having the target space be$^ { 6 6 } \mathcal { M } _ { F }$⋉$\mathcal { D } ^ { \gamma \bullet }$, with the understanding that each “fiber”$\mathcal { D } ^ { \gamma }$is modelled on the corresponding model in$\mathcal { M } _ { F }$. The map$\boldsymbol { \mathcal { S } }$ would then simply act as the identity on$\mathcal { M } _ { F }$

Finally, we show that it is possible to find a sequence of elements$M _ { \varepsilon } \in \Re$such that the sequence of renormalised models$M _ { \varepsilon } Z ( \xi _ { \varepsilon } )$converge to some limiting model $\hat { Z }$and we identify$\mathcal { R } S \big ( u _ { 0 } , M _ { \varepsilon } Z ( \xi _ { \varepsilon } ) \big )$with the classical solution to a modified equation. The proof of this fact is the only part of the whole theory which is not “automated”, but has to be performed by hand for each class of problems. However, if two problems give rise to the same structure$\mathcal { M } _ { F }$and are based on the same linear operator${ \mathcal { L } } ,$then they can be treated with the same procedure, since it is only the details of the solution map that change from one problem to the other. We treat two classes of problems in detail in Sections 9 and 10. Section 10 also contains a quite general toolbox that is very useful for treating the renormalisation of many equations with Gaussian driving noise.

## 1.6 Alternative theories

Before we proceed to the meat of this article, let us give a quick review of some of the main existing theories allowing to make sense of products of distributions. For each of these theories, we will highlight the differences with the theory of regularity structures.

## 1.6.1 Bony’s paraproduct

Denoting by$\Delta _ { j } f$the jth Paley-Littlewood block of a distribution$f ,$one can define the bilinear operators

$$
\pi_ {<  } (f, g) = \sum_ {i <   j - 1} \Delta_ {i} f \Delta_ {j} g, \quad \pi_ {>} (f, g) = \pi_ {<  } (g, f), \quad \pi_ {o} (f, g) = \sum_ {| i - j | \leq 1} \Delta_ {i} f \Delta_ {j} g,
$$

so that, at least formally, one has$f g = \pi _ { < } ( f , g ) + \pi _ { > } ( f , g ) + \pi _ { o } ( f , g )$. (See [Bon81] for the original article and some applications to the analysis of solutions to fully nonlinear PDEs, as well as the monograph and review article [BCD11, BMN10]. The notation of this section is borrowed from the recent work [GIP12].) It turns out that$\pi _ { < }$<sub><</sub> and$\pi _ { > }$ make sense for any two distributions$f$and$g .$Furthermore, if$f \in \mathcal { C } ^ { \alpha }$and$g \in \mathcal { C } ^ { \beta }$with

$\alpha + \beta > 0$, then

$$
\pi_ {<  } (f, g) \in \mathcal {C} ^ {\beta}, \qquad \pi_ {>} (f, g) \in \mathcal {C} ^ {\alpha}, \qquad \pi_ {o} (f, g) \in \mathcal {C} ^ {\alpha + \beta},\tag{1.7}
$$

so that one has a gain of regularity there, but one does again encounter a “barrie$\mathrm { r } ^ { \prime \prime }$at $\alpha + \beta = 0$

The idea exploited in [GIP12] is to consider a “model distribution” η and to consider “controlled distributions” of the type

$$
f = \pi_ {<  } (f ^ {\eta}, \eta) + f ^ {\sharp},
$$

where both$f ^ { \eta }$and$f ^ { \sharp }$are more regular than$\eta .$The construction is such that, at small scales, irregularities of$f$“look like” irregularities of$\eta .$. The hope is then that if$f$is controlled by$\eta , g$is controlled by$\zeta ,$, and one knows of a renormalisation procedure allowing to make sense of the product ηζ (by using tools from stochastic analysis for example), then one can also give a consistent meaning to the product$f g$. This is the philosophy that was implemented in [GIP12, Theorems 9 and 31].

This approach is very close to the one taken in the present work, and indeed it is possible to recover the results of [GIP12] in the context of regularity structures, modulo slight modifications in the precise rigorous formulation of the convergence results. There are also some formal similarities: compare for example (1.7) with the bounds on each of the three terms appearing in (4.4). The main philosophical difference is that the approach presented here is very local in nature, as opposed to the more global approach used in Bony’s paraproduct. It is also more general, allowing for an arbitrary number of controls which do themselves have small-scale structures that are linked to each other.$\mathrm { A s }$a consequence, the current work also puts a strong emphasis on the highly non-trivial algebraic structures underlying our construction. In particular, we allow for rather sophisticated renormalisation procedures going beyond the usual Wick ordering, which is something that is required in several of the examples presented above.

## 1.6.2 Colombeau’s generalised functions

In the early eighties, Colombeau introduced an algebra$\mathcal { G } ( \mathbf { R } ^ { d } )$of generalised functions on$\mathbf { R } ^ { d }$(or an open subset thereof) with the property that$S ^ { \prime } ( \mathbf { R } ^ { d } ) \subset \mathcal { G } ( \mathbf { R } ^ { d } )$where$S ^ { \prime }$ denotes the usual Schwartz distributions [Col83, Col84]. Without entering into too much detail,$\mathcal { G } ( \mathbf { R } ^ { d } )$is essentially defined as the set of smooth functions from$S ( \mathbf { R } ^ { d } )$ the set of Schwartz test functions, into R, quotiented by a certain natural equivalence relation.

Some (but not all) generalised functions have an “associated distribution”. In other words, the theory comes with a kind of “projection operator”$P \colon \mathcal G ( \mathbf R ^ { d } )  S ^ { \prime } ( \mathbf R ^ { d } )$ which is a left inverse for the injection ι :$S ^ { \prime } ( \mathbf { R } ^ { d } ) \hookrightarrow \mathcal { G } ( \mathbf { R } ^ { d } )$. However, it is important to note that the domain of definition of$P$is not all of$\mathcal { G } ( \mathbf { R } ^ { d } )$. Furthermore, the product in$\mathcal { G } ( \mathbf { R } ^ { d } )$behaves as one would expect on the images of objects that one would classically know how to multiply. For example, if$f$and$g$are continuous functions, then $P ( ( \iota f ) ( \iota g ) ) = f g$. The same holds true if$f$is a smooth function and$g$is a distribution.

There are some similarities between the theory of regularity structures and that of Colombeau generalised functions. For example, just like elements in$\mathcal { G } ,$, elements in the spaces$\mathcal { D } ^ { \alpha }$(see Definition 3.1 below) contain more information than what is strictly required in order to reconstruct the corresponding distribution. The theory of regularity structures involves a reconstruction operator${ \mathcal { R } } ,$which plays a very similar role to the operator$P$from the theory of Colombeau’s generalised functions by allowing to discard that additional information. Also, both theories allow to provide a rigorous mathematical interpretation of some of the calculations performed in the context of quantum field theory.

One major difference between the two theories is that the theory of regularity structures has more flexibility built in. Indeed, it allows some freedom in the definition of the product between elements of the “model” used for performing the local Taylor expansions. This allows to account for the fact that taking limits along different smooth approximations might in general yield different answers. (A classical example is the fact that sin$( x / \varepsilon ) \to 0$in any reasonable topology where it does converge, while $\sin ^ { 2 } ( x / \varepsilon ) \to 1 / 2$. More sophisticated effects of this kind can easily be encoded in a regularity structure, but are invisible to the theory of Colombeau’s generalised functions.) This could be viewed as a disadvantage of the theory of regularity structures: it requires substantially more effort on the part of the “user” in order to specify the theory completely in a given example. Also, there isn’t just “one” regularity structure: the precise algebraic structure that is suitable for analysing a given problem does depend a lot on the problem in question. However, we will see in Section 8 that there is a general procedure allowing to build a large class of regularity structures arising in the analysis of semilinear SPDEs in a unified way.

## 1.6.3 White noise analysis

One theory that in principle allows to give some meaning to$( \Phi ^ { 4 } )$, (PAM), and (SNS) (but to the best of the author’s knowledge not to (PAMg) or (KPZ) with non-constant coefficients) is the theory of “white noise analysis” (WNA), exposed for example in [HØUZ10] (see also [Hid75, HP90] for some of the earlier works). For example, the case of the stochastic Navier-Stokes equations has been considered in [MR04], while the case of a stochastic version of the nonlinear heat equation was considered in [BDP97]. Unfortunately, WNA has a number of severe drawbacks that are not shared by the theory of regularity structures:

Solutions in the WNA sense typically do not consist of random variables but of “Hida distributions”. As a consequence, only some suitable moments are obtained by this theory, but no actual probability distributions and / or random variables.

Solutions in the WNA sense are typically not obtained as limits of classical solutions to some regularised version of the problem. As a consequence, their physical interpretation is unclear. As a matter of fact, it was shown in [Cha00] that the WNA solution to the KPZ equation exhibits a physically incorrect large-time behaviour, while the Cole-Hopf solution (which can also be obtained via a suitable regularity structure, see [Hai13]) is the physically relevant solution [BG97].

There are exceptions to these two rules (usually when the only ill-posed product is of the form$F ( u ) \cdot \xi$with$\xi$some white noise, and the problem is parabolic), and in such cases the solutions obtained by the theory of regularity structures typically “contain” the solutions obtained by WNA. On the other hand, white noise analysis (or, in general, the Wiener chaos decomposition of random variables) is a very useful tool when building explicit models associated to a Gaussian noise. This will be exploited in Section 10 below.

## 1.6.4 Rough paths

The theory of rough paths was originally developed in [Lyo98] in order to interpret solutions to controlled differential equations of the type

$$
d Y (t) = F (Y) d X (t),
$$

where$X \colon \mathbf { R } ^ { + }  \mathbf { R } ^ { m }$is an irregular function and$F \colon \mathbf { R } ^ { d }  \mathbf { R } ^ { d m }$is a sufficiently regular collection of vector fields on$\mathbf { R } ^ { d }$. This can be viewed as an instance of the general problem (1.1) if we set${ \mathcal { L } } = \partial _ { t }$and$\begin{array} { r } { \xi = \frac { d X } { d t } } \end{array}$, which is now a rather irregular distribution. It turns out that, in the case of H¨older-regular rough paths, the theory of rough paths can be recast into our framework. It can then be interpreted as one particular class of regularity structures (one for each pair$( \alpha , m )$, where m is the dimension of the rough path and α its index of H¨older regularity), with the corresponding space of rough paths being identified with the associated space of models. Indeed, the theory of rough paths, and particularly the theory of controlled rough paths as developed in [Gub04, Gub10], was one major source of inspiration of the present work. See Section 4.4 below for more details on the link between the two theories.

## 1.7 Notations

Given a distribution ξ and a test function$\varphi ,$we will use indiscriminately the notations $\langle \xi , \varphi \rangle$and$\xi ( \varphi )$for the evaluation of ξ against$\varphi .$. We will also sometimes use the abuse of notation$\textstyle \int \varphi ( x ) \xi ( x )$dx or$\textstyle \int \varphi ( x ) \xi ( d x )$

R RThroughout this article, we will always work with multiindices on$\mathbf { R } ^ { d }$. A multiindex k is given by a vector$( k _ { 1 } , \ldots , k _ { d } )$with each$k _ { i } \geq 0$a positive integer. For$\boldsymbol { x } \in \mathbf { R } ^ { d }$ we then write$x ^ { \dot { k } }$as a shorthand for$x _ { 1 } ^ { k _ { 1 } } \cdot \cdot \cdot x _ { d } ^ { k _ { d } }$. The same notation will still be used when$X \in T ^ { d }$for some algebra T. For a sufficiently regular function$g \colon \mathbf { R } ^ { d }  \mathbf { R }$, we write$D ^ { k } g ( x )$as a shorthand for$\partial _ { x _ { 1 } } ^ { k _ { 1 } } \cdot \cdot \cdot \partial _ { x _ { d } } ^ { k _ { d } } g ( x )$. We also write k! as a shorthand for $k _ { 1 } ! \cdots k _ { d } !$

Finally, we will write$a \wedge b$for the minimum of a and b and$a \lor b$for the maximum.

## Acknowledgements

I am very grateful to M. Gubinelli and to H. Weber for our numerous discussions on quantum field theory, renormalisation, rough paths, paraproducts, Hopf algebras, etc. These discussions were of enormous help in clarifying the concepts presented in this article. Many other people provided valuable input that helped shaping the theory. In particular, I would like to mention A. Debussche, B. Driver, P. Friz, J. Jones, D. Kelly, X.-M. Li, M. Lewin, T. Lyons, J. Maas, K. Matetski, J.-C. Mourrat, N. Pillai, D. Simon, T. Souganidis, J. Unterberger, and L. Zambotti. Special thanks are due to L. Zambotti for pointing out a mistake in an earlier version of the definition of the class of regularity structures considered in Section 8.

Financial support was kindly provided by the Royal Society through a Wolfson Research Merit Award and by the Leverhulme Trust through a Philip Leverhulme Prize.

## 2 Abstract regularity structures

We start by introducing the abstract notion of a “regularity structure”, which was already mentioned in a loose way in the introduction, and which permeates the entirety of this work.

Definition 2.1 A regularity structure$\mathcal { T } ~ = ~ ( A , T , G )$consists of the following elements:

An index set$A \subset \mathbf { R }$such that$0 \in A ,$, A is bounded from below, and A is locally finite.

A model space$T ,$which is a graded vector space$T = \oplus _ { \alpha \in A } T _ { \alpha }$, with each$T _ { \alpha }$a Banach space. Furthermore,$T _ { 0 } \approx \mathbf { R }$Land its unit vector is denoted by 1.

A structure group G of linear operators acting on$T$such that, for every$\Gamma \in G ,$ every$\alpha \in A$, and every$a \in T _ { \alpha }$, one has

$$
\Gamma a - a \in \bigoplus_ {\beta <   \alpha} T _ {\beta}.\tag{2.1}
$$

Furthermore, Γ1 = 1 for every$\Gamma \in G$

Remark 2.2 It will sometimes be an advantage to consider$G$as an abstract group, together with a representation Γ of G on$T ,$. This point of view will be very natural in the construction of Section 7 below. We will then sometimes use the notation$g \in G$ for the abstract group element, and$\Gamma _ { g }$for the corresponding linear operator. For the moment however, we identify elements of$G$directly with linear operators on$T$in order to reduce the notational overhead.

Remark 2.3 Recall that the elements of$T = \oplus _ { \alpha \in A } T _ { \alpha }$are finite series of the type $\textstyle a = \sum _ { \alpha \in A } a _ { \alpha }$with$a _ { \alpha } \in T _ { \alpha }$L. All the operations that we will construct in the sequel Pwill then make sense component by component.

Remark 2.4 A good analogy to have in mind is the space of all polynomials, which will be explored in detail in Section 2.2 below. In line with this analogy, we say that $T _ { \alpha }$consists of elements that are homogeneous of order α. In the particular case of polynomials in commuting indeterminates our theory boils down to the very familiar theory of Taylor expansions on$\mathbf { R } ^ { d }$, so that the reader might find it helpful to read the present section and Section 2.2 in parallel to help build an intuition. The reader familiar with the theory of rough paths [Lyo98] will also find it helpful to simultaneously read Section 4.4 which shows how the theory of rough paths (as well as the theory of “branched rough paths” [Gub10]) fits within our framework.

The idea behind this definition is that$T$is a space whose elements describe the “jet” or “local expansion” of a function (or distribution!) f at any given point. One should then think of$T _ { \alpha }$as encoding the information required to describe$f$locally “at order$\alpha ^ { \prime \prime }$in the sense that, at scale$\varepsilon ,$elements of$T _ { \alpha }$describe fluctuations of size $\varepsilon ^ { \alpha }$. This interpretation will be made much clearer below, but at an intuitive level it already shows that a regularity structure with$A \subset \mathbf { R } _ { + }$will describe functions, while a regularity structure with${ \cal A } \not \subset { \bf R } _ { + }$will also be able to describe distributions.

The role of the structure group G will be to translate coefficients from a local expansion around a given point into coefficients for an expansion around a different point. Keeping in line with the analogy of Taylor expansions, the coefficients of a Taylor polynomial are just given by the partial derivatives of the underlying function$\varphi$at some point$x .$However, in order to compare the Taylor polynomial at x with the Taylor polynomial at$y ,$it is not such a good idea to compare the coefficients themselves. Instead, it is much more natural to first translate the first polynomial by the quantity $y - x .$. In the case of polynomials on$\mathbf { R } ^ { d }$, the structure group$G$will therefore simply be given by$\mathbf { R } ^ { d }$with addition as its group property, but we will see that non-abelian structure groups arise naturally in more general situations. (For example, the structure group is non-Abelian in the theory of rough paths.)

Before we proceed to a study of some basic properties of regularity structures, let us introduce a few notations. For an element$a \in T$, we write${ \mathcal { Q } } _ { \alpha } a$for the component of a in$T _ { \alpha }$and$\| a \| _ { \alpha } = \| \mathcal { Q } _ { \alpha } a \|$for its norm. We also use the shorthand notations

$$
T _ {\alpha} ^ {+} = \bigoplus_ {\gamma \geq \alpha} T _ {\gamma}, \quad T _ {\alpha} ^ {-} = \bigoplus_ {\gamma <   \alpha} T _ {\gamma},\tag{2.2}
$$

with the conventions that$T _ { \alpha } ^ { + } = \{ 0 \}$if$\alpha >$max A and$T _ { \alpha } ^ { - } = \{ 0 \}$if α$\leq$min A. We furthermore denote by$L _ { 0 } ^ { - } ( T )$the space of all operators L on T such that$L a \in T _ { \alpha } ^ { - }$for $a \in T _ { \alpha }$and by$L ^ { - }$the set of operators L such that$L - 1 \in L _ { 0 } ^ { - }$, so that$G \subset L ^ { - }$

The condition that Γa$- ~ a \in T _ { \alpha } ^ { - }$for$a \in T _ { \alpha }$, together with the fact that the index set A is bounded from below, implies that, for every$\alpha \in A$there exists$n > 0$such that$( \Gamma - 1 ) ^ { n } T _ { \alpha } = 0$for every$\Gamma \in G$. In other words, G is necessarily nilpotent. In particular, one can define a function log:$G  L _ { 0 } ^ { - }$by

$$
\log \Gamma = \sum_ {k = 1} ^ {n} \frac {(- 1) ^ {k + 1}}{k} (\Gamma - 1) ^ {k}.\tag{2.3}
$$

Conversely, one can define an exponential map exp:$L _ { 0 } ^ { - } \to L ^ { - }$by its Taylor series, and one has the rather unsurprising identity$\Gamma = \exp ( \log \Gamma )$. As usual in the theory of Lie groups, we write${ \mathfrak { g } } = \log G$as a shorthand.

A useful definition will be the following:

Definition 2.5 Given a regularity structure as above and some$\alpha \leq 0$, a sector V of regularity α is a graded subspace$V = \oplus _ { \beta \in A } V _ { \beta }$with$V _ { \beta } \subset T _ { \beta }$having the following properties.

One has$V _ { \beta } = \{ 0 \}$for every$\beta < \alpha$

The space V is invariant under$G , { \mathrm { i . e . } } \Gamma V \subset V$for every$\Gamma \in G$

For every$\beta \in A$, there exists a complement$\bar { V } _ { \beta } \subset T _ { \beta }$such that$T _ { \beta }$is given by the direct sum$T _ { \beta } = V _ { \beta } \oplus \bar { V } _ { \beta }$

A sector of regularity 0 is also calledfunction-like for reasons that will become clear in Section 3.4.

Remark 2.6 The regularity of a sector will always be less or equal to zero. In the case of the regularity structure generated by polynomials for example, any non-trivial sector has regularity 0 since it always has to contain the element 1. See Corollary 3.16 below for a justification of this terminology.

Remark 2.7 Given a sector V, we can define$A _ { V } \subset A$as the set of indices α such that$V _ { \alpha } \neq \{ 0 \}$. If$\alpha > 0 ,$, our definitions then ensure that$\mathcal { T } _ { V } = ( V , A _ { V } , G )$is again a regularity structure with$\mathcal { T } _ { V } \subset \mathcal { T }$. (See below for the meaning of such an inclusion.) It is then natural to talk about a subsector$W \subset V$if$W$is a sector for$\mathcal { T } _ { V }$

Remark 2.8 Two natural non-empty sectors are given by$T _ { 0 } = \mathrm { s p a n } \{ { \bf 1 } \}$and by$T _ { \alpha }$ with$\alpha = \operatorname* { m i n } A$. In both cases, G automatically acts on them in a trivial way. Furthermore, as an immediate consequence of the definitions, given a sector$V$of regularity α and a real number$\gamma > \alpha$, the space$V \cap T _ { \gamma } ^ { - }$is again a sector of regularity α.

In the case of polynomials on$\mathbf { R } ^ { d }$, typical examples of sectors would be given by the set of polynomials depending only on some subset of the variables or by the set of polynomials of some fixed degree.

## 2.1 Basic properties of regularity structures

The smallest possible regularity structure is given by$\mathcal { T } _ { 0 } = ( \{ 0 \} , { \bf R } , \{ 1 \} )$, where$\{ 1 \}$ is the trivial group consisting only of the identity operator, and with${ \bf 1 } = { \bf 1 }$. This “trivial” regularity structure is the smallest possible structure that accommodates the local information required to describe an arbitrary continuous function, i.e. simply the value of the function at each point.

The set of all regularity structures comes with a natural partial order. Given two regularity structures$\mathcal { T } = ( A , T , G )$and$\bar { \mathcal { T } } = ( \bar { A } , \bar { T } , \bar { G } )$we say that$\mathcal { T }$contains$\bar { \mathcal T }$ and write$\bar { \mathcal T } \subset \mathcal T$if the following holds.

One has${ \bar { A } } \subset A .$

There is an injection$\iota \colon \bar { T }  T$such that, for every$\alpha \in { \bar { A } } .$, one has$\iota ( \bar { T } _ { \alpha } ) \subset T _ { \alpha }$

The space$\iota ( \bar { T } )$is invariant under$G$and the map$j \colon G \to L ( { \bar { T } } , { \bar { T } } )$defined by the identity$j \Gamma = \iota ^ { - 1 } \Gamma \iota$is a surjective group homomorphism from$G$to$\bar { G }$

With this definition, one has$\mathcal { T } _ { 0 } \subset \mathcal { T }$for every regularity structure$\mathcal { T }$, with$\iota 1 = 1$ and j given by the trivial homomorphism.

One can also define the product$\hat { \mathcal { T } } = \mathcal { T } \otimes \bar { \mathcal { T } }$of two regularity structures$\mathcal { T } =$ $( A , T , G )$and$\bar { \mathcal { T } } = ( \bar { A } , \bar { T } , \bar { G } ) \mathrm { b y } \hat { \mathcal { T } } = ( \hat { A } , \hat { T } , \hat { G } )$with

$\hat { A } = A + \bar { A } ,$

$\hat { T } = \oplus _ { ( \alpha , \beta ) } T _ { \alpha } \otimes \bar { T } _ { \beta }$and$\begin{array} { r } { \hat { T } _ { \gamma } = \bigoplus _ { \alpha + \beta = \gamma } T _ { \alpha } \otimes \bar { T } _ { \beta } } \end{array}$, where both sums run over pairs$( \alpha , \beta ) \in { \cal A } \times \bar { \cal A }$

$\hat { G } = G \otimes \bar { G } ,$

Setting$\hat { \mathbf { 1 } } = \mathbf { 1 } \otimes \bar { \mathbf { 1 } }$(where 1 and <sup>¯</sup>1 are the unit elements of$\mathcal { T }$and$\bar { \mathcal T }$respectively), it is easy to verify that this definition satisfies all the required axioms for a regularity structure. If the individual components of$T$and / or$\bar { T }$are infinite-dimensional, this construction does of course rely on choices of tensor products for$T _ { \alpha } \otimes { \bar { T } } _ { \beta }$

Remark 2.9 One has both$\mathcal { T } \subset \mathcal { T } \otimes \bar { \mathcal { T } }$and$\bar { \mathcal { T } } \subset \mathcal { T } \otimes \bar { \mathcal { T } }$with obvious inclusion maps. Furthermore, one has$\mathcal { T } \otimes \mathcal { T } _ { 0 } \approx \mathcal { T }$for the trivial regularity structure$\mathcal { T } _ { 0 }$

## 2.2 The polynomial regularity structure

One very important example to keep in mind for the abstract theory of regularity structures presented in the main part of this article is that generated by polynomials in d commuting variables. In this case, we simply recover the usual theory of Taylor expansions / regular functions in$\mathbf { R } ^ { d }$. However, it is still of interest since it helps building our intuition and provides a nicely unified way of treating regular functions with different scalings.

In this case, the model space$T$consists of all abstract polynomials in d indeterminates. More precisely, we have d “dummy variables”$\{ \bar { X } _ { i } \} _ { i = 1 } ^ { d }$and$T$consists of polynomials in$X$. Given a multiindex$k = ( k _ { 1 } , \ldots , k _ { d } )$, we will use throughout this article the shorthand notation

$$
X ^ {k} \stackrel {\mathrm{def}} {=} X _ {1} ^ {k _ {1}} \dots X _ {d} ^ {k _ {d}}.
$$

Finally, we denote by$\mathbf { 1 } = X ^ { 0 }$the “empty” monomial.

In general, we will be interested in situations where different variables come with different degrees of homogeneity. A good example to keep in mind is that of parabolic equations, where the linear operator is given by$\partial _ { t } - \Delta$, with the Laplacian acting on the spatial coordinates. By homogeneity, it is then natural to make powers of t “count double”. In order to implement this classical idea, we assume from now on that we fix a scaling$\mathfrak { s } \in \mathbf { N } ^ { d } \ \mathrm { o f } \ \mathbf { R } ^ { d }$, which is simply a vector of strictly positive relatively prime integers. The Euclidean scaling is simply given by$\mathfrak { s } _ { c } = ( 1 , \ldots , 1 )$.

Given such a scaling, we defined the “scaled degree” of a multiindex k by

$$
| k | _ {\mathfrak {s}} = \sum_ {i = 1} ^ {d} \mathfrak {s} _ {i} k _ {i}.\tag{2.4}
$$

With this notation we define, for every$n \in \mathbf { N } ,$the subspace$T _ { n } \subset T$by

$$
T _ {n} = \operatorname{span} \left\{X ^ {k}: | k | _ {\mathfrak {s}} = n \right\}.
$$

For a monomial$P$of the type$P ( X ) = X ^ { k }$, we then refer to$| k | _ { s }$as the scaled degree of$P .$Setting$A = \mathbf { N } ,$, we have thus constructed the first two components of a regularity structure.

Our structure comes with a natural model, which is given by the concrete realisation of an abstract polynomial as a function on$\mathbf { R } ^ { d }$. More precisely, for every$\boldsymbol { x } \in \mathbf { R } ^ { d }$, we have a natural linear map$\Pi _ { x } \colon T  { \mathcal { C } } ^ { \infty } ( \mathbf { R } ^ { d } )$given by

$$
(\Pi_ {x} X ^ {k}) (y) = (y - x) ^ {k}.\tag{2.5}
$$

In other words, given any “abstract polynomial” P(X),$\Pi _ { x }$realises it as a concrete polynomial on$\mathbf R ^ { \breve { d } }$based at the point x.

This suggests that there is a natural action of$\mathbf { R } ^ { d }$on$T$which simply shifts the base point$x .$This is precisely the action that is described by the group$G$which is the last ingredient missing to obtain a regularity structure. As an abstract group, G will simply be a copy of$\mathbf { R } ^ { d }$endowed with addition as its group operation. For any$h \in \mathbf { R } ^ { d } \approx G ,$ the action of$\Gamma _ { h }$on an abstract polynomial is then given by

$$
(\Gamma_ {h} P) (X) = P (X + h).
$$

It is obvious from our notation that one has the identities

$$
\Gamma_ {h} \circ \Gamma_ {\bar {h}} = \Gamma_ {h + \bar {h}}, \qquad \Pi_ {x + h} \Gamma_ {h} = \Pi_ {x},
$$

which will play a fundamental role in the sequel.

The triple$( \mathbf { N } , T , G )$constructed in this way thus defines a regularity structure, which we call$\mathcal { T } _ { d , \mathfrak { s } } .$. (It depends on the scaling s only in the way that$T$is split into subspaces, so s does not explicitly appear in the definition of$\mathcal { T } _ { d , { \mathfrak { s } } } . )$

In this construction, the space$T$comes with more structure than just that of a regularity structure. Indeed, it comes with a natural multiplication ⋆ given by

$$
(P \star Q) (X) = P (X) Q (X).
$$

It is then straightforward to verify that this representation satisfies the properties that

For$P \in T _ { m }$and$Q \in T _ { n }$, one has$P \star Q \in T _ { m + n }$

The element 1 is neutral for ⋆.

For every$\boldsymbol { h } \in  { \mathbf { R } } ^ { d }$and$P , Q \in T$, one has$\Gamma _ { h } ( P \star Q ) = \Gamma _ { h } P \star \Gamma _ { h } Q$

Furthermore, there exists a natural element$\langle \mathbf { 1 } , \cdot \rangle$in the dual of$T$which consists of formally evaluating the corresponding polynomial at the origin. More precisely, one sets$\langle \mathbf { 1 } , X ^ { k } \rangle = \delta _ { k , 0 }$

As a space of polynomials,$T$arises naturally as the space in which the Taylor expansion of a function$\varphi \colon { \mathbf { R } } ^ { d }  { \mathbf { R } }$takes values. Given a smooth function$\varphi \colon { \mathbf { R } ^ { d } }  { \mathbf { R } }$ and an integer$\ell \geq 0 .$, we can${ \mathrm { ~ \hat { ~ } { ~ } i f t ^ { \prime } ~ } } \varphi$in a natural way to$T$by computing its Taylor expansion of order less than ℓ at each point. More precisely, we set

$$
(\mathcal {T} _ {\ell} \varphi) (x) = \sum_ {| k | _ {\mathfrak {s}} <   \ell} \frac {X ^ {k}}{k !} D ^ {k} \varphi (x),\tag{2.6}
$$

where, for a given multiindex$k = ( k _ { 1 } , \ldots , k _ { d } ) , D ^ { k } \varphi$stands as usual for the partial derivative$\partial _ { 1 } ^ { k _ { 1 } ^ { - } } \cdot \cdot \cdot \partial _ { d } ^ { k _ { d } } \varphi ( x )$. It then follows immediately from the general Leibniz rule that for$\mathcal { C } ^ { \ell }$functions,$\mathcal { T } _ { \ell } \mathrm { i s }$“almost” an algebra morphism, in the sense that in addition to being linear, one has

$$
\mathcal {T} _ {\ell} (\varphi \cdot \psi) (x) = \mathcal {T} _ {\ell} \varphi (x) \star \mathcal {T} _ {\ell} \psi (x) + R (x),\tag{2.7}
$$

where the remainder$R ( x )$is a sum of homogeneous terms of scaled degree greater or equal to ℓ.

We conclude this subsection by defining the classes$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$of functions that are$\mathcal { C ^ { \alpha } }$with respect to a given scaling s. Recall that, for$\alpha \in ( 0 , 1 ]$, the class$\mathcal { C } ^ { \alpha } \mathrm { o f } ^ {  } \mathrm { u s u a l } ^ { \cdot }$α-H¨older continuous functions is given by those functions$f$such that$| f ( x ) - f ( y ) | \lesssim | x - y | ^ { \alpha }$ uniformly over x and$y$in any compact set. For any$\alpha > 1$, we can then define$\mathcal { C ^ { \alpha } }$ recursively as consisting of functions that are continuously differentiable and such that each directional derivative belongs to$\mathcal { C } ^ { \alpha - 1 }$

Remark 2.10$\bigtriangleup$In order to keep our notations consistent, we have slightly strayed from the usual conventions by declaring a function to be of class$\mathcal { C } ^ { 1 }$even if it is only Lipschitz continuous. A similar abuse of notation will be repeated for all positive integers, and this will be the case throughout this article.

Remark 2.11 We could have defined the spaces$\mathcal { C ^ { \alpha } }$for$\alpha \in [ 0 , 1 )$(note the missing point 1!) similarly as above, but replacing the bound on$f ( x ) - f ( y )$by

$$
\lim _ {| h | \rightarrow 0} | f (x + h) - f (x) | / | h | ^ {\alpha} = 0,\tag{2.8}
$$

imposing uniformity of the convergence for x in any compact set. If we extended this definition to$\alpha \geq 1$recursively as above, this would coincide with the usual spaces$\mathcal { C } ^ { k }$ for integer$k ,$but the resulting spaces would be slightly smaller than the H¨older spaces for non-integer values. (In fact, they would then coincide with the closure of smooth functions under the α-H¨older norm.) Since the bound (2.8) includes a supremum and a limit rather than just a supremum, we prefer to stick with the definition given above.

Keeping this characterisation in mind, one nice feature of the regularity structure just described is that it provides a very natural “direct” characterisation of$\mathcal { C ^ { \alpha } }$for any $\alpha > 0$without having to resort to an inductive construction. Indeed, in the case of the classical Euclidean scaling${ \mathfrak { s } } = ( 1 , \dotsc , 1 )$, we have the following result, where for $a \in T$, we denote by$\| a \| _ { m }$the norm of the component of a in$T _ { m }$

Lemma 2.12 A function$\varphi \colon { \mathbf { R } } ^ { d }  { \mathbf { R } }$is of class$\mathcal { C ^ { \alpha } }$with$\alpha > 0$if and only if there exists a function$\hat { \varphi } \colon  { \mathbb { R } ^ { d } } \to T _ { \alpha } ^ { - }$such that$\langle \mathbf { 1 } , \boldsymbol { \hat { \varphi } } ( x ) \rangle = \varphi ( x )$and such that

$$
\left\| \hat {\varphi} (x + h) - \Gamma_ {h} \hat {\varphi} (x) \right\| _ {m} \lesssim | h | ^ {\alpha - m},\tag{2.9}
$$

uniformly over$m < \alpha , \left| h \right| \leq 1$and x in any compact set.

Proof. For$\alpha \in ( 0 , 1 ] , ( 2 . 9 )$is just a rewriting of the definition of$\mathcal { C ^ { \alpha } }$. For the general case, denote by$\mathcal { D } ^ { \alpha }$the space of T-valued functions such that (2.9) holds. Denote furthermore by$\mathcal { D } _ { i } \colon T  T$the linear map defined by$\mathcal { D } _ { i } X _ { j } = \delta _ { i j } \mathbf { 1 }$and extended to higher powers of X by the Leibniz rule. For$\hat { \varphi } \in \mathcal { D } ^ { \alpha }$with$\alpha > 1$, we then have that:

The bound (2.9) for$m = 0$implies that$\varphi = \langle \mathbf { 1 } , \boldsymbol { \hat { \varphi } } \rangle$is differentiable at x with ith directional derivative given by$\partial _ { i } \varphi ( x ) = \langle \mathbf { 1 } , { \cal D } _ { i } \hat { \varphi } ( x ) \rangle$

The case$m = 1$implies that the derivative$\partial _ { i } \varphi$is itself continuous.

Since the operators$\mathcal { D } _ { i }$commute with$\Gamma _ { h }$for every$h ,$one has$\mathcal { D } _ { i } \varphi \in \mathcal { D } ^ { \alpha - 1 }$for every$i \in \{ 1 , \ldots , d \}$

The claim then follows at once from the fact that this is precisely the recursive characterisation of the spaces$\mathcal { C ^ { \alpha } }$□

This now provides a very natural generalisation of H¨older spaces of arbitrary order to non-Euclidean scalings. Indeed, to a scaling s of$\mathbf { R } ^ { d }$, we can naturally associate the metric$d _ { \mathfrak { s } }$on$\mathbf { R } ^ { d }$given by

$$
d _ {\mathfrak {s}} (x, y) \stackrel {{\text { def }}} {{=}} \sum_ {i = 1} ^ {d} | x _ {i} - y _ {i} | ^ {1 / \mathfrak {s} _ {i}}.\tag{2.10}
$$

We will also use in the sequel the notation$| \mathfrak { s } | = \mathfrak { s } _ { 1 } + \ldots + \mathfrak { s } _ { d } ,$, which plays the role of a dimension. Indeed, with respect to the metric$d _ { \mathfrak { s } }$, the unit ball in$\mathbf { R } ^ { d }$is easily seen to have Hausdorff dimension s rather than$d .$Even though the right hand side of (2.10) does not define a norm (it is not 1-homogeneous, at least not in the usual sense), we will usually use the notation$d _ { \mathfrak { s } } ( x , y ) = \| x - y \| _ { \mathfrak { s } }$

Remark 2.13 It may occasionally be more convenient to use a metric with the same scaling properties as$d _ { \mathfrak { s } }$which is smooth away from the origin. In this case, one can for example take$p = 2 \ \mathrm { l c m } ( \mathfrak { s } _ { 1 } , . . . , \mathfrak { s } _ { d } )$and set

$$
\tilde {d} _ {\mathfrak {s}} (x, y) \stackrel {{\text { def }}} {{=}} \left(\sum_ {i = 1} ^ {d} | x _ {i} - y _ {i} | ^ {p / \mathfrak {s} _ {i}}\right) ^ {1 / p}.
$$

It is easy to see that$\tilde { d } _ { s }$and$d _ { \mathfrak { s } }$are equivalent in the sense that they are bounded by fixed multiples of each other. In the Euclidean setting,$d _ { \mathfrak { s } }$would be the$\ell ^ { 1 }$distance, while$\ddot { d } _ { \mathfrak { s } }$ would be the$\ell ^ { 2 }$distance.

With this notation at hand, and in view of Lemma 2.12, the following definition is very natural:

Definition 2.14 Given a scaling s on$\mathbf { R } ^ { d }$and$\alpha > 0$, we say that a function$\varphi \colon { \mathbf { R } } ^ { d }  { \mathbf { R } }$ is of class$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$if there exists a function$\hat { \varphi } \colon  { \mathbb { R } } ^ { d } \to T _ { \alpha } ^ { - }$with$\langle \mathbf { 1 } , \boldsymbol { \hat { \varphi } } ( x ) \rangle = \varphi ( x )$for every x and such that, for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$, one has

$$
\| \hat {\varphi} (x + h) - \Gamma_ {h} \hat {\varphi} (x) \| _ {m} \lesssim \| h \| _ {\mathfrak {s}} ^ {\alpha - m},\tag{2.11}
$$

uniformly over$m < \alpha , \| h \| _ { \mathfrak { s } } \le 1$and$x \in { \mathfrak { A } }$

Remark 2.15 One can verify that the map$x \mapsto \| x \| _ { s } ^ { \alpha }$is in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for$\alpha \in ( 0 , 1 ]$. Another well-known example [Wal86, Hai09] is that the solutions to the additive stochastic heat equation on the real line belong to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( \mathbf { R } ^ { 2 } )$for every$\alpha < \textstyle { \frac { 1 } { 2 } }$, provided that the scaling s is the parabolic scaling${ \mathfrak { s } } = ( 2 , 1 )$. (Here, the first component is the time direction.)

Remark 2.16 The choice of$\hat { \varphi }$in Definition 2.14 is essentially unique in the sense that any two choices$\hat { \varphi } _ { 1 }$and$\hat { \varphi } _ { 2 }$satisfy$\mathcal { Q } _ { \ell } \hat { \varphi } _ { 1 } ( x ) = \mathcal { Q } _ { \ell } \hat { \varphi } _ { 2 } ( x )$for every x and every $\ell < \alpha .$(Recall that$\mathcal { Q } _ { \ell }$is the projection onto$T _ { \ell } . )$This is because, similarly to the proof of Lemma 2.12, one can show that the components in$T _ { \ell }$have to coincide with the corresponding directional derivatives of$\varphi \mathrm { a t } x ,$and that, if$( 2 . 1 1 )$is satisfied locally uniformly in x, these directional derivatives exist and are continuous.

## 2.3 Models for regularity structures

In this section, we introduce the key notion of a “model” for a regularity structure, which was already alluded to several times in the introduction. Essentially, a model associates to each “abstract” element in$T \textrm { a }$“concrete” function or distribution on$\mathbf { R } ^ { d }$ In the above example, such a model was given by an interplay of the maps$\Pi _ { x }$that would associate to$a \in T$a polynomial on$\mathbf { R } ^ { d }$centred around$x ,$and the maps$\Gamma _ { h }$that allow to translate the polynomial in question to any other point in$\mathbf { R } ^ { d }$

This is the structure that we are now going to generalise and this is where our theory departs significantly from the theory of jets, as our model will typically contain elements that are extremely irregular. If we take again the case of the polynomial regularity structures as our guiding principle, we note that the index$\alpha \in A$describes the speed at which functions of the form$\Pi _ { x } a$with$a \in T _ { c }$<sub>α</sub> vanish near x. The action of Γ is then necessary in order to ensure that this behaviour is the same at every point. In general, elements in the image of$\Pi _ { x }$are distributions and not functions and the index α can be negative, so how do we describe the behaviour near a point?

One natural answer to this question is to test the distribution in question against approximations to a delta function and to quantify this behaviour. Given a scaling s, we thus define scaling maps

$$
\mathcal {S} _ {\mathfrak {s}} ^ {\delta} \colon \mathbf {R} ^ {d} \to \mathbf {R} ^ {d}, \quad \mathcal {S} _ {\mathfrak {s}} ^ {\delta} (x _ {1}, \ldots , x _ {d}) = (\delta^ {- \mathfrak {s} _ {1}} x _ {1}, \ldots , \delta^ {- \mathfrak {s} _ {d}} x _ {d}).\tag{2.12}
$$

These scaling maps yield in a natural way a family of isometries on$L ^ { 1 } ( \mathbf { R } ^ { d } )$by

$$
\left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \varphi\right) (y) \stackrel {{\text { def }}} {{=}} \delta^ {- | \mathfrak {s} |} \varphi \left(\mathcal {S} _ {\mathfrak {s}} ^ {\delta} (y - x)\right).\tag{2.13}
$$

They are also the natural scalings under which$\| \cdot \| _ { s }$behaves like a norm in the sense that$\| S _ { \mathfrak { s } } ^ { \delta } x \| _ { \mathfrak { s } } = \delta ^ { - 1 } \| x \| _ { \mathfrak { s } }$. Note now that if$P$is a monomial of scaled degree$\ell \geq 0$over $\mathbf { R } ^ { d }$(where the scaled degree simply means that the monomial$x _ { i }$has degree$s _ { i }$rather than 1) and$\varphi \colon { \mathbf { R } ^ { d } }  { \mathbf { R } }$is a compactly supported function, then we have the identity

$$
\begin{array}{c} \int P (y - x) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \varphi) (y)   d y = \int P (\delta^ {\mathfrak {s} _ {1}} z _ {1}, \ldots , \delta^ {\mathfrak {s} _ {d}} z _ {d}) \varphi (z)   d z \\ = \delta^ {\ell} \int P (z) \varphi (z)   d z  . \end{array}\tag{2.14}
$$

Following the philosophy of taking the case of polynomials / Taylor expansions as our source of inspiration, this simple calculation motivates the following definition.

Definition 2.17 A model for a given regularity structure$\mathcal { T } = ( A , T , G )$on$\mathbf { R } ^ { d }$with scaling s consists of the following elements:

• <sup>A</sup> <sup>map</sup>$\Gamma \colon \mathbf { R } ^ { d } \times \mathbf { R } ^ { d }  G$such that$\Gamma _ { x x } = 1$, the identity operator, and such that $\Gamma _ { x y } \Gamma _ { y z } = \Gamma _ { x z }$for every$x , y , z \mathrm { ~ i n ~ } \mathbf { R } ^ { d }$

●$\mathrm { A }$collection of continuous linear maps$\Pi _ { x } \colon T  S ^ { \prime } ( \mathbf { R } ^ { d } )$such that$\Pi _ { y } = \Pi _ { x } \circ \Gamma _ { x y }$ for every$\boldsymbol { x } , \boldsymbol { y } \in \mathbf { R } ^ { d }$

Furthermore, for every$\gamma > 0$and every compact set${ \bf q } _ { \mathrm { ~ \tiny ~ C ~ } } { \bf R } ^ { d }$, there exists a constant $C _ { \gamma , \mathscr { R } }$such that the bounds

$$
| (\Pi_ {x} a) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \varphi) | \leq C _ {\gamma , \mathfrak {K}} \| a \| \delta^ {\ell}, \| \Gamma_ {x y} a \| _ {m} \leq C _ {\gamma , \mathfrak {K}} \| a \| \| x - y \| _ {\mathfrak {s}} ^ {\ell - m},\tag{2.15}
$$

hold uniformly over all$x , y \in { \mathcal { R } } ,$, all$\delta \in ( 0 , 1 ]$, all smooth test functions$\varphi \colon B _ { \mathfrak { s } } ( 0 , 1 ) \to$ R with$\| \varphi \| _ { \mathcal { C } ^ { r } } \leq 1$, all$\ell \in A$with$\ell < \gamma$, all$m < \ell ,$and all$a \in T _ { \ell }$. Here, r is the smallest integer such that$\ell > - r$for every$\ell \in A$. (Note that$\| \Gamma _ { x y } a \| _ { m } = \| \Gamma _ { x y } a - a \| _ { n }$m since$a \in T _ { \ell }$and$m < \ell . )$

Remark 2.18 We will also sometimes call the pair (Π, Γ) a model for the regularity structure$\mathcal { T }$

The following figure illustrates a typical example of model for a simple regularity structure where$\bar { A } = \{ 0 , { \textstyle \frac { 1 } { 2 } } , 1 , { \textstyle \frac { 3 } { 2 } } \}$and each$T _ { \alpha }$is one-dimensional:

![](images/page_25_image_5.jpg)

Write$\tau _ { \alpha }$for the unit vector in$T _ { \alpha }$. Given a <sup>1</sup><sub>2</sub> -H¨older continuous function$f \colon \mathbf { R }  \mathbf { R } \quad$ the above picture has

$$
\left(\Pi_ {x} \tau_ {\frac {1}{2}}\right) (y) = f (y) - f (x), \quad \left(\Pi_ {x} \tau_ {\frac {3}{2}}\right) (y) = \int_ {x} ^ {y} \left(f (z) - f (x)\right) d z,
$$

while$\Pi _ { x } \tau _ { 0 }$and$\Pi _ { x } \tau _ { 1 }$are given by the canonical one-dimensional model of polynomials.

A typical action of$\Gamma _ { x y }$is illustrated below:

![](images/page_25_image_10.jpg)

Here, the left figure shows$\Pi _ { x } \tau _ { \frac { 3 } { \alpha } }$, while the right figure shows$\Pi _ { y } \tau _ { \frac { 3 } { 2 } } = \Pi _ { x } \Gamma _ { x y } \tau _ { \frac { 3 } { 2 } }$. In this particular example, this is obtained from$\Pi _ { x } \tau _ { \frac { 3 } { 7 } }$by adding a suitable affine function, i.e. a linear combination of$\Pi _ { x } \tau _ { 0 }$and$\Pi _ { x } \tau _ { 1 }$

Remark 2.19 Given a sector$V \subset T$, it will on occasion be natural to consider models for$\mathcal { T } _ { V }$rather than all of$\mathcal { T }$. In such a situation, we will say that (Π, Γ) is a model for $\mathcal { T }$on$V ,$, or just a model for V .

Remark 2.20 Given a map$( x , y ) \mapsto \Gamma _ { x y }$as above, the set of maps$x \mapsto \Pi _ { x }$as above is actually a linear space. We can endow it with the natural system of seminorms$\| \Pi \| _ { \gamma ; \mathbb { A } }$ given by the smallest constant$C _ { \gamma , \mathfrak { R } }$such that the first bound in (2.15) holds. Similarly, we denote by$\| \Gamma \| _ { \gamma ; \mathcal { R } }$the smallest constant$C _ { \gamma , \mathfrak { R } }$such that the second bound in (2.15) holds. Occasionally, it will be useful to have a notation for the combined bound, and we will then write

$$
\| Z \| _ {\gamma ; \mathfrak {K}} = \| \Pi \| _ {\gamma ; \mathfrak {K}} + \| \Gamma \| _ {\gamma ; \mathfrak {K}},\tag{2.16}
$$

where we set$Z = ( \Pi , \Gamma )$

Remark 2.21 The first bound in (2.15) could alternatively have been formulated as $\begin{array} { r } { | ( \Pi _ { x } a ) ( \varphi ) | \leq C \Vert a \Vert \delta ^ { \ell } } \end{array}$for all smooth test functions$\varphi$with support in a ball of radius $\delta$around x (in the d<sub>s</sub>-distance), which are bounded by$\delta ^ { - | \mathfrak { s } | }$<sup>|</sup> and such that their derivatives satisfy sup$\begin{array} { r } { \rangle _ { x } | D ^ { \ell } \varphi ( x ) | \le \delta ^ { - | \mathfrak { s } | - | \ell | _ { \mathfrak { s } } } } \end{array}$for all multiindices$\ell$of (usual) size less or equal to r.

One important notion is that of an extension of a model (Π, Γ):

Definition 2.22 Let$\mathcal { T } \subset \hat { \mathcal { T } }$be two regularity structures and let$( \Pi , \Gamma )$be a model for T. A model (Π<sup>ˆ</sup> , Γ<sup>ˆ</sup>) is said to extend (Π, Γ) for$\hat { \mathcal T }$if one has

$$
\iota \Gamma_ {x y} a = \hat {\Gamma} _ {x y} \iota a, \quad \Pi_ {x} a = \hat {\Pi} _ {x} \iota a,
$$

for every$a \in T$and every$x , y$in$\mathbf { R } ^ { d }$. Here, ι is as in Section 2.1.

We henceforth denote by$\mathcal { M } _ { \mathcal { T } }$the set of all models of$\mathcal { T }$, which is a slight abuse of notation since one should also fix the dimension d and the scaling s, but these are usually very clear from the context. This space is endowed with a natural system of pseudo-metrics by setting, for any two models$Z = ( \Pi , \Gamma )$and$\bar { Z } = ( \bar { \Pi } , \bar { \Gamma } )$,

$$
\| Z; \bar {Z} \| _ {\gamma ; \mathfrak {K}} \stackrel {\mathrm{def}} {=} \| \Pi - \bar {\Pi} \| _ {\gamma ; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}}.\tag{2.17}
$$

While$\| \cdot ; \cdot \| _ { \gamma ; \mathcal { R } }$defined in this way looks very much like a seminorm, the space$\mathcal { M } _ { \mathcal { T } }$is not a linear space due to the two nonlinear constraints

$$
\Gamma_ {x y} \Gamma_ {y z} = \Gamma_ {x z}, \mathrm{and} \Pi_ {y} = \Pi_ {x} \circ \Gamma_ {x y},\tag{2.18}
$$

and due to the fact that G is not necessarily a linear set of operators. While$\mathcal { M } _ { \mathcal { T } }$is not linear, it is however an algebraic variety in some infinite-dimensional Banach space.

Remark 2.23 In most cases considered below, our regularity structure contains$\mathcal { T } _ { d , \mathfrak { s } }$s for some dimension d and scaling s. In such a case, we denote by$\bar { T } \subset T$the image of the model space of$\mathcal { T }$in$T$under the inclusion map and we only consider models (Π, Γ) that extend (in the sense of Definition 2.22) the polynomial model on$\bar { T }$. It is straightforward to verify that the polynomial model does indeed verify the bounds and algebraic relations of Definition 2.17, provided that we make the identification $\Gamma _ { x y } \sim \Gamma _ { h }$with$h = x - y$

Remark 2.24 If, for every$a \in T _ { \ell } , \Pi _ { x } a$happens to be a function such that$| \Pi _ { x } a ( y ) | \leq$ $C \| x - y \| _ { s } ^ { \ell }$for y close to x, then the first bound in (2.15) holds for$\ell \geq 0$. Informally, it thus states that$\Pi _ { x } a$behaves$\mathrm { ^ { 6 6 } a s \ i f ^ { \circ } }$it were ℓ-H¨older continuous at$x .$. The formulation given here has the very significant advantage that it also makes sense for negative values of ℓ.

Remark 2.25 Given a linear map Π:<sup>¯</sup>$T \to S ^ { \prime } ( D )$, and a function$F \colon D \to G$, we can always set

$$
\Gamma_ {x y} = F (x) \cdot F (y) ^ {- 1}, \Pi_ {x} = \bar {\Pi} \circ F (x) ^ {- 1}.\tag{2.19}
$$

Conversely, given a model (Π, Γ) as above and a reference point o, we could set

$$
F (x) = \Gamma_ {x o}, \qquad \bar {\Pi} = \Pi_ {o},\tag{2.20}
$$

and$\Gamma$and Π could then be recovered from F and Π<sup>¯</sup> by (2.19). The reason why we choose to keep our seemingly redundant formulation is that the definition (2.17) and the bounds (2.15) are more natural in this formulation. We will see in Section 8.2 below that in all the cases mentioned in the introduction, there are natural maps Π<sup>¯</sup> and $F$such that (Π, Γ) are given by (2.19). These are however not of the form (2.20) for any reference point.

Remark 2.26 It follows from the definition (2.3) that the second bound in (2.15) is equivalent to the bound

$$
\| \log \Gamma_ {x y} a \| _ {m} \lesssim \| a \| \| x - y \| _ {\mathfrak {s}} ^ {\ell - m},\tag{2.21}
$$

for all$a \in T _ { \ell }$. Similarly, one can consider instead of (2.17) the equivalent distance obtained by replacing$\Gamma _ { x y }$by log$\Gamma _ { x y }$and similarly for${ \bar { \Gamma } } _ { x y }$

Remark 2.27 The reason for separating the notion of a regularity structure from the notion of a model is that, in the type of applications that we have in mind, the regularity structure will be fixed once and for all. The model however will typically be random and there will be a different model for the regularity structure for every realisation of the driving noise.

## 2.4 Automorphisms of regularity structures

There is a natural notion of “automorphism” of a given regularity structure. For this, we first define the set$L _ { 0 } ^ { + }$of linear maps$L \colon T \to T$such that, for every$\alpha \in A$there exists$\gamma \in A$such that La$\in \oplus _ { \alpha < \beta \leq \gamma } T _ { \beta }$for every$a \in T _ { \alpha }$. We furthermore denote by$L _ { 1 } ^ { + }$Lthe set of all linear operators$Q$of the form

$$
Q a - a = L a, \quad L \in L _ {0} ^ {+}.
$$

Finally, we denote by$L ^ { 0 }$the set of invertible “block-diagonal” operators D such that $D T _ { \alpha } \subset T _ { \alpha }$for every$\alpha \in A$

With these notations at hand, denote by$L ^ { + }$the set of all operators of the form

$$
M = D \circ Q, \qquad D \in L ^ {0}, \quad Q \in L _ {1} ^ {+}.
$$

This factorisation is unique since it suffices to define$\begin{array} { r } { D = \sum _ { \alpha \in A } \mathcal { Q } _ { \alpha } M \mathcal { Q } _ { \alpha } } \end{array}$and to set $Q = D ^ { - 1 } M$, which yields an element of$L _ { 1 } ^ { + }$P. Note also that conjugation by blockdiagonal operators preserves$L _ { 1 } ^ { + }$. Furthermore, elements in$L _ { 1 } ^ { + }$can be inverted by using the identity

$$
(1 - L) ^ {- 1} = 1 + \sum_ {n \geq 1} L ^ {n},\tag{2.22}
$$

although this might map some elements of$T _ { \alpha }$into an infinite series. With all of these notations at hand, we then give the following definition:

Definition 2.28 Given a regularity structure$\mathcal { T } ~ = ~ ( A , T , G )$, its group of automorphisms Aut$\mathcal { T }$is given by

$$
\operatorname{Aut} \mathcal {T} = \left\{M \in L ^ {+}: M ^ {- 1} \Gamma M \in G \quad \forall \Gamma \in G \right\}.
$$

Remark 2.29 This is really an abuse of terminology since it might happen that Aut$\mathcal { T }$ contains some elements in whose inverse maps finite series into infinite series and therefore does not belong to$L ^ { + }$. In most cases of interest however, the index set A is finite, in which case Aut$\mathcal { T }$is always an actual group.

The reason why Aut$\mathcal { T }$is important is that its elements induce an action on the models for$\mathcal { T }$by

$$
R _ {M} \colon (\Pi , \Gamma) \mapsto (\bar {\Pi}, \bar {\Gamma}), \quad \bar {\Pi} _ {x} = \Pi_ {x} M, \quad \bar {\Gamma} _ {x y} = M ^ {- 1} \Gamma_ {x y} M.
$$

One then has:

Proposition 2.30 For every$M \in \mathrm { A u t } \mathcal { T } , R _ { M }$is a continuous map from$\mathcal { M } _ { \mathcal { T } }$into itself.

Proof. It is clear that the algebraic identities (2.18) are satisfied, so we only need to check that the analytical bounds of Definition$2 . 1 7$hold for$( { \bar { \Pi } } , { \bar { \Gamma } } )$

For Π, this is straightforward since, for$a \in T _ { \alpha }$and any$M \in L ^ { + }$, one has

$$
\begin{array}{c} \bar {\Pi} _ {x} a (\psi_ {x} ^ {\lambda}) = \Pi_ {x} M a (\psi_ {x} ^ {\lambda}) = \sum_ {\beta \in A \cap [ \alpha , \gamma ]} \Pi_ {x} \mathcal {Q} _ {\beta} M a (\psi_ {x} ^ {\lambda}) \\ \leq C \| a \| _ {\alpha} \sum_ {\beta \in A \cap [ \alpha , \gamma ]} \lambda^ {\beta} \leq \tilde {C} \lambda^ {\alpha} \| a \| _ {\alpha}, \end{array}
$$

where, for a given test function$\psi$we use the shorthand$\psi _ { x } ^ { \lambda } = S _ { \mathfrak { s } , x } ^ { \lambda } \psi$and where$\tilde { C }$is a finite constant depending only on the norms of the components of M and on the value γ appearing in the definition of$L ^ { + }$

For Γ, we similarly write, for$a \in T _ { \alpha }$and$\beta < \alpha$

$$
\begin{array}{l} \| (\bar {\Gamma} _ {x y} - 1) a \| _ {\beta} = \| M ^ {- 1} (\Gamma_ {x y} - 1) M a \| _ {\beta} \leq C \sum_ {\zeta \leq \beta} \| (\Gamma_ {x y} - 1) M a \| _ {\zeta} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq C \sum_ {\zeta \leq \beta} \sum_ {\xi \geq \zeta} \| M a \| _ {\xi} \| x - y \| _ {\mathfrak {s}} ^ {\xi - \zeta} \leq C \sum_ {\zeta \leq \beta} \sum_ {\xi \geq (\zeta \vee \alpha)} \| a \| _ {\alpha} \| x - y \| _ {\mathfrak {s}} ^ {\xi - \zeta}. \end{array}
$$

Since one has on the one hand$\zeta \leq \beta$and on the other hand$\xi \ge \alpha$, all terms appearing in this sum involve a power of$\| x - y \| _ { \mathsf { s } }$<sub>s</sub> that is at least equal to$\alpha - \beta$. Furthermore, the sum is finite by the definition of$L ^ { + }$, so that the claim follows at once.□

## 3 Modelled distributions

Given a regularity structure$\mathcal { T }$, as well as a model (Π, Γ), we are now in a position to describe a class of distributions that locally “look like” the distributions in the model. Inspired by Definition 2.14, we define the space$\mathcal { D } ^ { \gamma }$(which depends in general not only on the regularity structure, but also on the model) in the following way.

Definition 3.1 Fix a regularity structure$\mathcal { T }$and a model (Π, Γ). Then, for any$\gamma \in \mathbf { R }$ the space$\mathcal { D } ^ { \gamma }$consists of all$T _ { \gamma } ^ { - }$-valued functions$f$such that, for every compact set $\mathcal { R } \subset \mathbf { R } ^ { d }$, one has

$$
\| f\|_{\gamma ;\mathfrak{K}} = \sup_{x\in \mathfrak{K}}\sup_{\beta <  \gamma}\| f(x)\|_{\beta} + \sup_{\substack{(x,y)\in \mathfrak{K}\\ \| x - y\|_{\mathfrak{s}}\leq 1}}\sup_{\beta <  \gamma}\frac{\|f(x) - \Gamma_{xy}f(y)\|_{\beta}}{\|x - y\|_{\mathfrak{s}}^{\gamma - \beta}} <  \infty   .\tag{3.1}
$$

Here, the supremum runs only over elements$\beta \in A .$We call elements of$\mathcal { D } ^ { \gamma }$modelled distributions for reasons that will become clear in Theorem 3.10 below.

Remark 3.2 One could alternatively think of$\mathcal { D } ^ { \gamma }$as consisting of equivalence classes of functions where$f \sim g \mathrm { i f } \ Q _ { \alpha } f ( x ) = \ Q _ { \alpha } g ( x )$for every$\bar { \boldsymbol { x } } \in \bar { \mathbf { R } ^ { d } }$and every$\alpha \ <$ $\gamma .$However, any such equivalence class has one natural distinguished representative, which is the function$f$such that$\mathcal { Q } _ { \alpha } f ( x ) = 0$for every α$\geq \gamma$, and this is the representative used in (3.1). (In general, the norm$\| \cdot \| _ { \gamma ; \mathbb { A } }$would depend on the choice of representative because$\Gamma _ { x y } \tau$can have components in$T _ { \gamma } ^ { - }$even$\mathrm { i f } ~ \tau$itself doesn’t.) In the sequel, if we state that$f \in \mathcal { D } ^ { \gamma }$for some$f$which does not necessarily take values in$T _ { \gamma } ^ { - }$, it is this representative that we are talking about. This also allows to identify <sup>γ¯</sup> as a subspace of$\mathcal { D } ^ { \gamma }$for any$\bar { \gamma } > \gamma$. (Verifying that this is indeed the case is a useful exercise!)

Remark 3.3 The choice of notation$\mathcal { D } ^ { \gamma }$is intentionally close to the notation$\mathcal { C } ^ { \gamma }$for the space of γ-H¨older continuous functions since, in the case of the “canonical” regularity structures built from polynomials, the two spaces essentially agree, as we saw in Section 2.2.

Remark 3.4 The spaces$\mathcal { D } ^ { \gamma }$, as well as the norms$\| \cdot \| _ { \gamma ; \mathcal { R } }$do depend on the choice of Γ, but not on the choice of Π. However, Definition 2.17 strongly interweaves Γ and Π, so that a given choice of Γ typically restricts the choice of Π very severely. As we will see in Proposition 3.31 below, there are actually situations in which the choice of Γ completely determines Π. In order to compare elements of spaces$\mathcal { D } ^ { \gamma }$corresponding to different choices of Γ, say$f \in { \mathcal { D } } ^ { \gamma } ( \Gamma )$and$\bar { f } \in \mathcal { D } ^ { \gamma } ( \bar { \Gamma } )$, it will be convenient to introduce the norm

$$
\| f - \bar {f} \| _ {\gamma ; \mathfrak {K}} = \sup _ {x \in \mathfrak {K}} \sup _ {\beta <   \gamma} \| f (x) - \bar {f} (x) \| _ {\beta},
$$

which is independent of the choice of Γ. Measuring the distance between elements of $\mathcal { D } ^ { \gamma }$in the norm$\| \cdot \| _ { \gamma ; \mathbb { A } }$will be sufficient to obtain some convergence properties, as long as this is supplemented by uniform bounds in$\| \cdot \| _ { \gamma ; \mathbb { A } }$

Remark 3.5 It will often be advantageous to consider elements of$\mathcal { D } ^ { \gamma }$that only take values in a given sector$V$of$T$. In this case, we use the notation${ \mathcal { D } } ^ { \gamma } ( V )$instead. In cases where$V$is of regularity α for some$\alpha \geq$min A, we will also occasionally use instead the notation$\mathcal { D } _ { \alpha } ^ { \gamma }$to emphasise this additional regularity. Occasionally, we will also write$\mathcal { D } ^ { \gamma } ( \Gamma )$or$\bar { \mathcal { D } } ^ { \gamma } ( \Gamma ; V )$to emphasise the dependence of these spaces on the particular choice of Γ.

Remark 3.6 A more efficient way of comparing elements$f \in { \mathcal { D } } ^ { \gamma } ( \Gamma )$and$\bar { f } \in \mathcal { D } ^ { \gamma } ( \bar { \Gamma } )$ for two different models (Π, Γ) and (Π<sup>¯</sup> , Γ<sup>¯</sup>) is to introduce the quantity

$$
\| f;\bar{f}\|_{\gamma ;\mathfrak{K}} = \| f - \bar{f}\|_{\gamma ;\mathfrak{K}} + \sup_{\substack{(x,y)\in \mathfrak{K}\\ \| x - y\|_{\mathfrak{s}}\leq 1}}\sup_{\beta <  \gamma}\frac{\|f(x) - \bar{f} (x) - \Gamma_{xy}f(y) + \bar{\Gamma}_{xy}\bar{f} (y)\|_{\beta}}{\|x - y\|_{\mathfrak{s}}^{\gamma - \beta}}  .
$$

Note that this quantity is not a function of$f - { \bar { f } } .$, which is the reason for the slightly unusual notation$\| f ; { \bar { f } } \| _ { \gamma ; { \mathcal { R } } }$

It turns out that the spaces$\mathcal { D } ^ { \gamma }$encode a very useful notion of regularity. The idea is that functions$f \in \mathcal { D } ^ { \gamma }$should be interpreted as$\mathrm { ^ { 6 6 } j e t s ^ { , 9 } }$of distributions that locally, around any given point$\boldsymbol { x } \in \mathbf { R } ^ { d }$, “look$\mathrm { l i k e } ^ { \prime \prime }$the model distribution$\Pi _ { x } f ( x ) \in S ^ { \prime }$. The results of this section justify this point of view by showing that it is indeed possible to “reconstruct” all elements of$\mathcal { D } ^ { \gamma }$as distributions in$\mathbf { R } ^ { d }$. Furthermore, the corresponding reconstruction map is continuous as a function of both the element in$f \in \mathcal { D } ^ { \gamma }$and the model (Π, Γ) realising the regularity structure under consideration.

To this end, we further extend the definition of the H¨older spaces$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$to include exponents$\alpha < 0 ,$, consisting of distributions that are suitable for our purpose. Informally speaking, elements of$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$have scaling properties akin to$\| x - y \| _ { s } ^ { \alpha }$when tested against a test function localised around some$\boldsymbol { x } \in \mathbf { R } ^ { d }$. In the following definition, we write$\mathcal { C } _ { 0 } ^ { r }$ for the space of compactly supported${ \mathcal { C } } ^ { r }$functions. For further properties of the spaces $\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$, see Section 3.2 below. We set:

Definition 3.7 Let$\alpha < 0$and let$r = - \lfloor \alpha \rfloor$. We say that$\xi \in { \cal S } ^ { \prime }$belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$if it belongs to the dual of$\mathcal { C } _ { 0 } ^ { r }$and, for every compact set K, there exists a constant$C$such that the bound

$$
\langle \xi , \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle \leq C \delta^ {\alpha}  ,
$$

holds for all$\eta \in \mathcal { C } ^ { r }$with$\| \eta \| _ { C ^ { r } } \leq 1$and supp$\eta \subset B _ { \mathfrak { s } } ( 0 , 1 )$, all$\delta \leq 1$, and all$x \in { \mathfrak { A } }$ Here,$B _ { \mathfrak { s } } ( 0 , 1 )$denotes the ball of radius 1 in the distance$d _ { \mathfrak { s } }$, centred at the origin.

From now on, we will denote by$B _ { { \mathfrak { s } } , 0 } ^ { r }$the set of all test functions η as in Definition 3.7. For$\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$and K a compact set, we will henceforth denote by$\| \xi \| _ { \alpha ; \mathcal { R } }$the seminorm given by

$$
\| \xi \| _ {\alpha ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \sup _ {x \in \mathfrak {K}} \sup _ {\eta \in \mathcal {B} _ {\mathfrak {s}, 0} ^ {r}} \sup _ {\delta \leq 1} \delta^ {- \alpha} | \langle \xi , \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle |.\tag{3.2}
$$

We also write$\| \cdot \| _ { \alpha }$for the same expression with$\mathcal { R } = \mathbf { R } ^ { d }$

Remark 3.8 The space$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$is essentially the Besov space$B _ { \infty , \infty } ^ { \alpha }$(see e.g. [Mey92]), with the slight difference that our definition is local rather than global and, more importantly, that it allows for non-Euclidean scalings.

Remark 3.9 The seminorm (3.2) depends of course not only on$\alpha ,$but also on the choice of scaling s. This scaling will however always be clear from the context, so we do not emphasise this in the notation.

The following “reconstruction theorem” is one of the main workhorses of this theory.

Theorem 3.10 (Reconstruction theorem) Let$\mathcal { T } = ( A , T , G )$be a regularity structure, let (Π, Γ) be a modelfor$\mathcal { T }$on$\mathbf { R } ^ { d }$with scaling s, let α = min A, and let$r > | \alpha |$

Then,for every$\gamma \in \mathbf { R }$, there exists a continuous linear map$\mathcal { R } \colon \mathcal { D } ^ { \gamma }  \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$with the property that, for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$

$$
| (\mathcal {R} f - \Pi_ {x} f (x)) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) | \lesssim \delta^ {\gamma} \| \Pi \| _ {\gamma ; \bar {\mathfrak {K}}} \| f \| _ {\gamma ; \bar {\mathfrak {K}}},\tag{3.3}
$$

uniformly over all test functions$\eta \in B _ { \mathfrak { s } , 0 } ^ { r } ,$all$\delta \in ( 0 , 1 ]$, all$f \in \mathcal { D } ^ { \gamma }$, and all$x \in { \mathfrak { A } }$If $\gamma > 0 ;$, then the bound (3.3) defines$\mathcal { R } f$uniquely. Here, we denoted by K<sup>¯</sup> the 1-fattening $o f \mathbb { A } ,$and the proportionality constant depends only on γ and the structure of$\mathcal { T }$.

Furthermore, if (Π<sup>¯</sup> , Γ<sup>¯</sup>) is a second model for$\mathcal { T }$with associated reconstruction operator${ \bar { \mathcal { R } } } ,$, then one has the bound

$$
\left| \left(\mathcal {R} f - \bar {\mathcal {R}} \bar {f} - \Pi_ {x} f (x) + \bar {\Pi} _ {x} \bar {f} (x)\right) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta\right) \right| \lesssim \delta^ {\gamma} \left(\left\| \bar {\Pi} \right\| _ {\gamma ; \bar {\mathfrak {K}}} \| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \left\| \Pi - \bar {\Pi} \right\| _ {\gamma ; \bar {\mathfrak {K}}} \| f \| _ {\gamma ; \bar {\mathfrak {K}}}\right), \tag {3.4}
$$

uniformly over x and η as above. Finally,for$0 < \kappa < \gamma / ( \gamma - \alpha )$and for every$C > 0 _ { i }$ one has the bound

$$
\begin{array}{c} | (\mathcal {R} f - \bar {\mathcal {R}} \bar {f} - \Pi_ {x} f (x) + \bar {\Pi} _ {x} \bar {f} (x)) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) | \\ \lesssim \delta^ {\bar {\gamma}} (\| f - \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} ^ {\kappa} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} ^ {\kappa} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \bar {\mathfrak {K}}} ^ {\kappa}), \end{array}\tag{3.5}
$$

where we set$\bar { \gamma } = \gamma - \kappa ( \gamma - \alpha )$, and where we assume that$\| f \| _ { \gamma ; \bar { \mathcal { R } } } , \| \Pi \| _ { \gamma ; \bar { \mathcal { R } } }$and$\| \Gamma \| _ { \gamma ; \bar { \mathcal { R } } }$ are bounded by$C ,$and similarlyfor <sup>¯</sup>f, Π<sup>¯</sup> and Γ<sup>¯</sup>.

Remark 3.11 At first sight, it might seem surprising that Γ does not appear in the bound (3.3). It does however appear in a hidden way through the definition of the spaces$\mathcal { D } ^ { \gamma }$and thus of the norm$\| f \| _ { \gamma ; { \bar { \mathcal { R } } } } .$. Furthermore, (3.3) is quite reasonable since, for Γ fixed, the map$\mathcal { R }$is actually bilinear in$f$and Π. However, the mere existence of depends crucially on the nonlinear structure encoded in Definition 2.17, and the spaces$\mathcal { D } ^ { \gamma }$do depend on the choice of Γ. Occasionally, when the particular model (Π, Γ) plays a role, we will denote$\mathcal { R }$by$\mathcal { R } _ { \mathrm { I } }$in order to emphasise its dependence on Γ.

Remark 3.12 Setting$\tilde { f } ( y ) = f ( y ) - \Gamma _ { y x } f ( x )$, we note that one has

$$
\mathcal {R} f - \Pi_ {x} f (x) = \mathcal {R} \tilde {f} - \Pi_ {x} \tilde {f} (x) = \mathcal {R} \tilde {f}.
$$

As a consequence, the bound (3.3) actually depends only on the second term in the right hand side of (3.1).

Remark 3.13 In the particular case when$( { \bar { \Pi } } , { \bar { \Gamma } } ) = ( \Pi , \Gamma )$, the bound (3.4) is a trivial consequence of (3.3) and the bilinearity of  in$f$and Π. As it stands however, this bound needs to be stated and proved separately. The bound (3.5) can be interpreted as an interpolation theorem between (3.3) and (3.4).

Proof(uniqueness only). The uniqueness of the map in the case$\gamma > 0$is quite easy to prove. Take$f \in \mathcal { D } ^ { \gamma }$as in the statement and assume that the two distributions$\xi _ { 1 }$ and$\xi _ { 2 }$are candidates for f that both satisfy the bound (3.3). Our aim is to show that one then necessarily has$\xi _ { 1 } = \xi _ { 2 }$. Take any smooth compactly supported test function $\psi : \mathbf { R } ^ { d } \to \mathbf { R }$, and choose an even smooth function η :$B _ { 1 } \to { \bf R } _ { + }$with$\textstyle \int \eta ( x ) d x = 1$ Define

$$
\psi_ {\delta} (y) = \left\langle \mathcal {S} _ {\mathfrak {s}, y} ^ {\delta} \eta , \psi \right\rangle = \int \psi (x) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta\right) (y) d x,
$$

so that, for any distribution$\xi ,$one has the identity

$$
\xi (\psi_ {\delta}) = \int \psi (x) \left\langle \xi , \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle d x.\tag{3.6}
$$

Choosing$\xi = \xi _ { 2 } - \xi _ { 1 }$, it then follows from (3.3) that

$$
| \xi (\psi_ {\delta}) | \lesssim \delta^ {\gamma} \int_ {D} \psi (x)   \bar {\varrho} (x)   d x  ,
$$

which converges to 0 as$\delta  0$. On the other hand, one has$\psi _ { \delta }  \psi$in the${ \mathcal { C } } ^ { \infty }$topology, so that$\xi ( \psi _ { \delta } ) \to \xi ( \psi )$. This shows that$\xi ( \psi ) = 0$for every smooth compactly supported test function ψ, so that$\xi = 0$

The existence of a map with the required properties is much more difficult to establish, and this is the content of the remainder of this section.□

Remark 3.14 We call the map  the “reconstruction map” as it allows to reconstruct a distribution in terms of its local description via a model and regularity structure.

Remark 3.15 One very important special case is when the model (Π, Γ) happens to be such that there exists$\alpha > 0$such that$\Pi _ { x } a \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( \mathbf { R } ^ { d } )$for every$a \in T$, even though the homogeneity of a might be negative. In this case, for$f \in \mathcal { D } ^ { \gamma }$with$\gamma > 0 , \mathcal { R } f$is a continuous function and one has the identity$( \mathcal { R } f ) ( x ) = \big ( \Pi _ { x } f ( x ) \big ) ( x )$. Indeed, setting $\tilde { \mathcal { R } } f ( x ) = ( \Pi _ { x } f ( x ) ) ( x )$, one has

$$
| \tilde {\mathcal {R}} f (y) - \tilde {\mathcal {R}} f (x) | \leq | (\Pi_ {x} f (x)) (x) - (\Pi_ {x} f (x)) (y) | + | \Pi_ {y} (\Gamma_ {y x} f (x) - f (y)) (y) |.
$$

By assumption, the first term is bounded by$C \| x - y \| _ { s } ^ { \alpha }$for some constant C. The second term on the other hand is bounded by$C \| x - y \| _ { s } ^ { \gamma }$by the definition of$\mathcal { D } ^ { \gamma }$ combined with the fact that our assumption on the model implies that$( \Pi _ { x } a ) ( x ) = 0$ whenever a is homogeneous of positive degree.

A straightforward corollary of this result is given by the following statement, which is the a posteriori justification for the terminology “regularity” in Definition 2.5:

Corollary 3.16 In the context of the statement of Theorem 3.10, if f takes values in a sector V ofregularity$\beta \in [ \alpha , 0 )$, then one has$\mathcal { R } f \in \mathcal { C } _ { \mathfrak { s } } ^ { \beta }$and, for every compact set K and$\gamma > 0 ,$, there exists a constant C such that

$$
\| \mathcal {R} f \| _ {\beta ; \mathfrak {K}} \leq C \| \Pi \| _ {\gamma ; \bar {\mathfrak {K}}} \| f \| _ {\gamma ; \bar {\mathfrak {K}}}.
$$

Proof. Immediate from (3.3), Remark 2.20, and the definition of$\| \cdot \| _ { \beta ; \mathscr { R } } .$

Before we proceed to the remainder of the proof of Theorem 3.10, we introduce some of the basic notions of wavelet analysis required for its proof. For a more detailed introduction to the subject, see for example [Dau92, Mey92].

## 3.1 Elements of wavelet analysis

Recall that a multiresolution analysis of R is based on a real-valued “scaling function” $\varphi \in L ^ { 2 } ( \mathbf R )$with the following two properties:

1. One has$\begin{array} { r } { \int \varphi ( x ) \varphi ( x + k ) d x = \delta _ { k , 0 } } \end{array}$for every$k \in \mathbf { Z }$

2. There exist “structure constants” a such that

$$
\varphi (x) = \sum_ {k \in \mathbf {Z}} a _ {k} \varphi (2 x - k).\tag{3.7}
$$

One classical example of such a function$\varphi$is given by the indicator function$\varphi ( x ) =$ ${ \bf 1 } _ { [ 0 , 1 ) } ( x )$, but this has the substantial drawback that it is not even continuous. A celebrated result by Daubechies (see the original article [Dau88] or for example the monograph [Dau92]) ensures the existence of functions$\varphi$as above that are compactly supported but still regular:

Theorem 3.17 (Daubechies) For every$r > 0$there exists a compactly supportedfunction$\varphi$with the two properties above and such that$\varphi \in \mathcal { C } ^ { r } ( \mathbf { R } )$□

From now on, we will always assume that the scaling function$\varphi$is compactly supported. Denote now$\Lambda _ { n } = \{ 2 ^ { - n } k : k \in \mathbf { Z } \}$and, for$n \in \mathbf { Z }$and$x \in \Lambda _ { n }$, set

$$
\varphi_ {x} ^ {n} (y) = 2 ^ {n / 2} \varphi \bigl (2 ^ {n} (y - x) \bigr).\tag{3.8}
$$

One furthermore denotes by$V _ { n } \subset L ^ { 2 } ( \mathbf { R } )$the subspace generated by$\{ \varphi _ { x } ^ { n } : x \in \Lambda _ { n } \}$ Property$2$above then ensures that these spaces satisfy the inclusion$V _ { n } \subset V _ { n + 1 }$for every$n .$Furthermore, it turns out that there is a simple description of the orthogonal complement$V _ { n } ^ { \perp }$of$V _ { n }$in$V _ { n + 1 }$. It turns out that it is possible to find finitely many coefficients$b _ { k }$such that, setting

$$
\psi (x) = \sum_ {k \in \mathbf {Z}} b _ {k} \varphi (2 x - k),\tag{3.9}
$$

and defining$\psi _ { x } ^ { n }$similarly to (3.8), the space$V _ { n } ^ { \perp }$is given by the linear span of$\{ \psi _ { x } ^ { n } ~ :$ $x \in \Lambda _ { n } \}$, see for example [Pin02, Chap. 6.4.5]. (One has actually$b _ { k } = ( - 1 ) ^ { k } a _ { 1 - k }$ but this isn’t important for us.) The following result is taken from [Mey92]:

Theorem 3.18 One has$\langle \psi _ { x } ^ { n } , \psi _ { y } ^ { m } \rangle = \delta _ { n , m } \delta _ { x , y }$for every${ \boldsymbol { n } } , { \boldsymbol { m } } \in \mathbf { Z }$and every$x \in \Lambda _ { n } ,$ $y \in \Lambda _ { m } .$Furthermore,$\langle \varphi _ { x } ^ { n } , \psi _ { y } ^ { \breve { m } } \rangle = 0 f o r$every m$\geq n$and every$x \in \Lambda _ { n } , y \in \Lambda _ { m } .$ Finally, for every$n \in \mathbf { Z } ,$, the set

$$
\left\{\varphi_ {x} ^ {n}: x \in \Lambda_ {n} \right\} \cup \left\{\psi_ {x} ^ {m}: m \geq n, x \in \Lambda_ {m} \right\},
$$

forms an orthonormal basis of$L ^ { 2 } ( \mathbf { R } )$.

Intuitively, one should think of the$\varphi _ { x } ^ { n }$as providing a description of a function at scales down to$2 ^ { - n }$and the$\psi _ { x } ^ { m }$as “filling in the details” at even smaller scales. In particular, for every function$f \in L ^ { 2 }$, one has

$$
\lim _ {n \rightarrow \infty} \mathcal {P} _ {n} f \stackrel {{\text { def }}} {{=}} \lim _ {n \rightarrow \infty} \sum_ {x \in \Lambda_ {n}} \langle f, \varphi_ {x} ^ {n} \rangle \varphi_ {x} ^ {n} = f,\tag{3.10}
$$

and this relation actually holds for much larger classes of$f ,$including sufficiently regular tempered distributions [Mey92].

One very useful properties of wavelets, which can be found for example in [Mey92, Chap. 3.2], is that the functions$\psi _ { x } ^ { m }$automatically have vanishing moments:

Lemma 3.19 Let$\varphi$be a compactly supported scaling function as above which is${ \mathcal { C } } ^ { r }$ $f o r \ r \ge 0$and let ψ be defined by (3.9). Then,$\begin{array} { r } { \int _ { \mathbf { R } } \psi ( x ) x ^ { m } d x = 0 f o r } \end{array}$every integer m$\downharpoonright$□

For our purpose, we need to extend this construction to$\mathbf { R } ^ { d }$. Classically, such an extension can be performed by simply taking products of the$\varphi _ { x } ^ { n }$for each coordinate. In our case however, we want to take into account the fact that we consider non-trivial scalings. For any given scaling s of$\mathbf { R } ^ { d }$and any$n \in \mathbf { Z } ,$, we thus define

$$
\Lambda_ {n} ^ {\mathfrak {s}} = \left\{\sum_ {j = 1} ^ {d} 2 ^ {- n \mathfrak {s} _ {j}} k _ {j} e _ {j}: k _ {j} \in \mathbf {Z} \right\} \subset \mathbf {R} ^ {d},
$$

where we denote by$e _ { j }$the jth element of the canonical basis of$\mathbf { R } ^ { d }$. For every$x \in \Lambda _ { n } ^ { \mathfrak { s } }$ we then set

$$
\varphi_ {x} ^ {n, \mathfrak {s}} (y) \stackrel {{\text { def }}} {{=}} \prod_ {j = 1} ^ {d} \varphi_ {x _ {j}} ^ {n \mathfrak {s} _ {j}} (y _ {j})  .\tag{3.11}
$$

Since we assume that$\varphi$is compactly supported, it follows from (3.7) that there exists a finite collection of vectors$\kappa \subset \Lambda _ { 1 } ^ { \mathfrak { s } }$and structure constants$\{ a _ { k } : k \in \mathcal K \}$such that the identity

$$
\varphi_ {x} ^ {0, \mathfrak {s}} (y) = \sum_ {k \in \mathcal {K}} a _ {k} \varphi_ {x + k} ^ {1, \mathfrak {s}} (y),\tag{3.12}
$$

holds. In order to simplify notations, we will henceforth use the notation

$$
2 ^ {- n \mathfrak {s}} k = \left(2 ^ {- n \mathfrak {s} _ {1}} k _ {1}, \dots , 2 ^ {- n \mathfrak {s} _ {d}} k _ {d}\right),
$$

so that the scaling properties of the$\varphi _ { x } ^ { n , { \mathfrak { s } } }$combined with (3.12) imply that

$$
\varphi_ {x} ^ {n, \mathfrak {s}} (y) = \sum_ {k \in \mathcal {K}} a _ {k} \varphi_ {x + 2 ^ {- n \mathfrak {s}} k} ^ {n + 1, \mathfrak {s}} (y).\tag{3.13}
$$

Similarly, there exists a finite collection$\Psi$of orthonormal compactly supported functions such that, if we define$V _ { n }$similarly as before,$V _ { n } ^ { \perp }$is given by

$$
V _ {n} ^ {\perp} = \operatorname{span} \left\{\psi_ {x} ^ {n, \mathfrak {s}}: \psi \in \Psi x \in \Lambda_ {n} ^ {\mathfrak {s}} \right\}.
$$

In this expression, given a function ψ$\mathbf { \Psi } ) \in \Psi$, we have set$\psi _ { x } ^ { n , 5 } = 2 ^ { - n | \mathfrak { s } | / 2 } S _ { \mathfrak { s } , x } ^ { 2 ^ { - n } } \mathfrak { v }$ψ, where the scaling map was defined in (2.13). (The additional factor makes sure that the scaling leaves the$L ^ { 2 }$norm invariant instead of the$L ^ { 1 }$norm, which is more convenient in this context.) Furthermore, this collection forms an orthonormal basis of$V _ { n } ^ { \perp }$. Actually, the set Ψ is given by all functions obtained by products of the form$\Pi _ { i = 1 } ^ { d } \psi _ { \pm } ( x _ { i } )$, where $\psi _ { - } = \psi$and$\psi _ { + } = \varphi _ { : }$, and where at least one factor consists of an instance of$\psi .$.

## 3.2 A convergence criterion in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$

The spaces$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$with$\alpha < 0$given in Definition 3.7 enjoy a number of remarkable properties that will be very useful in the sequel. In particular, it turns out that distributions in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$can be completely characterised by the magnitude of the coefficients in their wavelet expansion. This is true independently of the particular choice of the scaling function$\varphi ,$, provided that it has sufficient regularity.

In this sense, the interplay between the wavelet expansion and the spaces$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$is very similar to the classical interplay between Fourier expansion and fractional Sobolev spaces. The feature of wavelet expansions that makes it much more suitable for our purpose is that its basis functions are compactly supported with supports that are more and more localised for larger values of n. The announced characterisation is given by the following.

Proposition 3.20 Let$\alpha < 0$and$\xi \in \mathcal { S } ^ { \prime } ( \mathbf { R } ^ { d } )$. Consider a wavelet analysis as above with a compactly supported scalingfunction$\varphi \in \mathcal { C } ^ { r }$for some$r > | \alpha | .$. Then$\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$if and only$i f \xi$belongs to the dual$o f { \mathcal { C } } _ { 0 } ^ { r }$and,for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$, the bounds

$$
| \langle \xi , \psi_ {x} ^ {n, \mathfrak {s}} \rangle | \lesssim 2 ^ {- \frac {n | \mathfrak {s} |}{2} - n \alpha}, \qquad | \langle \xi , \varphi_ {y} ^ {0} \rangle | \lesssim 1,\tag{3.14}
$$

hold uniformly over$n \geq 0 ,$every$\psi \in \Psi$, every$x \in \Lambda _ { n } ^ { \mathfrak { s } } \cap \mathfrak { K } ,$and every$y \in \Lambda _ { 0 } ^ { \mathfrak { s } } \cap \mathfrak { K } .$

The proof of Proposition 3.20 relies on classical arguments very similar to those found for example in the monograph$[ \mathrm { M e y } 9 2 ]$. Since the spaces with inhomogeneous scaling do not seem to be standard in the literature and since we consider localised versions of the spaces, we prefer to provide a proof. Before we proceed, we state the following elementary fact:

Lemma 3.21 Let$a \in \mathbf { R }$and let$b _ { - } , b _ { + } \in { \bf R }$. Then, the bound

$$
\sum_ {n = 0} ^ {n _ {0}} 2 ^ {a n} 2 ^ {- b _ {-} (n _ {0} - n)} + \sum_ {n = n _ {0}} ^ {\infty} 2 ^ {a n} 2 ^ {- b _ {+} (n - n _ {0})} \lesssim 2 ^ {a n _ {0}},
$$

holds provided that$b _ { + } >$a and$b _ { - } > - a _ { \dagger }$

ProofofProposition 3.20. It is clear that the condition (3.14) is necessary, since it boils down to taking$\eta \in \Psi$and$\delta = 2 ^ { - n }$in Definition 3.7. In order to show that it is also sufficient, we take an arbitrary test function$\eta \in \mathcal { C } ^ { r }$with support in$B _ { 1 }$and we rewrite $\langle \xi , S _ { \mathfrak { s } , x } ^ { \delta } \eta \rangle$as

$$
\langle \xi , \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle = \sum_ {n \geq 0} \sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} \langle \xi , \psi_ {y} ^ {n, \mathfrak {s}} \rangle \langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle + \sum_ {y \in \Lambda_ {0} ^ {\mathfrak {s}}} \langle \xi , \varphi_ {y} ^ {0, \mathfrak {s}} \rangle \langle \varphi_ {y} ^ {0, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle .\tag{3.15}
$$

Let furthermore$n _ { 0 }$be the smallest integer such that$2 ^ { - n _ { 0 } } \leq \delta$. For the situations where the supports of$\psi _ { y } ^ { n , 5 }$and$S _ { \mathfrak { s } , x } ^ { \delta } \eta$overlap, we then have the following bounds.

First, we note that if$( x , y )$contributes to (3.15), then$\| x - y \| _ { \mathfrak { s } } \leq C$for some fixed constant$C .$As a consequence of this, it follows that one has the bound

$$
| \langle \xi , \psi_ {y} ^ {n, \mathfrak {s}} \rangle | \lesssim 2 ^ {- \frac {n | \mathfrak {s} |}{2} - n \alpha},\tag{3.16}
$$

uniformly over all pairs$( x , y )$yielding a non-vanishing contribution to (3.15).

For n$\geq n _ { 0 }$, and$\| x - y \| _ { \mathfrak { s } } \leq C \delta$, we furthermore have the bound

$$
| \langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle | \lesssim 2 ^ {- (n - n _ {0}) \left(r + \frac {| \mathfrak {s} |}{2}\right)} 2 ^ {\frac {n _ {0} | \mathfrak {s} |}{2}},\tag{3.17}
$$

so that

$$
\sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} | \langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle | \lesssim 2 ^ {- (n - n _ {0}) \left(r - \frac {| \mathfrak {s} |}{2}\right)} 2 ^ {\frac {n _ {0} | \mathfrak {s} |}{2}}.
$$

Here and below, the proportionality constants are uniform over all η with$\| \eta \| _ { C ^ { r } } \leq 1$ with supp$\eta \subset B _ { 1 }$. On the other hand, for$n \leq n _ { 0 }$, and$\| x - y \| _ { \mathfrak { s } } \leq C 2 ^ { - n _ { 0 } }$, we have the bound

$$
| \langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle | \lesssim 2 ^ {n \frac {| \mathfrak {s} |}{2}},\tag{3.18}
$$

so that, since only finitely many terms contribute to the sum,

$$
\sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} | \langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle | \lesssim 2 ^ {n ^ {\frac {| \mathfrak {s} |}{2}}}.
$$

Since, by the assumptions on r and$\alpha ,$one has indeed$r + \frac { | \mathfrak { s } | } { 2 } > \alpha + \frac { | \mathfrak { s } | } { 2 }$and$\begin{array} { r } { \frac { | \ s | } { 2 } > \frac { | \ s | } { 2 } - \alpha } \end{array}$ we can apply Lemma 3.21 to conclude that the first sum in (3.15) is indeed bounded by a multiple of$\delta ^ { \alpha }$, which is precisely the required bound. The second term on the other hand satisfies a bound similar to (3.18) with$n = 0 ,$, so that the claim follows.□

Remark 3.22 For$\alpha \geq 0$, it is not so straightforward to characterise the H ¨older regularity of a function by the magnitude of its wavelet coefficients due to special behaviour at integer values, but for non-integer values the characterisation given above still holds, see [Mey92].

Another nice property of the spaces$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$is that, using Proposition 3.20, one can give a very useful and sharp condition for a sequence of elements in$V _ { n }$to converge to an element in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$. Once again, we fix a multiresolution analysis of sufficiently high regularity$( \mathrm { i } . \mathrm { e } . \ r > | \alpha | )$and the spaces$V _ { n }$are given in terms of that particular analysis. For this characterisation, we use the fact that a sequence$\{ f _ { n } \} _ { n \geq 0 }$with$f _ { n } \in V _ { n }$for every n can always be written as

$$
f _ {n} = \sum_ {x \in \Lambda_ {n} ^ {\mathfrak {s}}} A _ {x} ^ {n} \varphi_ {x} ^ {n, \mathfrak {s}}, \qquad A _ {x} ^ {n} = \left\langle \varphi_ {x} ^ {n, \mathfrak {s}}, f _ {n} \right\rangle .\tag{3.19}
$$

Given a sequence of coefficients$A _ { x } ^ { n }$, we then define$\delta A _ { x } ^ { n }$by

$$
\delta A _ {x} ^ {n} = A _ {x} ^ {n} - \sum_ {k \in \mathcal {K}} a _ {k} A _ {x + 2 ^ {- n s} k} ^ {n + 1},
$$

where the set$\mathcal { \kappa }$and the structure constants$a _ { k }$are as in (3.12). We then have the following result, which can be seen as a generalisation of the “sewing lemma” (see [Gub04, Prop. 1] or [FdLP06, Lem. 2.1]), which can itself be viewed as a generalisation of Young’s original theory of integration [You36]. In order to make the link to these theories, consider the case where$\mathbf { R } ^ { d }$is replaced by an interval and take for$\varphi$the Haar wavelets.

Theorem 3.23 Let s be a scaling of$\mathbf { R } ^ { d }$, let$\alpha < 0 < \gamma ,$, andfix a wavelet basis with regularity$r > | \alpha | .$. For every$n \geq 0 ,$, let$x \mapsto A _ { x } ^ { n }$be a function on$\mathbf { R } ^ { d }$satisfying the bounds

$$
| A _ {x} ^ {n} | \leq \| A \| 2 ^ {- \frac {n \mathfrak {s}}{2} - \alpha n}, \quad | \delta A _ {x} ^ {n} | \lesssim \| A \| 2 ^ {- \frac {n \mathfrak {s}}{2} - \gamma n},\tag{3.20}
$$

for some constant$\| A \| _ { \ell }$, uniformly over n$\geq 0$and$\boldsymbol { x } \in \mathbf { R } ^ { d }$

Then, the sequence$\{ f _ { n } \} _ { n \geq 0 }$given$\begin{array} { r } { b y \ f _ { n } = \sum _ { x \in \Lambda _ { \mathfrak { n } } ^ { \mathfrak { s } } } A _ { x } ^ { n } \ \varphi _ { x } ^ { n , \mathfrak { s } } } \end{array}$converges in$\mathcal { C } _ { \mathfrak { s } } ^ { \bar { \alpha } }$for every$\bar { \alpha } < \alpha$and its limit f belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$P. Furthermore, the bounds

$$
\| f - f _ {n} \| _ {\bar {\alpha}} \lesssim \| A \| 2 ^ {- (\alpha - \bar {\alpha}) n}, \quad \| \mathcal {P} _ {n} f - f _ {n} \| _ {\alpha} \lesssim \| A \| 2 ^ {- \gamma n},\tag{3.21}
$$

hold for$\bar { \alpha } \in ( \alpha - \gamma , \alpha ) ,$, where$\mathcal { P } _ { n }$is as in$_ { ( 3 . I O ) }$

Proof. By linearity, it is sufficient to restrict ourselves to the case$\| A \| = 1$. By construction, we have$f _ { n + 1 } - f _ { n } \in V _ { n + 1 }$, so that we can decompose this difference as

$$
f _ {n + 1} - f _ {n} = g _ {n} + \delta f _ {n},\tag{3.22}
$$

where$\delta f _ { n } \in V _ { n } ^ { \perp }$and$g _ { n } \ \in \ V _ { n }$. By Proposition 3.20, we note that there exists a constant C such that, for every$n \geq 0$and$m \geq n$, and for every$\beta < 0$, one has

$$
\left\| \sum_ {k = n} ^ {m} \delta f _ {k} \right\| _ {\beta} \leq C \sup _ {k \in \{n, \dots , m \}} \| \delta f _ {k} \| _ {\beta},
$$

so that a sufficient condition for the sequence$\textstyle \{ \sum _ { k = 0 } ^ { n } \delta f _ { k } \} _ { n \geq 0 }$to have the required properties is given by

$$
\lim _ {n \to \infty} \| \delta f _ {n} \| _ {\bar {\alpha}} = 0, \quad \sup _ {n} \| \delta f _ {n} \| _ {\alpha} <   \infty .\tag{3.23}
$$

Regarding the bounds on$\delta f _ { n }$, we have

$$
\langle \delta f _ {n}, \psi_ {x} ^ {n, \mathfrak {s}} \rangle = \langle f _ {n + 1} - f _ {n}, \psi_ {x} ^ {n, \mathfrak {s}} \rangle = \sum_ {\| x - y \| _ {\mathfrak {s}} \leq K 2 ^ {- n | \mathfrak {s} |}} a _ {x y} A _ {y} ^ {n + 1},
$$

where the$a _ { x y } = \langle \varphi _ { y } ^ { n + 1 , 5 } , \psi _ { x } ^ { n , 5 } \rangle$are a finite number of uniformly bounded coefficients and$K > 0$is some fixed constant. It then follows from the assumption on the coefficients$A _ { y } ^ { n }$that

$$
| \langle \delta f _ {n}, \psi_ {x} ^ {n, \mathfrak {s}} \rangle | \lesssim 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n}.
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
\begin{array}{l} \langle g _ {n}, \varphi_ {x} ^ {n, \mathfrak {s}} \rangle = \langle f _ {n + 1} - f _ {n}, \varphi_ {x} ^ {n, \mathfrak {s}} \rangle = \left(\sum_ {k \in \mathcal {K}} a _ {k} \langle f _ {n + 1}, \varphi_ {x + 2 ^ {- n \mathfrak {s}} k} ^ {n + 1, \mathfrak {s}} \rangle\right) - \langle f _ {n}, \varphi_ {x} ^ {n, \mathfrak {s}} \rangle \\ = - \delta A _ {x} ^ {n}, \end{array}\tag{3.26}
$$

so that one can decompose$g _ { n }$as

$$
g _ {n} = - \sum_ {x \in \Lambda_ {n} ^ {\mathfrak {s}}} \delta A _ {x} ^ {n} \varphi_ {x} ^ {n, \mathfrak {s}}.\tag{3.27}
$$

It follows in a straightforward way from the definitions that, for$m \leq n$, there exists a constant$C$such that we have the bound

$$
| \langle \psi_ {y} ^ {m, \mathfrak {s}}, \varphi_ {x} ^ {n, \mathfrak {s}} \rangle | \leq C 2 ^ {(m - n) \frac {| \mathfrak {s} |}{2}} {\bf 1} _ {\| x - y \| _ {\mathfrak {s}} \leq C 2 ^ {- m}} .\tag{3.28}
$$

Since on the other hand, one has

$$
| \{x \in \Lambda_ {n} ^ {\mathfrak {s}}: \| x - y \| _ {\mathfrak {s}} \leq C 2 ^ {- m} \} | \lesssim 2 ^ {(n - m) | \mathfrak {s} |},
$$

we obtain from this and (3.27) the bound

$$
\begin{array}{c} | \langle \psi_ {y} ^ {m, \mathfrak {s}}, g _ {n} \rangle | \lesssim 2 ^ {(n - m) \frac {| \mathfrak {s} |}{2}} \sup \{| \delta A _ {x} ^ {n} |: \| x - y \| _ {\mathfrak {s}} \leq C 2 ^ {- m} \} \\ \lesssim 2 ^ {- m \frac {| \mathfrak {s} |}{2} - \gamma n}, \end{array}\tag{3.29}
$$

where we used again the fact that$\lVert x - y \rVert _ { \mathfrak { s } } \lesssim d _ { \mathfrak { s } } ( y , \partial D )$by the definition of the functions$\psi _ { y } ^ { m , s }$. Combining this with the characterisation of$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$given in Proposition 3.20, we conclude that

$$
\| \mathcal {Q} _ {m} g _ {n} \| _ {\alpha} \lesssim 2 ^ {\alpha m - \gamma n} \mathbf {1} _ {m \leq n},
$$

so that

$$
\sum_ {k = n} ^ {m} \| \mathcal {Q} _ {N} g _ {k} \| _ {\alpha} \lesssim \sum_ {k = n \vee N} ^ {m} 2 ^ {\alpha N - \gamma k} \lesssim 2 ^ {\alpha N - \gamma (N \vee n)}.
$$

This expression is maximised at$N = 0 ,$, so that the bound$\begin{array} { r } { \| \sum _ { k = n } ^ { m } g _ { k } \| _ { \alpha } \lesssim 2 ^ { - \gamma n } } \end{array}$ Pfollows from (3.25). Combining this with (3.24), we thus obtain (3.21), as stated.

A simple but important corollary of the proof is given by

Corollary 3.24 In the situation of Theorem 3.23, let$\mathcal { R } \subset \mathbf { R } ^ { d }$be a compact set and let K<sup>¯</sup> be its 1-fattening. Then, provided that (3.20) holds uniformly over K<sup>¯</sup>, the bound (3.21) still holds with$\| \cdot \| _ { \alpha }$replaced by$\| \cdot \| _ { \alpha ; \mathscr { R } } .$

Proof. Follow step by step the argument given above noting that, since all the arguments in the proof of Proposition 3.20 are local, one can bound the norm$\| \cdot \| _ { \alpha ; \mathscr { R } }$by the smallest constant such that the bounds (3.14) hold uniformly over$x , y \in { \mathcal { R } }$□

## 3.3 The reconstruction theorem for distributions

One very important special case of Theorem 3.23 is given by the situation where there exists a family$x \mapsto \zeta _ { x } \in S ^ { \prime } ( \mathbf { R } ^ { d } )$of distributions such that the sequence$f _ { n }$is given by (3.19) with$A _ { x } ^ { n } = \langle \varphi _ { x } ^ { n , \mathfrak { s } } , \zeta _ { x } \rangle$. Once this is established, the reconstruction theorem will be straightforward. In the situation just described, we have the following result which, as we will see shortly, can really be interpreted as a generalisation of the reconstruction theorem.

Proposition 3.25 In the above situation, assume that the family$\zeta _ { x }$is such that, for some constants$K _ { 1 }$and$K _ { 2 }$and exponents$\alpha < 0 < \gamma$, the bounds

$$
| \langle \varphi_ {x} ^ {n, \mathfrak {s}}, \zeta_ {x} - \zeta_ {y} \rangle | \leq K _ {1} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \alpha} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n}, \quad | \langle \varphi_ {x} ^ {n, \mathfrak {s}}, \zeta_ {x} \rangle | \leq K _ {2} 2 ^ {- \alpha n - \frac {n | \mathfrak {s} |}{2}},\tag{3.30}
$$

hold uniformly over all x, y such that$2 ^ { - n } \leq \| x - y \| _ { \mathfrak { s } } \leq 1$. Here, as before,$\varphi$is the scaling function for a wavelet basis of regularity$r > | \alpha | .$. Then, the assumptions of Theorem 3.23 are satisfied. Furthermore, the limit distribution$f \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$satisfies the bound

$$
\left| \left(f - \zeta_ {x}\right) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta\right) \right| \lesssim K _ {1} \delta^ {\gamma},\tag{3.31}
$$

uniformly over$\eta \in B _ { \mathfrak { s } , 0 } ^ { r }$. Here, the proportionality constant only depends on the choice ofwavelet basis, but not on$K _ { 2 }$

Proof. We are in the situation of Theorem 3.23 with$A _ { x } ^ { n } = \zeta _ { x } ( \varphi _ { x } ^ { n , 5 } )$, so that one has the identity

$$
\delta A _ {x} ^ {n} = \sum_ {k \in \mathcal {K}} a _ {k} \langle \zeta_ {x} - \zeta_ {y}, \varphi_ {y} ^ {(n + 1), \mathfrak {s}} \rangle ,\tag{3.32}
$$

where we used the shortcut$y \ : = \ : x + 2 ^ { - n . 5 } k$in the right hand side. It then follows immediately from (3.30) that the assumptions of Theorem 3.23 are indeed satisfied, so that the sequence$f _ { n }$converges to some limit$f .$It remains to show that the local behaviour of$f$around every point x is given by (3.31).

For this, we write

$$
f - \zeta_ {x} = (f _ {n _ {0}} - \mathcal {P} _ {n _ {0}} \zeta_ {x}) + \sum_ {n \geq n _ {0}} (f _ {n + 1} - f _ {n} - (\mathcal {P} _ {n + 1} - \mathcal {P} _ {n}) \zeta_ {x}),\tag{3.33}
$$

for some$n _ { 0 } > 0$. We choose$n _ { 0 }$to be the smallest integer such that$2 ^ { - n _ { 0 } } \leq \delta$. Note that, as in (3.17), one has for n$\geq n _ { 0 }$the bounds

$$
| \langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle | \lesssim 2 ^ {\frac {n _ {0} | s |}{2}} 2 ^ {- (n - n _ {0}) \left(r + \frac {| s |}{2}\right)}, \qquad | \langle \varphi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle | \lesssim 2 ^ {\frac {n _ {0} | s |}{2}} 2 ^ {- (n - n _ {0}) \frac {| s |}{2}}.\tag{3.34}
$$

Since, by construction, the first term in (3.33) belongs to$V _ { n _ { 0 } } .$, we can rewrite it as

$$
(f _ {n _ {0}} - \mathcal {P} _ {n _ {0}} \zeta_ {x}) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) = \sum_ {y \in \Lambda_ {n _ {0}} ^ {\mathfrak {s}}} (\zeta_ {y} - \zeta_ {x}) (\varphi_ {y} ^ {n _ {0}, \mathfrak {s}}) \left\langle \varphi_ {y} ^ {n _ {0}, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \right\rangle .
$$

Since terms appearing in the above sum with$\| x - y \| _ { s } \geq \delta$are identically$0 ,$, we can use the bound n |s|

$$
| (\zeta_ {y} - \zeta_ {x}) (\varphi_ {y} ^ {n _ {0}, \mathfrak {s}}) | \lesssim K _ {1} 2 ^ {- \gamma n _ {0} - \frac {n _ {0} | \mathfrak {s} |}{2}}.
$$

Combining this with (3.34) and the fact that there are only finitely many non-vanishing terms in the sum, we obtain the bound

$$
| (f _ {n _ {0}} - \mathcal {P} _ {n _ {0}} \zeta_ {x}) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) | \lesssim K _ {1} 2 ^ {- n _ {0} \gamma} \approx K _ {1} \delta^ {\gamma},\tag{3.35}
$$

which is of the required order.

Regarding the second term in (3.33), we decompose$f _ { n + 1 } - f _ { n }$as in the proof of Theorem 3.23 as$f _ { n + 1 } - f _ { n } = g _ { n } + \delta f _ { n }$with$g _ { n } \in V _ { n }$and$\delta f _ { n } \in V _ { n } ^ { \bot }$. As a consequence of (3.26) and of the bounds (3.30) and (3.34), we have the bound

$$
\begin{array}{r l} & {| \langle g _ {n}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle | \leq \sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} | \langle g _ {n}, \varphi_ {y} ^ {n, \mathfrak {s}} \rangle | | \langle \varphi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle |} \\ & {\quad \leq \sum_ {y \in \Lambda_ {n} ^ {\mathfrak {s}}} | \delta A _ {y} ^ {n} | | \langle \varphi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle | \lesssim K _ {1} 2 ^ {- (n - n _ {0}) (| \mathfrak {s} | + \alpha) - \gamma n},} \end{array}
$$

where we made use of (3.32) for the last bound. Summing this bound over all$n \geq n _ { 0 }$ we obtain again a bound of order$K _ { 1 } \delta ^ { \gamma }$, as required. It remains to obtain a similar bound for the quantity

$$
\sum_ {n \geq n _ {0}} (\delta f _ {n} - (\mathcal {P} _ {n + 1} - \mathcal {P} _ {n}) \zeta_ {x}) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta)  .
$$

Note that$\delta f _ { n }$is nothing but the projection of$f _ { n + 1 }$onto the space$V _ { n } ^ { \perp }$. Similarly, $( \mathcal { P } _ { n + 1 } - \mathcal { P } _ { n } ) \zeta _ { x }$is the projection of$\zeta _ { x }$onto that same space. As a consequence, we have the identity

$$
\begin{array}{l} (\delta f _ {n} - (\mathcal {P} _ {n + 1} - \mathcal {P} _ {n}) \zeta_ {x}) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) \\ = \sum_ {z \in \Lambda_ {\mathfrak {s}} ^ {n + 1}} \sum_ {y \in \Lambda_ {\mathfrak {s}} ^ {n}} \sum_ {\psi \in \Psi} \langle \zeta_ {z} - \zeta_ {x}, \varphi_ {z} ^ {n + 1, \mathfrak {s}} \rangle \langle \varphi_ {z} ^ {n + 1, \mathfrak {s}}, \psi_ {y} ^ {n, \mathfrak {s}} \rangle \langle \psi_ {y} ^ {n, \mathfrak {s}}, \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta \rangle . \end{array}
$$

Note that this triple sum only contains of the order of$2 ^ { ( n - n _ { 0 } ) | s | }$terms since, for any given value of$y ,$, the sum over z only has a fixed finite number of non-vanishing terms. At this stage, we make use of the first bound in (3.34), together with the assumption (3.30) and the fact that$2 ^ { - n _ { 0 } } \lesssim \| x - z \| _ { \mathfrak { s } } \lesssim \delta$for every term in this sum. This yields for this expression a bound of the order

$$
K _ {1} 2 ^ {(n - n _ {0}) | \mathfrak {s} |} \delta^ {\gamma - \alpha} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n} 2 ^ {\frac {n _ {0} | \mathfrak {s} |}{2}} 2 ^ {- (n - n _ {0}) (r + | \mathfrak {s} | / 2)} = K _ {1} \delta^ {\gamma - \alpha} 2 ^ {- r (n - n _ {0}) - \alpha n}.
$$

Since, by assumption,$r$is sufficiently large so that$r > | \alpha |$, this expression converges to 0 as$n  \infty$. Summing over$n \geq n _ { 0 }$and combining all of the above bounds, the claim follows at once.□

Remark 3.26 As before, the construction is completely local. As a consequence, the required bounds hold over a compact${ \mathcal { R } } ,$provided that the assumptions hold over its 1-fattening K<sup>¯</sup>.

We now finally have all the elements in place to give the proof of Theorem 3.10.

ProofofTheorem 3.10. We first consider the case$\gamma > 0$, where the operator$\mathcal { R }$is unique. In order to construct$\mathcal { R }$, we will proceed by successive approximations, using a multiresolution analysis. Again, we fix a wavelet basis as above associated with a compactly supported scaling function$\varphi .$. We choose$\varphi$to be${ \mathcal { C } } ^ { r }$for$r \mathrm { ~ > ~ }$min$A |$ (Which in particular also implies that the elements$\psi \in \Psi$annihilate polynomials of degree$r . )$

Since, for any given$n > 0$, the functions$\varphi _ { x } ^ { n , { \mathfrak { s } } }$are orthonormal and since, as$n$, they get closer and closer to forming a basis of very sharply localised functions of $L ^ { 2 }$, it appears natural to define a sequence of operators$\mathcal { R } _ { n } \colon \mathcal { D } ^ { \gamma }  \mathcal { C } ^ { r }$by

$$
\mathcal {R} _ {n} f = \sum_ {x \in \Lambda_ {n} ^ {\mathfrak {s}}} (\Pi_ {x} f (x)) (\varphi_ {x} ^ {n, \mathfrak {s}}) \varphi_ {x} ^ {n, \mathfrak {s}},
$$

and to define$\mathcal { R }$as the limit of$\mathcal { R } _ { n } \mathrm { ~ a s ~ } n  \infty$, if such a limit exists.

We are thus precisely in the situation of Proposition 3.25 with$\zeta _ { x } = \Pi _ { x } f ( x )$. Since we are interested in a local statement, we only need to construct the distribution$\mathcal { R } f$ acting on test functions supported on a fixed compact domain K. As a consequence, since all of our constructions involve some fixed wavelet basis, it suffices to obtain bounds on the wavelet coefficients$\psi _ { x } ^ { n }$with x such that$\psi _ { x } ^ { n }$is supported in${ \bar { \mathbf { \mathcal { R } } } } ,$the 1- fattening of${ \mathcal { R } } .$

It follows from the definitions of$\mathcal { D } ^ { \gamma }$and the space of models$\mathcal { M } _ { \mathcal { T } }$that, for such values of$x ,$one has

$$
| \langle \Pi_ {x} f (x), \varphi_ {x} ^ {n, \mathfrak {s}} \rangle | \lesssim \| f \| _ {\gamma ; \bar {\mathfrak {K}}} \| \Pi \| _ {\gamma ; \bar {\mathfrak {K}}} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n},
$$

where, as before,$\alpha =$min A is the smallest homogeneity arising in the description of the regularity structure$\mathcal { T }$. Similarly, we have

$$
\begin{array}{r l} & {| \langle \Pi_ {x} f (x) - \Pi_ {y} f (y), \varphi_ {x} ^ {n, \mathfrak {s}} \rangle | = | \langle \Pi_ {x} (f (x) - \Gamma_ {x y} f (y)), \varphi_ {x} ^ {n, \mathfrak {s}} \rangle |} \\ & {\quad \lesssim  \sum_ {\ell <   \gamma} \| f \| _ {\gamma ; \bar {\mathfrak {K}}} \| \Pi \| _ {\gamma ; \bar {\mathfrak {K}}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \ell n},} \end{array}\tag{3.36}
$$

where the sum runs over elements in$A .$. Since, in the assumption of Proposition 3.25, we only consider points$( x , y )$such that$\| x - y \| _ { s } \gtrsim 2 ^ { - n }$, the bound (3.30) follows.

As a consequence, we can apply Theorem 3.23 to construct a limiting distribution $\begin{array} { r } { \mathscr { R } f = \operatorname* { l i m } _ { n  \infty } \mathscr { R } _ { n } f } \end{array}$, where convergence takes place in$\mathcal { C } _ { \mathfrak { s } } ^ { \bar { \alpha } }$for every$\bar { \alpha } < \alpha$. Furthermore, the limit does itself belong to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$. The bound (3.3) follows immediately from Proposition 3.25.

In order to obtain the bound (3.4), we use again Proposition 3.25, but this time with $\zeta _ { x } = \Pi _ { x } f ( x ) - \bar { \Pi } _ { x } \bar { f } ( x )$. We then have the identity

$$
\zeta_ {x} - \zeta_ {y} = \Pi_ {x} (f (x) - \Gamma_ {x y} f (y) - \bar {f} (x) + \bar {\Gamma} _ {x y} \bar {f} (y)) + (\Pi_ {x} - \bar {\Pi} _ {x}) (\bar {f} (x) - \bar {\Gamma} _ {x y} \bar {f} (y)).
$$

Similarly to above, it then follows from the definition of$\| f ; { \bar { f } } \| _ { \gamma ; { \mathcal { R } } }$that

$$
| \langle \zeta_ {x} - \zeta_ {y}, \varphi_ {x} ^ {n, \mathfrak {s}} \rangle | \lesssim (\| \Pi \| _ {\gamma ; \mathfrak {K}} \| f; \bar {f} \| _ {\gamma ; \mathfrak {K}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \mathfrak {K}} \| \bar {f} \| _ {\gamma ; \mathfrak {K}}) \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \alpha} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n},
$$

from which the requested bound follows at once.

The bound (3.5) is obtained again from Proposition 3.25 with$\zeta _ { x } = \Pi _ { x } f ( x ) -$ ${ \bar { \Pi } } _ { x } { \bar { f } } ( x )$. This time however, we aim to obtain bounds on this quantity by only making use of bounds on$\| f - \bar { f } \| _ { \gamma ; \mathcal { R } }$rather than$\| f ; { \bar { f } } \| _ { \gamma ; { \mathcal { R } } }$. Note first that, as a consequence of (3.36), we have the bound

$$
| \langle \zeta_ {x} - \zeta_ {y}, \varphi_ {x} ^ {n, \mathfrak {s}} \rangle | \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \alpha} 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n}.\tag{3.37}
$$

On the other hand, we can rewrite$\zeta _ { x } - \zeta _ { y }$as

$$
\begin{array}{c} \zeta_ {x} - \zeta_ {y} = \Pi_ {x} (f (x) - \bar {f} (x)) + (\bar {\Pi} _ {x} - \Pi_ {x}) (\bar {\Gamma} _ {x y} \bar {f} (y) - \bar {f} (x)) \\ - \Pi_ {x} \Gamma_ {x y} (f (y) - \bar {f} (y)) + \Pi_ {x} (\bar {\Gamma} _ {x y} - \Gamma_ {x y}) \bar {f} (x). \end{array}
$$

It follows at once that one has the bound

$$
| \langle \zeta_ {x} - \zeta_ {y}, \varphi_ {x} ^ {n, \mathfrak {s}} \rangle | \lesssim (\| f - \bar {f} \| _ {\gamma ; \mathfrak {K}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}}) 2 ^ {- \frac {n | \mathfrak {s} |}{2} - \alpha n}.
$$

Combining this with (3.37) and making use of the bound a$\textstyle \bigwedge b \leq a ^ { \kappa } b ^ { 1 - \kappa }$, which is valid for any two positive numbers a and$b ,$we have

$$
| \langle \zeta_ {x} - \zeta_ {y}, \varphi_ {x} ^ {n, \mathfrak {s}} \rangle | \lesssim (\| f - \bar {f} \| _ {\gamma ; \mathfrak {K}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}}) ^ {\kappa} \| x - y \| _ {\mathfrak {s}} ^ {\bar {\gamma} - \alpha} 2 ^ {- \frac {n   |   \mathfrak {s} |}{2} - \alpha n}  ,
$$

from which the claimed bound follows.

We now prove the claim for$\gamma \le 0$. It is clear that in this case  cannot be unique since, if$\mathcal { R } f$satisfies (3.3) and$\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \gamma }$, then$\mathcal { R } f + \xi$does again satisfy (3.3). Still, the existence of$\mathcal { R } f$is not completely trivial in general since$\Pi _ { x } f ( x )$itself only belongs to $\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$and one can have$\alpha < \gamma \leq 0$in general. It turns out that one very simple choice for $\mathcal { R } f$is given by

$$
\mathcal {R} f = \sum_ {n \geq 0} \sum_ {x \in \Lambda_ {\mathfrak {s}} ^ {n}} \sum_ {\psi \in \Psi} \langle \Pi_ {x} f (x), \psi_ {x} ^ {n, \mathfrak {s}} \rangle \psi_ {x} ^ {n, \mathfrak {s}} + \sum_ {x \in \Lambda_ {\mathfrak {s}} ^ {0}} \langle \Pi_ {x} f (x), \varphi_ {x} ^ {0, \mathfrak {s}} \rangle \varphi_ {x} ^ {0, \mathfrak {s}}.\tag{3.38}
$$

This is obviously not canonical: different choices for our multiresolution analysis yield different definitions for$\mathcal { R }$. However, it has the advantage of not relying at all on the axiom of choice, which was used in [LV07] to prove a similar result in the onedimensional case. Furthermore, it has the additional property that if$f$is “constant” in the sense that$f ( x ) = \Gamma _ { x y } f ( y )$for any two points x and$y ,$, then one has the identity

$$
\mathcal {R} f = \Pi_ {x} f (x),\tag{3.39}
$$

where the right hand side is independent of x by assumption. (This wouldn’t be the case if the second term in (3.38) were absent.) Actually, our construction is related in spirit to the one given in [Unt10], but it has the advantage of being very straightforward to analyse.

For$\mathcal { R } f$as in (3.38), it remains to show that (3.3) holds. Note first that the second part of (3.38) defines a smooth function, so that we can discard it. To bound the remainder, let η be a suitable test function and note that one has the bounds

$$
| \langle \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta , \psi_ {y} ^ {n, \mathfrak {s}} \rangle | \lesssim \left\{ \begin{array}{c l} 2 ^ {- n \frac {| \mathfrak {s} |}{2} - r n} \delta^ {- | \mathfrak {s} | - r} & \text { if } 2 ^ {- n} \leq \delta , \\ 2 ^ {n \frac {| \mathfrak {s} |}{2}} & \text { otherwise }. \end{array} \right.
$$

Furthermore, one has of course$\langle S _ { \mathfrak { s } , x } ^ { \delta } \eta , \psi _ { y } ^ { n , \mathfrak { s } } \rangle = 0$unless$\| x - y \| _ { \mathfrak { s } } \lesssim \delta + 2 ^ { - n }$. It also follows immediately from the definition (3.38) that one has the bound

$$
\begin{array}{c} | (\mathcal {R} f - \Pi_ {x} f (x)) (\psi_ {y} ^ {n, \mathfrak {s}}) | = | (\Pi_ {y} f (y) - \Pi_ {x} f (x)) (\psi_ {y} ^ {n, \mathfrak {s}}) | = | \Pi_ {y} (f (y) - \Gamma_ {y x} f (x)) (\psi_ {y} ^ {n, \mathfrak {s}}) | \\ \lesssim \sum_ {\beta <   \gamma} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \beta} 2 ^ {- n \frac {| \mathfrak {s} |}{2} - \beta n}, \end{array}
$$

where the proportionality constant is as in (3.3). These bounds are now inserted into the identity

$$
(\mathcal {R} f - \Pi_ {x} f (x)) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta) = \sum_ {n > 0} \sum_ {y \in \Lambda_ {\mathfrak {s}} ^ {n}} \sum_ {\psi \in \Psi} (\mathcal {R} f - \Pi_ {x} f (x)) (\psi_ {y} ^ {n, \mathfrak {s}}) \bigl \langle \mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \eta , \psi_ {y} ^ {n, \mathfrak {s}} \bigr \rangle .
$$

For the terms with$2 ^ { - n } \leq \delta .$, we thus obtain a contribution of the order

$$
\delta^ {| \mathfrak {s} |} \sum_ {2 ^ {- n} \leq \delta} 2 ^ {n | \mathfrak {s} |} \sum_ {\beta <   \gamma} \delta^ {\gamma - \beta} 2 ^ {- n \frac {| \mathfrak {s} |}{2} - \beta n} 2 ^ {- n \frac {| \mathfrak {s} |}{2} - r n} \delta^ {- | \mathfrak {s} | - r} \lesssim \delta^ {\gamma}.
$$

Here, the bound follows from the fact that we have chosen r such that$r > | \gamma |$and the factor$\delta ^ { | s | } 2 ^ { n | s | }$counts the number of non-zero terms appearing in the sum over$y .$. For the terms with$2 ^ { - n } > \delta .$, we similarly obtain a contribution of

$$
\sum_ {2 ^ {- n} > \delta} \sum_ {\beta <   \gamma} \delta^ {\gamma - \beta} 2 ^ {- n \frac {| s |}{2} - \beta n} 2 ^ {n \frac {| s |}{2}} \lesssim \delta^ {\gamma},
$$

where we used the fact that$\beta < \gamma \leq 0$. The claim then follows at once.

Remark 3.27 Recall that in Proposition 3.25, the bound on$f - \zeta _ { x }$depends on$K _ { 1 }$but not on$K _ { 2 } .$. This shows that in the reconstruction theorem, the bound on$\mathcal { R } f - \Pi _ { x } f ( x )$ only depends on the second part of the definition of$\| f \| _ { \gamma ; { \mathcal R } }$. This remark will be important when dealing with singular modelled distributions in Section 6 below.

## 3.4 The reconstruction theorem for functions

A very important special case is given by the situation in which$\mathcal { T }$contains a copy of the canonical regularity structure$\mathcal { T } _ { d , \mathfrak { s } }$<sub>s</sub> (write$\bar { T } \subset T$for the model space associated to the abstract polynomials) as in Remark 2.23, and where the model (Π, Γ) we consider yields the canonical polynomial model when restricted to$\bar { T }$. We consider the particular case of the reconstruction theorem applied to elements$f \in { \mathcal { D } } ^ { \gamma } ( V )$, where$V$is a sector of regularity$0 ,$but such that

$$
V \subset \bar {T} + T _ {\alpha} ^ {+},\tag{3.40}
$$

for some$\alpha \in ( 0 , \gamma )$. Loosely speaking, this states that the elements of the model Π used to describe$\mathcal { R } f$consist only of polynomials and of functions that are H¨older regular of order α or more.

This is made more precise by the following result:

Proposition 3.28 Let$f \in { \mathcal { D } } ^ { \gamma } ( V )$, where$V$is a sector as in$_ { ( 3 . 4 0 ) }$. Then,$\mathcal { R } f$coincides with thefunction given by

$$
\mathcal {R} f (x) = \left\langle \mathbf {1}, f (x) \right\rangle ,\tag{3.41}
$$

and one has$\mathcal { R } f \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$

Proof. The fact that the function$x \mapsto \langle \mathbf { 1 } , f ( x ) \rangle$belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$is an immediate consequence of the definitions and the fact that the projection of$f$onto$\bar { T }$belongs to$\mathcal { D } ^ { \alpha }$. It follows immediately that one has

$$
\int_ {\mathbf {R} ^ {d}} \left(\mathcal {R} f (x) - \langle \mathbf {1}, f (x) \rangle\right) \psi_ {y} ^ {\lambda} (x) d x \lesssim \lambda^ {\alpha},
$$

from which, by the uniqueness of the reconstruction operator, we deduce that one does indeed have the identity (3.41).□

Another useful fact is the following result showing that once we know that$f \in \mathcal { D } ^ { \gamma }$ for some$\gamma > 0$, the components of$f$in$\hat { T } _ { k }$for$0 < k < \gamma$are uniquely determined by the knowledge of the remaining components. More precisely, we have

Proposition 3.29 If$f , g \in \mathcal { D } ^ { \gamma }$with$\gamma > 0$are such that$f ( x ) - g ( x ) \in \bigoplus _ { 0 < k < \gamma } { \bar { T } } _ { k }$ then$f = g .$

Proof. Setting$h = f - g$, one has$\mathcal { R } h = 0$from the uniqueness of the reconstruction operator. The fact that this implies that$h = 0$was already shown in Remark$2 . 1 6 . \ \bigtriangledown$

Remark 3.30 In full generality, it is not true that h is completely determined by the knowledge of h. Actually, whether such a determinacy holds or not depends on the intricate details of the particular model (Π, Γ) that is being considered. However, for models that are built in a “natural” way from a sufficiently non-degenerate Gaussian process, it does tend to be the case that h fully determines h. See [HP13] for more details in the particular case of rough paths.

## 3.5 Consequences of the reconstruction theorem

To conclude this section, we provide a few very useful consequences of the reconstruction theorem which shed some light on the interplay between Π and Γ. First, we show that for$\alpha > 0 ,$, the action of$\Pi _ { x }$on$T _ { \alpha }$is completely determined by Γ. In a way, one can interpret this result as a generalisation of [Lyo98, Theorem 2.2.1].

Proposition 3.31 Let$\mathcal { T }$be a regularity structure, let$\alpha > 0 ,$, and let (Π, Γ) be a model for$\mathcal { T }$over$\mathbf { R } ^ { d }$with scaling s. Then, the action of Π on$T _ { \alpha }$is completely determined by the action ofΠ on$T _ { \alpha } ^ { - }$and the action ofΓ on$T _ { \alpha } .$. Furthermore, one has the bound

$$
\sup_{x\in \mathfrak{K}}\sup_{\delta <  1}\sup_{\varphi \in \mathcal{B}_{\mathfrak{s},0}^{r}}\sup_{\substack{a\in T_{\alpha}\\ \| a\| \leq 1}}\delta^{-\alpha}|(\Pi_{x}a)(\mathcal{S}_{\mathfrak{s},x}^{\delta}\varphi)|\leq \| \Pi \|_{\alpha ;\bar{\mathfrak{K}}}\| \Gamma \|_{\alpha ;\bar{\mathfrak{K}}},\tag{3.42}
$$

where K<sup>¯</sup> denotes the 1-fattening of K as before and$r >$min A .$I f ( { \bar { \Pi } } , { \bar { \Gamma } } )$is a second modelfor the same regularity structure, onefurthermore has the bound

$$
\begin{array}{r l} \sup _ {x \in \mathfrak {K}} \sup _ {\delta ; \varphi ; a} \delta^ {- \alpha} | (\Pi_ {x} a - \bar {\Pi} _ {x} a) (\mathcal {S} _ {\mathfrak {s}, x} ^ {\delta} \varphi) | & \leq \| \Pi - \bar {\Pi} \| _ {\alpha ; \bar {\mathfrak {K}}} (\| \Gamma \| _ {\alpha ; \bar {\mathfrak {K}}} + \| \Gamma \| _ {\alpha ; \bar {\mathfrak {K}}}) \\ & \quad + \| \Gamma - \bar {\Gamma} \| _ {\alpha ; \bar {\mathfrak {K}}} (\| \Pi \| _ {\alpha ; \bar {\mathfrak {K}}} + \| \bar {\Pi} \| _ {\alpha ; \bar {\mathfrak {K}}}), \end{array}\tag{3.43}
$$

where the supremum runs over the same set as in$( 3 . 4 2 )$.

Proof. For any$a \in T _ { \alpha }$and$\boldsymbol { x } \in \mathbf { R } ^ { d }$, we define a function$f _ { a , x } \colon \mathbf { R } ^ { d } \to T _ { \alpha } ^ { - }$by

$$
f _ {a, x} (y) = \Gamma_ {y x} a - a.\tag{3.44}
$$

It follows immediately from the definitions that$f _ { a , x } \in \mathcal { D } ^ { \alpha }$and that, uniformly over al a with$\| a \| \leq 1$, its norm over any domain K is bounded by the corresponding norm of Γ. Indeed, we have the identity

$$
\begin{array}{c} \Gamma_ {y z} f _ {a, x} (z) - f _ {a, x} (y) = (\Gamma_ {y x} a - \Gamma_ {y z} a) - (\Gamma_ {y x} a - a) \\ = a - \Gamma_ {y z} a, \end{array}
$$

so that the required bound follows from Definition 2.17.

We claim that one then has$\Pi _ { x } a = \mathcal { R } f _ { a , x }$, which depends only on the action of Π on$T _ { \alpha } ^ { - }$. This follows from the fact that, for every$\boldsymbol { y } \in \mathbf { R } ^ { d }$, one has$\Pi _ { x } a = \Pi _ { y } \Gamma _ { y x } a .$, so that

$$
\begin{array}{c} (\Pi_ {x} a - \Pi_ {y} f _ {a, x} (y)) (\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \eta) = (\Pi_ {y} a) (\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \eta) \lesssim \lambda^ {\alpha} \| \Pi \| _ {\alpha ; \bar {\mathfrak {K}}} \| f _ {a, x} \| _ {\alpha ; \bar {\mathfrak {K}}} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq \lambda^ {\alpha} \| \Pi \| _ {\alpha ; \bar {\mathfrak {K}}} \| \Gamma \| _ {\alpha ; \bar {\mathfrak {K}}}, \end{array}\tag{3.45}
$$

for all suitable test functions$\eta .$The claim now follows from the uniqueness part of the reconstruction theorem. Furthermore, the bound (3.42) is a consequence of (3.45) with $y = x$, noting that$f _ { a , x } ( x ) = 0$

It remains to obtain the bound (3.43). For this, we consider two models as in the statement, and we set$\bar { f } _ { a , x } ( y ) = \bar { \Gamma } _ { y x } a - a$, We then apply the generalised version of the reconstruction theorem, Proposition 3.25, noting that we are exactly in the situation that it covers, with$\zeta _ { y } = \Pi _ { y } f _ { a , x } ( y ) - \bar { \Pi } _ { y } \bar { f } _ { a , x } ( y )$. We then have the identity

$$
\begin{array}{r l} & {\zeta_ {y} - \zeta_ {z} = (\Pi_ {y} (\Gamma_ {y x} - I) - \bar {\Pi} _ {y} (\bar {\Gamma} _ {y x} - I)) a - (\Pi_ {z} (\Gamma_ {z x} - I) - \bar {\Pi} _ {z} (\bar {\Gamma} _ {z x} - I)) a} \\ & {\qquad = \Pi_ {y} (\Gamma_ {y z} - I) a - \bar {\Pi} _ {y} (\bar {\Gamma} _ {y z} - I) a} \\ & {\qquad = (\Pi_ {y} - \bar {\Pi} _ {y}) (\Gamma_ {y z} - I) a + \bar {\Pi} _ {y} (\Gamma_ {y z} - \bar {\Gamma} _ {y z}) a.} \end{array}
$$

It follows that one has the bound

$$
\begin{array}{r l} & 2 ^ {\frac {n | \mathfrak {s} |}{2}} \langle \zeta_ {y} - \zeta_ {z}, \varphi_ {y} ^ {n, \mathfrak {s}} \rangle \leq \| \Pi - \bar {\Pi} \| _ {\alpha ; \bar {\mathfrak {K}}} \| \Gamma \| _ {\alpha ; \bar {\mathfrak {K}}} \sum_ {\beta <   \alpha} \| y - z \| _ {\mathfrak {s}} ^ {\alpha - \beta} 2 ^ {- \beta n} \\ & \qquad + \| \Gamma - \bar {\Gamma} \| _ {\alpha ; \bar {\mathfrak {K}}} \| \bar {\Pi} \| _ {\alpha ; \bar {\mathfrak {K}}} \sum_ {\beta <   \alpha} \| y - z \| _ {\mathfrak {s}} ^ {\alpha - \beta} 2 ^ {- \beta n}, \end{array}
$$

where, in both instances, the sum runs over elements in A. Since we only need to consider pairs$( y , z )$such that$\| y - z \| _ { \mathfrak { s } } \geq 2 ^ { - n }$, this does imply the bound (3.30) with the desired constants, so that the claim follows from Proposition 3.25.□

Another consequence of the reconstruction theorem is that, in order to characterise a model (Π, Γ) on some sector$V \subset T$, it suffices to know the action of$\Gamma _ { x y }$on$V$, as well as the values of$( \Pi _ { x } a ) ( \varphi _ { x } ^ { n , 5 } )$for$a \in V , x \in \Lambda _ { \mathfrak { s } } ^ { n }$and$\varphi$the scaling function of some fixed sufficiently regular multiresolution analysis as in Section 3.1. More precisely, we have:

Proposition 3.32 A model$( \Pi , \Gamma )$for a given regularity structure is completely determined by the knowledge of$( \Pi _ { x } a ) ( \varphi _ { x } ^ { n , 5 } )$for$x \in \Lambda _ { \mathfrak { s } } ^ { n }$and$n \geq 0$, as well as$\Gamma _ { x y } a$for $\boldsymbol { x } , \boldsymbol { y } \in \mathbf { R } ^ { d }$

Furthermore,for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$and every sector V, one has the bound

$$
\| \Pi \| _ {V; \mathfrak {K}} \lesssim (1 + \| \Gamma \| _ {V; \mathfrak {K}}) \sup _ {\alpha \in A _ {V}} \sup _ {a \in V _ {\alpha}} \sup _ {n \geq 0} \sup _ {x \in \Lambda_ {\mathfrak {g}} ^ {n} (\bar {\mathfrak {K}})} 2 ^ {\alpha n + \frac {n | s |}{2}} \frac {| (\Pi_ {x} a) (\varphi_ {x} ^ {n , s}) |}{\| a \|}.\tag{3.46}
$$

Here, we denote by$\| \Pi \| _ { V ; \mathcal { R } }$the norm given as in Definition 2.17, but where we restrict ourselves to vectors$a \in V .$. Finally,for any two models (Π, Γ) and$( { \bar { \Pi } } , { \bar { \Gamma } } )$, one has

$$
\| \Pi - \bar {\Pi} \| _ {V; \mathfrak {K}} \lesssim (1 + \| \Gamma \| _ {V; \mathfrak {K}}) \sup _ {\alpha \in A _ {V}} \sup _ {a \in V _ {\alpha}} \sup _ {n \geq 0} \sup _ {x \in \Lambda_ {\mathfrak {s}} ^ {n} (\bar {\mathfrak {K}})} 2 ^ {\alpha n + \frac {n | s |}{2}} \frac {| (\Pi_ {x} a - \bar {\Pi} _ {x} a) (\varphi_ {x} ^ {n , \mathfrak {s}}) |}{\| a \|}.
$$

Proof. Given$a \in V _ { \alpha }$and$\boldsymbol { x } \in \mathbf { R } ^ { d }$, we define similarly to above a function$f _ { x } ^ { a } \colon { \mathbf { R } } ^ { d } \to V$ by$f _ { x } ^ { a } ( y ) = \Gamma _ { y x } a$. (This time α can be arbitrary though.) One then has$\Pi _ { y } f _ { x } ^ { a } ( y ) =$ $\Pi _ { y } \Gamma _ { y x } a = \Pi _ { x } a$, so that${ \mathcal R } f _ { x } ^ { a } = \Pi _ { x } a$. On the other hand, the proof of the reconstruction theorem only makes use of the values$( \Pi _ { x } a ) ( \varphi _ { x } ^ { n , 5 } )$) and the function$( x , y ) \mapsto \Gamma _ { x y } ,$ so that the claim follows.

The bound (3.46), as well as the corresponding bound on$\Pi - \bar { \Pi }$are an immediate consequence of Theorem 3.23, noting again that the coefficients$A _ { x } ^ { n }$only involve evaluations of$( \Pi _ { x } a ) ( \varphi _ { x } ^ { n , 5 } )$and the map$\Gamma _ { x y }$□

Although this result was very straightforward to prove, it is very important when constructing random models for a regularity structure. Indeed, provided that one has suitable moment estimates, it is in many cases possible to show that the right hand side of (3.46) is bounded almost surely. One can then make use of this knowledge to define the distribution$\Pi _ { x } a$by$\mathcal { R } f _ { x } ^ { a }$via the reconstruction theorem. This is completely analogous to Kolmogorov’s continuity criterion where the knowledge of a random function on a dense countable subset of$\dot { \mathbf { R } ^ { d } }$is sufficient to define a random variable on the space of continuous functions on$\mathbf { R } ^ { d }$as a consequence of suitable moment bounds. Actually, the standard proof of Kolmogorov’s continuity criterion is very similar in spirit to the proof given here, since it also relies on the hierarchical approximation of points in$\mathbf { R } ^ { d }$ by points with dyadic coordinates, see for example [RY91].

## 3.6 Symmetries

It will often be useful to consider modelled distributions that, although they are defined on all of$\mathbf { R } ^ { d }$, are known to obey certain symmetries. Although the extension of the framework to such a situation is completely straightforward, we perform it here mostly in order to introduce the relevant notation which will be used later.

Consider some discrete symmetry group$\mathcal { S }$which acts on$\mathbf { R } ^ { d }$via isometries$T _ { g }$. In other words, for every$g \in \mathcal { S } , T _ { g }$is an isometry of$\mathbf { R } ^ { d }$and${ \cal T } _ { g \bar { g } } = { \cal T } _ { g } \circ { \cal T } _ { \bar { g } }$. Given a regularity structure$\mathcal { T } ,$, we call a map$M \colon \mathcal { S } \stackrel { \cdot } {  } L ^ { 0 }$(where$L ^ { 0 }$is as in Section 2.4) an action of$\mathcal { S }$on$\mathcal { T }$if$M _ { g } \in \operatorname { A u t } { \mathcal { T } }$for every$g \in \mathcal { S }$and furthermore one has the identity$M _ { g \bar { g } } = M _ { \bar { g } } \circ M _ { g }$for any two elements$g , { \bar { g } } \in { \mathcal { S } }$. Note that$\mathcal { S }$also acts naturally on any space of functions on$\mathbf { R } ^ { d }$via the identity

$$
(T _ {g} ^ {\star} \psi) (x) = \psi (T _ {g} ^ {- 1} x)  .
$$

With these notations, the following definition is natural:

Definition 3.33 Let$\mathcal { S }$be a group of symmetries of$\mathbf { R } ^ { d }$acting on some regularity structure$\mathcal { T }$. A model (Π, Γ) for$\mathcal { T }$is said to be adapted to the action of$\mathcal { S }$if the following two properties hold:

For every test function$\psi : \mathbf { R } ^ { d }  \mathbf { R }$, every$\boldsymbol { x } \in \mathbf { R } ^ { d }$, every$a \in T$, and every$g \in \mathcal { S }$ one has the identity$( \Pi _ { T _ { g } x } a ) ( T _ { g } ^ { \star } \psi ) = ( \Pi _ { x } M _ { g } a ) ( \psi )$

For every$x , y \in \mathbf { R } ^ { d }$and every$g \in { \mathcal { S } } ,$, one has the identity$M _ { g } \Gamma _ { T _ { g } x T _ { g } y } = \Gamma _ { x y } M _ { g }$ A modelled distribution$f \colon \mathbf R ^ { d }  T$is said to be symmetric if$M _ { g } f ( T _ { g } x ) = f ( x )$for every$\boldsymbol { x } \in \mathbf { R } ^ { d }$and every$g \in \mathcal { S }$

Remark 3.34 One could additionally impose that the norms on the spaces$T _ { \alpha }$are chosen in such a way that the operators$M _ { g }$all have norm 1. This is not essential but makes some expressions nicer.

Remark 3.35 In the particular case where$\mathcal { T }$contains the polynomial regularity structure$\mathcal { T } _ { d , { \mathfrak { s } } }$and (Π, Γ) extends its canonical model, the action$M _ { g }$of$\mathcal { S }$on the abstract element$X$is necessarily given by$M _ { g } X = A _ { g } X$, where$A _ { g }$is the$d \times d$matrix such that$T _ { g }$acts on elements of$\mathbf { R } ^ { d }$by$T _ { g } x = A _ { g } x + b _ { g } ,$for some vector$b _ { g }$. This can be checked by making use of the first identity in Definition 3.33.

The action on elements of the form$X ^ { k }$for an arbitrary multiindex k is then naturally given by$\begin{array} { r } { M _ { g } ( X ^ { k } ) = ( A _ { g } X ) ^ { k } = \prod _ { i } ( \sum _ { j } A _ { g } ^ { i j } X _ { j } ) ^ { k _ { i } } } \end{array}$

Remark 3.36 One could have relaxed the first property to the identity$\begin{array} { r l } { ( \Pi _ { T _ { g } x } a ) ( T _ { g } ^ { \star } \psi ) = } \end{array}$ $( - 1 ) ^ { \varepsilon ( g ) } ( \Pi _ { x } M _ { g } a ) ( \psi )$, where$\varepsilon \colon \mathcal { S }  \{ \pm 1 \}$is any group morphism. This would then also allow to treat Dirichlet boundary conditions in domains generated by reflections. We will not consider this for the sake of conciseness.

Remark 3.37 While Definition 3.33 ensures that the model$( \Pi , \Gamma )$behaves “nicely” under the action of$\mathcal { S }$, this does not mean that the distributions$\Pi _ { x }$themselves are symmetric in the sense that$\Pi _ { x } ( \psi ) = \Pi _ { x } ( T _ { q } ^ { \star } \psi )$. The simplest possible example on which this is already visible is the case where$\mathcal { S }$consists of a subgroup of the translations. If we take$\mathcal { T }$to be the canonical polynomial structure and M to be the trivial action, then it is straightforward to verify that the canonical model (Π, Γ) is indeed adapted to the action of${ \mathcal { S } } .$. Furthermore,$f$being “symmetric” in this case simply means that$f$has a suitable periodicity. However, polynomials themselves of course aren’t periodic.

Our definitions were chosen in such a way that one has the following result.

Proposition 3.38 Let$\mathcal { S }$be as above, acting on$\mathcal { T }$, let (Π, Γ) be adapted to the action of${ \mathcal { S } } ,$and let$f ~ \in ~ \mathcal { D } ^ { \gamma }$(for some$\gamma \ > \ 0 )$be symmetric. Then,$\mathcal { R } f$satisfies $( \mathcal { R } f ) ( T _ { g } ^ { \star } \psi ) = ( \mathcal { R } f ) ( \psi )$for every testfunction ψ and every$g \in { \mathcal { S } } .$

Proof. Take a smooth compactly supported test function$\varphi$that integrates to 1 and fix an element$g \in \mathcal { S }$. Since$T _ { g }$is an isometry of$\mathbf { R } ^ { d }$, its action is given by$T _ { g } ( x ) =$ $A _ { g } x + b _ { g }$for some orthogonal matrix$A _ { g }$and a vector$b _ { g } ~ \in ~ \mathbf { R } ^ { d }$. We then define $\varphi ^ { \bar { g } } ( x ) = \bar { \varphi } ( A _ { q } ^ { - 1 } x )$, which is a test function having the same properties as$\varphi$itself.

One then has the identity

$$
\psi (x) = \lim _ {\lambda \rightarrow 0} \int_ {\mathbf {R} ^ {d}} (\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi) (x)   \psi (y)   d y  .
$$

Furthermore, this convergence holds not only pointwise, but in every space$\mathcal { C } ^ { k }$. As a consequence of this, combined with the reconstruction theorem, we have

$$
\begin{array}{l} (\mathcal {R} f) (\psi) = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} (\mathcal {R} f) (\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi)   \psi (y)   d y = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} (\Pi_ {y} f (y)) (\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi)   \psi (y)   d y \\ = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} (\Pi_ {T _ {g} y} M _ {g} ^ {- 1} M _ {g} f (T _ {g} y)) (T _ {g} ^ {\star} \mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi)   \psi (y)   d y \\ = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} (\Pi_ {y} f (y)) (T _ {g} ^ {\star} \mathcal {S} _ {\mathfrak {s}, T _ {g} ^ {- 1} y} ^ {\lambda} \varphi)   (T _ {g} ^ {\star} \psi) (y)   d y \\ = \lim _ {\lambda \to 0} \int_ {\mathbf {R} ^ {d}} (\Pi_ {y} f (y)) (\mathcal {S} _ {\mathfrak {s}, y} ^ {\lambda} \varphi^ {g})   (T _ {g} ^ {\star} \psi) (y)   d y = (\mathcal {R} f) (T _ {g} ^ {\star} \psi)  , \end{array}
$$

as claimed. Here, we used the symmetry of$f$and the adaptedness of$( \Pi , \Gamma )$to obtain the second line, while we performed a simple change of variables to obtain the third line.□

One particularly nice situation is that when the fundamental domain$\mathcal { \kappa }$of$\mathcal { S }$is compact in$\mathbf { R } ^ { d }$. In this case, provided of course that (Π, Γ) is adapted to the action of ${ \mathcal { S } } ,$, the analytical bounds (2.15) automatically hold over all of$\mathbf { R } ^ { d }$. The same is true for the bounds (3.1) if$f$is a symmetric modelled distribution.

## 4 Multiplication

So far, our theory was purely descriptive: we have shown that T -valued maps with a suitable regularity property can be used to provide a precise local description of a class of distributions that locally look like a given family of “model distributions”. We now proceed to show that one can perform a number of operations on these modelled distributions, while still retaining their description as elements in some$\mathcal { D } ^ { \gamma }$

The most conceptually non-trivial of such operations is of course the multiplication of distributions, which we address in this section. Surprisingly, even though elements $\mathcal { D } ^ { \gamma }$describe distributions that can potentially be extremely irregular, it is possible to work with them largely as if they consisted of continuous functions. In particular, if we are given a product ⋆ on$T$(see below for precise assumptions on ⋆), then we can multiply modelled distributions by forming the pointwise product

$$
(f \star g) (x) = f (x) \star g (x),\tag{4.1}
$$

and then projecting the result back to$T _ { \gamma } ^ { - }$for a suitable$\gamma$.

Definition 4.1 A continuous bilinear map$( a , b ) \mapsto a \star b$is a product on$T$if

For every$a \in T _ { \alpha }$and$b \in T _ { \beta }$, one has a$\star b \in T _ { \alpha + \beta }$

One has${ \bf 1 } \star a = a \star { \bf 1 } = a$for every$a \in T$

Remark 4.2 In all of the situations considered later on, the product ⋆ will furthermore be associative and commutative. However, these properties do not seem to be essential as far as the abstract theory is concerned.

Remark 4.3 What we mean by “continuous” here is that for any two indices$\alpha , \beta \in A$ the bilinear map$\star \colon T _ { \alpha } \times T _ { \beta } \to T _ { \alpha + \beta }$is continuous.

Remark 4.4 If$V _ { 1 }$and$V _ { 2 }$are two sectors of$\mathcal { T }$and ⋆ is defined as a bilinear map on $V _ { 1 } \times V _ { 2 }$, we can always extend it to$T$by setting$a \star b = 0$if either a belongs to the complement of$V _ { 1 }$or b belongs to the complement of$V _ { 2 }$.

Remark 4.5 We could have slightly relaxed the first assumption by allowing$a \star b \in$ $T _ { \alpha + \beta } ^ { + } .$. However, the current formulation appears more natural in the context of interpreting elements of the spaces$T _ { \alpha }$as “homogeneous elements”.

Ideally, one would also like to impose the additional property that$\Gamma ( a \star b ) = ( \Gamma a ) \star$ (Γb) for every$\Gamma \in G$and every$a , b \in T$. Indeed, assume for a moment that$\Pi _ { x }$takes values in some function space and that the operation ⋆ represents the actual pointwise product between two functions, namely

$$
\Pi_ {x} (a \star b) (y) = (\Pi_ {x} a) (y) (\Pi_ {x} b) (y).\tag{4.2}
$$

In this case, one has the identity

$$
\begin{array}{c} \Pi_ {x} \Gamma_ {x y} (a \star b) = \Pi_ {y} (a \star b) = (\Pi_ {y} a) (\Pi_ {y} b) = (\Pi_ {x} \Gamma_ {x y} a) (\Pi_ {x} \Gamma_ {x y} b) \\ = \Pi_ {x} (\Gamma_ {x y} a \star \Gamma_ {x y} b). \end{array}
$$

In many cases considered in this article however, the model space$T$is either finitedimensional or, even though it is infinite-dimensional, some truncation still takes place and one cannot expect (4.2) to hold exactly. Instead, the following definition ensures that it holds up to an error which is “of order$\gamma ^ { \ast }$

Definition 4.6 Let$\mathcal { T }$be a regularity structure, let$V$and$W$be two sectors of$\mathcal { T }$, and let ⋆ be a product on$\mathcal { T }$. The pair$( V , W )$is said to be γ-regular if$\Gamma ( a { \star } b ) = ( \Gamma a ) { \star } ( \Gamma b )$ for every$\Gamma \in G$and for every$a \in V _ { \alpha }$and$b \in W _ { \beta }$such that$\alpha + \beta < \gamma$and every $\Gamma \in G$

We say that$( V , W )$is regular if it is γ-regular for every$\gamma$. In the case$V = W$, we say that$V$is (γ-)regular if this is true for the pair (V, V).

The aim of this section is to demonstrate that, provided that a pair of sectors is γ-regular for some$\gamma > 0$, the pointwise product between modelled distributions in these sectors yields again a modelled distribution. Throughout this section, we assume that$V$and$W$are two sectors of regularities$\alpha _ { 1 }$and$\alpha _ { 2 }$respectively. We then have the following:

Theorem 4.7 Let$( V , W )$be a pair of sectors with regularities$\alpha _ { 1 }$and$\alpha _ { 2 }$respectively, let$f _ { 1 } \in { \mathcal { D } } ^ { \gamma _ { 1 } } ( V )$and$f _ { 2 } \in { \mathcal { D } } ^ { \gamma _ { 2 } } ( W )$, and let$\gamma = ( \gamma _ { 1 } + \alpha _ { 2 } ) \wedge ( \gamma _ { 2 } + \alpha _ { 1 } )$. Then, provided that$( V , W )$is γ-regular, one has$f _ { 1 } \star f _ { 2 } \in { \mathcal { D } } ^ { \gamma } ( T )$and, for every compact set${ \mathcal { R } } ,$the bound

$$
\left\| f _ {1} \star f _ {2} \right\| _ {\gamma ; \mathfrak {K}} \lesssim \left\| f _ {1} \right\| _ {\gamma_ {1}; \mathfrak {K}} \left\| f _ {2} \right\| _ {\gamma_ {2}; \mathfrak {K}} (1 + \| \Gamma \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}}) ^ {2},
$$

holds for some proportionality constant only depending on the underlying structure$\mathcal { T }$

Remark 4.8 If we denote as before by$\mathcal { D } _ { \alpha } ^ { \gamma }$an element of${ \mathcal { D } } ^ { \gamma } ( V )$for some sector$V$of regularity α, then Theorem 4.7 can loosely be stated as

$$
f _ {1} \in \mathcal {D} _ {\alpha_ {1}} ^ {\gamma_ {1}} \& f _ {2} \in \mathcal {D} _ {\alpha_ {2}} ^ {\gamma_ {2}} \Rightarrow f _ {1} \star f _ {2} \in \mathcal {D} _ {\alpha} ^ {\gamma},
$$

where$\alpha = \alpha _ { 1 } + \alpha _ { 2 }$and$\gamma = ( \gamma _ { 1 } + \alpha _ { 2 } ) \wedge ( \gamma _ { 2 } + \alpha _ { 1 } )$. This statement appears to be slightly misleading since it completely glosses over the assumption that the pair$( V , W )$ be γ-regular. However, at the expense of possibly extending the regularity structure$\mathcal { T }$ and the model (Π, Γ), we will see in Proposition 4.11 below that it is always possible to ensure that this assumption holds, albeit possibly in a non-canonical way.

Remark 4.9 The proof of this result is a rather straightforward consequence of our definitions, combined with standard algebraic manipulations. It has nontrivial consequences mostly when combined with the reconstruction theorem, Theorem 3.10.

Proof of Theorem$4 . 7 .$Note first that since we are only interested in showing that$f _ { 1 }$⋆ $f _ { 2 } ~ \in ~ \mathcal { D } ^ { \gamma }$, we discard all of the components in$T _ { \gamma } ^ { + }$. (See also Remark 3.2.) As a consequence, we actually consider the function given by

$$
f (x) \stackrel {{\text { def }}} {{=}} \left(f _ {1} \star_ {\gamma} f _ {2}\right) (x) \stackrel {{\text { def }}} {{=}} \sum_ {m + n <   \gamma} \mathcal {Q} _ {m} f _ {1} (x) \star \mathcal {Q} _ {n} f _ {2} (x).\tag{4.3}
$$

It then follows immediately from the properties of the product that

$$
\left\| f _ {1} \star_ {\gamma} f _ {2} \right\| _ {\gamma ; \mathfrak {K}} \lesssim \left\| f _ {1} \right\| _ {V; \mathfrak {K}} \left\| f _ {2} \right\| _ {W; \mathfrak {K}},
$$

where the proportionality constant depends only on$\gamma$and$\mathcal { T }$, but not on${ \mathcal { \mathrm { R } } } .$

From now on we will assume that$\| f _ { 1 } \| _ { V ; \mathbb { A } } \leq 1$and$\| f _ { 2 } \| _ { W ; \mathscr { R } } \leq 1$, which is not a restriction by bilinearity. It remains to obtain a bound on

$$
\Gamma_ {x y} (f _ {1} \star_ {\gamma} f _ {2}) (y) - (f _ {1} \star_ {\gamma} f _ {2}) (x).
$$

Using the triangle inequality and recalling that$\mathcal { Q } _ { \ell } ( f _ { 1 } \star _ { \gamma } f _ { 2 } ) = \mathcal { Q } _ { \ell } ( f _ { 1 } \star f _ { 2 } )$for$\gamma < \ell ,$ we can write

$$
\begin{array}{l} \| \Gamma_ {x y} f (y) - f (x) \| _ {\ell} \leq \| \Gamma_ {x y} (f _ {1} \star_ {\gamma} f _ {2}) (y) - (\Gamma_ {x y} f _ {1} (y)) \star (\Gamma_ {x y} f _ {2} (y)) \| _ {\ell} \\ \qquad + \| (\Gamma_ {x y} f _ {1} (y) - f _ {1} (x)) \star (\Gamma_ {x y} f _ {2} (y) - f _ {2} (x)) \| _ {\ell} \\ \qquad + \| (\Gamma_ {x y} f _ {1} (y) - f _ {1} (x)) \star f _ {2} (x) \| _ {\ell} \\ \qquad + \| f _ {1} (x) \star (\Gamma_ {x y} f _ {2} (y) - f _ {2} (x)) \| _ {\ell}. \end{array}\tag{4.4}
$$

It follows from (4.3) and the definition of$( V , W )$being γ-regular that for the first term, one has the identity

$$
\Gamma_ {x y} f (y) - \left(\Gamma_ {x y} f _ {1} (y)\right) \star \left(\Gamma_ {x y} f _ {2} (y)\right) = - \sum_ {m + n \geq \gamma} \left(\Gamma_ {x y} \mathcal {Q} _ {m} f _ {1} (y)\right) \star \left(\Gamma_ {x y} \mathcal {Q} _ {n} f _ {2} (y)\right).\tag{4.5}
$$

Furthermore, one has

$$
\begin{array}{l} \| (\Gamma_ {x y} \mathcal {Q} _ {m} f _ {1} (y)) \star (\Gamma_ {x y} \mathcal {Q} _ {n} f _ {2} (y)) \| _ {\ell} \lesssim \sum_ {\beta_ {1} + \beta_ {2} = \ell} \| \Gamma_ {x y} \mathcal {Q} _ {m} f _ {1} (y) \| _ {\beta_ {1}} \| \Gamma_ {x y} \mathcal {Q} _ {n} f _ {2} (y) \| _ {\beta_ {2}} \\ \lesssim \sum_ {\beta_ {1} + \beta_ {2} = \ell} \| \Gamma \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}} ^ {2} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \beta_ {1} - \beta_ {2}} \end{array}
$$

$$
\lesssim \| \Gamma \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}} ^ {2} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell}\tag{4.6}
$$

where we have made use of the facts that$m + n \ge \gamma$and that$\| x - y \| _ { 5 } \leq 1$

It follows from the properties of the product ⋆ that the second term in (4.4) is bounded by a constant times

$$
\begin{array}{l} \sum_ {\beta_ {1} + \beta_ {2} = \ell} \| \Gamma_ {x y} f _ {1} (y) - f _ {1} (x) \| _ {\beta_ {1}} \| \Gamma_ {x y} f _ {2} (y) - f _ {2} (x) \| _ {\beta_ {2}} \\ \lesssim \sum_ {\beta_ {1} + \beta_ {2} = \ell} \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {1} - \beta_ {1}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {2} - \beta_ {2}} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {1} + \gamma_ {2} - \ell}. \end{array}
$$

The third term is bounded by a constant times

$$
\sum_ {\beta_ {1} + \beta_ {2} = \ell} \| \Gamma_ {x y} f _ {1} (y) - f _ {1} (x) \| _ {\beta_ {1}} \| f _ {2} (x) \| _ {\beta_ {2}} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {1} - \beta_ {1}} \mathbf {1} _ {\beta_ {2} \geq \alpha_ {2}} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {1} + \alpha_ {2} - \ell},
$$

where the second inequality uses the identity$\beta _ { 1 } + \beta _ { 2 } = \ell .$. The last term is bounded similarly by reversing the roles played by$f _ { 1 }$and$f _ { 2 }$.□

In applications, one would also like to have suitable continuity properties of the product as a function of its factors. By bilinearity, it is of course straightforward to obtain bounds of the type

$$
\begin{array}{l} \| f _ {1} \star f _ {2} - g _ {1} \star g _ {2} \| _ {\gamma ; \mathfrak {K}} \lesssim \| f _ {1} - g _ {1} \| _ {\gamma_ {1}; \mathfrak {K}} \| f _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} + \| f _ {2} - g _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} \| g _ {1} \| _ {\gamma_ {1}; \mathfrak {K}}, \\ \| f _ {1} \star f _ {2} - g _ {1} \star g _ {2} \| _ {\gamma ; \mathfrak {K}} \lesssim \| f _ {1} - g _ {1} \| _ {\gamma_ {2}; \mathfrak {K}} \| f _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} + \| f _ {2} - g _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} \| g _ {1} \| _ {\gamma_ {1}; \mathfrak {K}}, \end{array}
$$

provided that both$f _ { i }$and$g _ { i }$belong to$\mathcal { D } ^ { \gamma _ { i } }$with respect to the same model. Note also that as before the proportionality constants implicit in these bounds depend on the size of Γ in the domain${ \mathcal { R } } .$However, one has also the following improved bound:

Proposition 4.10 Let$( V , W )$be as above, let (Π, Γ) and$( { \bar { \Pi } } , { \bar { \Gamma } } )$be two modelsfor$\mathcal { T } _ { ; }$ and let$f _ { 1 } \in \mathcal { D } ^ { \gamma _ { 1 } } ( V ; \Gamma ) , f _ { 2 } \in \mathcal { D } ^ { \gamma _ { 2 } } ( W ; \Gamma ) , g _ { 1 } \in \mathcal { D } ^ { \gamma _ { 1 } } ( V ; \bar { \Gamma } ) , a n d g _ { 2 } \in \mathcal { D } ^ { \gamma _ { 2 } } ( W ; \bar { \Gamma } )$

Then, for every$C > 0 ,$, one has the bound

$$
\left\| f _ {1} \star f _ {2}; g _ {1} \star g _ {2} \right\| _ {\gamma ; \mathfrak {K}} \lesssim \left\| f _ {1}; g _ {1} \right\| _ {\gamma_ {1}; \mathfrak {K}} + \left\| f _ {2}; g _ {2} \right\| _ {\gamma_ {2}; \mathfrak {K}} + \left\| \Gamma - \bar {\Gamma} \right\| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}},
$$

uniformly over all$f _ { i }$and$g _ { i }$with$\| f _ { i } \| _ { \gamma _ { i } ; \mathbb { R } } + \| g _ { i } \| _ { \gamma _ { i } ; \mathbb { R } } \le C ,$, as well as models satisfying $\| \Gamma \| _ { \gamma _ { 1 } + \gamma _ { 2 } ; \Re } + \| \bar { \Gamma } \| _ { \gamma _ { 1 } + \gamma _ { 2 } ; \Re } \leq C$. Here, the proportionality constant depends only on C.

Proof. As before, our aim is to bound the components in$T _ { \ell }$for$\ell < \gamma$of the quantity

$$
f _ {1} (x) \star f _ {2} (x) - g _ {1} (x) \star g _ {2} (x) - \Gamma_ {x y} (f _ {1} \star_ {\gamma} f _ {2}) (y) + \bar {\Gamma} _ {x y} (g _ {1} \star_ {\gamma} g _ {2}) (y).
$$

First, as in the proof of Theorem$4 . 7 ,$we would like to replace$\Gamma _ { x y } ( f _ { 1 } \star _ { \gamma } f _ { 2 } ) ( y )$by $\Gamma _ { x y } f _ { 1 } ( y ) \star \Gamma _ { x y } f _ { 2 } ( y )$and similarly for the corresponding term involving the$g _ { i }$. This can be done just as in (4.6), which yields a bound of the order

$$
\big (\| \Gamma - \bar {\Gamma} \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}} + \| f _ {1} - g _ {1} \| _ {\gamma_ {1}; \mathfrak {K}} + \| f _ {2} - g _ {2} \| _ {\gamma_ {2}; \mathfrak {K}} \big) \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell},
$$

as required. We rewrite the remainder as

$$
f _ {1} (x) \star f _ {2} (x) - g _ {1} (x) \star g _ {2} (x) - \Gamma_ {x y} f _ {1} (y) \star \Gamma_ {x y} f _ {2} (y) + \bar {\Gamma} _ {x y} g _ {1} (y) \star \bar {\Gamma} _ {x y} g _ {2} (y)
$$

$$
\begin{array}{l} = \big (f _ {1} (x) - g _ {1} (x) - \Gamma_ {x y} f _ {1} (y) + \bar {\Gamma} _ {x y} g _ {1} (y) \big) \star f _ {2} (x) \\ \quad + \Gamma_ {x y} f _ {1} (y) \star \big (f _ {2} (x) - g _ {2} (x) - \Gamma_ {x y} f _ {2} (y) + \bar {\Gamma} _ {x y} g _ {2} (y) \big) \\ \quad + \bar {\Gamma} _ {x y} \big (g _ {1} (y) - f _ {1} (y) \big) \star \big (\bar {\Gamma} _ {x y} g _ {2} (y) - g _ {2} (x) \big) \\ \quad + \big (\bar {\Gamma} _ {x y} f _ {1} (y) - \Gamma_ {x y} f _ {1} (y) \big) \star \big (\bar {\Gamma} _ {x y} g _ {2} (y) - g _ {2} (x) \big) \\ \quad + \big (g _ {1} (y) - \bar {\Gamma} _ {x y} g _ {1} (y) \big) \star \big (f _ {2} (x) - g _ {2} (x) \big) \\ \stackrel {{\mathrm{def}}} {{=}} T _ {1} + T _ {2} + T _ {3} + T _ {4} + T _ {5}. \end{array}\tag{4.7}
$$

It follows from the definition of$\| \cdot ; \cdot \| _ { \gamma _ { 1 } ; \mathcal { R } }$that we have the bound

$$
\| T_{1}\|_{\ell}\lesssim \| f_{1};g_{1}\|_{\gamma_{1};\mathfrak{K}}\sum_{\substack{m + n = \ell \\ m\geq \alpha_{1};n\geq \alpha_{2}}}\| x - y\|_{\mathfrak{s}}^{\gamma_{1} - m}  .
$$

(As usual, sums are performed over exponents in$A . )$Since the largest possible value for m is equal to$\ell - \alpha _ { 2 } ,$, this is the required bound. A similar bound on$T _ { 2 }$follows in virtually the same way. The term$T _ { 3 }$is bounded by

$$
\| T_{3}\|_{\ell}\lesssim \| f_{1} - g_{1}\|_{\gamma_{1};\mathfrak{K}}\sum_{\substack{m + n = \ell \\ m\geq \alpha_{1};n\geq \alpha_{2}}}\| x - y\|_{\mathfrak{s}}^{\gamma_{2} - n}  .
$$

Again, the largest possible value for n is given by$\ell - \alpha _ { 1 }$, so the required bound follows. The bound on$T _ { 4 }$is obtained in a similar way, replacing$\| f _ { 1 } - g _ { 1 } \| _ { \gamma _ { 1 } ; \mathbb { A } } \mathrm { b y } \| \Gamma - \bar { \Gamma } \| _ { \gamma _ { 1 } ; \mathbb { A } }$ The last term$T _ { 5 }$is very similar to$T _ { 3 }$and can be bounded in the same fashion, thus concluding the proof.□

As already announced earlier, the regularity condition on$( V , W )$can always be satisfied by possibly extending our regularity structure. However, at this level of generality, the way of extending$\mathcal { T }$and (Π, Γ) can of course not be expected to be canonical! In practice, one would have to identify a “natural” extension, which can potentially require a great deal of effort. Our abstract result however is:

Proposition 4.11 Let$\mathcal { T }$be a regularity structure such that each of the$T _ { \alpha }$is finitedimensional, let$( V , W )$be two sectors of${ \mathcal { T } } ,$, let (Π, Γ) be a model for${ \mathcal { T } } ,$, and let $\gamma \in \mathbf { R } .$. Then, it is always possible to find a regularity structure$\bar { \mathcal T }$containing$\mathcal { T }$and a model (Π<sup>¯</sup> , Γ<sup>¯</sup>)for$\bar { \mathcal T }$extending (Π, Γ), such that the pair$( \iota V , \iota W )$is γ-regular in$\bar { \mathcal T }$.

Proof. It suffices to consider the situation where there exist α and$\beta$in A such that $( V , W )$is$( \alpha + \beta )$-regular but ⋆ isn’t yet defined on$V _ { \alpha }$and$W _ { \beta }$. In such a situation, we build the required extension as follows. First, extend the action of G to$T \oplus ( V _ { \alpha } \otimes W _ { \beta } )$ by setting

$$
\Gamma (a \otimes b) \stackrel {{\text { def }}} {{=}} \Gamma a \bar {\star} \Gamma b, \quad a \in V _ {\alpha}, \quad b \in W _ {\beta}, \quad \Gamma \in G,\tag{4.8}
$$

where ¯⋆ is defined on$V _ { \alpha } \times W _ { \beta }$by$a \bar { \star } b = a \otimes b .$. (Outside of$V _ { \alpha } \times W _ { \beta }$, we simply set $\bar { \star } = \star . )$Then, consider some linear equivalence relation on$T _ { \alpha + \beta } \oplus ( V _ { \alpha } \otimes W _ { \beta } )$such that

$$
a \sim b \Rightarrow \Gamma a - a = \Gamma b - b \quad \forall \Gamma \in G,\tag{4.9}
$$

and such that no two elements in$T _ { \alpha + \beta }$are equivalent. (Note that the implication only goes from left to right. In particular, it is always possible to take for the trivial relation under which no two distinct elements are equivalent. However, allowing for non-trivial equivalence relations allows to impose additional algebraic properties, like the commutativity of ¯⋆ or Leibniz’s rule.) Given such an equivalence relation, we now define$\bar { \mathcal { T } } = ( \bar { A } , \bar { T } , \bar { G } )$by setting

$$
\bar {A} = A \cup \{\alpha + \beta \}, \quad \bar {T} _ {\alpha + \beta} = (T _ {\alpha + \beta} \oplus (V _ {\alpha} \otimes W _ {\beta})) / \sim .
$$

For$\gamma \neq \alpha + \beta$, we simply set$\bar { T } _ { \gamma } = T _ { \gamma }$. Furthermore, we use ¯⋆ as the product in$\bar { T }$ which, by construction, coincides with ⋆, except on$T _ { \alpha } \otimes T _ { \beta }$. Finally, the group$\bar { G }$is identical to$G$as an abstract group, but each element of$G$is extended to$\bar { T } _ { \alpha + \beta }$in the way described above. Property (4.9) ensures that this is well-defined in the sense that the action of$G$on different elements of an equivalence class of$\sim$is compatible.

It remains to extend (Π, Γ) to a model (Π<sup>¯</sup> , Γ<sup>¯</sup>) for$\bar { \mathcal T }$as an abstract group element, with its action on$\bar { T }$given by (4.8). For Γ<sup>¯</sup>, we simply set$\bar { \Gamma } _ { x y } = \Gamma _ { x y }$. The definition (4.9) then ensures that the bound (2.15) for Γ also holds for elements in$\bar { T } _ { \alpha + \beta }$. Regarding Π<sup>¯</sup> , since$\bar { T } _ { \alpha + \beta }$still contains$T _ { \alpha + \beta }$as a subspace, it remains to define it on some basis of the complement of$T _ { \alpha + \beta }$in$\bar { T } _ { \alpha + \beta }$. For each such basis vector$^ { a , }$we can then proceed as in Proposition 3.31 to construct$\Pi _ { x } a$for some (and therefore all)$\boldsymbol { x } \in \mathbf { R } ^ { d }$ More precisely, we define$\Pi _ { x } a$by$\Pi _ { x } a = \mathcal { R } f _ { a , x }$with$f _ { a , x }$as in (3.44), where  is the reconstruction operator given in the proof of Theorem$3 . 1 0$. In case$\alpha + \beta \leq 0 ,$ the choice of$\mathcal { R }$is not unique and we explicitly make the choice given in (3.38) for a suitable wavelet basis. This definition then implies for any two points x and z the identity

$$
\Pi_ {z} \Gamma_ {z x} a - \Pi_ {x} a = \Pi_ {z} a - \Pi_ {x} a + \Pi_ {z} (\Gamma_ {z x} a - a) = \mathcal {R} (f _ {a, z} - f _ {a, x}) + \Pi_ {z} (\Gamma_ {z x} a - a),
$$

where we used the linearity of$\mathcal { R }$. Note now that$( f _ { a , z } - f _ { a , x } ) ( y ) = \Gamma _ { y z } ( a - \Gamma _ { z x } a )$ so that we are precisely in the situation of$_ { ( 3 . 3 9 ) }$. This shows that our construction guarantees that$\mathcal { R } ( f _ { a , z } - f _ { a , x } ) ~ = ~ - \Pi _ { z } ( \Gamma _ { z x } a - a )$, so that the algebraic identity $\Pi _ { z } \Gamma _ { z x } a = \Pi _ { x } a$holds for any two points, as required. The required analytical bounds on$\Pi _ { x } a$on the other hand are an immediate consequence of Theorem 3.10.

As a byproduct of our construction and of Proposition 3.31, we see that the extension is essentially unique if α$+ \beta > 0$, but that there is considerable freedom whenever $\alpha + \beta \leq 0$□

Remark 4.12 At this stage one might wonder what the meaning of$\mathcal { R } ( f _ { 1 } \star f _ { 2 } )$is in situations where the distributions$\mathcal { R } f _ { 1 }$and$\mathcal { R } f _ { 2 }$cannot be multiplied in any “classical” sense. In general, this strongly depends on the choice of model and of regularity structure. However, we will see below that in cases where the model was built using a natural renormalisation procedure and the$f _ { i }$are obtained as solutions to some fixed point problem, it is usually possible to interpret$\mathcal { R } ( f _ { 1 } \star f _ { 2 } )$as the weak limit of some (possibly quite non-trivial) expression involving the$f _ { i } { } ^ { \circ } \mathrm { s }$

Remark 4.13 In situations where a model happens to consist of continuous functions such that one has indeed$\Pi _ { x } ( a \star b ) ( y ) \ = \ \left( \Pi _ { x } a \right) ( y ) ( \Pi _ { x } b ) ( y )$, it follows from Remark 3.15 that one has the identity$\mathcal { R } ( f _ { 1 } \star f _ { 2 } ) = \mathcal { R } f _ { 1 } \mathcal { R } f _ { 2 }$. In some situations, it may thus happen that there are natural approximating models and approximating functions such that$\begin{array} { r } { \mathcal { R } f _ { 1 } = \operatorname* { l i m } _ { \varepsilon \to 0 } \mathcal { R } _ { \varepsilon } f _ { 1 ; \varepsilon } } \end{array}$(and similarly for$f _ { 2 } )$and$\mathcal { R } ( f _ { 1 } \star f _ { 2 } ) =$ $\begin{array} { r } { \operatorname* { l i m } _ { \varepsilon \to 0 } ( \mathcal { R } _ { \varepsilon } f _ { 1 ; \varepsilon } ) ( \mathcal { R } _ { \varepsilon } f _ { 2 ; \varepsilon } ) } \end{array}$. See for example Section 4.4, as well as [CQ02, FV10a].

However, this need not always be the case. As we have already seen in Section$2 . 4 ,$ the formalism is sufficiently flexible to allow for products that encode some renormalisation procedure, which is actually the main purpose of this theory.

## 4.1 Classical multiplication

We are now able to give a rather straightforward application of this theory, which can be seen as a multidimensional analogue of Young integration. In the case of the Euclidean scaling, this result is of course well-known, see for example [BCD11].

Proposition 4.14 For$\alpha , \beta \in \mathbf { R } ,$, the map$( f , g ) \mapsto f \cdot \underline { { \vartriangle } }$extends to a continuous bilinear map from$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( \mathbf { R } ^ { d } ) \times \mathcal { C } _ { \mathfrak { s } } ^ { \beta } ( \mathbf { R } ^ { d } ) t o \mathcal { C } _ { \mathfrak { s } } ^ { \alpha \wedge \beta } ( \bar { \mathbf { R } ^ { d } } ) \mathrm { ~ } i f \alpha + \bar { \beta } > 0 .$. Furthermore,$i f \alpha \not \in \mathbf { N } ,$, then this condition is also necessary.

Remark 4.15 More precisely, if$\mathscr { R }$is a compact subset of$\mathbf { R } ^ { d }$and K<sup>¯</sup> its 1-fattening, then there exists a constant$C$such that

$$
\left\| f \cdot g \right\| _ {(\alpha \wedge \beta); \mathfrak {K}} \leq C \| f \| _ {\alpha ; \bar {\mathfrak {K}}} \| g \| _ {\beta ; \bar {\mathfrak {K}}},\tag{4.10}
$$

for any two smooth functions$f$and$g .$

Proof. The necessity of the condition$\alpha + \beta > 0$is straightforward. Fixing a compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$and assuming that$\alpha + \beta \le 0$(or the corresponding strict inequality for integer values), it suffices to exhibit a sequence of${ \mathcal { C } } ^ { r }$functions$f _ { n } , g _ { n } \in \mathcal { C } ( \mathcal { R } )$(with $r > \operatorname* { m a x } \{ | \alpha | , | \beta | \} )$such that$\left\{ f _ { n } \right\}$is bounded in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha } ( \mathfrak { s } ) , g _ { n }$is bounded in$\mathcal { C } _ { \mathfrak { s } } ^ { \beta } ( \mathfrak { s } )$, and $\langle f _ { n } , g _ { n } \rangle \to \infty$, where$\langle \cdot , \cdot \rangle$denotes the usual$L ^ { 2 }$-scalar product. This is because, since $f _ { n }$and$g _ { n }$are supported in${ \mathfrak { R } } ,$one can easily find a smooth compactly supported test function$\varphi$such that$\langle f _ { n } , g _ { n } \rangle = \langle \varphi , f _ { n } g _ { n } \rangle$

A straightforward modification of$[ \mathrm { M e y } 9 2$, Thm 6.5] shows that the characterisation of Proposition 3.20 for$f \in \mathcal { C } ( \mathbb { A } )$to belong to$\mathcal { C } _ { s } ^ { \alpha }$is also valid for$\alpha \in \mathbf { R } _ { + } \backslash \mathbf { N }$(since $f$is compactly supported, there are no boundary effects). The required counterexample can then easily be constructed by setting for example

$$
f _ {n} = \sum_ {k = 0} ^ {n} \frac {1}{\sqrt {k}} \sum_ {x \in \Lambda_ {k} ^ {\mathfrak {s}} \cap \bar {\mathfrak {K}}} 2 ^ {- k \frac {| \mathfrak {s} |}{2} - \alpha k} \psi_ {x} ^ {k, \mathfrak {s}},
$$

and similarly for$g _ { n }$with α replaced by$\beta .$Here,${ \bar { \mathcal { R } } } \subset { \mathcal { R } }$is such that the support of each of the$\psi _ { x } ^ { k , { \mathfrak { s } } }$is indeed in K. (One may have to start the sum from some$k _ { 0 } > 0 . )$) Noting that lim$\mathfrak { l } _ { n  \infty } \langle f _ { n } , g _ { n } \rangle = \infty$as soon as$\alpha + \beta \leq 0$, this is the required counterexample.

Combining Theorem 4.7 and the reconstruction theorem, Theorem 3.10, we can give a short and elegant proof of the sufficiency of$\alpha + \beta > 0$that no longer makes any reference to wavelet analysis. Assume from now on that$\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for some$\alpha < 0$ and that$f \in \mathcal { C } _ { \mathfrak { s } } ^ { \beta }$for some$\beta > | \alpha |$. By bilinearity, we can also assume without loss of generality that the norms appearing in the right hand side of (4.10) are bounded by 1. We then build a regularity structure$\mathcal { T }$in the following way. For the set$A ,$we take $A = \mathbf { N } \cup ( \mathbf { N } + \alpha )$. For$T ,$, we set$T = V \oplus W$, where each of the sectors$V$and W is a copy of$\mathcal { T } _ { d , { \mathfrak { s } } }$, the canonical model. We also choose Γ as in the canonical model, acting simultaneously on each of the two instances.

As before, we denote by$X ^ { k }$the canonical basis vectors in$V .$We also use the suggestive notation${ \stackrel { 6 6 } { \mathop {  X } } } ^ { k } { \stackrel { , } { \mathop { ( } } \lambda ^ { 6 } ) }$for the corresponding basis vector in$W$, but we postulate that$\Xi X ^ { k } \in T _ { \alpha + | k | }$rather than$\Xi X ^ { k } \in { \cal T } _ { | k | _ { s } }$. With this notation at hand, we also s define the product ⋆ between$V$and W by the natural identity

$$
\left(\Xi X ^ {k}\right) \star \left(X ^ {\ell}\right) = \Xi X ^ {k + \ell}.
$$

It is straightforward to verify that, with this product, the pair (V, W) is regular.

Finally, we define a map$J \colon { \mathcal { C } } _ { \mathfrak { s } } ^ { \alpha }  { \mathcal { M } } _ { { \mathcal { T } } }$given by$J \colon \xi \mapsto ( \Pi ^ { \xi } , \Gamma )$, where Γ is as in the canonical model, while Π<sup>ξ</sup> acts as

$$
(\Pi_ {x} ^ {\xi} X ^ {k}) (y) = (y - x) ^ {k}, \qquad (\Pi_ {x} ^ {\xi} \Xi X ^ {k}) (y) = (y - x) ^ {k} \xi (y),
$$

with the obvious abuse of notation in the second expression. It is then straightforward to verify that$\Pi _ { y } = \Pi _ { x } \circ \Gamma _ { x y }$and that the map J is Lipschitz continuous.

Denote now by$\mathcal { R } ^ { \xi }$the reconstruction map associated to the model$J ( \xi )$and, for$u \in$ $\mathcal { C } _ { \mathfrak { s } } ^ { \beta }$, denote by$\mathcal { T } _ { \beta } u$as in$_ { ( 2 . 6 ) }$the unique element in${ \mathcal { D } } ^ { \beta } ( V )$such that$\langle \mathbf { 1 } , ( \mathcal { T } _ { \beta } u ) ( x ) \rangle =$ $u ( x )$. Note that even though the space${ \mathcal { D } } ^ { \beta } ( V )$does in principle depend on the choice of model, in our situation it is independent of$\xi$for every model$J ( \xi )$. Since, when viewed as a W-valued function, one has$\Xi \in { \mathcal { D } } ^ { \infty } ( W )$, one has$\mathcal { T } _ { \beta } u \star \Xi \in \mathcal { D } ^ { \alpha + \beta }$by Theorem 4.7. We now consider the map

$$
B (u, \xi) = \mathcal {R} ^ {\xi} (\mathcal {T} _ {\beta} u \star \Xi).
$$

By Theorem 3.10, combined with the continuity of J, this is a jointly continuous map from$\mathcal { C } _ { \mathfrak { s } } ^ { \beta } \times \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$into$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$, provided that$\alpha + \beta > 0$. If ξ happens to be a smooth function, then it follows immediately from Remark 3.15 that$B ( u , \xi ) = u ( x ) \xi ( x )$, so that B is indeed the requested continuous extension of the product.□

## 4.2 Composition with smooth functions

In general, it makes no sense to compose elements$f ~ \in ~ \mathcal { D } ^ { \gamma }$with arbitrary smooth functions. In the particular case when$f \in { \mathcal { D } } ^ { \gamma } ( V )$for a function-like sector V however, this is possible. Throughout this subsection, we decompose elements$a \in V$as$a =$ $\bar { a } \mathbf { 1 } + \tilde { a } ,$, with$\tilde { a } \in T _ { 0 } ^ { + }$and$\bar { a } = \langle \mathbf { 1 } , a \rangle$. (This notation is suggestive of the fact that a˜ encodes the small-scale fluctuations of$\Pi _ { x } a$near x.) We denote by$\zeta > 0$the smallest non-zero value such that$V _ { \zeta } \neq 0$, so that one actually has$\tilde { a } \in T _ { \epsilon } ^ { + }$

Given a function-like sector$V$and a smooth function$F \colon \vec { \mathbf { R } ^ { n } }  \mathbf { R }$, we lift$F$to a function${ \hat { F } } \colon V ^ { n } \to V$by setting

$$
\hat {F} (a) = \sum_ {k} \frac {D ^ {k} F (\bar {a})}{k !} \tilde {a} ^ {\star k},\tag{4.11}
$$

where the sum runs over all possible multiindices. Here,$a = ( a _ { 1 } , \ldots , a _ { n } )$with$a _ { i } \in V$ and, for an arbitrary multiindex$k = ( k _ { 1 } , \ldots , k _ { n } )$, we used the shorthand notation

$$
\tilde {a} ^ {\star k} = \tilde {a} _ {1} ^ {\star k _ {1}} \star \dots \star \tilde {a} _ {d} ^ {\star k _ {n}},
$$

with the convention that$\tilde { a } ^ { \star 0 } = \mathbf { 1 }$

In order for this definition to make any sense, the sector V needs of course to be endowed with a product ⋆ which also leaves V invariant. In principle, the sum in (4.11) looks infinite, but by the properties of the product ⋆, we have$\tilde { a } ^ { \star k } \in T _ { | k | \zeta } ^ { + }$. Since $\zeta$is strictly positive, only finitely many terms in (4.11) contribute at each order of homogeneity, so that$\hat { F } ( a )$is well-defined as soon as$F \in { \mathcal { C } } ^ { \infty }$. The main result in this subsection is given by:

Theorem 4.16 Let V be afunction-like sector ofsome regularity structure$\mathcal { T }$, let$\zeta >$ 0 be as above, let$\gamma > 0 ,$, and let$F \in \mathcal { C } ^ { \kappa } ( \mathbf { R } ^ { k }$, R) for some$\kappa \geq \gamma / \zeta \vee 1$. Assume furthermore that$V$is γ-regular. Then,for any$f \in { \mathcal { D } } ^ { \gamma } ( V )$, the map$\hat { F } _ { \gamma } ( f )$defined by

$$
\hat {F} _ {\gamma} (f) (x) = \mathcal {Q} _ {\gamma} ^ {-} \hat {F} (f (x)),
$$

again belongs to${ \mathcal { D } } ^ { \gamma } ( V )$. Ifonefurthermore has$F \in \mathcal { C } ^ { \kappa } ( \mathbf { R } ^ { k } , \mathbf { R } ) f o r \kappa \geq ( \gamma / \zeta \vee 1 ) + 1$ then the map$f \mapsto { \hat { F } } ( f )$is locally Lipschitz continuous in the sense that one has the bounds

$$
\| \hat {F} _ {\gamma} (f) - \hat {F} _ {\gamma} (g) \| _ {\gamma ; \mathfrak {K}} \lesssim \| f - g \| _ {\gamma ; \mathfrak {K}}, \quad \| \hat {F} _ {\gamma} (f) - \hat {F} _ {\gamma} (g) \| _ {\gamma ; \mathfrak {K}} \lesssim \| f - g \| _ {\gamma ; \mathfrak {K}},\tag{4.12}
$$

for any compact set$\mathcal { R } \subset \mathbf { R } ^ { d } ,$, where the proportionality constant in the first bound is uniform over all$f , g$with$\| f \| _ { \gamma ; \mathbb { A } } + \| g \| _ { \gamma ; \mathbb { A } } \le C$, while in the second bound it is uniform over all$f , g$with$\| f \| _ { \gamma ; \mathbb { A } } + \| g \| _ { \gamma ; \mathbb { A } } \le C ,$, for any fixed constant$C .$. We furthermore performed a slight abuse ofnotation by writing again$\| f \| _ { \gamma ; \kappa } ( f o r$example) instead of $\textstyle \sum _ { i \leq n } { \| f _ { i } \| _ { \gamma ; \mathscr { R } } }$

Proof. From now on we redefine ζ so that$\zeta = \gamma$in the case when A contains no index between 0 and γ. In this case, our original condition$\kappa \geq \gamma / \zeta \vee 1$reads simply as $\kappa \geq \gamma / \zeta$

Let$L = \lfloor \gamma / \zeta \rfloor$, which is the length of the largest multiindex appearing in (4.11) which still yields a contribution to$T _ { \gamma } ^ { - }$. Writing$b ( x ) = \mathcal { Q } _ { \gamma } ^ { - } \hat { F } \big ( f ( x ) \big )$, we aim to find a bound on$\Gamma _ { y x } b ( x ) - b ( y )$. It follows from a straightforward generalisation of the computation from Theorem 4.7 that

$$
\begin{array}{l} \Gamma_ {y x} b (x) = \sum_ {| k | \leq L} \frac {D ^ {k} F (\bar {f} (x))}{k !} \Gamma_ {y x} (\mathcal {Q} _ {\gamma} ^ {-} \tilde {f} (x) ^ {\star k}) \\ = \sum_ {| k | \leq L} \frac {D ^ {k} F (\bar {f} (x))}{k !} (\Gamma_ {y x} \tilde {f} (x)) ^ {\star k} + R _ {1} (x, y), \end{array}
$$

with a remainder term$R _ { 1 }$such that$\| R _ { 1 } ( x , y ) \| _ { \beta } \lesssim \| x - y \| _ { \mathfrak { s } } ^ { \gamma - \beta }$, for all$\beta < \gamma$. Since $\Gamma _ { y x } \mathbf { 1 } = \mathbf { 1 }$, we can furthermore write

$$
\Gamma_ {y x} \tilde {f} (x) = \Gamma_ {y x} f (x) - \bar {f} (x) {\bf 1} = \tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) {\bf 1} + R _ {f} (x, y),
$$

where, by the assumption on$f ,$the remainder term$R _ { f }$again satisfies the bound $\| R _ { f } ( x , y ) \| _ { \beta } \lesssim \| x - y \| _ { \mathfrak { s } } ^ { \gamma - \beta }$for all$\beta < \gamma$. Combining this with the bound we already obtained, we get

$$
\Gamma_ {y x} b (x) = \sum_ {| k | \leq L} \frac {D ^ {k} F (\bar {f} (x))}{k !} (\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1}) ^ {\star k} + R _ {2} (x, y),\tag{4.13}
$$

with

$$
\| R _ {2} (x, y) \| _ {\beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \beta},
$$

for all$\beta < \gamma$as above. We now expand$D ^ { k } F$around$\bar { f } ( y )$, yielding

$$
D ^ {k} F (\bar {f} (x)) = \sum_ {| k + \ell | \leq L} \frac {D ^ {k + \ell} F (\bar {f} (y))}{\ell !} (\bar {f} (x) - \bar {f} (y)) ^ {\ell} + \mathcal {O} (\| x - y \| _ {\mathfrak {s}} ^ {\gamma - | k | \zeta}),\tag{4.14}
$$

where we made use of the fact that$| { \bar { f } } ( x ) - { \bar { f } } ( y ) | \lesssim \| x - y \| _ { \mathfrak { s } } ^ { \zeta }$by the definition of$\mathcal { D } ^ { \gamma }$ and the fact that$F \operatorname { i s } { \mathcal { C } } ^ { \gamma / \zeta }$by assumption. Similarly, we have the bound

$$
\left\| \left(\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1}\right) ^ {\star k} \right\| _ {\beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\zeta | k | - \beta},\tag{4.15}
$$

so that, combining this with (4.13) and (4.14), we obtain the identity

$$
\Gamma_ {y x} b (x) = \sum_ {| k + \ell | \leq L} \frac {D ^ {k + \ell} F (\bar {f} (y))}{k ! \ell !} (\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1}) ^ {\star k} (\bar {f} (x) - \bar {f} (y)) ^ {\ell} + R _ {3} (x, y),\tag{4.16}
$$

where$R _ { 3 }$is again a remainder term satisfying the bound

$$
\| R _ {3} (x, y) \| _ {\beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \beta}.\tag{4.17}
$$

Using the generalised binomial identity, we have

$$
\sum_ {k + \ell = m} \frac {1}{k ! \ell !} (\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1}) ^ {\star k} (\bar {f} (x) - \bar {f} (y)) ^ {\ell} = \frac {\tilde {f} (y) ^ {\star m}}{m !},
$$

so that the component in$T _ { \gamma } ^ { - }$of the first term in the right hand side of (4.16) is precisely equal to the component in$T _ { \gamma } ^ { - }$of$b ( y )$. Since the remainder satisfies (4.17), this shows that one does indeed have$b \in { \mathcal { D } } ^ { \gamma } ( V )$.

The first bound in (4.12) is immediate from the definition$( 4 . 1 1 )$, as well as the fact that the assumption implies the local Lipschitz continuity of$D ^ { k } F$for every$| k | \leq L$

The second bound is a little more involved. One way of obtaining it is to first define $h = f - g$and to note that one then has the identity

$$
\begin{array}{l} \hat {F} (f (x)) - \hat {F} (g (x)) = \sum_ {k, i} \int_ {0} ^ {1} \frac {D ^ {k + e _ {i}} F (\bar {g} (x) + t \bar {h} (x))}{k !} (\tilde {g} (x) + t \tilde {h} (x)) ^ {\star k} \bar {h} _ {i} (x) d t \\ \qquad + \sum_ {k, i} \int_ {0} ^ {1} \frac {D ^ {k} F (\bar {g} (x) + t \bar {h} (x))}{k !} k _ {i} (\tilde {g} (x) + t \tilde {h} (x)) ^ {\star (k - e _ {i})} \tilde {h} _ {i} (x) d t \\ \qquad = \sum_ {k, i} \int_ {0} ^ {1} \frac {D ^ {k + e _ {i}} F (\bar {g} (x) + t \bar {h} (x))}{k !} (\tilde {g} (x) + t \tilde {h} (x)) ^ {\star k} h _ {i} (x) d t. \end{array}
$$

Here, k runs over all possible multiindices and i takes the values$1 , \ldots , n$. We used the notation$e _ { i }$for the ith canonical multiindex. Note also that our way of writing the second term makes sense since, whenever$k _ { i } ~ = ~ 0$so that$k - e _ { i }$isn’t a multiindex anymore, it vanishes thanks to the prefactor$k _ { i }$

From this point on, the calculation is virtually identical to the calculation already performed previously. The main differences are that F appears with one more derivative and that every term always appears with a prefactor h, which is responsible for the bound proportional to$\| h \| _ { \gamma ; \mathcal { R } }$□

## 4.3 Relation to Hopf algebras

Structures like the one of Definition 4.6 must seem somewhat familiar to the reader used to the formalism of Hopf algebras [Swe69]. Indeed, there are several natural instances of regularity structures that are obtained from a Hopf algebra (see for example Section 4.4 below). This will also be useful in the context of the kind of structures arising when solving semilinear PDEs, so let us quickly outline this construction.

Let be a connected, graded, commutative Hopf algebra with product ⋆ and a compatible coproduct$\Delta$so that$\Delta ( f \star g ) = \Delta f \star \Delta g$. We assume that the grading is indexed by$\mathbf { \bar { z } } _ { + } ^ { d }$for some$d \geq 1$, so that$\mathcal { H } = \oplus _ { k \in \mathbf { Z } _ { + } ^ { d } } \mathcal { H } _ { k }$, and that each of the $\mathcal { H } _ { k }$is finite-dimensional. The grading is assumed to be compatible with the product structures, meaning that

$$
\star \colon \mathcal {H} _ {k} \otimes \mathcal {H} _ {\ell} \to \mathcal {H} _ {k + \ell}, \quad \Delta \colon \mathcal {H} _ {k} \to \bigoplus_ {\ell + m = k} \mathcal {H} _ {\ell} \otimes \mathcal {H} _ {m}.\tag{4.18}
$$

Furthermore,$\mathcal { H } _ { 0 }$is spanned by the unit 1 (this is the definition of connectedness), the antipode$\mathcal { A }$maps$\mathcal { H } _ { k }$to itself for every$k ,$and the counit$^ { 1 ^ { * } }$is normalised so that $\langle \mathbf { 1 } ^ { * } , \mathbf { 1 } \rangle = 1$

The dual$\mathcal { H } ^ { \star } = \oplus _ { k \in \mathbf { Z } _ { \pm } ^ { d } } \mathcal { H } _ { k } ^ { * }$is then again a graded Hopf algebra with a product Lgiven by the adjoint of$\Delta$and a coproduct$\Delta ^ { \star }$given by the adjoint of ⋆. (Note that while ⋆ is assumed to be commutative, is definitely not in general!) By (4.18), both and$\Delta ^ { \star }$respect the grading of$\mathcal { H } ^ { \star }$. There is a natural action Γ of$\mathcal { H } ^ { \star }$onto given by the identity

$$
\langle \ell , \Gamma_ {g} f \rangle = \langle \ell \circ g, f \rangle ,\tag{4.19}
$$

valid for all$\ell , g \in { \mathcal { H } } ^ { \star }$and all$f \in { \mathcal { H } } .$An alternative way of writing this is

$$
\Gamma_ {g} f = (1 \otimes g) \Delta f,\tag{4.20}
$$

where we view$g$as a linear operator from$\mathcal { H }$to R. It follows easily from (4.18) that, if $g$and$f$are homogeneous of degrees$d _ { g }$and$d _ { f }$respectively, then$\Gamma _ { g } f$is homogeneous of degree$d _ { f } \mathrm { ~ - ~ } d _ { g }$, provided that$d _ { f } - d _ { g } \in \mathbf { Z } _ { + } ^ { d }$. If not, then one necessarily has $\Gamma _ { g } f = 0$

Remark 4.17 Another natural action of$\mathcal { H } ^ { \star }$onto would be given by

$$
\langle \ell , \bar {\Gamma} _ {g} f \rangle = \left\langle (\mathcal {A} ^ {\star} g) \circ \ell , f \right\rangle ,
$$

where,$\mathcal { A } ^ { \star }$, the adjoint of${ \mathcal { A } } ,$is the antipode for$\mathcal { H } ^ { \star }$. Since it is an antihomomorphism, one has indeed the required identity$\bar { \Gamma } _ { g _ { 1 } } \bar { \Gamma } _ { g _ { 2 } } = \bar { \Gamma } _ { g _ { 1 } \circ g _ { 2 } }$

Since we assumed that ⋆ is commutative, it follows from the Milnor-Moore theorem [MM65] that$\mathcal { H } ^ { \star }$is the universal enveloping algebra of$P ( \mathcal { H } ^ { \star } )$, the set of primitive elements of$\mathcal { H } ^ { \star }$given by

$$
P (\mathcal {H} ^ {\star}) = \left\{g \in \mathcal {H} ^ {\star}: \Delta^ {\star} g = \mathbf {1} ^ {\star} \otimes g + g \otimes \mathbf {1} ^ {\star} \right\}.
$$

Using the fact that the coproduct$\Delta ^ { \star }$is an algebra morphism, it is easy to check that $P ( \mathcal { H } ^ { \star } )$is indeed a Lie algebra with bracket given by$[ g _ { 1 } , g _ { 2 } ] = g _ { 1 } \circ g _ { 2 } - g _ { 2 } \circ g _ { 1 }$. This yields in a natural way a Lie group$G \subset { \mathcal { H } } ^ { \star }$given by$G = \exp ( P ( \mathcal { H } ^ { \star } ) )$). It turns out (see [Swe67]) that this Lie group has the very useful property that

$$
\Delta^ {\star} (g) = g \otimes g, \quad \forall g \in G.
$$

As a consequence, it is straightforward to verify that one has the remarkable identity

$$
\Gamma_ {g} (f _ {1} \star f _ {2}) = (\Gamma_ {g} f _ {1}) \star (\Gamma_ {g} f _ {2}),\tag{4.21}
$$

valid for every$g \in G$. This is nothing but an exact version of the regularity requirement of Definition 4.6! Note also that (4.21) is definitely not true for arbitrary elements $g \in \mathcal { H } ^ { \star }$

All this suggests that a very natural way of constructing a regularity structure is from a graded commutative Hopf algebra. The typical set-up will then be to fix scaling exponents$\{ \alpha _ { i } \} _ { i = 1 } ^ { d }$and to write$\begin{array} { r } { \langle \alpha , k \rangle = \sum _ { i = 1 } ^ { d } \alpha _ { i } k _ { 1 } } \end{array}$for any index$k \in \mathbf { Z } _ { + } ^ { d }$. We then set

$$
A = \left\{\langle \alpha , k \rangle : k \in \mathbf {Z} _ {+} ^ {d} \right\}, T _ {\gamma} = \bigoplus_ {\langle \alpha , k \rangle = \gamma} \mathcal {H} _ {k}.
$$

With this notation at hand, we have:

Lemma 4.18 In the setting ofthis subsection,$( A , T , G )$is a regularity structure, with G acting on T via Γ. Furthermore, T equipped with the product ⋆ is regular.

Proof. In view of (4.21), the only property that remains to be shown is that$\Gamma _ { g } a - a \in$ $T _ { \gamma } ^ { - }$for$a \in T _ { \gamma }$

It is easy to show that$P ( \mathcal { H } ^ { \star } )$has a basis consisting of homogeneous elements and that these belong to$\mathcal { H } _ { k } ^ { \star }$for some$k \neq 0$. (Since$\Delta ^ { \star } \mathbf { 1 } ^ { \star } = \mathbf { 1 } ^ { \star } \otimes \mathbf { 1 } ^ { \star } . )$As a consequence, for$a \in T _ { \gamma } , g \in P ( \mathcal { H } ^ { \star } )$, and$n > 0$, we have$\Gamma _ { g ^ { n } } a \in T _ { \beta }$for some$\beta < \gamma$. Since every element of$G$is of the form exp(g) for some$g \in P ( \mathcal { H } ^ { \star } )$and since$g \mapsto \Gamma _ { g }$is linear, one has indeed$\Gamma _ { g } a - a \in T _ { \gamma } ^ { - }$□

Remark 4.19 The canonical regularity structure is an example of a regularity structure that can be obtained via this construction. Indeed, a natural dual to the space of polynomials in$d$indeterminates is given by the space$\mathcal { H } ^ { \star }$of differential operators over$\mathbf { R } ^ { d }$with constant coefficients, which does itself come with a natural commutative product given by the composition of operators. (Here, the word “differential operator” should be taken in a somewhat loose sense since it consists in general of an infinite power series.) Given such a differential operator$\mathcal { L }$and an (abstract) polynomial$P ,$a natural duality pairing$\langle \mathcal { L } , P \rangle$is given by applying$\mathcal { L }$to$P$and evaluating the resulting polynomial at the origin. Somewhat informally, one sets

$$
\langle \mathcal {L}, P \rangle = (\mathcal {L} P) (0).
$$

The action Γ described in (4.19) is then given by simply applying$\mathcal { L }$to$P 3$

$$
\Gamma_ {\mathcal {L}} P = \mathcal {L} P.
$$

It is indeed obvious that (4.19) holds in this case. The space of primitives of$\mathcal { H } ^ { \star }$then consists of those differential operators that satisfy Leibniz’s rule, which are of course precisely the first-order differential operators. The group-like elements consist of their exponentials, which act on polynomials indeed precisely as the group of translations on$\mathbf { R } ^ { d }$

## 4.4 Rough paths

A prime example of a regularity structure on R that is quite different from the canonical structure of polynomials is the structure associated to E-valued geometric rough paths of class$\mathcal { C } ^ { \gamma }$for some$\gamma \in ( 0 , 1 ]$, and some Banach space$E .$. For an introduction to the theory of rough paths, see for example the monographs [LQ02, LCL07, FV10b] or the original article [Lyo98]. We will see in this section that, given a Banach space$E ,$we can associate to it in a natural way a regularity structure$\Re _ { E } ^ { \gamma }$which describes the space of E-valued rough paths. The regularity index$\gamma$will only appear in the definition of the index set A. Given such a structure, the space of rough paths with regularity γ turns out to be nothing but the space of models for$\Re _ { E } ^ { \gamma }$

Setting$A = \gamma \mathbf { N } ,$we take for$T$the tensor algebra built upon$E ^ { * }$, the topological dual of$E \colon$

$$
T = \bigoplus_ {k = 0} ^ {\infty} T _ {k \gamma}, \quad T _ {k \gamma} = (E ^ {*}) ^ {\otimes k},\tag{4.22}
$$

where$( E ^ { * } ) ^ { \otimes 0 } = \mathbf { R }$. The choice of tensor product on$E$and$E ^ { * }$does not matter in principle, as long as we are consistent in the sense that$\left( E ^ { \otimes k } \right) ^ { * } = ( E ^ { * } ) ^ { \otimes k }$for every$k .$ We also introduce the space$T _ { \star }$(which is the predual of$T )$as the tensor algebra built from$E ,$namely$T _ { \star } = T ( ( E ) )$).

Remark 4.20 One would like to write again$T _ { \star } = \bigoplus _ { k = 0 } ^ { \infty } E ^ { \otimes k }$. However, while we Lconsider for T finite linear combinations of elements in the spaces$T _ { k \gamma }$, for$T _ { \star }$, it will be useful to allow for infinite linear combinations.

Both$T$and$T _ { \star }$come equipped with a natural product. On$T _ { \star }$, it will be natural to consider the tensor product$\otimes ,$which will be used to define$G$and its action on$T ,$ The space$T$also comes equipped with a natural product, the shuffle product, which plays in this context the role that polynomial multiplication played for the canonical regularity structures. Recall that, for any alphabet$\mathcal { W }$, the shuffle product  is defined on the free algebra over$\mathcal { W }$by considering all possible ways of interleaving two words in ways that preserve the original order of the letters. In our context, if$^ { a , }$b and c are elements of$E ^ { * }$, we set for example

$$
(a \otimes b) \text {山} (a \otimes c) = a \otimes b \otimes a \otimes c + 2 a \otimes a \otimes b \otimes c + 2 a \otimes a \otimes c \otimes b + a \otimes c \otimes a \otimes b.
$$

Regarding the group$G ,$we then perform the following construction. For any two elements$a , b \in T _ { \star }$, we define their$^ { 6 6 } \mathrm { I }$Lie bracket” by

$$
[ a, b ] = a \otimes b - b \otimes a.
$$

We then define$\mathfrak { L } \subset T ,$as the (possibly infinite) linear combinations of all such brackets, and we set$G = \exp ( \mathfrak { L } ) \subset T _ { \star }$, with the group operation given by the tensor product. Here, for any element$a \in T _ { \star }$, we write

$$
\exp (a) = \sum_ {k = 0} ^ {\infty} \frac {a ^ {\otimes k}}{k !},
$$

with the convention that$a ^ { \otimes 0 } = \mathbf { 1 } \in T _ { 0 }$. Note that this sum makes sense for every element in$T _ { \star }$, and that$\exp ( - a ) = \left( \exp ( a ) \right) ^ { - 1 }$. For every$a \in G$, the corresponding linear map$\Gamma _ { a }$acting on$T$is then obtained by duality, via the identity

$$
\langle c, \Gamma_ {a} b \rangle = \left\langle a ^ {- 1} \otimes c, b \right\rangle ,\tag{4.23}
$$

where$\langle \cdot , \cdot \rangle$denotes the pairing between$T$and$T _ { \star }$. Let us denote by$\Re _ { E } ^ { \gamma }$the regularity structure$( A , T , G )$constructed in this way.

Remark 4.21 The regularity structure$\Re _ { E } ^ { \gamma }$is yet another example of a regularity structure that can be obtained via the general construction of Section 4.3. In this case, our Hopf algebra is given by$T ,$equipped with the commutative product  and the non-commutative coproduct obtained from$\otimes { \mathsf { b y } }$duality. The required morphism property then just reflects the fact that the shuffle product is indeed a morphism for the deconcatenation coproduct. The choice of action is then the one given by Remark 4.17.

What are the models (Π, Γ) for the regularity structure$\Re _ { E } ^ { \gamma } \}$It turns out that the elements$\Gamma _ { s t }$(which we identify with an element$X _ { s t }$in$T _ { \star }$acting via (4.23)) are nothing but what is generally referred to as geometric rough paths. Indeed, the identity $\Gamma _ { s t } \circ \Gamma _ { t u } = \Gamma _ { s u }$, translates into the identity

$$
\boldsymbol {X} _ {s u} = \boldsymbol {X} _ {s t} \otimes \boldsymbol {X} _ {t u},\tag{4.24}
$$

which is nothing but Chen’s relations [Che54]. The bound (2.21) on the other hand precisely states that the rough path X is γ-H¨older continuous in the sense of [FV10b] for example. Finally, it is well-known (see (4.21) or [Reu93]) that, for$a \in T _ { k \gamma }$and $b \in T _ { \ell \gamma }$with$k + \ell \leq p ,$and any$\Gamma \in G ,$one has the shuffle identity,

$$
\Gamma (a \sqcup b) = (\Gamma a) \sqcup (\Gamma b),
$$

which can be interpreted as a way of encoding the chain rule. This should again be compared to Definition$4 . 6 ,$which shows that the shuffle product is indeed the natural product for$T$in this context and that$T$is regular for .

By Proposition 3.31, since our regularity structure only contains elements of positive homogeneity, the model Π is uniquely determined by Γ. It is straightforward to check that if we set

$$
(\Pi_ {s} a) (t) = \left<   \boldsymbol {X} _ {s t}, a \right > ,
$$

then the relations and bounds of Definition 2.17 are indeed satisfied, so that this is the unique model Π compatible with a given choice of Γ (or equivalently X).

The interpretation of such a rough path is as follows. Denote by$X _ { t }$the projection of$X _ { 0 t }$onto$E _ { \mathrm { { : } } }$, the predual of$T _ { \gamma }$. Then, for every$a \in T _ { k \gamma }$with$k \in \mathbf { N } ,$, we interpret $\langle X _ { s t } , a \rangle$as providing a value for the corresponding k-fold iterated integral, i.e.,

$$
\left\langle \boldsymbol {X} _ {s t}, a \right\rangle “ = ” \int_ {s} ^ {t} \int_ {s} ^ {t _ {k}} \dots \int_ {s} ^ {t _ {2}} \left\langle d X _ {t _ {1}} \otimes \dots \otimes d X _ {t _ {k - 1}} \otimes d X _ {t _ {k}}, a \right\rangle .\tag{4.25}
$$

A celebrated result by Chen [Che54] then shows that indeed, if$t \mapsto X _ { t } \ \in \ E$is a continuous function of bounded variation, and if X is defined by the right hand side of (4.25), then it is the case that$\pmb { X } _ { s t } \in G$for every s, t and (4.24) holds.

Now that we have identified geometric rough paths with the space of models realising$\Re _ { E } ^ { \gamma } ,$, it is natural to ask what is the interpretation of the spaces$\mathcal { D } ^ { \beta }$introduced in Section 3. An element$f$of$\mathcal { D } ^ { \beta }$should then be thought of as describing a function whose increments can locally (at scale ε) be approximated by linear combinations of components of$X ,$, up to errors of order$\varepsilon ^ { \beta }$. Setting$p = \lfloor 1 / \gamma \rfloor$, it can be checked that elements of$\mathcal { D } ^ { \beta }$with$\beta = p \gamma$are nothing but the controlled rough paths in the sense of [Gub04].

Writing$f _ { 0 } ( t )$for the component of$f ( t )$in$T _ { 0 } = \mathbf { R }$, it does indeed follow from the definition of$\mathcal { D } ^ { \beta }$that

$$
\left| f _ {0} (t) - \left\langle \boldsymbol {X} _ {s t}, f (s) \right\rangle \right| \lesssim | t - s | ^ {\beta}.
$$

Since, on the other hand,$\langle X _ { s t } , 1 \rangle = 1$, we see that one has indeed

$$
f _ {0} (t) - f _ {0} (s) = \langle \pmb {X} _ {s t}, \mathcal {Q} _ {0} ^ {\perp} f (s) \rangle + \mathcal {O} (| t - s | ^ {\beta}),
$$

where$\mathcal { Q } _ { 0 } ^ { \perp }$is the projection onto the orthogonal complement to 1.

The power of the theory is then that, even though$f _ { 0 }$itself is typically only γ- H¨older continuous, it does in many respects behave “as if” it was actually$\beta \mathrm { . }$-H¨older continuous, and one can have$\beta > \gamma$. In particular, it is now quite straightforward to define “integration map$\because \mathcal { T } _ { a }$for$a \in E ^ { * }$such that$F =  { \mathcal { T } } _ { a } f$should be thought of as describing the integral$\begin{array} { r } { F _ { 0 } ( t ) = \int _ { 0 } ^ { t } f _ { 0 } ( s ) d \langle X _ { s } , a \rangle } \end{array}$, provided that$\beta + \gamma > 1$

RIt follows from the interpretation (4.25) that if$f _ { 0 } ( t ) = \langle X _ { t } , b \rangle$for some element $b \in T$, then it is natural to have$F _ { 0 } ( t ) = \langle X _ { t } , b \otimes a \rangle$. At first sight, this suggests that one should simply set$F ( t ) = ( {  { \mathbb { Z } } } _ { a } f ) ( t ) = f ( t ) \otimes a .$. However, since$\langle \mathbf { 1 } , f ( t ) \otimes a \rangle = 0 .$ this would not define an element of$\mathcal { D } _ { \gamma } ^ { \beta }$for any$\beta > \gamma$so one still needs to find the correct value for$\langle \mathbf { 1 } , F ( t ) \rangle$. The following result, which is essentially a reformulation of [Gub10, Thm 8.5] in the geometric context, states that there is a unique natural way of constructing this missing component.

Theorem 4.22 For every$\beta > 1 - \gamma$and every$a \in E ^ { * }$there exists a unique linear map$I _ { a } \colon { \mathcal { D } } ^ { \beta } \to { \mathcal { C } } ^ { \gamma }$such that$( I _ { a } f ) ( 0 ) = 0$and such that the map${ \mathcal { T } } _ { a }$defined by

$$
(\mathcal {I} _ {a} f) (t) = f (t) \otimes a + (I _ {a} f) (t) \mathbf {1},
$$

maps$\mathcal { D } ^ { \beta }$into$\mathcal { D } ^ { \bar { \beta } }$with$\bar { \beta } = ( \beta \wedge \gamma p ) + \gamma$

Remark 4.23 Even in the context of the classical theory of rough paths, one advantage of the framework presented here is that it is straightforward to accommodate the case of driving processes with different orders of regularity for different components.

Remark 4.24 Using Theorem 4.22, it is straightforward to combine it with Theorem 4.16 in order to solve “rough differential equations” of the form$d Y = F ( Y ) d X$ It does indeed suffice to formulate them as fixed point problems

$$
Y = y _ {0} + \mathcal {I} (\hat {F} (Y)).
$$

As a map from$\mathcal { D } ^ { \beta } ( [ 0 , T ] )$into itself, then has norm$\mathcal { O } ( T ^ { \bar { \beta } - \beta } )$, which tends to 0 as $T  0$and the composition with$F$is (locally) Lipschitz continuous for sufficiently regular$F ,$so that this map is indeed a contraction for small enough T .

Remark 4.25 In general, one can imagine theories of integration in which the chain rule fails, which is very natural in the context of numerical approximations. In this case, it makes sense to replace the tensor algebra by the Connes-Kreimer Hopf algebra of rooted trees [Bro04], which plays in this context the role of the “free” algebra generated by the multiplication and integration maps. This is precisely what was done in [Gub10], and one can verify that the construction given there is again equivalent to the construction of Section 4.3. See also [But72, HW74] for more details on the role of the Connes-Kreimer algebra (whose group-like elements are also called the “Butcher group” in the numerical analysis literature) in the context of the numerical approximation of solutions to ODEs with smooth coefficients. See also [HK12] for an analysis of this type of structure from a different angle more closely related to the present work.

## 5 Integration against singular kernels

In this section, we show how to integrate a modelled distribution against a kernel (think of the Green’s function for the linear part of the stochastic PDE under consideration) with a well-behaved singularity on the diagonal in order to obtain another modelled distribution. In other words, given a modelled distribution$f ,$we would like to build another modelled distribution$\kappa f$with the property that

$$
(\mathcal {R K} f) (x) = \bigl (K * \mathcal {R} f \bigr) (x) \stackrel {\text { def }} {=} \int_ {\mathbf {R} ^ {d}} K (x, y) \mathcal {R} f (y) d y  ,\tag{5.1}
$$

for a given kernel K :$\mathbf { R } ^ { d } \times \mathbf { R } ^ { d }  \mathbf { R }$, which is singular on the diagonal. Here, denotes the reconstruction operator as before. Of course, this way of writing is rather formal since neither$\mathcal { R } f$nor$\mathcal { R } { \cal { K } } f$need to be functions, but it is more suggestive than the actual property we are interested in, namely

$$
(\mathcal {R K} f) (\psi) = (K * \mathcal {R} f) (\psi) \stackrel {\text { def }} {=} (\mathcal {R} f) (K ^ {\star} \psi), \quad K ^ {\star} \psi (y) \stackrel {\text { def }} {=} \int_ {\mathbf {R} ^ {d}} K (x, y) \psi (x) d x, \tag {5.2}\tag{5.2}
$$

for all sufficiently smooth test functions$\psi .$In the remainder of this section, we will always use a notation of the type (5.1) instead of (5.2) in order to state our assumptions and results. It is always straightforward to translate it into an expression that makes sense rigorously, but this would clutter the exposition of the results, so we only use the more cumbersome notation in the proofs. Furthermore, we would like to encode the fact that the kernel$K$“improves regularity by$\beta ^ { \bullet }$in the sense that, in the notation of Remark 4.8, is bounded from$\mathcal { D } _ { \alpha } ^ { \gamma }$into$\bar { \mathcal { D } } _ { ( \alpha + \beta ) \wedge 0 } ^ { \gamma + \beta }$for some$\beta > 0$. For example, in the case of the convolution with the heat kernel, one would like to obtain such a bound with$\beta = 2 .$, which would be a form of Schauder estimate in our context.

In the case when the right hand side of (5.1) actually defines a function (which is the case for many examples of interest), it may appear that it is straightforward to define$\kappa \colon$simply encode it into the canonical part of the regularity structure by (5.1) and possibly some of its derivatives. The problem with this is that since, for$f \in \mathcal { D } _ { \alpha } ^ { \gamma }$ one has${ \mathcal { R } } f \in { \mathcal { C } } ^ { \alpha }$, the best one can expect is to have$\mathcal { R } \mathcal { K } f \in \mathcal { C } ^ { \alpha + \beta }$. Encoding this into the canonical regularity structure would then yield an element of$\mathcal { D } _ { 0 } ^ { \alpha + \beta }$, provided that one even has$\alpha + \beta > 0$. In cases where$\gamma > \alpha$, which is the generic situation considered in this article, this can be substantially short of the result announced above. As a consequence,$\kappa f$should in general also have non-zero components in parts of$T$ that do not encode the canonical regularity structure, which is why the construction of is highly non-trivial.

Let us first state exactly what we mean by the fact that the kernel$K \colon \mathbf { R } ^ { d } \times \mathbf { R } ^ { d }  \mathbf { R }$ “improves regularity by order$\beta ^ { \bullet }$:

Assumption 5.1 Thefunction K can be decomposed as

$$
K (x, y) = \sum_ {n \geq 0} K _ {n} (x, y),\tag{5.3}
$$

where the functions$K _ { n }$have the following properties:

For all$n \geq 0 ,$, the map$K _ { n }$is supported in the set$\left\{ ( x , y ) : \| x - y \| _ { 5 } \leq 2 ^ { - n } \right\}$

For any two multiindices k and$\ell ,$there exists a constant$C$such that the bound

$$
\left| D _ {1} ^ {k} D _ {2} ^ {\ell} K _ {n} (x, y) \right| \leq C 2 ^ {(| \mathfrak {s} | - \beta + | \ell | _ {\mathfrak {s}} + | k | _ {\mathfrak {s}}) n},\tag{5.4}
$$

holds uniformly over all$n \geq 0$and all x,$\boldsymbol { y } \in \mathbf { R } ^ { d }$

For any two multiindices k and ℓ, there exists a constant$C$such that the bounds

$$
\begin{array}{l} \Big | \int_ {\mathbf {R} ^ {d}} (x - y) ^ {\ell} D _ {2} ^ {k} K _ {n} (x, y)   d x \Big | \leq C 2 ^ {- \beta n}, \\ \Big | \int_ {\mathbf {R} ^ {d}} (y - x) ^ {\ell} D _ {1} ^ {k} K _ {n} (x, y)   d y \Big | \leq C 2 ^ {- \beta n}, \end{array}\tag{5.5}
$$

hold uniformly over all$n \geq 0$and all$x , y \in \mathbf { R } ^ { d }$

In these expressions, we write$D _ { 1 }$for the derivative with respect to the first argument and$D _ { 2 }$for the derivative with respect to the second argument.

Remark 5.2 In principle, we typically only need (5.4) and (5.5) to hold for multi-indices k and ℓ that are smaller than some fixed number, which depends on the particular “Schauder estimate” we wish to obtain. In practice however these bounds tend to hold for all multiindices, so we assume this in order to simplify notations.

A very important insight is that polynomials are going to play a distinguished role in this section. As a consequence, we work with a fixed regularity structure$\mathcal { T } =$ $( A , T , G )$and we assume that one has$\mathcal { T } _ { d , \mathfrak { s } } \subset \mathcal { T }$for the same scaling s and dimension d as appearing in Definition 5.1. As already mentioned in Remark 2.23, we will use the notation$\bar { T } \subset T$for the subspace spanned by the “abstract polynomials”. Furthermore, as in Section 2.2, we will denote by$X ^ { k }$the canonical basis vectors of$\bar { T } .$, where k is a multiindex in$\mathbf { N } ^ { d }$. We furthermore assume that, except for polynomials, integer homogeneities are avoided:

Assumption 5.3 For every integer value$n \ge 0 , T _ { n } = \bar { T } _ { n }$consists of the linear span of elements of the form$X ^ { \dot { k } }$with$| k | _ { s } = n$. Furthermore, one considers models that are compatible with this structure in the sense that$( \Pi _ { x } X ^ { k } ) ( y ) = ( y - x ) ^ { k }$

In order to interplay nicely with our structure, we will make the following additional assumption on the decomposition of the kernel$K \colon$:

Assumption 5.4 There exists$r > 0$such that

$$
\int_ {\mathbf {R} ^ {d}} K _ {n} (x, y) P (y) d y = 0,\tag{5.6}
$$

for every$n \geq 0 ,$, every$\boldsymbol { x } \in \mathbf { R } ^ { d }$, and every polynomial P of scaled degree less than or equal to r.

All of these three assumptions will be standing throughout this whole section. We will therefore not restate this explicitly, except in the statements of the main theorems. Even though Assumption 5.4 seems quite restrictive, it turns out not to matter at all. Indeed, a kernel K that is regularity improving in the sense of Definition 5.1 can typically be rewritten as$K = K _ { 0 } + K _ { 1 }$such that$K _ { 0 }$is smooth and$K _ { 1 }$additionally satisfies both Assumptions 5.1 and 5.4. Essentially, it suffices to “excise the singularity” with the help of a compactly supported smooth cut-off function and to then add and subtract some smooth function supported away from the origin which ensures that the required number of moments vanish.

In many cases of interest, one can take K to depend only on the difference between its two arguments. In this case, one has the following result, which shows that our assumptions typically do cover the Green’s functions of differential operators with constant coefficients.

Lemma 5.5 Let$\bar { \cal K } \colon { \bf R } ^ { d } \backslash \{ 0 \}   { \mathrm { ~  ~ \cdot ~ } }$R be a smoothfunction which is homogeneous under the scaling s in the sense that there exists a$\beta > 0$such that the identity

$$
\bar {K} (\mathcal {S} _ {\mathfrak {s}} ^ {\delta} x) = \delta^ {| \mathfrak {s} | - \beta} \bar {K} (x),\tag{5.7}
$$

holdsfor all x = 0 and all$\delta \in ( 0 , 1 ]$. Then, it is possible to decompose$\bar { K }$as$\bar { K } ( x ) =$ $K ( x ) + R ( x )$in such a way that the “remainder” R is${ \mathcal { C } } ^ { \infty }$on all of$\mathbf { R } ^ { d }$and such that the map$( x , y ) \mapsto K ( x - y )$satisfies Assumptions 5.1 and 5.4.

Proof. Note first that if each of the$K _ { n }$is a function of$x - y$, then the bounds (5.5) follow from (5.4) by integration by parts. We therefore only need to exhibit a decomposition$K _ { n }$such that (5.4) is satisfied and such that (5.6) holds for every polynomial $P$of some fixed but arbitrary degree.

Let$N \colon { \mathbf { R } } ^ { d } \setminus \{ 0 \} \to { \mathbf { R } } _ { + }$be a smooth “norm” for the scaling s in the sense that $N$is smooth, convex, strictly positive, and$N ( S _ { \mathfrak { s } } ^ { \delta } x ) = \delta N ( x )$. (See for example Remark$2 . 1 3 . )$Then, we can introduce “spherical coordinates$\vec { \mathbf { \nabla } } ^ { \prime } ( r , \theta )$with$r \in \mathbf { R } _ { + }$and $\theta \in S { \stackrel { \mathrm { d e f } } { = } } N ^ { - 1 } ( 1 )$by$r ( x ) = N ( x )$, and$\theta ( x ) = S _ { \mathfrak { s } } ^ { r ( x ) } x$. With these notations, (5.7) is another way of stating that K<sup>¯</sup> can be factored as

$$
\bar {K} (x) = r ^ {\beta - | \mathfrak {s} |} \Theta (\theta),\tag{5.8}
$$

for some smooth function Θ on S. Here and below, we suppress the implicit dependency of r and θ on x.

Our main ingredient is then the existence of a smooth “cutoff function$\ " \varphi : { \bf R } _ { + }$ [0, 1] such that$\varphi ( r ) = 0$for$r \not \in [ 1 / 2 , 2 ]$, and such that

$$
\sum_ {n \in \mathbf {Z}} \varphi (2 ^ {n} r) = 1,\tag{5.9}
$$

for all$r > 0$(see for example the construction of Paley-Littlewood blocks in [BCD11]). We also set$\begin{array} { r } { \varphi _ { R } ( r ) = \sum _ { n < 0 } \varphi ( 2 ^ { n } r ) } \end{array}$and, for$n \ge 0 , \varphi _ { n } ( r ) = \varphi ( 2 ^ { n } r )$. With these Pfunctions at hand, we define

$$
\bar {K} _ {n} (x) = \varphi_ {n} (r) \bar {K} (x), \qquad \bar {R} (x) = \varphi_ {R} (r) \bar {K} (x).
$$

Since$\varphi _ { R }$is supported away from the origin, the function$\bar { R }$is globally smooth. Furthermore, each of the$\bar { K } _ { n }$is supported in the ball of radius$2 ^ { - n }$, provided that the “norm” $N$was chosen such that$N ( x ) \geq 2 \| x \| _ { \mathfrak { s } }$

It is straightforward to verify that (5.4) also holds. Indeed, by the exact scaling property (5.7) of$\bar { K } .$, one has the identity

$$
\bar {K} _ {n} (x) = 2 ^ {- (\beta - | \mathfrak {s} |) n} \bar {K} _ {0} (\mathcal {S} _ {\mathfrak {s}} ^ {2 ^ {- n}} x),
$$

and (5.4) then follows immediately form the fact that$K _ { 0 }$is a compactly supported smooth function.

It remains to modify this construction in such a way that (5.6) holds as well. For this, choose any function$\psi$which is smooth, supported in the unit ball around the origin, and such that, for every multiindex k with$| k | _ { \mathfrak { s } } \leq r ,$one has the identity

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

Since ψ is smooth and$K _ { n }$has the same scaling properties as before, it is clear that the required bounds are still satisfied. Furthermore, our construction is such that one has the identity

$$
\sum_ {n = 0} ^ {N - 1} K _ {n} (x) = \sum_ {n = 0} ^ {N - 1} \bar {K} _ {n} (x) - \psi (x) + 2 ^ {- (\beta - | \mathfrak {s} |) N} \psi (\mathcal {S} _ {\mathfrak {s}} ^ {2 ^ {N}} x),
$$

so that it is still the case that$\begin{array} { r } { \bar { K } ( x ) = R ( x ) + \sum _ { n > 0 } K _ { n } ( x ) } \end{array}$. Finally, the exact scaling properties of these expressions imply that

$$
\begin{array}{r l} \int x ^ {k} K _ {n} (x) d x & = 2 ^ {- (\beta + | k | _ {\mathfrak {s}}) n} \int x ^ {k} K _ {0} (x) d x \\ & = 2 ^ {- (\beta + | k | _ {\mathfrak {s}}) n} \int x ^ {k} \big (\bar {K} _ {0} (x) - \psi (x) + 2 ^ {| \mathfrak {s} | - \beta} \psi (\mathcal {S} _ {\mathfrak {s}} ^ {2} x) \big) d x \\ & = 2 ^ {- (\beta + | k | _ {\mathfrak {s}}) n} \int x ^ {k} \big (\bar {K} _ {0} (x) - (1 - 2 ^ {- \beta - | k | _ {\mathfrak {s}}}) \psi (x) \big) d x = 0, \end{array}
$$

as required.

Remark 5.6 A slight modification of the argument given above also allows to cover the situation where (5.8) is replaced by$\bar { K } ( x ) = \Theta ( \theta )$log r. One can then set

$$
\bar {K} _ {n} (x) = - \Theta (\theta) \int_ {r} ^ {\infty} \frac {\varphi_ {n} (r)}{r} d r,
$$

and the rest of the argument is virtually identical to the one just given. In such a situation, one then has$\beta ~ = ~ | \mathfrak { s } |$, thus covering for example the case of the Green’s function of the Laplacian in dimension 2.

Of course, in order to have any chance at all to obtain a Schauder-type bound as above, our model needs to be sufficiently$\mathbf { \ddot { r i } c h } \mathbf { \vec { \theta } } \mathbf { \vec { \phi } }$to be able to describe$\kappa f$with sufficient amount of detail. For this, we need two ingredients. First, we need the existence of a map$\mathcal { T } \colon T  T$that provides an “abstract” representation of$\mathcal { \kappa }$operating at the level of the regularity structure, and second we need that the model Π is adapted to this representation in a suitable manner.

In our definition, we denote again by$\bar { T }$the sector spanned by abstract monomials of the type$X ^ { k }$for some multiindex k.

Definition 5.7 Given a sector V , a linear map${ \mathcal { T } } \colon V \to T$is an abstract integration map of order$\beta > 0$if it satisfies the following properties:

One has${ \mathcal { T } } \colon V _ { \alpha } \to T _ { \alpha + \beta }$for every$\alpha \in A$

One has$\mathcal { T } a = 0$for every$a \in V \cap { \bar { T } }$

One has${ \underline { { \mathcal { T } } } } \Gamma a - \Gamma { \underline { { \mathcal { T } } } } a \in { \bar { T } }$for every$a \in V$and every$\Gamma \in G$

(The first property should be interpreted as$\mathcal { T } a = 0$if$a \in V _ { \alpha }$and$\alpha + \beta \not \in A . )$

Remark 5.8 At first sight, the second and third conditions might seem strange. It would have been aesthetically more pleasing to impose that commutes with G, i.e. that$\mathcal { T } \Gamma = \Gamma \mathcal { T }$. This would indeed be very natural if was a “direct” abstraction of our integration map in the sense that

$$
\Pi_ {x} \mathcal {I} a = \int_ {\mathbf {R} ^ {d}} K (\cdot , z) (\Pi_ {x} a) (d z).\tag{5.10}
$$

The problem with such a definition is that if$a \in T _ { \alpha }$with$\alpha > - \beta _ { \mathrm { { \scriptsize ~ \cdot ~ } } }$, so that$\mathcal { T } a \in T _ { \bar { \alpha } }$ for some$\bar { \alpha } > 0$, then (2.15) requires us to define$\Pi _ { x } \mathcal { Z } a$in such a way that it vanishes to some positive order for localised test functions. This is simply not true in general, so that (5.10) is not the right requirement. Instead, we will see below that one should modify (5.10) in a way to subtract a suitable polynomial that forces the$\Pi _ { x } \mathcal { Z } a$to vanish at the correct order. It is this fact that leads to consider structures with${ \underline { { \mathcal { T } } } } \Gamma a - \Gamma { \underline { { \mathcal { T } } } } a \in { \bar { T } }$ rather than$\mathscr { T } \Gamma a - \Gamma \mathscr { T } a = 0$

Our second and main ingredient is that the model should be “compatible” with the fact that encodes the integral kernel K. For this, given an integral kernel K as above, an important role will be played by the function$\mathcal { I } \colon \mathbf { R } ^ { d } \to L _ { T } ^ { \beta }$which, for every$a \in T _ { \alpha }$ and every$\alpha \in A$, is given by

$$
\mathcal {J} (x) a = \sum_ {| k | _ {\mathfrak {s}} <   \alpha + \beta} \frac {X ^ {k}}{k !} \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k} K (x, z) (\Pi_ {x} a) (d z),\tag{5.11}
$$

where we denote by$D _ { 1 }$the differentiation operator with respect to the first variable. It is straightforward to verify that, writing$K = \sum K _ { n }$as before and swapping the sum Pover n with the integration, this expression does indeed make sense.

Definition 5.9 Given a sector V and an abstract integration operator$\mathcal { T }$on$V ,$, we say that a model Π realises K for if, for every$\alpha \in A$, every$a \in V _ { \alpha }$and every$\boldsymbol { x } \in \mathbf { R } ^ { \bar { d } }$ one has the identity

$$
\Pi_ {x} \mathcal {I} a = \int_ {\mathbf {R} ^ {d}} K (\cdot , z) (\Pi_ {x} a) (d z) - \Pi_ {x} \mathcal {J} (x) a,\tag{5.12}
$$

Remark 5.10 The rigorous way of stating this definition is that, for all smooth and compactly supported test functions ψ and for all$a \in T _ { \alpha }$, one has

$$
(\Pi_ {x} \mathcal {I} a) (\psi) = \sum_ {n \geq 0} \int_ {\mathbf {R} ^ {d}} \psi (y) (\Pi_ {x} a) (K _ {n; x y} ^ {\alpha}) d y,\tag{5.13}
$$

where the function$K _ { n ; x y } ^ { \alpha }$is given by

$$
K _ {n; x y} ^ {\alpha} (z) = K _ {n} (y, z) - \sum_ {| k | _ {s} <   \alpha + \beta} \frac {(y - x) ^ {k}}{k !} D _ {1} ^ {k} K _ {n} (x, z).\tag{5.14}
$$

The purpose of subtracting the term involving the truncated Taylor expansion of$K$is to ensure that$\Pi _ { x } \mathcal { Z } a$vanishes at x at sufficiently high order. We will see below that in our context, it is always guaranteed that the sum over n appearing in (5.13) converges absolutely, see Lemma 5.19 below.

Remark 5.11 The case of simple integration in one dimension is very special in this respect. Indeed, the role of the “Green’s function” K is then played by the Heaviside function. This has the particular property of being constant away from the origin, so that all of its derivatives vanish. In particular, the quantity$\mathcal { I } ( x ) a$then always takes values in$T _ { 0 }$. This is why it is possible to consider expansions of arbitrary order in the theory of rough paths without ever having to incorporate the space of polynomials into the corresponding regularity structure.

Note however that the “rough integral” is not an immediate corollary of Theorem 5.12 below, due in particular to the fact that Assumption 5.4 does not hold for the Heaviside function. It is however straightforward to build the rough integral of any controlled path against the underlying rough path using the formalism developed here. In order not to stray too far from our main line of investigation we refrain from giving this construction.

With all of these definitions at hand, we are now in the position to provide the definition of the map$\mathcal { \kappa }$on modelled distributions announced at the beginning of this section. Actually, it turns out that for different values of$\gamma$one should use slightly different definitions. Given$f \in \mathcal { D } ^ { \gamma }$, we set

$$
\left(\mathcal {K} _ {\gamma} f\right) (x) = \mathcal {I} f (x) + \mathcal {J} (x) f (x) + \left(\mathcal {N} _ {\gamma} f\right) (x),\tag{5.15}
$$

where$\mathcal { T }$is as above, acting pointwise,$\mathcal { I }$is given in (5.11), and the operator$\mathcal { N } _ { \gamma }$maps $f$into a$\bar { T } .$-valued function by setting

$$
(\mathcal {N} _ {\gamma} f) (x) = \sum_ {| k | _ {\mathfrak {s}} <   \gamma + \beta} \frac {X ^ {k}}{k !} \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k} K (x, y) (\mathcal {R} f - \Pi_ {x} f (x)) (d y).\tag{5.16}
$$

(We will show later that this expression is indeed well-defined for all$f \in \mathcal { D } ^ { \gamma } . )$

With all of these definitions at hand, we can state the following two results, which are the linchpin around which the whole theory developed in this work revolves. First, we have the announced Schauder-type estimate:

Theorem 5.12 Let$\mathcal { T } = ( A , T , G )$be a regularity structure and (Π, Γ) be a modelfor $\mathcal { T }$satisfying Assumption 5.3. Let K be a β-regularising kernelfor some$\beta > 0 ;$, let be an abstract integration map oforder$\beta$acting on some sector$V _ { i }$, and let Π be a model realising K for . Letfurthermore$\gamma > 0 ,$, assume that$K$satisfies Assumption 5.4for $r = \gamma + \beta _ { ; }$, and define the operator$\mathcal { K } _ { \gamma } b y \ ( 5 . I 5 )$

Then, provided that$\gamma + \beta \not \in { \bf N } , { \cal K } _ { \gamma }$maps${ \mathcal { D } } ^ { \gamma } ( V )$into$\mathcal { D } ^ { \gamma + \beta }$, and the identity

$$
\mathcal {R K} _ {\gamma} f = K * \mathcal {R} f,\tag{5.17}
$$

holds for every$f \in { \mathcal { D } } ^ { \gamma } ( V )$. Furthermore,$i f ( { \bar { \Pi } } , { \bar { \Gamma } } )$is a second model realising K and one has$\bar { f } \in \mathcal { D } ^ { \gamma } ( V ; \bar { \Gamma } )$, then the bound

$$
\| \mathcal {K} _ {\gamma} f; \bar {\mathcal {K}} _ {\gamma} \bar {f} \| _ {\gamma + \beta ; \mathfrak {K}} \lesssim \| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma + \beta ; \bar {\mathfrak {K}}},
$$

holds. Here, K is a compact and$\bar { \mathbf { x } }$is its 1-fattening. The proportionality constant implicit in the bound depends only on the norms$\| f \| _ { \gamma ; \bar { \hat { \kappa } } } , \| \bar { f } \| _ { \gamma ; \bar { \hat { \kappa } } }$, as well as similar bounds on the two models.

Remark 5.13 One surprising feature of Theorem 5.12 is that the only non-local term in $\kappa _ { \gamma }$is the operator$\mathcal { N } _ { \gamma }$which is a kind of “remainder term”. In particular, the “rough”

parts of$\kappa _ { \gamma } f ,$, i.e. the fluctuations that cannot be described by the canonical model consisting of polynomials, are always obtained as the image of the “rough” parts of$f$ under a simple local linear map. We will see in Section 8 below that, as a consequence of this fact, if$f \in \mathcal { D } ^ { \gamma }$is the solution to a stochastic PDE built from a local fixed point argument using this theory, then the “rough” part in the description of$f$is always given by explicit localfunctions of the “smooth part”, which can be interpreted as some kind of renormalised Taylor series.

The assumptions on the model Π and on the regularity structure$\mathcal { T } = ( A , T , G )$(in particular the existence of a map  with the right properties) may look quite stringent at first sight. However, it turns out that it is always possible to embed any regularity structure$\mathcal { T }$into a larger regularity structure in such a way that these assumptions are satisfied. This is our second main result, which can be stated in the following way.

Theorem 5.14 (Extension theorem) Let$\mathcal { T } = ( A , T , G )$be a regularity structure containing the canonical regularity structure$\mathcal { T } _ { d , { \mathfrak { s } } }$as stated in Assumption 5.3, let$\beta > 0 _ { i }$ and let$V \subset T$be a sector of order γ¯ with the property that for every α  N with $V _ { \alpha } \neq 0 ,$one has$\alpha + \beta \not \in \mathbf { N } .$. Let furthermore$W \subset V$be a subsector ofV and let K be a kernel on$\mathbf { R } ^ { d }$satisfying Assumptions 5.1 and 5.4 for every$r \leq \bar { \gamma }$. Let (Π, Γ) be a modelfor$\mathcal { T }$, and let$\mathcal { T } \colon W \to T$be an abstract integration map of order$\beta$such that Π realises$K f o r \mathcal { T } .$

Then, there exists a regularity structure$\hat { \mathcal T }$containing$\mathcal { T } _ { ; }$, a model$( \hat { \Pi } , \hat { \Gamma } ) f o r \mathcal { \hat { T } }$ extending (Π, Γ), and an abstract integration map <sup>ˆ</sup> of order$\beta$acting on$\hat { V } = \iota V$such that:

The model Π<sup>ˆ</sup> realises K for <sup>ˆ</sup>.

The map$\hat { \mathcal { T } }$extends in the sense that$\hat { \mathcal { T } } \iota a = \iota \mathcal { T } a$for every$a \in W$

Furthermore, the map$( \Pi , \Gamma ) \mapsto ( \hat { \Pi } , \hat { \Gamma } )$is locally bounded and Lipschitz continuous in the sense that$i f ( \Pi , \Gamma )$and (Π<sup>¯</sup> , Γ<sup>¯</sup>) are two modelsfor$\mathcal { T }$and (Π<sup>ˆ</sup>, Γ<sup>ˆ</sup>) and$( \ddot { \Pi } , \dot { \bar { \Gamma } } )$are their respective extensions, then one has the bounds

$$
\| \hat {\Pi} \| _ {\hat {V}; \mathfrak {K}} + \| \hat {\Gamma} \| _ {\hat {V}; \mathfrak {K}} \lesssim \| \Pi \| _ {V; \bar {\mathfrak {K}}} (1 + \| \Gamma \| _ {V; \bar {\mathfrak {K}}}),\tag{5.18}
$$

$$
\| \hat {\Pi} - \hat {\bar {\Pi}} \| _ {\hat {V}; \mathfrak {K}} + \| \hat {\Gamma} - \hat {\bar {\Gamma}} \| _ {\hat {V}; \mathfrak {K}} \lesssim \| \Pi - \bar {\Pi} \| _ {V; \bar {\mathfrak {K}}} (1 + \| \Gamma \| _ {V; \bar {\mathfrak {K}}}) + \| \bar {\Pi} \| _ {V; \bar {\mathfrak {K}}} \| \Gamma - \bar {\Gamma} \| _ {V; \bar {\mathfrak {K}}},
$$

for any compact$\mathcal { R } \subset \mathbf { R } ^ { d }$and its 2-fattening K<sup>¯</sup>.

Remark 5.15 In this statement, the sector$W$is also allowed to be empty. See also Section 8.2 below for a general construction showing how one can build a regularity structure from an abstract integration map.

The remainder of this section is devoted to the proof of these two results. We start with the proof of the extension theorem, which allows us to introduce all the objects that are then needed in the proof of the multi-level Schauder estimate, Theorem 5.12.

## 5.1 Proof of the extension theorem

Before we turn to the proof, we prove the following lemma which will turn out to be very useful:

Lemma 5.16 Let$\mathcal { I } \colon \mathbf { R } ^ { d }  \bar { T }$be as above, let$V \subset T$be a sector, and let :$V  T$ be adapted to the kernel K. Then one has the identity

$$
\Gamma_ {x y} (\mathcal {I} + \mathcal {J} (y)) = (\mathcal {I} + \mathcal {J} (x)) \Gamma_ {x y},\tag{5.19}
$$

for every x,$y \in \mathbf { R } ^ { d } .$

Proof. Note first that$\mathcal { I }$is well-defined in the sense that the following expression converges:

$$
\big(\mathcal{J}(x)a \big)_{k} = \frac{1}{k!}\sum_{\substack{\gamma \in A\\ |k|_{\mathfrak{s}} <   \gamma +\beta}}\sum_{n\geq 0}(\Pi_{x}\mathcal{Q}_{\gamma}a)(D_{1}^{k}K_{n}(x,\cdot))  .\tag{5.20}
$$

Indeed, applying the bound (5.29) which will be obtained in the proof of Lemma 5.19 below, we see that the sum in (5.20) is uniformly convergent for every$\gamma \in A$

In order to show (5.19) we use the fact that, by the definition of an abstract integration map, we have$\Gamma _ { x y } \mathcal { T } a - \mathcal { T } \Gamma _ { x y } a \in \bar { T }$for every$a \in T$and every pair$x , y \in \mathbf { \bar { R } } ^ { d }$ Since$\Pi _ { x }$is injective on$\bar { T }$(it maps an abstract polynomial into its concrete realisation based at x), it therefore suffices to show that one has the identity

$$
\Pi_ {y} (\mathcal {I} + \mathcal {J} (y)) = \Pi_ {x} (\mathcal {I} + \mathcal {J} (x)) \Gamma_ {x y}.
$$

This however follows immediately from (5.12).

ProofofTheorem 5.14. We first argue that we can assume without loss of generality that we are in a situation where the sector$V$is given by a finite sum

$$
V = V _ {\alpha_ {1}} \oplus V _ {\alpha_ {2}} \oplus \ldots \oplus V _ {\alpha_ {n}},\tag{5.21}
$$

where the$\alpha _ { i }$are an increasing sequence of elements in$A ,$and where furthermore $W _ { \alpha _ { k } } ~ = ~ V _ { \alpha _ { k } }$for all$k \ < \ n$. Indeed, we can first consider the case$V = V _ { \alpha _ { 1 } }$and $W = W _ { \alpha _ { 1 } }$and apply our result to build an extension to all of$V _ { \alpha _ { 1 } }$. We then consider the case$V ~ = ~ V _ { \alpha _ { 1 } } \oplus V _ { \alpha _ { 2 } }$and$W \ : = \ : V _ { \alpha _ { 1 } }$①$W _ { \alpha _ { 2 } } ,$, etc. We then denote by W<sup>¯</sup> the complement of$W _ { \alpha _ { n } }$in$V _ { \alpha _ { r } }$so that$V _ { \alpha _ { n } } = W _ { \alpha _ { n } } \oplus \bar { W } _ { \alpha _ { n } }$

The proof then consists of two steps. First, we build the regularity structure$\hat { \mathcal { T } } =$ $( \hat { A } , \hat { T } , \hat { G } )$and the map$\hat { \mathcal { T } } _ { : }$, and we show that they have the required properties. In a second step, we will then build the required extension (Π<sup>ˆ</sup> , Γ<sup>ˆ</sup>) and we will show that it satisfies the identity given by Definition$5 . 9 ,$, as well as the bounds of Definition 2.17 required to make it a bona fide model for$\hat { \mathcal T }$

The only reason why$\mathcal { T }$needs to be extended is that we have no way a priori to define$\hat { \mathcal { T } }$to$\bar { W } .$, so we simply add a copy of it to$T$and we postulate this copy to be image of$\bar { W }$under the extension$\hat { \mathcal { T } }$of . We then extend G in a way which is consistent with Definition 5.7. More precisely, our construction goes as follows. We first define

$$
\hat {A} = A \cup \left\{\alpha_ {n} + \beta \right\},
$$

where$\alpha _ { n }$is as in (5.21), and we define$\hat { T }$to be the space given by

$$
\hat {T} = T \oplus \bar {W}.
$$

We henceforth denote elements in$\hat { T }$by$( a , b )$with$a \in T$and$b \in \bar { W }$, and the injection map$\iota \colon T  { \hat { T } }$is simply given by$\iota a = ( a , 0 )$. Furthermore, we set

$$
\hat {T} _ {\alpha} = \left\{ \begin{array}{l l} T _ {\alpha} \oplus \bar {W} & \text { if } \alpha = \alpha_ {n} + \beta , \\ T _ {\alpha} \oplus 0 & \text { otherwise }. \end{array} \right.
$$

With these notations, one then indeed has the identity$\hat { T } = \oplus _ { \alpha \in \hat { A } } \hat { T } _ { \alpha }$as required.

In order to complete the construction of$\hat { \mathcal T }$, it remains to extend G. As a set, we simply set$\hat { G } = { G } \stackrel { \bullet } { \times } M _ { \bar { W } } ^ { \alpha _ { n } + \beta }$, where$M _ { \bar { W } } ^ { \alpha }$denotes the set of linear maps from W<sup>¯</sup> into $\bar { T } _ { \alpha } ^ { - } ~ ( \mathrm { i . e }$. the polynomials of scaled degree strictly less than$\alpha )$. The composition rule on G<sup>ˆ</sup> is then given by the following skew-product:

$$
(\Gamma_ {1}, M _ {1}) \circ (\Gamma_ {2}, M _ {2}) = \left(\Gamma_ {1} \Gamma_ {2}, \Gamma_ {1} M _ {2} + M _ {1} + \left(\Gamma_ {1} \mathcal {I} - \mathcal {I} \Gamma_ {1}\right) (\Gamma_ {2} - 1)\right).\tag{5.22}
$$

One can check that this composition rule yields an element of$\hat { G } .$. Indeed, by assumption, G leaves$\bar { T }$invariant, so that$\Gamma _ { 1 } M _ { 2 }$is indeed again an element of$M _ { \hat { W } } ^ { \alpha _ { n } + \beta }$. Furthermore,$\Gamma _ { 1 } \mathcal { T } - \mathcal { I } \Gamma _ { 1 }$is an element of$L _ { V } ^ { \beta } \subset M _ { V } ^ { \alpha _ { n } + \beta }$by assumption, so that the last term also maps W<sup>¯</sup> into$\bar { T } _ { \alpha _ { n } + \beta } ^ { - }$as required. For any$( \Gamma , M ) \in { \hat { G } }$, we then give its action on$\hat { T }$by setting

$$
(\Gamma , M) (a, b) = \left(\Gamma a + \mathcal {I} (\Gamma b - b) + M b, b\right).
$$

Observe that

$$
(\Gamma , M) (a, b) - (a, b) = \left((\Gamma a - a) + \mathcal {I} (\Gamma b - b) + M b, 0\right),
$$

so that this definition does satisfy the condition (2.1).

Straightforward verification shows that one has indeed

$$
\big ((\Gamma_ {1}, M _ {1}) \circ (\Gamma_ {2}, M _ {2}) \big) (a, b) = (\Gamma_ {1}, M _ {1}) \big ((\Gamma_ {2}, M _ {2}) (a, b) \big).
$$

Since it is immediate that this action is also faithful, this does imply that the operation defined in (5.22) is associative as required. Furthermore, one can verify that (1, 0) is neutral for the operation  and that$( \Gamma , M )$has an inverse given by

$$
(\Gamma , M) ^ {- 1} = \bigl (\Gamma^ {- 1}, - \Gamma^ {- 1} \bigl (M + (\Gamma \mathcal {I} - \mathcal {I} \Gamma) (\Gamma - 1) \bigr) \bigr),
$$

so that$( { \hat { G } } , \circ )$is indeed a group. This shows that$\hat { \mathcal { T } } = ( \hat { A } , \hat { T } , \hat { G } )$is indeed again a regularity structure. Furthermore, the map$j \colon { \hat { G } }  G$given by$j ( \Gamma , M ) = \Gamma$is a group homomorphism which verifies that, for every$a \in T$and$\Gamma \in G$, one has the identity

$$
(j (\Gamma , M)) a = \Gamma a = \iota^ {- 1} (\Gamma a, 0) = \iota^ {- 1} (\Gamma , M) \iota a.
$$

This shows that ι and j do indeed define a canonical inclusion$\mathcal { T } \subset \hat { \mathcal { T } }$, see Section 2.1.

It is now very easy to extend to the image of all of V in$\hat { T } .$Indeed, for any$a \in V$ we have a unique decomposition$a = a _ { 0 } + a _ { 1 }$with$a _ { 0 } \in W$and$a _ { 1 } \in \hat { W }$. We then set

$$
\hat {\mathcal {I}} (a, 0) = (\mathcal {I} a _ {0}, a _ {1}).
$$

Since$a _ { 1 } = 0$for$a \in W$, one has indeed$\hat { \mathcal { T } } \iota a = \hat { \mathcal { T } } ( a , 0 ) = ( \mathcal { T } a , 0 ) = \iota \mathcal { T } a$in this case, as claimed in the statement of the theorem. As far as the abstract part of our construction is concerned, it therefore remains to verify that$\hat { \mathcal { T } }$defined in this way does verify our definition of an abstract integration map. The fact that$\hat { \mathcal { T } } \colon \hat { V } _ { \alpha } \to \hat { T } _ { \alpha + \beta }$is a direct consequence of the fact that we have simply postulated that$0 \oplus \bar { W } \subset \hat { T } _ { \alpha _ { n } + \beta }$ Since the action of$\mathcal { T }$on$\bar { T }$did not change in our construction, one still has$\hat { \cal T } \bar { \cal T } = 0$ Regarding the third property, for any$( \Gamma , \bar { M } ) \in \hat { G }$and every$a = a _ { 1 } + a _ { 2 } \in V$as above, we have

$$
\hat {\mathcal {I}} (\Gamma , M) (a, 0) = \hat {\mathcal {I}} (\Gamma a, 0) = \left(\mathcal {I} \Gamma a _ {1} + \mathcal {I} (\Gamma a _ {2} - a _ {2}), a _ {2}\right),
$$

where we use the fact that$\Gamma a _ { 2 } - a _ { 2 } \in V$by the structural assumption (5.21) we made at the beginning of this proof. On the other hand, we have

$$
(\Gamma , M) \hat {\mathcal {I}} (a, 0) = (\Gamma , M) (\mathcal {I} a _ {1}, a _ {2}) = \left(\Gamma \mathcal {I} a _ {1} + \mathcal {I} (\Gamma a _ {2} - a _ {2}) + M a _ {2}, a _ {2}\right),
$$

so that the last property of an abstract integration map is also satisfied.

It remains to provide an explicit formula for the extended model (Π<sup>ˆ</sup> , Γ<sup>ˆ</sup>). Regarding ${ \hat { \Pi } } ,$for$b \in \bar { W }$and$\boldsymbol { x } \in \mathbf { R } ^ { d }$, we simply define it to be given by

$$
\hat {\Pi} _ {x} (a, b) = \Pi_ {x} a + \int_ {\mathbf {R} ^ {d}} K (\cdot , z) (\Pi_ {x} b) (d z) - \Pi_ {x} \mathcal {J} (x) b,\tag{5.23}
$$

where$\mathcal { I }$is given by (5.11), which guarantees that the model Π<sup>ˆ</sup> realises K for$\hat { \mathcal { T } }$on$V .$ Again, this expression is only formal and should really be interpreted as in (5.13). It follows from Lemma 5.19 below that the sum in (5.13) converges and that it furthermore satisfies the required bounds when tested against smooth test functions that are localised near$x .$. Note that the map$\Pi _ { x } \mapsto { \hat { \Pi } } _ { x }$is linear and does not depend at all on the realisation of Γ. As a consequence, the bound on the difference between the extensions of different regularity structures follows at once. It remains to define$\hat { \Gamma } _ { x y } \in \hat { G }$ and to show that it satisfies both the algebraic and the analytical conditions given by Definition 2.17.

We set

$$
\hat {\Gamma} _ {x y} = (\Gamma_ {x y}, M _ {x y}), \qquad M _ {x y} b = \mathcal {J} (x) \Gamma_ {x y} b - \Gamma_ {x y} \mathcal {J} (y) b.\tag{5.24}
$$

By the definition of$\mathcal { I }$, the linear map$M _ { x y }$defined in this way does indeed belong to $M _ { \bar { W } } ^ { \alpha _ { n } + \beta }$. Making use of Lemma 5.16, we then have the identity

$$
\begin{array}{r l} & {\hat {\Gamma} _ {x y} \circ \hat {\Gamma} _ {y z} = (\Gamma_ {x y} \Gamma_ {y z}, \Gamma_ {x y} (\mathcal {J} (y) \Gamma_ {y z} - \Gamma_ {y z} \mathcal {J} (z)) + \mathcal {J} (x) \Gamma_ {x y} - \Gamma_ {x y} \mathcal {J} (y)} \\ & {\qquad + (\Gamma_ {x y} \mathcal {I} - \mathcal {I} \Gamma_ {x y}) (\Gamma_ {y z} - 1))} \\ & {\qquad = (\Gamma_ {x z}, - \Gamma_ {x z} \mathcal {J} (z) + \Gamma_ {x y} \mathcal {J} (y) \Gamma_ {y z} + \mathcal {J} (x) \Gamma_ {x y} - \Gamma_ {x y} \mathcal {J} (y)} \\ & {\qquad + (\mathcal {J} (x) \Gamma_ {x y} - \Gamma_ {x y} \mathcal {J} (y)) (\Gamma_ {y z} - 1))} \\ & {\qquad = (\Gamma_ {x z}, \mathcal {J} (x) \Gamma_ {x z} - \Gamma_ {x z} \mathcal {J} (z)),} \end{array}
$$

which is the first required algebraic identity. Regarding the second identity, we have

$$
\begin{array}{l} \hat {\Pi} _ {x} \hat {\Gamma} _ {x y} (a, b) = \hat {\Pi} _ {x} (\Gamma_ {x y} a + \mathcal {I} (\Gamma_ {x y} b - b) + \mathcal {J} (x) \Gamma_ {x y} b - \Gamma_ {x y} \mathcal {J} (y) b, b) \\ \quad = \Pi_ {x} a + \int_ {\mathbf {R} ^ {d}} K (\cdot , z) \Pi_ {x} (\Gamma_ {x y} b - b) (d z) - \Pi_ {x} \mathcal {J} (x) (\Gamma_ {x y} b - b) \\ \quad + \Pi_ {x} \mathcal {J} (x) \Gamma_ {x y} b - \Pi_ {y} \mathcal {J} (y) b + \int_ {\mathbf {R} ^ {d}} K (\cdot , z) \Pi_ {x} b (d z) - \Pi_ {x} \mathcal {J} (x) b \\ \quad = \Pi_ {x} a + \int_ {\mathbf {R} ^ {d}} K (\cdot , z) \Pi_ {y} b (d z) - \Pi_ {y} \mathcal {J} (y) b \\ \quad = \hat {\Pi} _ {y} (a, b). \end{array} \tag {5.}\tag{5.25}
$$

Here, in order to go from the first to the second line, we used the fact that realises K for  on W by assumption.

It then only remains to check the bound on$\hat { \Gamma } _ { x y }$stated in (2.15). Since$\hat { \Gamma } _ { x y } ( a , 0 ) =$ $( \Gamma _ { x y } a , 0 )$, we only need to check that the required bound holds for elements of the form $( 0 , b )$. Note here that$( 0 , b ) \in \hat { T } _ { \alpha _ { n } + \beta }$, but that$( b , 0 ) \in \hat { T } _ { \alpha _ { n } }$. As a consequence,

$$
\| \mathcal {I} (\Gamma_ {x y} b - b) \| _ {\gamma} = \| \Gamma_ {x y} b - b \| _ {\gamma - \beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\alpha_ {n} - (\gamma - \beta)} = \| x - y \| _ {\mathfrak {s}} ^ {(\alpha_ {n} + \beta) - \gamma},
$$

as required. It therefore remains to obtain a similar bound on the term$\| M _ { x y } b \| _ { \gamma }$. In view of (5.24), this on the other hand is precisely the content of Lemma 5.21 below, which concludes the proof.□

Remark 5.17 It is clear from the construction that$\hat { \mathcal T }$is the “smallest possible” extension of$\mathcal { T }$which is guaranteed to have all the required properties. In some particular cases it might however happen that there exists an even smaller extension, due to the fact that the matrices$M _ { x y }$appearing in (5.24) may have additional structure.

The remainder of this subsection is devoted to the proofof the quantitative estimates given in Lemma 5.19 and Lemma 5.21. We will assume without further restating it that some regularity structure$\mathcal { T } = ( A , T , G )$is given and that K is a kernel satisfying Assumptions 5.1 and 5.4 for some$\beta > 0$. The test functions$K _ { n ; x y } ^ { \alpha }$introduced in (5.14) will play an important role in these bounds. Actually, we will encounter the following variant: for any multiindex k and for$\alpha \in \mathbf { R }$, set

$$
K _ {n, x y} ^ {k, \alpha} (z) = D _ {1} ^ {k} K _ {n} (y, z) - \sum_ {| k + \ell | _ {\mathfrak {s}} <   \alpha + \beta} \frac {(y - x) ^ {\ell}}{\ell !} D _ {1} ^ {k + \ell} K _ {n} (x, z),
$$

so that$K _ { n , x y } ^ { \alpha } = K _ { n , x y } ^ { 0 , \alpha }$. We then have the following bound:

Lemma 5.18 Let$K _ { n , x y } ^ { k , \alpha }$be as above,$a \ \in \ T _ { \alpha }$for some$\alpha \in \ A$, and assume that $\alpha + \beta \not \in \mathbf { N } .$. Then, one has the bound

$$
| (\Pi_ {y} a) (K _ {n, x y} ^ {k, \alpha}) | \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}}) \sum_ {\delta > 0} 2 ^ {\delta n} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \alpha + \beta - | k | _ {\mathfrak {s}}} ,\tag{5.26}
$$

and similarly for$| ( \Pi _ { x } a ) ( K _ { n , x y } ^ { k , \alpha } ) |$. Here, the sum runs over finitely many strictly positive values and we used the shorthand${ \mathcal { \bar { R } } } _ { x }$for the ball of radius 2 centred around x. Furthermore, one has the bound

$$
\begin{array}{l} \left| \left(\Pi_ {y} - \bar {\Pi} _ {y} a\right) \left(K _ {n, x y} ^ {k, \alpha}\right) \right| \lesssim \left(\left\| \Pi - \bar {\Pi} \right\| _ {\alpha ; \mathfrak {K} _ {x}} \left(1 + \left\| \Gamma \right\| _ {\alpha ; \mathfrak {K} _ {x}}\right) + \left\| \bar {\Pi} \right\| _ {\alpha ; \mathfrak {K} _ {x}} \left\| \Gamma - \bar {\Gamma} \right\| _ {\alpha ; \mathfrak {K} _ {x}}\right) \\ \times \sum_ {\delta > 0} 2 ^ {\delta n} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \alpha + \beta - | k | _ {\mathfrak {s}}} \end{array} , \tag {5.27}
$$

(and similarlyfor$\Pi _ { x } - { \bar { \Pi } } _ { x } )$for any two models (Π, Γ) and$( { \bar { \Pi } } , { \bar { \Gamma } } )$

Proof. It turns out that the cases$\alpha + \beta > | k | _ { s }$and$\alpha + \beta < | k | _ { s }$are treated slightly differently. (The case$\alpha + \beta = | k | _ { \xi }$is ruled out by assumption.) In the case$\alpha + \beta > | k | _ { \mathfrak { s } } ,$ it follows from Proposition A.1 that we can express$K _ { n ; x y } ^ { k , \alpha }$as

$$
K _ {n; x y} ^ {k, \alpha} (z) = \sum_ {\ell \in \partial A _ {\alpha}} \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k + \ell} K _ {n} (y + h, z) \mathcal {Q} ^ {\ell} (x - y, d h),\tag{5.28}
$$

where$A _ { \alpha }$is the set of multiindices given by$A _ { \alpha } = \{ \ell : | k + \ell | _ { \mathfrak { s } } < \alpha + \beta \}$and the objects$\partial A _ { \alpha }$and$\mathcal { Q } ^ { \ell }$are as in Proposition A.1. In particular, note that$| \ell | _ { \mathfrak { s } } \geq \alpha { + } \beta { - } | k | _ { \mathfrak { s } }$ for every term appearing in the above sum.

At this point, we note that, thanks to the first two properties in Definition 5.1, we have the bound

$$
| (\Pi_ {y} a) (D _ {1} ^ {k + \ell} K _ {n} (y, \cdot)) | \lesssim 2 ^ {| k + \ell | _ {\mathfrak {s}} n - \alpha n - \beta n} \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}},\tag{5.29}
$$

uniformly over all y with$\| y - x \| _ { \mathfrak { s } } \leq 1$and for all$a \in T _ { \alpha }$. Unfortunately, the function $D ^ { k + \ell } K _ { n }$is evaluated at$( y + h , z )$in our case, but this can easily be remedied by shifting the model:

$$
\begin{array}{c} (\Pi_ {y} a) (D _ {1} ^ {k + \ell} K _ {n} (y + h, \cdot)) = (\Pi_ {y + h} \Gamma_ {y + h, x} a) (D _ {1} ^ {k + \ell} K _ {n} (y + h, \cdot)) \\ \lesssim \sum_ {\zeta \leq \alpha} \| h \| _ {\mathfrak {s}} ^ {\alpha - \zeta} 2 ^ {| k + \ell | _ {\mathfrak {s}} n - \zeta n - \beta n}, \end{array}\tag{5.30}
$$

where the sum runs over elements in A (in particular, it is a finite sum). In order to obtain the bound on the second line, we made use of the properties$( 2 . 1 5 )$of the model. We now use the fact that$\mathcal { Q } ^ { \ell } ( y - x , \cdot )$is supported on values h such that$\| h \| _ { \mathfrak { s } } \le \| x - y \| _ { \mathfrak { s } }$ and that

$$
\mathcal {Q} ^ {\ell} (y - x, \mathbf {R} ^ {d}) \lesssim \prod_ {i = 1} ^ {d} | y _ {i} - x _ {i} | ^ {\ell_ {i}} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}}.\tag{5.31}
$$

Combining these bounds, it follows that one has indeed

$$
| (\Pi_ {y} a) (K _ {n; x y} ^ {k, \alpha}) | \lesssim \sum_ {\zeta ; \ell} \| x - y \| _ {\mathfrak {s}} ^ {\alpha - \zeta + | \ell | _ {\mathfrak {s}}} 2 ^ {| k + \ell | _ {\mathfrak {s}} n - \zeta n - \beta n},
$$

where the sum runs over finitely many values of$\zeta$and ℓ with$\zeta \ \leq \ \alpha$and$| \ell | _ { \mathfrak { s } } ~ \geq$ $\alpha + \beta - | k | _ { \mathfrak { s } } .$Since, by assumption, one has$\alpha + \beta \not \in \mathbf { N } .$, it follows that one actually has$| \ell | _ { s } > \alpha + \beta - | k | _ { s }$for each of these terms, so that the required bound follows at once. The bound with$\Pi _ { y }$replaced by$\Pi _ { x }$follows in exactly the same way as above.

In the case$\alpha + \beta < | k | _ { \mathfrak { s } } ,$we have$K _ { n ; y x } ^ { k , \alpha } ( z ) = D _ { 1 } ^ { k } K _ { n } ( x , z )$and, proceeding almost exactly as above, one obtains

$$
\begin{array}{l} | (\Pi_ {x} a) (D _ {1} ^ {k} K _ {n} (x, \cdot)) | \lesssim 2 ^ {| k | _ {\mathfrak {s}} n - \alpha n - \beta n}, \\ | (\Pi_ {y} a) (D _ {1} ^ {k} K _ {n} (x, \cdot)) | \lesssim \sum_ {\zeta \leq \alpha} \| x - y \| _ {\mathfrak {s}} ^ {\alpha - \zeta} 2 ^ {| k | _ {\mathfrak {s}} n - \zeta n - \beta n}. \end{array}
$$

with proportionality constants of the required order.

Regarding the bound on the differences between two models, the proof is again virtually identical, so we do not repeat it.□

Definition 5.9 makes sense thanks to the following lemma:

Lemma 5.19 In the same setting as above, for any$\alpha \in A$with$\alpha + \beta \not \in { \bf N } ,$the right hand side in (5.13) with$a \in T _ { \alpha }$converges absolutely. Furthermore, one has the bound

$$
\sum_ {n \geq 0} \int_ {\mathbf {R} ^ {d}} (\Pi_ {x} a) (K _ {n; y x} ^ {\alpha}) \psi_ {x} ^ {\lambda} (y) d y \lesssim \lambda^ {\alpha + \beta} \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}}),\tag{5.32}
$$

uniformly over all$\boldsymbol { x } \in \mathbf { R } ^ { d }$, all$\lambda \in ( 0 , 1 ]$, and all smooth functions supported in$B _ { \mathfrak { s } } ( 1 )$ with$\| \psi \| _ { \mathcal { C } ^ { r } } \leq 1 \quad$. Here, we used the shorthand notation$\psi _ { x } ^ { \lambda } = S _ { s , x } ^ { \lambda } \psi$, and${ \mathcal { \bar { R } } } _ { x }$is as above. As in Lemma 5.18, a similar bound holdsfor$\Pi _ { x } - { \bar { \Pi } } _ { x } ,$, but with the expression from the right hand side of the first line of (5.18) replaced by the expression appearing on the second line.

Remark 5.20 The condition that$\alpha + \beta \not \in { \bf N }$is actually known to be necessary in general. Indeed, it is possible to construct examples of functions$f \in \mathcal { C } ( \mathbf { R } ^ { 2 } )$such that ${ \bar { K } } * f \not \in { \mathcal { C } } ^ { 2 } ( \mathbf { R } ^ { 2 } )$, where K denotes the Green’s function of the Laplacian [Mey92].

Proof. We treat various regimes separately. For this, we obtain separately the bounds

$$
(\Pi_ {x} a) (K _ {n; y x} ^ {\alpha}) \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}}) \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\alpha + \beta + \delta} 2 ^ {\delta n},\tag{5.33a}
$$

$$
\int_ {\mathbf {R} ^ {d}} (\Pi_ {x} a) (K _ {n; y x} ^ {\alpha}) \psi_ {x} ^ {\lambda} (y) d y \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} \sum_ {\delta > 0} \lambda^ {\alpha + \beta - \delta} 2 ^ {- \delta n},\tag{5.33b}
$$

for$\| x - y \| _ { \mathfrak { s } } \le 1$. Both sums run over some finite set of strictly positive indices$\delta .$ Furthermore, (5.33a) holds whenever$\| x - y \| _ { s } \leq 2 ^ { - n }$, while (5.33b) holds whenever $2 ^ { - n } \leq \lambda$. Using the expression (5.13), it is then straightforward to show that (5.33) implies (5.32) by using the bound

$$
\int_ {\mathbf {R} ^ {d}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma} \psi_ {x} ^ {\lambda} (y) d y \lesssim \lambda^ {\gamma},
$$

and summing the resulting expressions over$n .$

The bound (5.33a) (as well as the corresponding version for the difference between two different models for our regularity structure) is a particular case of Lemma 5.18, so we only need to consider the second bound. This bound is only useful in the regime $2 ^ { - n } \leq \lambda$, so that we assume this from now on. It turns out that in this case, the bound (5.33b) does not require the use of the identity$\Pi _ { z } = \Pi _ { x } \Gamma _ { x z }$, so that the corresponding bound on the difference between two models follows by linearity. For fixed$n ,$it follows from the linearity of$\Pi _ { x } a$that

$$
\int_ {\mathbf {R} ^ {d}} (\Pi_ {x} a) (K _ {n; y x} ^ {\alpha}) \psi_ {x} ^ {\lambda} (y) d y = (\Pi_ {x} a) \Bigl (\int_ {\mathbf {R} ^ {d}} K _ {n; y x} ^ {\alpha} (\cdot) \psi_ {x} ^ {\lambda} (y) d y \Bigr).
$$

We decompose$K _ { n ; y x } ^ { \alpha }$according to (5.14) and consider the first term. It follows from the first property in Definition 5.1 that the function

$$
Y _ {n} ^ {\lambda} (z) = \int_ {\mathbf {R} ^ {d}} K _ {n} (y, z) \psi_ {x} ^ {\lambda} (y) d y\tag{5.34}
$$

is supported in a ball of radius 2λ around x, and bounded by$C 2 ^ { - \beta n } \lambda ^ { - | \mathfrak { s } | }$for some constant C. In order to bound its derivatives, we use the fact that

$$
D ^ {\ell} Y _ {n} ^ {\lambda} (z) = \sum_ {k <   \ell} \frac {(D ^ {k} \psi_ {x} ^ {\lambda}) (x)}{k !} \int_ {\mathbf {R} ^ {d}} D _ {2} ^ {\ell} K _ {n} (y, z) (y - x) ^ {k} d y + \int_ {\mathbf {R} ^ {d}} D _ {2} ^ {\ell} K _ {n} (y, z) R _ {x} (y) d y,
$$

where the remainder$R _ { x } ( y )$satisfies the bound$\begin{array} { r } { | R _ { x } ( y ) | \lesssim \lambda ^ { - | \mathfrak { s } | - | \ell | _ { \mathfrak { s } } } \| x - y \| _ { \mathfrak { s } } ^ { | \ell | _ { \mathfrak { s } } } } \end{array}$. Making use of (5.4) and (5.5), we thus obtain the bound

$$
\begin{array}{c} \sup _ {z \in \mathbf {R} ^ {d}} | D ^ {\ell} Y _ {n} ^ {\lambda} (z) | \lesssim \sum_ {k <   \ell} 2 ^ {- \beta n} \lambda^ {- | \mathfrak {s} | - | k | _ {\mathfrak {s}}} + 2 ^ {- \beta n} \lambda^ {- | \mathfrak {s} | - | \ell | _ {\mathfrak {s}}} \\ \lesssim 2 ^ {- \beta n} \lambda^ {- | \mathfrak {s} | - | \ell | _ {\mathfrak {s}}}. \end{array}\tag{5.35}
$$

Combining these bounds with Remark 2.21, we obtain the estimate

$$
| (\Pi_ {x} a) (Y _ {n} ^ {\lambda}) | \lesssim \lambda^ {\alpha} 2 ^ {- \beta n}.
$$

It remains to obtain a similar bound on the remaining terms in the decomposition of $K _ { n ; y x } ^ { \alpha }$. This follows if we obtain a bound analogous to (5.35), but for the test functions

$$
Z _ {n, \ell} ^ {\lambda} (z) = D _ {1} ^ {\ell} K _ {n} (x, z) \int_ {\mathbf {R} ^ {d}} (y - x) ^ {\ell} \psi_ {x} ^ {\lambda} (y) d y.
$$

These are supported in a ball of radius$2 ^ { - n }$around x and bounded by a constant multiple of$2 ^ { ( | \ell | _ { s } + | s | - \beta ) n } \lambda ^ { | \ell | _ { s } }$. Regarding their derivatives, the bound (5.4) immediately yields

$$
\sup _ {z \in \mathbf {R} ^ {d}} | D ^ {k} Z _ {n, \ell} ^ {\lambda} (z) | \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} + | k | _ {\mathfrak {s}} + | \mathfrak {s} | - \beta) n} \lambda^ {| \ell | _ {\mathfrak {s}}}.
$$

Combining these bounds again with Remark 2.21 yields the estimate

$$
| (\Pi_ {x} a) (Z _ {n, \ell} ^ {\lambda}) | \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \alpha - \beta) n} \lambda^ {| \ell | _ {\mathfrak {s}}}.
$$

Since the indices ℓ appearing in (5.14) all satisfy$| \ell | _ { \mathfrak { s } } < \alpha + \beta$, the bound (5.33b) does indeed hold for some finite collection of strictly positive indices$\delta .$□

The following lemma is the last ingredient required for the proof of the extension theorem. In order to state it, we make use of the shorthand notation

$$
\mathcal {J} _ {x y} \stackrel {\mathrm{def}} {=} \mathcal {J} (x) \Gamma_ {x y} - \Gamma_ {x y} \mathcal {J} (y),\tag{5.36}
$$

where, given a regularity structure$\mathcal { T }$and a model (Π, Γ), the map$\mathcal { I }$was defined in (5.11).

Lemma 5.21 Let$V ~ \subset ~ T$be a sector satisfying the same assumptions as in$T h e o .$ rem 5.14. Then, for every$\alpha \in A , a \in V _ { \alpha }$, every multiindex k with$| k | _ { \mathfrak { s } } < \alpha + \beta ,$, and every pair (x, y) with$\| x - y \| _ { s } \leq 1$, one has the bound

$$
| (\mathcal {J} _ {x y} a) _ {k} | \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}}) \| x - y \| _ {\mathfrak {s}} ^ {\alpha + \beta - | k | _ {\mathfrak {s}}},\tag{5.37}
$$

where${ \mathcal { \mathrm { R } } } _ { x }$is as before. Furthermore, if we denote by${ \bar { \mathcal { I } } } _ { x y }$the function defined like $( 5 . 3 6 ) ,$, but with respect to a second model (Π<sup>¯</sup> , Γ<sup>¯</sup>), then we obtain a bound similar to (5.37) on the difference$\mathcal { T } _ { x y } a - \bar { \mathcal { T } } _ { x y } a ,$again with the expression from the right hand side ofthefirst line of(5.18) replaced by the expression appearing on the second line.

Proof. For any multiindex k with$| k | _ { \mathfrak { s } } < \alpha + \beta$, we can rewrite the kth component of $\mathcal { I } _ { x y } a$as

$$
\begin{array}{l} (\mathcal {J} _ {x y} a) _ {k} = \frac {1}{k !} \sum_ {n \geq 0} \Big (\sum_ {| k | _ {\mathfrak {s}} - \beta <   \gamma \leq \alpha} (\Pi_ {x} \mathcal {Q} _ {\gamma} \Gamma_ {x y} a) (D _ {1} ^ {k} K _ {n} (x, \cdot)) \\ \qquad - \sum_ {| \ell | _ {\mathfrak {s}} <   \alpha + \beta - | k | _ {\mathfrak {s}}} \frac {(x - y) ^ {\ell}}{\ell !} (\Pi_ {y} a) (D _ {1} ^ {k + \ell} K _ {n} (y, \cdot)) \Big) \\ \stackrel {{\mathrm{def}}} {{=}} \frac {1}{k !} \sum_ {n \geq 0} \mathcal {J} _ {x y} ^ {n, k} a. \end{array}\tag{5.38}
$$

As usual, we treat separately the cases$\| x - y \| _ { s } \leq 2 ^ { - n }$and$\| x - y \| _ { s } \geq 2 ^ { - n }$. In the case$\| x - y \| _ { s } \leq 2 ^ { - n }$, we rewrite$\mathcal { J } _ { x y } ^ { n , k }$a as

$$
\mathcal {J} _ {x y} ^ {n, k} a = (\Pi_ {y} a) (K _ {n; x y} ^ {k, \alpha}) - \sum_ {\gamma \leq | k | _ {\mathfrak {s}} - \beta} (\Pi_ {x} \mathcal {Q} _ {\gamma} \Gamma_ {x y} a) (D _ {1} ^ {k} K _ {n} (x, \cdot))  .\tag{5.39}
$$

The first term has already been bounded in Lemma 5.18, yielding a bound of the type (5.37) when summing over the relevant values of n. Regarding the second term, we make use of the fact that, for$\gamma < \alpha$(which is satisfied since$| k | _ { \mathfrak { s } } < \alpha + \beta )$, one has the bound$\| \Gamma _ { x y } a \| _ { \gamma } \lesssim \| x - y \| _ { \mathfrak { s } } ^ { \alpha - \gamma }$. Furthermore, for any$b \in T _ { \gamma }$, one has

$$
(\Pi_ {x} b) (D _ {x} ^ {k} K _ {n} (x, \cdot)) \lesssim \| b \| 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \gamma) n}.\tag{5.40}
$$

In principle, the exponent appearing in this term might vanish. As a consequence of our assumptions, this however cannot happen. Indeed, if γ is such that$\gamma + \beta = | k | _ { s }$, then we necessarily have that$\gamma$itself is an integer. By Assumptions 5.3 and 5.4 however, we have the identity

$$
(\Pi_ {x} b) (D _ {x} ^ {k} K _ {n} (x, \cdot)) = 0,
$$

for every b with integer homogeneity.

Combining all these bounds, we thus obtain similarly to before the bound

$$
| \mathcal {J} _ {x y} ^ {n, k} a | \lesssim \| \Pi \| _ {\alpha ; \mathfrak {K} _ {x}} (1 + \| \Gamma \| _ {\alpha ; \mathfrak {K} _ {x}}) \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\alpha + \beta - | k | _ {\mathfrak {s}} + \delta} 2 ^ {\delta n},\tag{5.41}
$$

where the sum runs over a finite number of exponents. This expression is valid for all $n \geq 0$with$\| x - y \| _ { s } \leq 2 ^ { - n }$. Furthermore, if we consider two different models (Π, Γ) and (Π<sup>¯</sup> , Γ<sup>¯</sup>), we obtain a similar bound on the difference$\mathcal { T } _ { x y } ^ { n , k } a - \bar { \mathcal { T } } _ { x y } ^ { n , k } a$

In the case$\| x - y \| _ { 5 } \geq 2 ^ { - n }$, we treat the two terms in (5.38) separately and, for both cases, we make use of the bound (5.40). As a consequence, we obtain

$$
\begin{array}{c} | \mathcal {J} _ {x y} ^ {n, k} a | \lesssim \sum_ {| k | _ {\mathfrak {s}} - \beta <   \gamma \leq \alpha} \| x - y \| _ {\mathfrak {s}} ^ {\alpha - \gamma} 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \gamma) n} \\ + \sum_ {| \ell | _ {\mathfrak {s}} <   \alpha + \beta - | k | _ {\mathfrak {s}}} \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}} 2 ^ {(| k | _ {\mathfrak {s}} + | \ell | _ {\mathfrak {s}} - \beta - \alpha) n}, \end{array}
$$

with a proportionality constant as before. Thanks to our assumptions, the exponent of $2 ^ { n }$appearing in each of these terms is always strictly negative. We thus obtain a bound like (5.41), but where the sum now runs over a finite number of exponents δ with$\delta < 0$ Summing both bounds over n, we see that (5.37) does indeed hold for${ \mathcal { I } } _ { x y } .$. In this case, the bound on the difference again simply holds by linearity.□

## 5.2 Multi-level Schauder estimate

We now have all the ingredients in place to prove the “multi-level Schauder estimate” announced at the beginning of this section. Our proof has a similar flavour to proofs of the classical (elliptic or parabolic) Schauder estimates using scale-invariance, like for example [Sim97].

ProofofTheorem 5.12. We first note that (5.16) is well-defined for every k with$| k | _ { s } <$ $\gamma + \beta$. Indeed, it follows from the reconstruction theorem and the assumptions on$K$ that

$$
(\mathcal {R} f - \Pi_ {x} f (x)) (D _ {1} ^ {k} K _ {n} (x, \cdot)) \lesssim 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \gamma) n},\tag{5.42}
$$

which is summable since the exponent appearing in this expression is strictly negative. Regarding$\kappa _ { \gamma } f - \bar { \kappa } _ { \gamma } \bar { f }$, we use (3.4), which yields

$$
\begin{array}{c} | (\mathcal {R} f - \bar {\mathcal {R}} \bar {f} - \Pi_ {x} f (x) + \bar {\Pi} _ {x} \bar {f} (x)) (D _ {1} ^ {k} K _ {n} (x, \cdot)) | \\ \lesssim 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \gamma) n} (\| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}})  , \end{array}\tag{5.43}
$$

where the proportionality constants depend on the bounds on$f , { \bar { f } } .$, and the two models. In particular, this already shows that one has the bounds

$$
\| \mathcal {K} _ {\gamma} f \| _ {\gamma + \beta ; \mathfrak {K}} \lesssim \| f \| _ {\gamma ; \bar {\mathfrak {K}}}, \quad \| \mathcal {K} _ {\gamma} f - \bar {\mathcal {K}} _ {\gamma} \bar {f} \| _ {\gamma + \beta ; \mathfrak {K}} \lesssim \| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}},
$$

so that it remains to obtain suitable bounds on differences between two points.

We also note that by the definition of$\kappa _ { \gamma }$and the properties of , one has for$\boldsymbol { \ell } \not \in \mathbf { N }$ the bound

$$
\begin{array}{c} \| \mathcal {K} _ {\gamma} f (x) - \Gamma_ {x y} \mathcal {K} _ {\gamma} f (y) \| _ {\ell} = \| \mathcal {I} (f (x) - \Gamma_ {x y} f (y)) \| _ {\ell} \lesssim \| f (x) - \Gamma_ {x y} f (y) \| _ {\ell - \beta} \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma + \beta - \ell}, \end{array}
$$

which is precisely the required bound. A similar calculation allows to bound the terms involved in the definition of$\| \mathcal { K } _ { \gamma } f ; \bar { \mathcal { K } } _ { \gamma } \bar { f } \| _ { \gamma + \beta ; \bar { \mathcal { R } } }$, so that it remains to show a similar bound for$\boldsymbol { \ell } \in \mathbf { N }$

It follows from (5.19), combined with the fact that$\mathcal { T }$does not produce any component in$\bar { T }$by assumption, that one has the identity

$$
\begin{array}{r} \left(\Gamma_ {x y} \mathcal {K} _ {\gamma} f (y)\right) _ {k} - \left(\mathcal {K} _ {\gamma} f (x)\right) _ {k} = \left(\Gamma_ {x y} \mathcal {N} _ {\gamma} f (y)\right) _ {k} - \left(\mathcal {N} _ {\gamma} f (x)\right) _ {k} \\ + \left(\mathcal {J} (x) (\Gamma_ {x y} f (y) - f (x))\right) _ {k}, \end{array}
$$

so our aim is to bound this expression. We decompose$\mathcal { I }$as$\begin{array} { r } { \mathcal { T } = \sum _ { n > 0 } \mathcal { T } ^ { ( n ) } } \end{array}$and $\begin{array} { r } { \mathcal { N } _ { \gamma } = \sum _ { n \ge 0 } \mathcal { N } _ { \gamma } ^ { ( n ) } } \end{array}$, where the nth term in each sum is obtained by replacing$K$by $K _ { n }$Pin the expressions for$\mathcal { I }$and$\mathcal { N } _ { \gamma }$respectively. It follows from the definition of $\mathcal { N } _ { \gamma }$, as well as the action of Γ on the space of elementary polynomials that one has the identities

$$
\begin{array}{l} \left(\Gamma_ {x y} \mathcal {N} _ {\gamma} ^ {(n)} f (y)\right) _ {k} = \frac {1}{k !} \sum_ {| k + \ell | _ {\mathfrak {s}} <   \gamma + \beta} \frac {(x - y) ^ {\ell}}{\ell !} (\mathcal {R} f - \Pi_ {y} f (y)) \left(D _ {1} ^ {k + \ell} K _ {n} (y, \cdot)\right), \\ \left(\mathcal {J} ^ {(n)} (x) \Gamma_ {x y} f (y)\right) _ {k} = \frac {1}{k !} \sum_ {\delta \in B _ {k}} \left(\Pi_ {x} \mathcal {Q} _ {\delta} \Gamma_ {x y} f (y)\right) \left(D _ {1} ^ {k} K _ {n} (x, \cdot)\right), \\ \left(\mathcal {J} ^ {(n)} (x) f (x)\right) _ {k} = \frac {1}{k !} \sum_ {\delta \in B _ {k}} \left(\Pi_ {x} \mathcal {Q} _ {\delta} f (x)\right) \left(D _ {1} ^ {k} K _ {n} (x, \cdot)\right), \end{array} \tag {5.}\tag{5.44}
$$

where the set$B _ { k }$is given by

$$
B _ {k} = \left\{\delta \in A: | k | _ {\mathfrak {s}} - \beta <   \delta <   \gamma \right\}.
$$

(The upper bound$\gamma$appearing in$B _ { k }$actually has no effect since, by assumption,$f$has no component in$T _ { \delta }$for$\delta \geq \gamma . \rfloor$As previously, we use different strategies for small scales and for large scales.

We first bound the terms at small scales, i.e. when$2 ^ { - n } \leq \| x - y \| _ { \mathfrak { s } }$. In this case, we bound separately the terms$\mathcal { N } _ { \gamma } ^ { ( n ) } f , \Gamma _ { x y } \mathcal { N } _ { \gamma } ^ { ( n ) } f$, and$\mathcal { T } ^ { ( n ) } ( x ) ( \Gamma _ { x y } f ( y ) - f ( x ) )$. In order to bound the distance between$\kappa _ { \gamma } f$and$\bar { \kappa } _ { \gamma } \bar { f } ,$, we also need to obtain similar bounds on$\mathcal { N } _ { \gamma } ^ { ( n ) } f - \bar { \mathcal { N } } _ { \gamma } ^ { ( n ) } \bar { f } , \Gamma _ { x y } \mathcal { N } _ { \gamma } ^ { ( n ) } f - \bar { \Gamma } _ { x y } \bar { \mathcal { N } } _ { \gamma } ^ { ( n ) } \bar { \bar { f } } ,$, as well as$\mathcal { T } ^ { ( n ) } ( x ) ( \Gamma _ { x y } f ( y ) - f ( x ) ) \ : - \ :$ $\bar { \mathcal { J } } ^ { ( n ) } ( \dot { x } ) ( \bar { \Gamma } _ { x y } \bar { f } ( y ) - \bar { f } ( x ) )$. Here, we denote by$\bar { \mathcal { I } }$the same function as$\mathcal { I }$, but defined from the model$( { \bar { \Pi } } , { \bar { \Gamma } } )$. The same holds for$\bar { \mathcal { N } } _ { \gamma }$

Recall from (5.42) that we have for$\mathcal { N } _ { \gamma } ^ { ( n ) } f$the bound

$$
\left| \left(\mathcal {N} _ {\gamma} ^ {(n)} f (x)\right) _ {k} \right| \lesssim 2 ^ {(| k | _ {\mathfrak {s}} - \beta - \gamma) n},\tag{5.45}
$$

so that, since we only consider indices k such that$| k | _ { \mathfrak { s } } - \beta - \gamma < 0$, one obtains

$$
\sum_ {n: 2 ^ {- n} \leq \| x - y \| _ {\mathfrak {s}}} | (\mathcal {N} _ {\gamma} ^ {(n)} f (x)) _ {k} | \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\beta + \gamma - | k | _ {\mathfrak {s}}},
$$

as required. In the same way, we obtain the bound

$$
\sum_ {n: 2 ^ {- n} \leq \| x - y \| _ {\mathfrak {s}}} | (\mathcal {N} _ {\gamma} ^ {(n)} f (x) - \bar {\mathcal {N}} _ {\gamma} ^ {(n)} \bar {f} (x)) _ {k} | \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\beta + \gamma - | k | _ {\mathfrak {s}}} \big (\| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} \big)  ,
$$

where we made use of (5.43) instead of (5.42).

Similarly, we obtain for$( \Gamma _ { x y } \mathcal { N } _ { \gamma } ^ { ( n ) } f ( y ) ) _ { k }$the bound

$$
\left| \left(\Gamma_ {x y} \mathcal {N} _ {\gamma} ^ {(n)} f (y)\right) _ {k} \right| \lesssim \sum_ {| k + \ell | _ {\mathfrak {s}} <   \gamma + \beta} \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \gamma) n}.
$$

Summing over values of n with$2 ^ { - n } \leq \| x - y \| _ { \mathfrak { s } }$, we can bound this term again by a multiple of$\| x - y \| _ { \mathfrak { s } } ^ { \beta + \gamma - | k | _ { s } }$. In virtually the same way, we obtain the bound

$$
\begin{array}{r l} & {| (\Gamma_ {x y} \mathcal {N} _ {\gamma} ^ {(n)} f - \bar {\Gamma} _ {x y} \bar {\mathcal {N}} _ {\gamma} ^ {(n)} \bar {f}) _ {k} |} \\ & {\quad \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\beta + \gamma - | k | _ {\mathfrak {s}}} (\| f; \bar {f} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma + \beta ; \bar {\mathfrak {K}}}),} \end{array}
$$

where rewrote the left hand side as$( \Gamma _ { x y } - \bar { \Gamma } _ { x y } ) \mathcal { N } _ { \gamma } ^ { ( n ) } f + \bar { \Gamma } _ { x y } \big ( \bar { \mathcal { N } } _ { \gamma } ^ { ( n ) } \bar { f } - \mathcal { N } _ { \gamma } ^ { ( n ) } f \big )$and then proceeded to bound both terms as above.

We now turn to the term involving${ \mathcal { I } } ^ { ( n ) }$. From the definition of${ \mathcal { I } } ^ { ( n ) }$, we then obtain the bound

$$
\begin{array}{l} \left| \left(\mathcal {J} ^ {(n)} (x) \left(\Gamma_ {x y} f (y) - f (x)\right)\right) _ {k} \right| = \sum_ {\delta \in B _ {k}} \left(\Pi_ {x} \mathcal {Q} _ {\delta} \left(\Gamma_ {x y} f (y) - f (x)\right)\right) \left(D _ {1} ^ {k} K _ {n} (x, \cdot)\right) \\ \lesssim \sum_ {\delta \in B _ {k}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \delta} 2 ^ {\left(| k | _ {\mathfrak {s}} - \beta - \delta\right) n}. \end{array} \tag {5}\tag{5.46}
$$

It follows from the definition of$B _ { k }$that$| k | _ { \mathfrak { s } } - \beta - \delta < 0$for every term appearing in this sum. As a consequence, summing over all n such that$2 ^ { - n } \leq \| x - y \| _ { \mathfrak { s } }$, we obtain a bound of the order$\| x - y \| _ { \mathfrak { s } } ^ { \gamma + \beta - | k | _ { s } }$as required. Regarding the corresponding term arising in$\begin{array} { r } { \kappa _ { \gamma } f - \bar { \kappa } _ { \gamma } \bar { \bar { f } } , } \end{array}$, we use the identity

$$
\begin{array}{r l} & {\Pi_ {x} \mathcal {Q} _ {\delta} (\Gamma_ {x y} f (y) - f (x)) - \bar {\Pi} _ {x} \mathcal {Q} _ {\delta} (\bar {\Gamma} _ {x y} \bar {f} (y) - \bar {f} (x))} \\ & {\qquad = (\Pi_ {x} - \bar {\Pi} _ {x}) \mathcal {Q} _ {\delta} (\Gamma_ {x y} f (y) - f (x))} \\ & {\qquad + \bar {\Pi} _ {x} \mathcal {Q} _ {\delta} (\bar {f} (x) - f (x) - \bar {\Gamma} _ {x y} \bar {f} (y) + \Gamma_ {x y} f (y)),} \end{array}\tag{5.47}
$$

and we bound both terms separately in the same way as above, making use of the definition of$\| f ; { \bar { f } } \| _ { \gamma ; { \bar { \mathcal { R } } } }$in order to control the second term.

It remains to obtain similar bounds on large scales, i.e. in the regime$2 ^ { - n } \geq \Vert x -$ y <sub>s</sub>. We define

$$
\begin{array}{l} \mathcal {T} _ {1} ^ {k} \stackrel {{\text { def }}} {{=}} - k! ((\mathcal {N} _ {\gamma} ^ {(n)} f) (x) + \mathcal {J} ^ {(n)} (x) f (x)) _ {k}  , \\ \mathcal {T} _ {2} ^ {k} \stackrel {{\text { def }}} {{=}} k! ((\Gamma_ {x y} \mathcal {N} _ {\gamma} ^ {(n)} f) (y) + \mathcal {J} ^ {(n)} (x) \Gamma_ {x y} f (y)) _ {k}  . \end{array}
$$

Inspecting the definitions of these terms, we then obtain the identities

$$
\begin{array}{l} \mathcal {T} _ {1} ^ {k} = \Big (\sum_ {\zeta \leq | k | _ {\mathfrak {s}} - \beta} \Pi_ {x} \mathcal {Q} _ {\zeta} f (x) - \mathcal {R} f \Big) (D _ {1} ^ {k} K _ {n} (x, \cdot))  , \\ \mathcal {T} _ {2} ^ {k} = \sum_ {\zeta > | k | _ {\mathfrak {s}} - \beta} (\Pi_ {x} \mathcal {Q} _ {\zeta} \Gamma_ {x y} f (y)) (D _ {1} ^ {k} K _ {n} (x, \cdot)) \\ - \sum_ {| k + \ell | _ {\mathfrak {s}} <   \gamma + \beta} \frac {(x - y) ^ {\ell}}{\ell !} (\Pi_ {y} f (y) - \mathcal {R} f) (D _ {1} ^ {k + \ell} K _ {n} (y, \cdot))  . \end{array}
$$

Adding these two terms, we have

$$
\begin{array}{l} \mathcal {T} _ {2} ^ {k} + \mathcal {T} _ {1} ^ {k} = (\Pi_ {y} f (y) - \mathcal {R} f) (K _ {n; x y} ^ {k, \gamma}) \\ \qquad - \sum_ {\zeta \leq | k | _ {\mathfrak {s}} - \beta} (\Pi_ {x} \mathcal {Q} _ {\zeta} (\Gamma_ {x y} f (y) - f (x))) (D _ {1} ^ {k} K _ {n} (x, \cdot))  . \end{array}\tag{5.48}
$$

In order to bound the first term, we proceed similarly to the proof of the second part of Lemma 5.18. The only difference is that the analogue to the left hand side of (5.30) is now given by

$$
\begin{array}{r l} (\Pi_ {y} f (y) - \mathcal {R} f) (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)) & = (\Pi_ {\bar {y}} f (\bar {y}) - \mathcal {R} f) (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)) \\ & \quad + (\Pi_ {\bar {y}} (\Gamma_ {\bar {y} y} f (y) - f (\bar {y}))) (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)), \end{array} \tag {5.4}\tag{5.49}
$$

where we set${ \bar { y } } = y + h$. Regarding the first term in this expression, recall from (5.42) that

$$
| (\Pi_ {\bar {y}} f (\bar {y}) - \mathcal {R} f) (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)) | \lesssim 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \gamma) n}.
$$

Since$\beta + \gamma \notin \mathbf { N }$by assumption, the exponent appearing in this expression is always strictly positive, thus yielding the required bound. The corresponding bound on$\kappa _ { \gamma } f -$ $\bar { \kappa } _ { \gamma } \bar { f }$is obtained in the same way, but making use of (5.43) instead of (5.42).

To bound the second term in (5.49), we use the fact that$f \in \mathcal { D } ^ { \gamma }$which yields

$$
| (\Pi_ {\bar {y}} (\Gamma_ {\bar {y} y} f (y) - f (\bar {y}))) (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)) | \lesssim \sum_ {\zeta \leq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \zeta} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \zeta - \beta) n}.
$$

We thus obtain a bound analogous to (5.30), with α replaced by$\gamma .$. Proceeding analogously to (5.47), we obtain a similar bound (but with a prefactor$\| \Gamma - \bar { \Gamma } \| _ { \gamma + \beta ; \bar { \hat { \kappa } } } +$ $\| f ; { \bar { f } } \| _ { \gamma ; { \bar { \mathcal { R } } } } )$for the corresponding term appearing in the difference between$\kappa _ { \gamma } f$and $\bar { \kappa } _ { \gamma } \bar { f }$. Proceeding as in the remainder of the proof of Lemma 5.18, we then obtain the bound

$$
| (\Pi_ {y} f (y) - \mathcal {R} f) (K _ {n; x y} ^ {k, \gamma}) | \lesssim \sum_ {\delta > 0} 2 ^ {\delta n} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \gamma + \beta - | k | _ {\mathfrak {s}}} ,\tag{5.50}
$$

where the sum runs only over finitely many values of δ. The corresponding bound for the difference is obtained in the same way.

Regarding the second term in (5.48), we obtain the bound

$$
\left| \left(\Pi_ {x} \mathcal {Q} _ {\zeta} \left(\Gamma_ {x y} f (y) - f (x)\right)\right) \left(D _ {1} ^ {k} K _ {n} (x, \cdot)\right) \right| \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \zeta} 2 ^ {\left(| k | _ {\mathfrak {s}} - \beta - \zeta\right) n}.
$$

At this stage, one might again have summability problems if$\zeta = | k | _ { \mathfrak { s } } - \beta$. However, just as in the proof of Lemma 5.21, our assumptions guarantee that such terms do not contribute. Summing both of these bounds over the relevant values of$n ,$the requested bound follows at once. Again, the corresponding term involved in the difference can be bounded in the same way, by making use of the decomposition (5.47).

It remains to show that the identity (5.17) holds. Actually, by the uniqueness part of the reconstruction theorem, it suffices to show that, for any suitable test function ψ and any$x \in D$, one has

$$
\left(\Pi_ {x} \mathcal {K} f (x) - K * \mathcal {R} f\right) \left(\mathcal {S} _ {\mathfrak {s}, x} ^ {\lambda} \psi\right) \lesssim \lambda^ {\delta},
$$

for some strictly positive exponent δ. Writing$\psi _ { x } ^ { \lambda } = S _ { s , x } ^ { \lambda } \psi$as a shorthand, we obtain the identity

$$
\begin{array}{l} (\Pi_ {x} \mathcal {K} f (x) - K * \mathcal {R} f) (\psi_ {x} ^ {\lambda}) \\ = \sum_ {n \geq 0} \int \bigg (\sum_ {\zeta \in A} (\Pi_ {x} \mathcal {Q} _ {\zeta} f (x)) \Big (K _ {n} (y, \cdot) - \sum_ {| \ell | _ {s} <   \zeta + \beta} \frac {(y - x) ^ {\ell}}{\ell !} D _ {1} ^ {\ell} K _ {n} (x, \cdot) \Big) \\ + \sum_ {\zeta \in A} \sum_ {| \ell | _ {s} <   \zeta + \beta} \frac {(y - x) ^ {\ell}}{\ell !} (\Pi_ {x} \mathcal {Q} _ {\zeta} f (x)) (D _ {1} ^ {\ell} K _ {n} (x, \cdot)) \\ + \sum_ {| k | _ {s} <   \gamma + \beta} \frac {(y - x) ^ {k}}{k !} (\mathcal {R} f - \Pi_ {x} f (x)) (D _ {1} ^ {k} K _ {n} (x, \cdot)) \\ - (\mathcal {R} f) (K _ {n} (y, \cdot)) \Big) \psi_ {x} ^ {\lambda} (y) d y \\ = \sum_ {n \geq 0} \int (\Pi_ {x} f (x) - \mathcal {R} f) (K _ {n; y x} ^ {\gamma}) \psi_ {x} ^ {\lambda} (y) d y. \end{array}
$$

It thus remains to obtain a suitable bound on$( \Pi _ { x } f ( x ) - \mathcal { R } f ) ( K _ { n ; y x } ^ { \gamma } )$. As is by now usual, we treat separately the cases$2 ^ { - n } \leqslant \lambda$

In the case$2 ^ { - n } \geq \lambda$, we already obtained the bound (5.50) (with$k = 0 )$, which yields a bound of the order of$\lambda ^ { \gamma + \beta }$when summed over n and integrated against$\psi _ { x } ^ { \lambda }$ In the case$2 ^ { - n } \leq \lambda ,$we rewrite$K _ { n ; y x } ^ { \gamma }$as

$$
K _ {n; y x} ^ {\gamma} = K _ {n} (y, \cdot) - \sum_ {| \ell | _ {\mathfrak {s}} <   \gamma + \beta} \frac {(y - x) ^ {\ell}}{\ell !} D _ {x} ^ {\ell} K _ {n} (x, \cdot),\tag{5.51}
$$

and we bound the resulting terms separately. To bound the terms involving derivatives of$K _ { n }$, we note that, as a consequence of the reconstruction theorem, we have the bound

$$
\big | \big (\Pi_ {y} f (y) - \mathcal {R} f \big) \big (D _ {x} ^ {\ell} K _ {n} (x, \cdot) \big) \big | \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - \gamma) n}.
$$

Since this exponent is always strictly negative (because$\gamma + \beta \not \in \mathbf { N }$by assumption), this term is summable for large n. After summation and integration against$\psi _ { x } ^ { \lambda }$, we indeed obtain a bound of the order of$\lambda ^ { \gamma + \beta }$as required.

To bound the expression arising from the first term in (5.51), we rewrite it as

$$
\int (\Pi_ {x} f (x) - \mathcal {R} f) (K _ {n} (y, \cdot)) \psi_ {x} ^ {\lambda} (y) d y = (\Pi_ {x} f (x) - \mathcal {R} f) (Y _ {n} ^ {\lambda}),
$$

where$Y _ { n } ^ { \lambda }$is as in (5.34). It then follows from (5.35), combined with the reconstruction theorem, that

$$
\left| \left(\Pi_ {x} f (x) - \mathcal {R} f\right) \left(Y _ {n} ^ {\lambda}\right) \right| \lesssim 2 ^ {- \beta n} \lambda^ {\gamma}.
$$

Summing over all n with$2 ^ { - n } \leq \lambda$, we obtain again a bound of the order$\lambda ^ { \gamma + \beta }$, which concludes the proof.□

Remark 5.22 Alternatively, it is also possible to prove the multi-level Schauder estimate as a consequence of the extension and the reconstruction theorems. The argument goes as follows: first, we add to$T$one additional “abstract” element b which we decree to be of homogeneity$\gamma .$We then extend the representation (Π, Γ) to b by setting

$$
\Pi_ {x} b \stackrel {\text { def }} {=} \mathcal {R} f - \Pi_ {x} f (x), \quad \Gamma_ {x y} b - b \stackrel {\text { def }} {=} f (x) - \Gamma_ {x y} f (y).
$$

(Of course the group G has to be suitable extended to ensure the second identity.) It is an easy exercise to verify that this satisfies the required algebraic identities. Furthermore, the required analytical bounds on Π are satisfied as a consequence of the reconstruction theorem, while the bounds on Γ are satisfied by the definition of$\mathcal { D } ^ { \gamma }$

Setting${ \hat { f } } ( x ) = f ( x ) + b$, it then follows immediately from the definitions that $\Pi _ { x } { \hat { f } } ( x ) = { \mathcal { R } } f$for every x. One can then apply the extension theorem to construct an element b such that (5.12) holds. In particular, this shows that the function$\hat { F }$given by

$$
\hat {F} (x) = \mathcal {I} \hat {f} (x) + \mathcal {J} (x) \hat {f} (x),
$$

satisfies$\Pi _ { x } \hat { F } ( x ) = K * \mathcal { R } f$for every x. Noting that$\Gamma _ { x y } \hat { F } ( x ) = \hat { F } ( y )$, it is then possible to show that on the one hand the map$x \mapsto { \hat { F } } ( x ) - { \mathcal { T } } b$belongs to$\mathcal { D } ^ { \gamma + \beta }$, and that on the other hand one has$\hat { F } ( x ) - \mathcal { T } b = ( \mathcal { K } _ { \gamma } f ) ( x )$, so the claim follows.

The reason for providing the longer proof is twofold. First, it is more direct and therefore gives a “reality check” of the rather abstract construction performed in the extension theorem. Second, the direct proof extends to the case of singular modelled distributions considered in Section 6 below, while the short argument given above does not.

## 5.3 The symmetric case

If we are in the situation of some symmetry group$\mathcal { S }$acting on$\mathcal { T }$as in Section$3 . 6 ,$ then it is natural to impose that$K$is also symmetric in the sense that$K ( T _ { g } x , T _ { g } y ) =$ $K ( x , y )$, and that the abstract integration map$\mathcal { T }$commutes with the action of$\mathcal { S }$in the sense that$M _ { g } \mathcal { T } = \mathscr { T } M _ { g }$for every$g \in \mathcal { S }$

One then has the following result:

Proposition 5.23 In the setting of Theorem 5.12, assume furthermore that a discrete symmetry group$\mathcal { S }$acts on$\mathbf { R } ^ { d }$and on$\mathcal { T }$, that K is symmetric under this action, that (Π, Γ) is adapted to$i t ,$and that commutes with it. Then,$i f f \in \mathcal { D } ^ { \gamma }$is symmetric, so is$\kappa _ { \gamma } f$

Proof. For$g \in { \mathcal { S } } .$, we write again its action on$\mathbf { R } ^ { d }$as$T _ { g } x = A _ { g } x + b _ { g }$. We want to verify that$M _ { g } ( \mathcal { K } _ { \gamma } f ) ( T _ { g } x ) = ( \mathcal { K } _ { \gamma } f ) ( x )$. Actually, this identity holds true separately for the three terms that make up$\kappa _ { \gamma } f$in (5.15).

For the first term, this holds by our assumption on$\mathcal { T } .$To treat the second term, recall Remark 3.37. With the notation used there, we have the identity

$$
M _ {g} \mathcal {J} (T _ {g} x) a = \sum_ {| k | _ {\mathfrak {s}} \leq \alpha} \frac {(A _ {g} X) ^ {k}}{k !} \int D _ {1} ^ {k} K (T _ {g} x, z) (\Pi_ {T _ {g} x} a) (d z)
$$

$$
\begin{array}{l} = \sum_ {| k | _ {\mathfrak {s}} \leq \alpha} \frac {(A _ {g} X) ^ {k}}{k !} \int D _ {1} ^ {k} K (T _ {g} x, T _ {g} z) (\Pi_ {x} M _ {g} a) (d z) \\ = \sum_ {| k | _ {\mathfrak {s}} \leq \alpha} \frac {X ^ {k}}{k !} \int D _ {1} ^ {k} K (x, z) (\Pi_ {x} M _ {g} a) (d z) = \mathcal {J} (x) M _ {g} a  , \end{array}
$$

as required. Here, we made use of the symmetry of$K .$, combined with the fact that$A _ { g }$ is an orthogonal matrix, to go from the second line to the third. The last term is treated similarly by exploiting the symmetry of$\mathcal { R } f$given by Proposition 3.38.□

Finally, one has

Lemma 5.24 In the setting of Lemma 5.5, if$\bar { K }$is symmetric, then it is possible to choose the decomposition$\bar { K } = K + R$in such a way that both K and R are symmetric.

Proof. Denote by$\mathcal { G }$the crystallographic point group associated to${ \mathcal { S } } .$. Then, given any decomposition$\bar { K } = K _ { 0 } + R _ { 0 }$given by Lemma 5.5, it suffices to set

$$
K (x) = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} K (A x), \qquad R (x) = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} R (A x).
$$

The required properties then follow at once.

## 5.4 Differentiation

Being a local operation, differentiating a modelled distribution is straightforward, provided again that the model one works with is sufficiently rich. Denote by$D _ { i }$the (usual) derivative of a distribution on$\mathbf { R } ^ { d }$with respect to the ith coordinate. We then have the following natural definition:

Definition 5.25 Given a sector$V$of a regularity structure$\mathcal { T }$, a family of operators $\mathcal { D } _ { i } \colon V  T$is an abstract gradient for$\mathbf { R } ^ { d }$with scaling s if

one has$\mathcal { D } _ { i } a \in T _ { \alpha - { \mathfrak { s } } _ { i } }$for every$a \in V _ { \alpha }$

one has$\Gamma \mathcal { D } _ { i } a = \mathcal { D } _ { i }$Γa for every$a \in V$and every i.

Regarding the realisation of the actual derivations$D _ { i } .$, we use the following definition:

Definition 5.26 Given an abstract gradient$\mathcal { D }$as above, a model (Π, Γ) on$\mathbf { R } ^ { d }$with scaling s is compatible with$\mathcal { D }$if the identity

$$
D _ {i} \Pi_ {x} a = \Pi_ {x} \mathcal {D} _ {i} a,
$$

holds for every$a \in V$and every$\boldsymbol { x } \in \mathbf { R } ^ { d }$

Remark 5.27 Note that we do not make any assumption on the interplay between the abstract gradient D and the product ⋆. In particular, unless one happens to have the identity$\mathcal { D } _ { i } ( a \star b ) = a \star \mathcal { D } _ { i } b + \mathcal { D } _ { i } a \star b$, there is absolutely no a priori reason forcing the Leibniz rule to hold. This is not surprising since our framework can accommodate Itˆo integration, where the chain rule (and thus the Leibniz rule) fails. See [HK12] for a more thorough investigation of this fact.

Proposition 5.28 Let$\mathcal { D }$be an abstract gradient as above and let$f \in { \mathcal { D } } _ { \alpha } ^ { \beta } ( V )$for some $\beta > \mathfrak { s } _ { i }$and some model (Π, Γ) compatible with${ \mathcal { D } } .$Then,$\mathcal { D } _ { i } f \in \mathcal { D } _ { \alpha - { \mathfrak { s } } _ { i } } ^ { \beta - { \mathfrak { s } } _ { i } }$and the identity$\mathcal { R D } _ { i } f = D _ { i } \mathcal { R } f$holds.

Proof. The fact that$\mathcal { D } _ { i } f \in \mathcal { D } _ { \alpha - { \mathfrak { s } } _ { i } } ^ { \beta - { \mathfrak { s } } _ { i } }$is an immediate consequence of the definitions, so we only need to show that$\mathcal { R D } _ { i } f \stackrel { \cdot } { = } D _ { i } \mathcal { R } f$

By the “uniqueness” part of the reconstruction theorem, this on the other hand follows immediately if we can show that, for every fixed test function$\psi$and every $x \in D ,$, one has

$$
(\Pi_ {x} \mathcal {D} _ {i} f (x) - D _ {i} \mathcal {R} f) (\psi_ {x} ^ {\lambda}) \lesssim \lambda^ {\delta},
$$

for some$\delta > 0$. Here, we defined$\psi _ { x } ^ { \lambda } = S _ { s , x } ^ { \lambda } \psi$as before. By the assumption on the model Π, we have the identity

$$
(\Pi_ {x} \mathscr {D} _ {i} f (x) - D _ {i} \mathscr {R} f) (\psi_ {x} ^ {\lambda}) = (D _ {i} \Pi_ {x} f (x) - D _ {i} \mathscr {R} f) (\psi_ {x} ^ {\lambda}) = - (\Pi_ {x} f (x) - \mathscr {R} f) (D _ {i} \psi_ {x} ^ {\lambda}).
$$

Since$D _ { i } \psi _ { x } ^ { \lambda } = \lambda ^ { - s _ { i } } \mathcal { D } _ { s , x } ^ { \lambda } D _ { i } \psi$, it then follows immediately from the reconstruction theorem that the right hand side of this expression is of order$\lambda ^ { \beta - \mathfrak { s } _ { i } }$, as required.$\boxminus$

Remark 5.29 The polynomial regularity structures$\mathcal { T } _ { d , \mathfrak { s } }$do of course come equipped with a natural gradient operator, obtained by setting$\mathcal { D } _ { i } X _ { j } = \delta _ { i j } \mathbf { 1 }$and extending this to all of$T$by imposing the Leibniz rule.

Remark 5.30 In cases where a symmetry$\mathcal { S }$acts on$\mathcal { T } ,$, it is natural to impose that the abstract gradient is covariant in the sense that if$g \in \mathcal { S }$acts on$\mathbf { R } ^ { d }$as$T _ { g } x = A _ { g } x + b _ { g }$ and$M _ { g }$denotes the corresponding action on$T$, then one imposes that

$$
M _ {g} \mathcal {D} _ {i} \tau = \sum_ {j = 1} ^ {d} A _ {g} ^ {i j} \mathcal {D} _ {j} \tau ,
$$

for every τ in the domain of D. This is consistent with the fact that

$$
\begin{array}{r l} & {(\Pi_ {x} M _ {g} \mathcal {D} _ {i} \tau) (\psi) = (\Pi_ {T _ {g} x} \mathcal {D} _ {i} \tau) (T _ {g} ^ {\sharp} \psi) = (D _ {i} \Pi_ {T _ {g} x} \tau) (T _ {g} ^ {\sharp} \psi)} \\ & {\qquad = - (\Pi_ {T _ {g} x} \tau) (D _ {i} T _ {g} ^ {\sharp} \psi) = - A _ {g} ^ {i j} (\Pi_ {T _ {g} x} \tau) (T _ {g} ^ {\sharp} D _ {j} \psi)} \\ & {\qquad = - A _ {g} ^ {i j} (\Pi_ {x} M _ {g} \tau) (D _ {j} \psi) = A _ {g} ^ {i j} (\Pi_ {x} \mathcal {D} _ {j} M _ {g} \tau) (\psi),} \end{array}
$$

where summation over$j$is implicit. It is also consistent with Remark 3.35.

## 6 Singular modelled distributions

In all of the previous section, we have considered situations where our modelled distributions belong to some space$\mathcal { D } ^ { \gamma }$, which ensures that the bounds (3.1) hold locally uniformly in$\mathbf { R } ^ { \tilde { d } }$. One very important situation for the treatment of initial conditions and / or boundary values is that of functions$f \colon \mathbf { R } ^ { d }  T$which are of the class$\mathcal { D } ^ { \gamma }$away from some fixed sufficiently regular submanifold P (think of the hyperplane formed by “time$0 ^ { \circ }$, which will be our main example), but may exhibit a singularity on$P .$

In order to streamline the exposition, we only consider the case where$P$is given by a hyperplane that is furthermore parallel to some of the canonical basis elements of$\mathbf { R } ^ { d }$. The extension to general submanifolds is almost immediate. Throughout this section, we fix again the ambient space$\mathbf { R } ^ { d }$and its scaling s, and we fix a hyperplane $P$which we assume for simplicity to be given by

$$
P = \left\{x \in \mathbf {R} ^ {d}: x _ {i} = 0, i = 1, \ldots , \bar {d} \right\}.
$$

An important role will be played by the “effective codimension” of$P ,$which we denote by

$$
\mathfrak {m} = \mathfrak {s} _ {1} + \dots + \mathfrak {s} _ {\bar {d}}.\tag{6.1}
$$

Remark 6.1 In the case where$P$is a smooth submanifold, it is important for our analysis that it has a product structure with each factor belonging to a subspace with all components having the same scaling. More precisely, we consider a partition$\mathcal { P }$of the set$\{ 1 , \ldots , d \}$into$J$disjoint non-empty subsets with cardinalities$\{ d _ { j } \} _ { j = 1 } ^ { J }$such that${ \mathfrak { s } } _ { i } = { \mathfrak { s } } _ { j }$if and only if i and$j$belong to the same element of$\mathcal { P }$. This yields a decomposition

$$
\mathbf {R} ^ {d} \sim \mathbf {R} ^ {d _ {1}} \times \dots \times \mathbf {R} ^ {d _ {J}}.
$$

With this notation, we impose that$P$is of the form$\mathcal { M } _ { 1 } \times . . . \times \mathcal { M } _ { J }$, with each of the $\mathcal { M } _ { j }$being a smooth (or at least Lipschitz) submanifold of$\mathbf { R } ^ { d _ { j } }$. The effective codimension m is then given by$\begin{array} { r } { \mathfrak { m } = \sum _ { j = 1 } ^ { J } \mathfrak { m } _ { j } } \end{array}$, where${ \mathfrak { m } } _ { j }$is the codimension of$\mathcal { M } _ { j }$in$\mathbf { R } ^ { d _ { j } }$ Pmultiplied by the corresponding scaling factor.

We also introduce the notations

$$
\| x \| _ {P} = 1 \wedge d _ {\mathfrak {s}} (x, P), \quad \| x, y \| _ {P} = \| x \| _ {P} \wedge \| y \| _ {P}.
$$

Given a subset K$C \mathbf { R } ^ { d }$, we also denote by${ \mathfrak { R } } _ { P }$the set

$$
\mathfrak {K} _ {P} = \left\{(x, y) \in (\mathfrak {K} \setminus P) ^ {2}: x \neq y \quad \text { and } \quad \| x - y \| _ {\mathfrak {s}} \leq \| x, y \| _ {P} \right\}.
$$

With these notations at hand, we define the spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$similarly to$\mathcal { D } ^ { \gamma }$, but we introduce an additional exponent$\eta$controlling the behaviour of the coefficients near$P _ { - }$. Our precise definition goes as follows:

Definition 6.2 Fix a regularity structure$\mathcal { T }$and a model (Π, Γ), as well as a hyperplane $P$as above. Then, for any$\gamma > 0$and$\eta \in \mathbf { R }$, we set

$$
\| f \| _ {\gamma , \eta ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \sup _ {x \in \mathfrak {K} \setminus P} \sup _ {\ell <   \gamma} \frac {\| f (x) \| _ {\ell}}{\| x \| _ {P} ^ {(\eta - \ell) \wedge 0}}, \qquad \| f \| _ {\gamma , \eta ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \sup _ {x \in \mathfrak {K} \setminus P} \sup _ {\ell <   \gamma} \frac {\| f (x) \| _ {\ell}}{\| x \| _ {P} ^ {\eta - \ell}}.
$$

The space$\mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$then consists of all functions$f \colon \mathbf { R } ^ { d } \backslash P  T _ { \gamma } ^ { - }$such that, for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$, one has

$$
\| f \| _ {\gamma , \eta ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \| f \| _ {\gamma , \eta ; \mathfrak {K}} + \sup _ {(x, y) \in \mathfrak {K} _ {P}} \sup _ {\ell <   \gamma} \frac {\| f (x) - \Gamma_ {x y} f (y) \| _ {\ell}}{\| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x , y \| _ {P} ^ {\eta - \gamma}} <   \infty .\tag{6.2}
$$

Similarly to before, we also set

$$
\| f; \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} \stackrel {{\text { def }}} {{=}} \| f - \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} + \sup _ {(x, y) \in \mathfrak {K} _ {P}} \sup _ {\ell <   \gamma} \frac {\| f (x) - \bar {f} (x) - \Gamma_ {x y} f (y) + \bar {\Gamma} _ {x y} \bar {f} (y) \| _ {\ell}}{\| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x , y \| _ {P} ^ {\eta - \gamma}}.
$$

Remark 6.3 In the particular case of$\mathcal { T } = \mathcal { T } _ { d , \mathfrak { s } }$and$( \Pi , \Gamma )$being the canonical model consisting of polynomials, we use the notation$\mathcal { C } _ { P } ^ { \gamma , \eta } ( V )$instead of$\mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$

At distances of order 1 from$P ,$we see that the spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$and$\mathcal { D } ^ { \gamma }$coincide. However, if K is such that$d _ { \mathfrak { s } } ( x , P ) \sim \lambda$for all$x \in { \mathfrak { A } }$, then one has, roughly speaking,

$$
\left\| f \right\| _ {\gamma , \eta ; \mathfrak {K}} \sim \lambda^ {\gamma - \eta} \left\| f \right\| _ {\gamma ; \mathfrak {K}}.\tag{6.3}
$$

In fact, this is not quite true: the components appearing in the first term in (6.2) scale slightly differently. However, it turns out that the first bound actually follows from the second, provided that one has an order one bound on$f$somewhere at order one distance from$P ,$so that (6.3) does convey the right intuition in most situations.

The spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$will be particularly useful when setting up fixed point arguments to solve semilinear parabolic problems, where the solution exhibits a singularity (or at least some form of discontinuity) at$t = 0$. In particular, in all of the concrete examples treated in this article, we will have$P = \{ ( t , x ) : t = 0 \}$

Remark 6.4 The space$\mathcal { D } _ { P } ^ { \gamma , 0 }$does not coincide with$\mathcal { D } ^ { \gamma }$. This is due to the fact that our definition still allows for some discontinuity at$P ,$However,$\mathcal { D } _ { P } ^ { \gamma , \gamma }$essentially coincides with$\mathcal { D } ^ { \gamma }$, the difference being that the supremum in (6.2) only runs over elements in $\mathcal { R } _ { P } . \mathrm { ~ I f ~ } P$is a hyperplane of codimension 1, then$f ( x )$can have different limits whether x approaches$P$from one side or the other.

Definition 6.2 is tailored in such a way that if K is of bounded diameter and we know that

$$
\sup _ {\ell <   \gamma} \| f (x) \| _ {\ell} <   \infty
$$

for some$x \in { \mathfrak { K } } \setminus P ,$, then the bound on the first term in (6.2) follows from the bound on the second term. The following statement is a slightly different version of this fact which will be particularly useful when setting up local fixed point arguments, since it yields good control on$f ( x )$for x near$P .$

For$\boldsymbol { x } \in \mathbf { R } ^ { d }$and$\delta > 0$, we write$S _ { P } ^ { \delta }$x for the value

$$
\mathcal {S} _ {P} ^ {\delta} x = (\delta x _ {1}, \ldots , \delta x _ {\bar {d}}, x _ {\bar {d} + 1}, \ldots , x _ {d}).
$$

With this notation at hand, we then have:

Lemma 6.5 Let K be a domain such that for every$x = ( x _ { 1 } , \ldots , x _ { d } ) \in \mathfrak { R } ,$, one has $S _ { P } ^ { \delta } x \in$K for every$\delta \in [ 0 , 1 ]$. Let$f \in \mathcal { D } _ { P } ^ { \gamma , \eta }$for some$\gamma > 0$and assume that, for every$\ell < \eta ,$, the map$x \mapsto \mathcal Q _ { \ell } f ( x )$extends continuously to all ofK in such a way that $Q _ { \ell } f ( x ) = 0 f o r \ : x \in P$. Then, one has the bound

$$
\llbracket f \rrbracket_ {\gamma , \eta ; \mathfrak {K}} \lesssim \| f \| _ {\gamma , \eta ; \mathfrak {K}},
$$

with a proportionality constant depending affinely on$\| \Gamma \| _ { \gamma ; \mathcal { R } }$. Similarly, let$\bar { f } \in \mathcal { D } _ { P } ^ { \gamma , \eta }$ with respect to a second model$( { \bar { \Pi } } , { \bar { \Gamma } } )$and assume this time that lim$_ { x  P } \mathcal { Q } _ { \ell } ( f ( x ) -$ $\bar { f } ( x ) ) = 0 f o r$every$\ell < \eta .$. Then, one has the bound

$$
\llbracket f - \bar {f} \rrbracket_ {\gamma , \eta ; \mathfrak {K}} \lesssim \| f; \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}} (\| f \| _ {\gamma , \eta ; \mathfrak {K}} + \| \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}}),
$$

with a proportionality constant depending again affinely on$\| \Gamma \| _ { \gamma ; \kappa a n d } \| \bar { \Gamma } \| _ { \gamma ; \kappa . }$

Proof. For$d _ { \mathfrak { s } } ( x , P ) \geq 1$or$\ell \geq \eta _ { ! }$, the bounds follow trivially from the definitions, so we only need to consider the case$d _ { \mathfrak { s } } ( x , P ) < 1$and$\ell < \eta$. We then set$x _ { n } = { \cal S } _ { P } ^ { 2 ^ { - n } } x$ and$x _ { \infty } = S _ { P } ^ { 0 } x$. We also use the shorthand$\Gamma _ { n } = \Gamma _ { x _ { n + 1 } x _ { n } }$, and we assume without loss of generality that$\| f \| _ { \gamma , \eta ; \mathscr { R } } \le 1$. Note that the sequence$x _ { n }$converges to$x _ { \infty }$and that

$$
\| x _ {n + 1} - x _ {n} \| _ {\mathfrak {s}} = \| x _ {n + 1} - x _ {\infty} \| _ {\mathfrak {s}} = \| x _ {n + 1} \| _ {P} = 2 ^ {- (n + 1)} \| x \| _ {P}.\tag{6.4}
$$

The argument now goes by “reverse induction” on ℓ. Assume that the bound $\| f ( x ) \| _ { m } \ \overset { \cdot } { \underset { \sim } { \lesssim } } \| x \| _ { P } ^ { \eta - m }$holds for all$m > \ell ,$which we certainly know to be the case when ℓ is the largest element in A smaller than η since then this bound is already controlled by$\| f \| _ { \gamma , \eta ; \mathcal { R } }$. One then has

$$
\begin{array}{l} \| f (x _ {n + 1}) - f (x _ {n}) \| _ {\ell} \leq \| f (x _ {n + 1}) - \Gamma_ {n} f (x _ {n}) \| _ {\ell} + \| (1 - \Gamma_ {n}) f (x _ {n}) \| _ {\ell} \\ \lesssim 2 ^ {- n (\eta - \ell)} \| x \| _ {P} ^ {\eta - \ell} + \sum_ {m > \ell} 2 ^ {- n (m - \ell)} \| x \| _ {P} ^ {m - \ell} 2 ^ {- n (\eta - m)} \| x \| _ {P} ^ {\eta - m} \\ \lesssim 2 ^ {- n (\eta - \ell)} \| x \| _ {P} ^ {\eta - \ell}, \end{array} \tag {6.5}
$$

where we made use of the definition of$\| f \| _ { \gamma , \eta ; \mathcal { R } }$and (6.4) to bound the first term and of the inductive hypothesis, combined with (6.4) and the bounds on Γ for the second term. It immediately follows that

$$
\| f (x) \| _ {\ell} = \| f (x) - f (x _ {\infty}) \| _ {\ell} \leq \sum_ {n \geq 0} \| f (x _ {n + 1}) - f (x _ {n}) \| _ {\ell} \lesssim \sum_ {n \geq 0} 2 ^ {- n (\eta - \ell)} \| x \| _ {P} ^ {\eta - \ell},
$$

which is precisely what is required for the first bound to hold. Here, the induction argument on ℓ works because A is locally finite by assumption.

The second bound follows in a very similar way. Setting$\delta f = f - \bar { f } ,$we write

$$
\begin{array}{c} \| \delta f (x _ {n + 1}) - \delta f (x _ {n}) \| _ {\ell} \leq \| f (x _ {n + 1}) - \bar {f} (x _ {n + 1}) - \Gamma_ {n} f (x _ {n}) + \bar {\Gamma} _ {n} \bar {f} (x _ {n}) \| _ {\ell} \\ + \| (1 - \Gamma_ {n}) f (x _ {n}) - (1 - \bar {\Gamma} _ {n}) \bar {f} (x _ {n}) \| _ {\ell}. \end{array}
$$

The first term in this expression is bounded in the same way as above. The second term is bounded by

$$
\| (1 - \Gamma_ {n}) f (x _ {n}) - (1 - \bar {\Gamma} _ {n}) \bar {f} (x _ {n}) \| _ {\ell} \lesssim 2 ^ {- n (\eta - \ell)} \| x \| _ {P} ^ {\eta - \ell} \big (\| f, \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma ; \mathfrak {K}} \big)  ,
$$

from which the stated bound then also follows in the same way as above.

The following kind of interpolation inequality will also be useful:

Lemma 6.6 Let$\gamma > 0$and$\kappa \in ( 0 , 1 )$and let f and <sup>¯</sup>f satisfy the assumptions of Lemma 6.5. Then, for every compact set K, one has the bound

$$
\| f; \bar {f} \| _ {(1 - \kappa) \gamma , \eta ; \mathfrak {K}} \lesssim [   [ f - \bar {f} ]   ] _ {\gamma , \eta ; \mathfrak {K}} ^ {\kappa} (\| f \| _ {\gamma , \eta ; \mathfrak {K}} + \| \bar {f} \| _ {\gamma , \eta ; \mathfrak {K}}) ^ {1 - \kappa},
$$

where the proportionality constant depends on$\| \Gamma \| _ { \gamma ; \kappa } + \| \bar { \Gamma } \| _ { \gamma ; \kappa } .$

Proof. All the operations are local, so we can just as well take$\mathcal { R } = \mathbf { R } ^ { d }$. First, one then has the obvious bound

$$
\| f (x) - \Gamma_ {x y} f (y) - \bar {f} (x) + \bar {\Gamma} _ {x y} \bar {f} (y) \| _ {\ell} \leq (\| f \| _ {\gamma , \eta} + \| \bar {f} \| _ {\gamma , \eta}) \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {\eta - \gamma}.
$$

On the other hand, one also has the bound

$$
\| f (x) - \Gamma_ {x y} f (y) - \bar {f} (x) + \bar {\Gamma} _ {x y} \bar {f} (y) \| _ {\ell} \lesssim [   [ f - \bar {f} ]   ] _ {\gamma , \eta} \| x, y \| _ {P} ^ {\eta - \ell},
$$

where the proportionality depends on the sizes of Γ and Γ<sup>¯</sup>. As a consequence of these two bounds, we obtain

$$
\begin{array}{r l} & {\| f (x) - \Gamma_ {x y} f (y) - \bar {f} (x) + \bar {\Gamma} _ {x y} \bar {f} (y) \| _ {\ell} \lesssim [   [ f - \bar {f} ]   ] _ {\gamma , \eta} ^ {\kappa} (\| f \| _ {\gamma , \eta} + \| \bar {f} \| _ {\gamma , \eta}) ^ {1 - \kappa}} \\ & {\qquad \times \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell - \kappa (\gamma - \ell)} \| x, y \| _ {P} ^ {\eta - \kappa \ell - (1 - \kappa) \gamma}} \\ & {\qquad \lesssim [   [ f - \bar {f} ]   ] _ {\gamma , \eta} ^ {\kappa} (\| f \| _ {\gamma , \eta} + \| \bar {f} \| _ {\gamma , \eta}) ^ {1 - \kappa} \| x - y \| _ {\mathfrak {s}} ^ {(1 - \kappa) \gamma - \ell} \| x, y \| _ {P} ^ {\eta - (1 - \kappa) \gamma},} \end{array}
$$

which is precisely the required bound. Here, we made use of the fact that we only consider points with$\| x - y \| _ { \mathfrak { s } } \lesssim \| x , y \| _ { P }$to obtain the last inequality.

Regarding the bound on$\| f ( x ) - { \bar { f } } ( x ) \| _ { \ell }$, one immediately obtains the required bound

$$
\| f (x) - \bar {f} (x) \| _ {\ell} \lesssim \llbracket f - \bar {f} \rrbracket_ {\gamma , \eta} ^ {\kappa} (\| f \| _ {\gamma , \eta} + \| \bar {f} \| _ {\gamma , \eta}) ^ {1 - \kappa} \| x \| _ {P} ^ {(\eta - \ell) \wedge 1},
$$

simply because both$\mathbb { I } \cdot \mathbb { I } _ { \gamma , \eta }$and$\Vert \cdot \Vert _ { \gamma , \eta }$dominate that term.

In this section, we show that all of the calculus developed in the previous sections still carries over to these weighted spaces, provided that the exponents η are chosen in a suitable way. The proofs are mostly based on relatively straightforward but tedious modifications of the existing proofs in the uniform case, so we will try to focus mainly on those aspects that do actually differ.

## 6.1 Reconstruction theorem

We first obtain a modified version of the reconstruction theorem for elements$f \in \mathcal { D } _ { P } ^ { \gamma , \eta }$ Since the reconstruction operator is local and since f belongs to$\mathcal { D } ^ { \gamma }$away from$P ,$ there exists a unique element$\tilde { \mathcal { R } } f$in the dual of smooth functions that are compactly supported away from$P$which is such that

$$
(\tilde {\mathcal {R}} f - \Pi_ {x} f (x)) (\psi_ {x} ^ {\lambda}) \lesssim \lambda^ {\gamma},
$$

for all x$\notin \boldsymbol { P }$and$\lambda \ll d ( x , P )$. The aim of this subsection is to show that, under suitable assumptions,$\tilde { \mathcal { R } } f$extends in a natural way to an actual distribution$\mathcal { R } f$on$\mathbf { R } ^ { d }$ In order to prepare for this result, the following result will be useful.

Lemma 6.7 Let$\mathcal { T } = ( A , T , G )$be a regularity structure and let (Π, Γ) be a model for$\mathcal { T }$over$\mathbf { R } ^ { d }$with scaling s. Let$\psi \in B _ { \mathfrak { s } , 0 } ^ { r }$with$r > |$min$A |$and$\lambda > 0$. Then, for $f \in \mathcal { D } ^ { \gamma }$, one has the bound

$$
| (\mathcal {R} f - \Pi_ {x} f (x)) (\psi_ {x} ^ {\lambda}) | \lesssim \lambda^ {\gamma} \sup _ {y, z \in B _ {2 \lambda} (x)} \sup _ {\ell <   \gamma} \frac {\| f (z) - \Gamma_ {z y} f (y) \| _ {\ell}}{\| z - y \| _ {\mathfrak {s}} ^ {\gamma - \ell}},
$$

where the proportionality constant is oforder$1 + \| \Gamma \| _ { \gamma ; B _ { 2 \lambda } ( x ) } \| \Pi \| _ { \gamma ; B _ { 2 \lambda } ( x ) } .$

Remark 6.8 This is essentially a refinement of the reconstruction theorem. The difference is that the bound only uses information about$f$in a small area around the support of$\varphi _ { x } ^ { \lambda }$

Proof. Inspecting the proof of Proposition 3.25, we note that one really only uses the bounds (3.30) only for pairs x and y with$\| x - y \| _ { \mathfrak { s } } \leq C \lambda$for some fixed$C > 0$. By choosing$n _ { 0 }$sufficiently large, one can furthermore easily ensure that$C \le 2$□

Proposition 6.9 Let$f \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$for some sector V ofregularity$\alpha \leq 0 ,$some$\gamma > 0 ;$ and some$\eta \le \gamma$. Then, provided that α$\wedge \eta > - \mathfrak { m }$where m is as in$( 6 . I ) ,$, there exists a unique distribution$\mathcal { R } f \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha \wedge \eta }$such that$( \mathcal { R } f ) ( \varphi ) = ( \tilde { \mathcal { R } } f ) ( \varphi )$for smooth test functions that are compactly supported away from P. If f and$\bar { f }$are modelled after two models$Z$and${ \bar { Z } } ,$, then one has the bound

$$
\| \mathcal {R} f - \bar {\mathcal {R}} \bar {f} \| _ {\alpha \wedge \eta ; \mathfrak {K}} \lesssim \| f; \bar {f} \| _ {\gamma , \eta ; \bar {\mathfrak {K}}} + \| Z; \bar {Z} \| _ {\gamma ; \bar {\mathfrak {K}}},
$$

where the proportionality constant depends on the norms of$\cdot _ { f , \bar { f } } ,$Z and${ \bar { Z } } .$Here, K is any compact set and K<sup>¯</sup> is its 1-fattening.

Remark 6.10 The condition α$\wedge \eta > -$m rules out the possibility of creating a non-integrable singularity on$P .$, which would prevent$\tilde { \mathcal { R } } f$from defining a distribution on all of$\mathbf { R } ^ { d }$. (Unless one “cancels out” the singularity by a diverging term located on$P ,$ but this would then lead to$\mathcal { R } f$being well-posed only up to some finite distribution localised on$P . )$

Remark 6.11 If$\alpha = 0$and$\eta \geq 0$, then due to our definition of$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$, Proposition 6.9 only implies that$\mathcal { R } f$is a bounded function, not that it is actually continuous.

Proof. Since the reconstruction operator is linear and local, it suffices to consider the case where$\| f \| _ { \gamma , \eta ; \mathscr { R } } \le 1$, which we will assume from now on.

Our main tool in the proof of this result is a suitable partition of the identity in the complement of$P .$. Let$\varphi : \mathbf { R } _ { + } \to [ 0 , 1 ]$be as in Lemma 5.5 and let$\tilde { \varphi } \colon  { \mathbf { R } }  [ 0 , 1 ]$be a smooth function such that supp$\tilde { \varphi } \subset [ - 1 , 1 ]$and

$$
\sum_ {k \in \mathbf {Z}} \tilde {\varphi} (x + k) = 1.
$$

For$n \in \mathbf { Z }$, we then define the countable sets$\boldsymbol { \Xi } _ { P } ^ { n }$by

$$
\Xi_ {P} ^ {n} = \left\{x \in \mathbf {R} ^ {d}: x _ {i} = 0 \text {   for   } i \leq \bar {d} \text {   and   } x _ {i} \in 2 ^ {- n \mathfrak {s} _ {i}} \mathbf {Z} \text {   for   } i > \bar {d} \right\}.
$$

This is very similar to the definition of the sets$\Lambda _ { n } ^ { \mathfrak { s } }$in Section 3.1, except that the points in$\boldsymbol { \Xi } _ { P } ^ { n }$are all located in a small “boundary layer” around$P .$For$\mathbf { \psi } _ { n } \in \mathbf { Z }$and$x \in \Xi _ { P } ^ { n }$ we define the cutoff function$\varphi _ { x , n }$by

$$
\varphi_ {x, n} (y) = \varphi (2 ^ {n} N _ {P} (y)) \tilde {\varphi} \big (2 ^ {n \mathfrak {s} _ {\bar {d} + 1}} (y _ {\bar {d} + 1} - x _ {\bar {d} + 1}) \big) \dots \tilde {\varphi} \big (2 ^ {n \mathfrak {s} _ {d}} (y _ {d} - x _ {d}) \big),
$$

where$N _ { P }$is a smooth function on$\mathbf R ^ { d } \setminus P$which depends only on$( y _ { 1 } , \ldots , y _ { \bar { d } } )$, and which is “1-homogeneous” in the sense that$N _ { P } ( D _ { \mathfrak { s } } ^ { \delta } y ) = \delta N _ { P } ( y )$

One can verify that this construction yields a partition of the unity in the sense that

$$
\sum_ {n \in \mathbf {Z}} \sum_ {x \in \Xi_ {P} ^ {n}} \varphi_ {x, n} (y) = 1,
$$

for every$\boldsymbol { y } \in \mathbf { R } ^ { d } \setminus P$

Let furthermore$\hat { \varphi } _ { N }$be given by$\begin{array} { r } { \hat { \varphi } _ { N } = \sum _ { n \leq N } \sum _ { x \in \Xi _ { P } ^ { n } } \varphi _ { x , n } } \end{array}$. One can then show that, for every distribution$\xi \in \mathcal { C } _ { \mathfrak { s } } ^ { \bar { \alpha } }$with$\bar { \alpha } > - \mathfrak { m }$and every smooth test function ψ, one has

$$
\lim _ {N \to \infty} \xi (\psi (1 - \hat {\varphi} _ {N})) = 0.
$$

As a consequence, it suffices to show that, for every smooth compactly supported test function ψ, the sequence$( \tilde { \mathcal { R } } f ) ( \psi \hat { \varphi } _ { N } )$is Cauchy and that its limit, which we denote by $( \mathcal { R } f ) ( \psi )$, satisfies the bound of Definition 3.7.

Take now a smooth test function ψ supported in$B ( 0 , 1 )$and define the translated and rescaled versions$\psi _ { x } ^ { \lambda }$as before with$\lambda \in ( 0 , 1 ]$. If$d _ { \mathfrak { s } } ( x , P ) \geq 2 \lambda$, then it follows from Lemma 6.7 that

$$
(\tilde {\mathcal {R}} f - \Pi_ {x} f (x)) (\psi_ {x} ^ {\lambda}) \lesssim d _ {\mathfrak {s}} (x, P) ^ {\eta - \gamma} \lambda^ {\gamma} \lesssim \lambda^ {\eta},\tag{6.6}
$$

where the last bound follows from the fact that$\gamma \geq \eta$by assumption. Since furthermore

$$
(\Pi_ {x} f (x)) (\psi_ {x} ^ {\lambda}) \lesssim \sum_ {\alpha \leq \ell <   \gamma} \| x \| _ {P} ^ {(\eta - \ell) \wedge 0} \lambda^ {\ell} \lesssim \lambda^ {\alpha \wedge \eta},\tag{6.7}
$$

we do have the required bound in this case.

In the case$d _ { \mathfrak { s } } ( x , P ) \leq 2 \lambda .$, we rewrite$\psi _ { x } ^ { \lambda }$as

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

for any multiindex k. Furthermore, just as in the case of the bound (6.6), every point in the support of$\chi _ { n , x y }$is located at a distance of$P$that is of the same order. Using a suitable partition of unity, one can therefore rewrite it as

$$
\chi_ {n, x y} = \sum_ {j = 1} ^ {M} \chi_ {n, x y} ^ {(j)},
$$

where M is a fixed constant and where each of the$\chi _ { n , x y } ^ { ( j ) }$has its support centred in a ball of radius$\textstyle { \frac { 1 } { 2 } } d _ { \mathfrak { s } } ( z _ { j } , P )$around some point$z _ { j }$. As a consequence, by the same argument as before, we obtain the bound

$$
(\tilde {\mathcal {R}} f - \Pi_ {z _ {j}} f (z _ {j})) (\chi_ {n, x y}) \lesssim \sum_ {j = 1} ^ {M} d _ {\mathfrak {s}} (z _ {j}, P) ^ {\eta - \gamma} 2 ^ {- \gamma n} \lesssim 2 ^ {- \eta n}.\tag{6.8}
$$

Using the same argument as in (6.7), it then follows at once that

$$
| (\tilde {\mathcal {R}} f) (\chi_ {n, x y}) | \lesssim 2 ^ {- (\alpha \wedge \eta) n}.\tag{6.9}
$$

Note now that we have the identity

$$
(\tilde {\mathcal {R}} f) (\psi_ {x} ^ {\lambda} \hat {\varphi} _ {N}) = \sum_ {n = n _ {0}} ^ {N} \lambda^ {- | \mathfrak {s} |} 2 ^ {- n | \mathfrak {s} |} \sum_ {y \in \Xi_ {P} ^ {n}} (\tilde {\mathcal {R}} f) (\chi_ {n, x y}).
$$

At this stage, we make use of the fact that$\chi _ { n , x y } = 0$, unless$\| x - y \| _ { s } \lesssim \lambda$. As a consequence, for$n \geq n _ { 0 }$, the number of terms contributing in the above sum is bounded by$( 2 ^ { n } \lambda ) ^ { | \mathfrak { s } | - \mathfrak { m } }$. Combining this remark with (6.9) yields the bound

$$
\left| \lambda^ {- | \mathfrak {s} |} 2 ^ {- n | \mathfrak {s} |} \sum_ {y \in \Xi_ {P} ^ {n}} (\tilde {\mathcal {R}} f) (\chi_ {n, x y}) \right| \lesssim \lambda^ {- \mathfrak {m}} 2 ^ {- ((\alpha \wedge \eta) + \mathfrak {m}) n},
$$

from which the claim follows at once, provided that$\alpha \wedge \eta > - \mathfrak { m }$, which is true by assumption. The bound on$\mathcal { R } f - \bar { \mathcal { R } } f$then follows in exactly the same way.□

In the remainder of this section, we extend the calculus developed in the previous sections to the case of singular modelled distributions.

## 6.2 Multiplication

We now show that the product of two singular modelled distributions yields again a singular modelled distribution under suitable assumptions. The precise workings of the exponents is as follows:

Proposition 6.12 Let P be as above and let$f _ { 1 } \in \mathcal { D } _ { P } ^ { \gamma _ { 1 } , \eta _ { 1 } } ( V ^ { ( 1 ) } )$and$f _ { 2 } \in \mathcal { D } _ { P } ^ { \gamma _ { 2 } , \eta _ { 2 } } ( V ^ { ( 2 ) } )$ for two sectors$V ^ { ( 1 ) }$and$V ^ { ( 2 ) }$with respective regularities$\alpha _ { 1 }$and$\alpha _ { 2 } .$. Let furthermore ⋆ be a product on$T$such that$( V ^ { ( 1 ) } , \bar { V } ^ { ( 2 ) } )$is γ-regular with$\gamma = ( \gamma _ { 1 } + \alpha _ { 2 } ) \wedge ( \gamma _ { 2 } + \alpha _ { 1 } )$ Then, the function$f = f _ { 1 } \star _ { \gamma } f _ { 2 }$belongs to$\mathcal { D } _ { P } ^ { \gamma , \eta }$with$\eta = ( \eta _ { 1 } + \alpha _ { 2 } ) \wedge ( \eta _ { 2 } + \alpha _ { 1 } ) \wedge ( \eta _ { 1 } + \eta _ { 2 } )$ $( H e r e , \star _ { \gamma }$is the projection of the product ⋆ onto$T _ { \gamma } ^ { - }$as before.)

Furthermore, in the situation analogous to Proposition$4 . I O ,$writing$f = f _ { 1 } \star f _ { 2 }$ and$g = g _ { 1 } \star g _ { 2 }$, one has the bound

$$
\| f; g \| _ {\gamma , \eta ; \mathfrak {K}} \lesssim \| f _ {1}; g _ {1} \| _ {\gamma_ {1}, \eta_ {1}; \mathfrak {K}} + \| f _ {2}; g _ {2} \| _ {\gamma_ {2}, \eta_ {2}; \mathfrak {K}} + \| \Gamma - \bar {\Gamma} \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}},
$$

uniformly over any bounded set.

Proof. We first show that$f = f _ { 1 } \star _ { \gamma } f _ { 2 }$does indeed satisfy the claimed bounds. By Theorem$4 . 7 .$, we only need to consider points$x , y$which are both at distance less than 1 from$P .$. Also, by bilinearity and locality, it suffices to consider the case when both $f _ { 1 }$and$f _ { 2 }$are of norm 1 on the fixed compact K. Regarding the supremum bound on$f ,$ we have

$$
\begin{array}{l} \| f (x) \| _ {\ell} \leq \sum_ {\ell_ {1} + \ell_ {2} = k} \| f _ {1} (x) \| _ {\ell_ {1}} \| f _ {2} (x) \| _ {\ell_ {2}} \leq \sum_ {\ell_ {1} + \ell_ {2} = \ell} \| x \| _ {P} ^ {(\eta_ {1} - \ell_ {1}) \wedge 0} \| x \| _ {P} ^ {(\eta_ {2} - \ell_ {2}) \wedge 0} \\ \lesssim \| x \| _ {P} ^ {(\eta - \ell) \wedge 0}, \end{array}
$$

which is precisely as required.

It remains to obtain a suitable bound on$f ( x ) - \Gamma _ { x y } f ( y )$. For this, it follows from Definition 6.2 that it suffices to consider pairs$( x , y )$such that$2 \| x - y \| _ { \mathfrak { s } } \leq d _ { \mathfrak { s } } ( x , P ) \wedge$ $d _ { \mathfrak { s } } ( y , P ) \leq 1$. For such pairs$( x , y )$), it follows immediately from the triangle inequality that

$$
d _ {\mathfrak {s}} (x, P) = \| x \| _ {P} \sim \| y \| _ {P} \sim \| x, y \| _ {P},\tag{6.10}
$$

in the sense that any of these quantities is bounded by a multiple of any other quantity, with some universal proportionality constants. For$\ell < \gamma _ { i }$, one then has the bounds

$$
\begin{array}{r} \| f _ {i} (x) - \Gamma_ {x y} f _ {i} (y) \| _ {\ell} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma_ {i} - \ell_ {i}} \| x, y \| _ {P} ^ {\eta_ {i} - \gamma_ {i}}, \\ \| f _ {i} (x) \| _ {\ell} \lesssim \| x, y \| _ {P} ^ {(\eta_ {i} - \ell_ {i}) \wedge 0}, \end{array}\tag{6.11}
$$

for$i \in \{ 1 , 2 \}$

As in (4.6), one then has

$$
\begin{array}{l} \| \Gamma_ {x y} f (y) - (\Gamma_ {x y} f _ {1} (y)) \star (\Gamma_ {x y} f _ {2} (y)) \| _ {\ell} \lesssim \sum_ {m + n \geq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \ell} \| f _ {1} (y) \| _ {m} \| f _ {2} (y) \| _ {n} \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \sum_ {m + n \geq \gamma} \| x, y \| _ {P} ^ {m + n - \gamma} \| x, y \| _ {P} ^ {(\eta_ {1} - m) \wedge 0} \| x, y \| _ {P} ^ {(\eta_ {2} - n) \wedge 0} \\ = \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \sum_ {m + n \geq \gamma} \| x, y \| _ {P} ^ {- \gamma} \| x, y \| _ {P} ^ {\eta_ {1} \wedge m} \| x, y \| _ {P} ^ {\eta_ {2} \wedge n} \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {- \gamma} \| x, y \| _ {P} ^ {\eta_ {1} \wedge \alpha_ {2}} \| x, y \| _ {P} ^ {\eta_ {2} \wedge \alpha_ {1}} \\ = \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {\eta - \gamma}. \end{array} \tag {6.12}
$$

Here, in order to obtain the second line, we made use of (6.10), as well as the fact that we are only considering points$( x , y )$such that$\| x - y \| _ { \mathfrak { s } } \leq \| x , y \| _ { P } .$Combining this with the bound (4.4) from the proof of Theorem 4.7 and using again the bounds (6.11), the requested bound then follows at once.

It remains to obtain a bound on$\| f ; g \| _ { \gamma , \eta ; \mathcal { R } }$. For this, we proceed almost exactly as in Proposition 4.10. First note that, proceeding as above, one obtains the estimate

$$
\begin{array}{l} \| \Gamma_ {x y} f (y) - \bar {\Gamma} _ {x y} g (y) - \Gamma_ {x y} f _ {1} (y) \star \Gamma_ {x y} f _ {2} (y) + \bar {\Gamma} _ {x y} g _ {1} (y) \star \bar {\Gamma} _ {x y} g _ {2} (y) \| _ {\ell} \\ \leq \| \Gamma - \bar {\Gamma} \| _ {\gamma_ {1} + \gamma_ {2}; \mathfrak {K}} \sum_ {m + n \geq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \ell} \| f _ {1} (y) \| _ {m} \| f _ {2} (y) \| _ {n} \\ \quad + \sum_ {m + n \geq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \ell} \| f _ {1} (y) - g _ {1} (y) \| _ {m} \| f _ {2} (y) \| _ {n} \\ \quad + \sum_ {m + n \geq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {m + n - \ell} \| g _ {1} (y) \| _ {m} \| f _ {2} (y) - g _ {2} (y) \| _ {n}, \end{array}
$$

which then yields a bound of the desired type by proceeding as in (6.12). The remainder is then decomposed exactly as in (4.7). Denoting by$T _ { 1 } , \ldots , T _ { 5 }$the terms appearing there, we proceed to bound them again separately.

For the term$T _ { 1 }$, we obtain this time the bound

$$
\| T_{1}\|_{\ell}\lesssim \| f_{1};g_{1}\|_{\gamma_{1},\eta_{1};\mathfrak{K}}\sum_{\substack{m + n = \ell \\ n\geq \alpha_{2};m\geq \alpha_{1}}}\| x - y\|_{\mathfrak{s}}^{\gamma_{1} - m}\| x\|_{P}^{(\eta_{2} - n)\wedge 0}\| x,y\|_{P}^{\eta_{1} - \gamma_{1}}.
$$

Since, as in the proof of Proposition$4 . 1 0 ,$, all the terms in this sum satisfy$\gamma _ { 1 } - m >$ $\gamma - \ell ,$, we can bound$\| x - y \| _ { \mathfrak { s } } ^ { \gamma _ { 1 } - m }$by$\| x - y \| _ { \mathfrak { s } } ^ { \gamma - \ell } \| x , y \| _ { P } ^ { n + \gamma _ { 1 } - \gamma }$. We thus obtain the bound

$$
\| T _ {1} \| _ {\ell} \lesssim \| f _ {1}; g _ {1} \| _ {\gamma_ {1}, \eta_ {1}; \mathfrak {K}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {(\eta_ {2} \wedge \alpha_ {2}) + \eta_ {1} - \gamma}.
$$

Since$\eta \leq ( \eta _ { 2 } \land \alpha _ { 2 } ) + \eta _ { 1 }$, this bound is precisely as required.

The bound on$T _ { 2 }$follows in a similar way, once we note that for the pairs$( x , y )$ under consideration one has

$$
\begin{array}{c} \| \Gamma_ {x y} f _ {1} (y) \| _ {\ell} \lesssim \sum_ {m \geq \ell} \| x - y \| _ {\mathfrak {s}} ^ {m - \ell} \| f _ {1} (y) \| _ {m} \lesssim \sum_ {m \geq \ell} \varrho_ {\mathfrak {s}} ^ {m - \ell} (x, y) \| f _ {1} (y) \| _ {m} \\ \lesssim \sum_ {m \geq \ell} \varrho_ {\mathfrak {s}} ^ {m - \ell} (x, y) \varrho_ {\mathfrak {s}} ^ {(\eta_ {1} - m) \wedge 0} (x, y) \lesssim \varrho_ {\mathfrak {s}} ^ {(\eta_ {1} - \ell) \wedge 0} (x, y), \end{array}\tag{6.13}
$$

where we used (6.10) to obtain the penultimate bound, so that$\Gamma _ { x y } f _ { 1 } ( y )$satisfies essentially the same bounds as$f _ { 1 } ( x )$

Regarding the term$T _ { 5 }$, we obtain

$$
\| T_{5}\|_{\ell}\lesssim \| f_{2} - g_{2}\|_{\gamma_{2},\eta_{2};\mathfrak{K}}\sum_{\substack{m + n = \ell \\ m\geq \alpha_{1};n\geq \alpha_{2}}}\| x - y\|_{\mathfrak{s}}^{\gamma_{1} - m}\| x,y\|_{P}^{\eta_{1} - \gamma_{1}}\| y\|_{P}^{(\eta_{2} - n)\wedge 0}  ,
$$

from which the required bound follows in the same way as for$T _ { 1 }$. The term$T _ { 3 }$is treated in the same way by making again use of the remark (6.13), this time with $g _ { 1 } ( y ) - f _ { 1 } ( y )$playing the role of$f _ { 1 } ( y )$

The remaining term$T _ { 4 }$can be bounded in virtually the same way as$T _ { 5 }$, the main difference being that the bounds on$( \bar { \Gamma } _ { x y } - \Gamma _ { x y } ) f _ { 1 } ( y )$are proportional to$\| \Gamma - \bar { \Gamma } \| _ { \gamma _ { 1 } ; \mathbb { A } }$ so that one has

$$
\| T _ {4} \| _ {\ell} \lesssim \| \Gamma - \bar {\Gamma} \| _ {\gamma_ {1}; \mathfrak {K}} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell} \| x, y \| _ {P} ^ {(\eta_ {1} \wedge \alpha_ {1}) + \eta_ {2} - \gamma}.
$$

Combining all of these bounds completes the proof.

## 6.3 Composition with smooth functions

Similarly to the case of multiplication of two modelled distributions, we can compose them with smooth functions as in Section 4.2, provided that they belong to$\mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$for some function-like sector$V$stable under the product ⋆, and for some$\eta \geq 0$

Proposition 6.13 Let P be as above, let$\gamma > 0 ,$, and let$f _ { i } \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$be a collection of n modelled distributions for some function-like sector V which is stable under the product ⋆. Assume furthermore that V is γ-regular in the sense of Definition 4.6.

Letfurthermore$F \colon \mathbf { R } ^ { n }  \mathbf { R }$be a smoothfunction. Then, provided that$\eta \in [ 0 , \gamma ]$ the modelled distribution$\hat { F } _ { \gamma } ( f )$defined as in Section 4.2 also belongs to$\mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$ Furthermore, the map$\hat { F } _ { \gamma } \colon { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V ) \to { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V )$is locally Lipschitz continuous in any of the seminorms$\| { \bf \cdot } \| _ { \gamma , \eta ; \kappa } a \dot { n } d \| { \bf \cdot } \| _ { \gamma , \eta ; \kappa } .$

Remark 6.14 In fact, we do not need$F$to be${ \mathcal { C } } ^ { \infty }$, but the same regularity requirements as in Section 4.2 suffice. Also, it is likely that one could obtain continuity in the strong sense, but in the interest of brevity, we refrain from doing so.

Proof. Write$b ( x ) = \hat { F } _ { \gamma } ( f ( x ) )$as before. We also set$\zeta \in [ 0 , \gamma ]$as in the proof of Theorem 4.16. Regarding the bound on$\| b \| _ { \gamma , \eta ; \mathcal { R } }$, we note first that since we assumed that$\eta \ge 0 , ( 6 . 2 )$implies that the quantities$D ^ { k } F ( { \bar { f } } ( x ) )$are locally uniformly bounded. It follows that one has the bound

$$
\| b (x) \| _ {\ell} \lesssim \sum_ {\ell_ {1} + \dots + \ell_ {n} = \ell} \| f (x) \| _ {\ell_ {1}} \dots \| f (x) \| _ {\ell_ {n}},
$$

where the sum runs over all possible ways of decomposing ℓ into finitely many strictly positive elements$\ell _ { i } \in A$. Note now that one necessarily has the bound

$$
\left((\eta - \ell_ {1}) \wedge 0\right) + \ldots + \left((\eta - \ell_ {n}) \wedge 0\right) \geq (\eta - \ell) \wedge 0.\tag{6.14}
$$

Indeed, if all of the terms on the left vanish, then the bound holds trivially. Otherwise, at least one term is given by$\eta - \ell _ { i }$and, for all the other terms, we use the fact that $( \eta - \ell _ { j } ) \wedge 0 \geq - \ell _ { j }$. Since$\| x \| _ { P } \leq 1$, it follows at once that

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

where$\sum \ell _ { i } \geq \gamma$. Combining the bounds on Γ with the definition of the space$\mathcal { D } _ { P } ^ { \gamma , \eta }$, we Pknow furthermore that each of these factors satisfies a bound of the type

$$
\| \Gamma_ {x y} \mathcal {Q} _ {\ell_ {i}} \tilde {f} (y) \| _ {m} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\ell_ {i} - m} \| x \| _ {P} ^ {(\eta - \ell_ {i}) \wedge 0}.\tag{6.16}
$$

Combining this with the fact that$\sum \ell _ { i } \geq \gamma$, that$\| x - y \| _ { s } \lesssim \| x \| _ { P }$, and the bound (6.14), the bound (6.15) follows for$R _ { 1 }$

Regarding$R _ { f }$, it follows from the definitions that

$$
\| R _ {f} (x, y) \| _ {m} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma - m} \| x, y \| _ {P} ^ {\eta - \gamma}.\tag{6.17}
$$

Furthermore, as a consequence of the fact that$\eta \geq 0$and$\| x - y \| _ { s } \lesssim \| x \| _ { P }$, it follows from (6.16) and (6.17) that

$$
\| \Gamma_ {x y} \tilde {f} (y) \| _ {m} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {- m}, \qquad \| \tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1} \| _ {m} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {- m}.
$$

Combining this with (6.17) and the expression for$R _ { 2 }$, we immediately conclude that $R _ { 2 }$also satisfies (6.15).

Note now that one has the bound

$$
\begin{array}{l} | \bar {f} (x) - \bar {f} (y) | \lesssim \| \Gamma_ {x y} \tilde {f} (y) \| _ {0} + \| x - y \| _ {\mathfrak {s}} ^ {\gamma} \| x, y \| _ {P} ^ {\eta - \gamma} \\ \lesssim \sum_ {\zeta \leq \ell <   \gamma} \| x - y \| _ {\mathfrak {s}} ^ {\ell} \| x, y \| _ {P} ^ {(\eta - \ell) \wedge 0} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\zeta} \| x, y \| _ {P} ^ {(\eta - \zeta) \wedge 0}, \end{array}\tag{6.18}
$$

where we used the fact that$\zeta \leq \gamma$. Since we furthermore know that$f ( x )$is uniformly bounded in K as a consequence of the fact that$\eta \geq 0$, it follows that the bound equivalent to (4.14) in this context is given by

$$
D ^ {k} F (\bar {f} (x)) = \sum_ {| k + \ell | \leq L} \frac {D ^ {k + \ell} F (\bar {f} (y))}{\ell !} (\bar {f} (x) - \bar {f} (y)) ^ {\ell} + \mathcal {O} (\| x - y \| _ {\mathfrak {s}} ^ {\gamma - | k | \zeta} \| x, y \| _ {P} ^ {\mu_ {k}}),\tag{6.19}
$$

where$L = \lfloor \gamma / \zeta \rfloor$and the exponent$\mu _ { k }$is given by$\mu _ { k } = \left( | k | \zeta - \gamma - | k | \eta + ( \gamma \eta / \zeta ) \right) \wedge 0$ We can furthermore assume without loss of generality that$\zeta \leq 1$. Furthermore, making use of (6.18), it follows as in (4.15) that

$$
\begin{array}{r l} \| (\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) \mathbf {1}) ^ {\star k} \| _ {\beta} & \lesssim \sum_ {m \geq 0} \sum_ {\ell} \| x - y \| _ {\mathfrak {s}} ^ {\zeta (| k | - m)} \| x, y \| _ {P} ^ {(| k | - m) ((\eta - \zeta) \wedge 0)} \\ & \quad \times \| x, y \| _ {P} ^ {(\eta - \ell_ {1}) \wedge 0} \dots \| x, y \| _ {P} ^ {(\eta - \ell_ {m}) \wedge 0}, \end{array}
$$

where the second sum runs over all indices$\ell _ { 1 } , \ldots , \ell _ { m }$with$\textstyle \sum \ell _ { i } = \beta$and$\ell _ { i } \geq \zeta$for every i. In particular, one has the bound

$$
\begin{array}{l} \| (\tilde {f} (y) + (\bar {f} (y) - \bar {f} (x)) {\bf 1}) ^ {\star k} \| _ {\beta} \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\zeta | k | - \beta} \| x, y \| _ {P} ^ {\beta - \zeta m} \\ \qquad \times \sum_ {m \geq 0} \sum_ {\ell} \| x, y \| _ {P} ^ {(| k | - m) ((\eta - \zeta) \wedge 0)} \| x, y \| _ {P} ^ {(\eta - \ell_ {1}) \wedge 0} \dots \| x, y \| _ {P} ^ {(\eta - \ell_ {m}) \wedge 0}. \end{array}
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

where we used the fact that$\zeta \leq \gamma$and the last identity follows from the assumption that$\eta \leq \gamma$. Combining this with (6.19) and the definition of$R _ { 3 }$from (4.16), we obtain the bound (6.15) for$R _ { 3 }$, which implies that$\hat { F } ( f ) \in \mathcal { D } _ { P } ^ { \gamma , \eta }$as required.

The proof of the local Lipschitz continuity then follows in exactly the same way as in the proof of Theorem 4.16.□

## 6.4 Differentiation

In the same context as Section 5.4, one has the following result:

Proposition 6.15 Let D be an abstract gradient as in Section 5.4 and let$f \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$ for some$\gamma > { \mathfrak { s } } _ { i }$and$\eta \in \mathbf { R } .$. Then,$\mathcal { D } _ { i } f \in \mathcal { D } _ { P } ^ { \gamma - s _ { i } , \eta - { \mathfrak { s } } _ { i } }$

Proof. This is an immediate consequence of the definition (6.2) and the properties of abstract gradients.□

## 6.5 Integration against singular kernels

In this section, we extend the results from Section 5 to spaces of singular modelled distributions. Our main result can be stated as follows.

Proposition 6.16 Let T, V, K and β be as in Theorem 5.12 and let$f \in { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V )$ with$\eta < \gamma$. Denote furthermore by α the regularity of the sector V and assume that $\eta \wedge \alpha > - \mathfrak { m }$. Then, provided that$\gamma + \beta \not \in \mathbf { N }$and η${ \bf { + } } \beta \not \in { \bf N } ,$one has${ \cal K } _ { \gamma } f \in { \cal D } _ { P } ^ { \bar { \gamma } , \bar { \eta } }$ with$\bar { \gamma } = \gamma + \beta$and$\bar { \eta } = ( \eta \wedge \alpha ) + \beta .$

Furthermore, in the situation analogous to that of the last part of Theorem 5.12, one has the bound

$$
\| \mathcal {K} _ {\gamma} f; \bar {\mathcal {K}} _ {\gamma} \bar {f} \| _ {\bar {\gamma}, \bar {\eta}; \mathfrak {K}} \lesssim \| f; \bar {f} \| _ {\gamma , \eta ; \bar {\mathfrak {K}}} + \| \Pi - \bar {\Pi} \| _ {\gamma ; \bar {\mathfrak {K}}} + \| \Gamma - \bar {\Gamma} \| _ {\bar {\gamma}; \bar {\mathfrak {K}}},\tag{6.20}
$$

for all$f \in { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V ; \Gamma )$and$\bar { f } \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V ; \bar { \Gamma } )$.

Proof. We first observe that$\mathcal { N } _ { \gamma } f$is well-defined for a singular modelled distribution as in the statement. Indeed, for every$x \notin P$, it suffices to decompose K as$K =$ $K ^ { ( 1 ) } + K ^ { ( 2 ) }$, where$K ^ { ( 1 ) }$is given by$\begin{array} { r } { \dot { K ^ { ( 1 ) } } = \sum _ { n \geq n _ { 0 } } K _ { n } } \end{array}$, and$n _ { 0 }$is sufficiently large so that$2 ^ { - n _ { 0 } } \leq d _ { \mathfrak { s } } ( x , P ) / 2$P, say. Then, the fact that$_ { ( 5 . 1 6 ) }$is well-posed with K replaced by$K ^ { ( 1 ) }$follows from Theorem 5.12. The fact that it is well-posed with K replaced by$K ^ { ( 2 ) }$follows from the fact that$K ^ { ( 2 ) }$is globally smooth and compactly supported, combined with Proposition 6.9.

To prove that$\kappa _ { \gamma } f$belongs to${ \mathcal { D } } _ { P } ^ { \gamma + \beta , ( \eta \wedge \alpha ) + \beta } ( V )$, we proceed as in the proof of Theorem 5.12. We first consider values of ℓ with$\ell \not \in { \bf N }$. For such values, one has as before$\mathcal { Q } _ { \ell } ( \mathcal { K } _ { \gamma } f ) ( x ) = \mathcal { Q } _ { \ell } \mathcal { T } f ( x )$and$\mathcal { Q } _ { \ell } \Gamma _ { x y } ( \mathcal { K } _ { \gamma } f ) ( y ) = \mathcal { Q } _ { \ell } \mathcal { T } \Gamma _ { x y } f ( y )$, so that the required bounds on$\| K _ { \gamma } f ( x ) \| _ { \ell } , \| K _ { \gamma } f ( x ) - \Gamma _ { x y } K _ { \gamma } f ( x ) \| _ { \ell } , \| K _ { \gamma } f ( x ) - \bar { K } _ { \gamma } \bar { f } ( x ) \| _ { \ell }$, as well as$\| \mathcal { K } _ { \gamma } f ( x ) - \Gamma _ { x y } \mathcal { K } _ { \gamma } f ( x ) - \bar { \mathcal { K } } _ { \gamma } \bar { f } ( x ) + \bar { \Gamma } _ { x y } \bar { \mathcal { K } } _ { \gamma } \bar { f } ( x ) \| _ { \ell }$follow at once. (Here and below we use the fact that$\| x , y \| _ { P } ^ { \eta - \gamma } \leq \| x , y \| _ { P } ^ { ( \eta \wedge \alpha ) - \gamma }$since one only considers pairs $( x , y )$such that$\varrho _ { 5 } \leq 1 . )$

It remains to treat the integer values of ℓ. First, we want to show that one has the bound

$$
\| \mathcal {K} _ {\gamma} f (x) \| _ {\ell} \lesssim \| x \| _ {P} ^ {(\bar {\eta} - \ell) \wedge 0},
$$

and similarly for$\| \mathcal { K } _ { \gamma } f - \bar { \mathcal { K } } _ { \gamma } \bar { f } \| _ { \ell }$. For this, we proceed similarly to Theorem 5.12, noting that if$2 ^ { - ( n + 1 ) } \leq \| x \| _ { P }$then, by Remark 3.27, one has the bound

$$
| (\mathcal {R} f - \Pi_ {x} f (x)) (D _ {1} ^ {\ell} K _ {n} (x, \cdot)) | \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - \gamma) n} \| x \| _ {P} ^ {\eta - \gamma}.
$$

(In this expression, ℓ is a multiindex.) Furthermore, regarding${ \mathcal { T } } ^ { ( n ) } ( x ) f ( x )$, one has

$$
\| \mathcal {J} ^ {(n)} (x) f (x) \| _ {\ell} \lesssim \sum_ {\zeta > \ell - \beta} \| x \| _ {P} ^ {(\eta - \zeta) \wedge 0} 2 ^ {(\ell - \beta - \zeta) n}.
$$

Combining these two bounds and summing over the relevant values of n yields

$$
\sum_ {2 ^ {- (n + 1)} \leq \| x \| _ {P}} \| \mathcal {K} _ {\gamma} ^ {(n)} f \| _ {\ell} \lesssim \sum_ {\zeta > \ell - \beta} \| x \| _ {P} ^ {\zeta + \beta - \ell + ((\eta - \zeta) \wedge 0)},
$$

which is indeed bounded by$\| x \| _ { P } ^ { ( { \bar { \eta } } - { \ell } ) \wedge 0 }$as required since one always has$\zeta \geq \alpha$. For $\| x \| _ { P } < 2 ^ { - ( n + 1 ) }$on the other hand, we make use of the reconstruction theorem for modelled distributions which yields

$$
\begin{array}{l} | (\mathcal {R} f - \Pi_ {x} f (x)) (D _ {1} ^ {\ell} K _ {n} (x, \cdot)) + \mathcal {Q} _ {| \ell | _ {\mathfrak {s}}} \mathcal {J} ^ {(n)} (x) f (x) | \\ \lesssim | (\mathcal {R} f) (D _ {1} ^ {\ell} K _ {n} (x, \cdot)) | + \sum_ {\zeta \leq | \ell | _ {\mathfrak {s}} - \beta} | (\Pi_ {x} f (x)) (D _ {1} ^ {\ell} K _ {n} (x, \cdot)) | \\ \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - (\eta \wedge \alpha)) n} + \sum_ {\zeta \leq | \ell | _ {\mathfrak {s}} - \beta} 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - \zeta) n} \| x \| _ {P} ^ {(\eta - \zeta) \wedge 0}. \end{array}
$$

Summing again over the relevant values of n yields again

$$
\sum_ {2 ^ {- (n + 1)} > \| x \| _ {P}} \| \mathcal {K} _ {\gamma} ^ {(n)} f \| _ {\ell} \lesssim \sum_ {\zeta \leq \ell - \beta} \| x \| _ {P} ^ {\zeta + \beta - \ell + ((\eta - \zeta) \wedge 0)},
$$

which is bounded by$\| x \| _ { P } ^ { ( { \bar { \eta } } - { \ell } ) \wedge 0 }$for the same reason as before. The corresponding bounds on$\| \mathcal { K } _ { \gamma } f - \bar { \mathcal { K } } _ { \gamma } \bar { f } \| _ { \ell }$are obtained in virtually the same way.

It therefore remains to obtain the bounds on$\| \mathcal { K } _ { \gamma } f ( x ) - \bar { \mathcal { K } } _ { \gamma } \bar { f } ( x ) \| _ { \ell }$and$\| \mathcal { K } _ { \gamma } f ( x ) -$ $\Gamma _ { x y } K _ { \gamma } f ( x ) - \bar { K } _ { \gamma } \bar { f } ( x ) + \bar { \Gamma } _ { x y } \bar { K } _ { \gamma } \bar { f } ( x ) \| _ { \ell }$. For this, we proceed exactly as in the proof of Theorem 5.12, but we keep track of the dependency on x and$y ,$rather than just the difference. Recall also that we only ever consider the case where$( x , y ) \in \mathbb { A } _ { P }$, so that $\| x , y \| _ { P } > \| x - y \| _ { s }$. This time, we consider separately the three cases$2 ^ { - n } \leq \| x - y \| _ { s } ,$ $2 ^ { - n } \in [ \| x - y \| _ { \mathfrak { s } } , { \frac { 1 } { 2 } } \| x , y \| _ { P } ]$and$2 ^ { - n } \geq { \frac { 1 } { 2 } } \| x , y \| _ { P }$

When$2 ^ { - n } \leq \| { \bar { \boldsymbol { x } } } - \boldsymbol { y } \| _ { s } ,$, we use Remark 3.27 which shows that, when following the exact same considerations as in Theorem 5.12, we always obtain the same bounds, but multiplied by a factor$\| x , y \| _ { P } ^ { \eta - \gamma }$. The case$2 ^ { - n } \leq \| x - y \|$<sub>s</sub> therefore follows at once.

We now turn to the case$2 ^ { - n } \in [ \| x - y \| _ { s } , { \frac { 1 } { 2 } } \| x , y \| _ { P } ]$. As in the proof of Theorem 5.12 (see (5.48) in particular), we can again reduce this case to obtaining the bounds

$$
\begin{array}{c} | (\Pi_ {x} \mathcal {Q} _ {\zeta} (\Gamma_ {x y} f (y) - f (x))) (D _ {1} ^ {k} K _ {n} (x, \cdot)) | \lesssim \| x, y \| _ {P} ^ {\eta - \gamma} \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \gamma + \beta - | k | _ {\mathfrak {s}}} 2 ^ {\delta n} \\ | (\Pi_ {y} f (y) - \mathcal {R} f) (K _ {n; x y} ^ {k, \gamma}) | \lesssim \| x, y \| _ {P} ^ {\eta - \gamma} \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \gamma + \beta - | k | _ {\mathfrak {s}}} 2 ^ {\delta n}, \end{array}
$$

for every$\zeta \leq | k | _ { s } - \beta$and where the sums over$\delta$contain only finitely many terms. The first line is obtained exactly as in the proof of Theorem 5.12, so we focus on the second line. Following the same strategy as in the proof of Theorem 5.12, we similarly reduce it to obtaining bounds of the form

$$
| (\Pi_ {y} f (y) - \mathcal {R} f) (D _ {1} ^ {\ell} K _ {n} (\bar {y}, \cdot)) | \lesssim \| x, y \| _ {P} ^ {\eta - \gamma} \sum_ {\delta > 0} \| x - y \| _ {\mathfrak {s}} ^ {\delta + \gamma + \beta - | \ell | _ {\mathfrak {s}}} 2 ^ {\delta n},
$$

where y¯ is such that$\| x - \bar { y } \| _ { \mathfrak { s } } \leq \| x - y \| .$<sub>s</sub> and$\ell$is a multiindex with$| \ell | _ { \mathfrak { s } } \geq | k | _ { \mathfrak { s } } + ( 0 \vee$ $( \gamma + \beta ) \}$). Since we only consider pairs$( x , y )$such that$\begin{array} { r } { \| x - y \| _ { \hat { s } } \leq \frac { 1 } { 2 } \| x , y \| _ { P } , } \end{array}$, one has $\| y , \bar { y } \| _ { P } \sim \| x , y \| _ { P }$. As a consequence, we obtain as in the proof of Theorem 5.12

$$
\left| \left(\Pi_ {\bar {y}} \left(\Gamma_ {\bar {y} y} f (y) - f (\bar {y})\right)\right) \left(D _ {1} ^ {\ell} K _ {n} (\bar {y}, \cdot)\right) \right| \lesssim \| x, y \| _ {P} ^ {\eta - \gamma} \sum_ {\zeta \leq \gamma} \| x - y \| _ {\mathfrak {s}} ^ {\gamma - \zeta} 2 ^ {\left(| \ell | _ {\mathfrak {s}} - \zeta - \beta\right) n}.
$$

Furthermore, since$2 ^ { - n } \leq \| x , y \| _ { P }$, we obtain as in (6.6) the bound

$$
| (\Pi_ {\bar {y}} f (\bar {y}) - \mathcal {R} f) (D _ {1} ^ {\ell} K _ {n} (\bar {y}, \cdot)) | \lesssim 2 ^ {(| \ell | _ {\mathfrak {s}} - \beta - \gamma) n} \| x, y \| _ {P} ^ {\eta - \gamma}.
$$

The rest of the argument is then again exactly the same as for Theorem 5.12. The corresponding bounds on the distance between$\kappa _ { \gamma } f$and$\bar { \kappa } _ { \gamma } \bar { f }$follows analogously.

It remains to consider the case$\begin{array} { r } { 2 ^ { - n } \geq \frac { 1 } { 2 } \| x , y \| _ { P } ^ { - } } \end{array}$. In this case, we proceed as before but, in order to bound the term involving$\ln _ { y } f ( y ) - \mathcal { R } f$, we simply use the triangle inequality to rewrite it as

$$
| (\Pi_ {y} f (y) - \mathcal {R} f) (K _ {n; x y} ^ {k, \gamma}) | \leq | (\Pi_ {y} f (y)) (K _ {n; x y} ^ {k, \gamma}) | + | (\mathcal {R} f) (K _ {n; x y} ^ {k, \gamma}) |.
$$

We then use again the representation (5.28) for$K _ { n ; x y } ^ { k , \gamma }$, together with the bounds

$$
\begin{array}{c} | (\mathcal {R} f) (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)) | \lesssim 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - (\alpha \wedge \eta)) n}, \\ | (\Pi_ {y} f (y)) (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)) | \lesssim \sum_ {\alpha \leq \zeta <   \gamma} \| y \| _ {P} ^ {(\eta - \zeta) \wedge 0} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \zeta) n}. \end{array}
$$

Here, the first bound is a consequence of the reconstruction theorem for singular modelled distributions, while the second bound follows from Definition 6.2. Since

$$
2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - (\alpha \wedge \eta)) n} \leq 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \alpha) n} + 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \eta) n},
$$

and since$\eta \in [ \alpha , \gamma )$by assumption, we see that the first bound is actually of the same form as the second, so that

$$
| (\Pi_ {y} f (y) - \mathcal {R} f) (D _ {1} ^ {k + \ell} K _ {n} (\bar {y}, \cdot)) | \lesssim \sum_ {\alpha \leq \zeta <   \gamma} \| y \| _ {P} ^ {(\eta - \zeta) \wedge 0} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \zeta) n},
$$

where the sum runs over finitely many terms. Performing the integration in (5.28) and using the bound (5.31), we conclude that

$$
| (\Pi_ {y} f (y) - \mathcal {R} f) (K _ {n; x y} ^ {k, \gamma}) | \lesssim \sum_ {\zeta ; \ell} \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}} \| x, y \| _ {P} ^ {(\eta - \zeta) \wedge 0} 2 ^ {(| k + \ell | _ {\mathfrak {s}} - \beta - \zeta) n},
$$

where we used the fact that$\| y \| _ { P } \sim \| x , y \| _ { P }$. Here, the sum runs over exponents$\zeta$as before and multiindices ℓ such that$| k + \ell | _ { \mathfrak { s } } > \beta + \gamma$. Summing this expression over the relevant range of values for$n ,$, we have

$$
\begin{array}{c} \sum_ {2 ^ {- n} \geq \| x, y \| _ {P}} | (\Pi_ {y} f (y) - \mathcal {R} f) (K _ {n; x y} ^ {k, \gamma}) | \lesssim \sum_ {\zeta ; \ell} \| x - y \| _ {\mathfrak {s}} ^ {| \ell | _ {\mathfrak {s}}} \| x, y \| _ {P} ^ {(\eta \wedge \zeta) + \beta - | k + \ell | _ {\mathfrak {s}}} \\ \lesssim \| x - y \| _ {\mathfrak {s}} ^ {\gamma + \beta - | k | _ {\mathfrak {s}}} \| x, y \| _ {P} ^ {(\eta \wedge \alpha) - \gamma}, \end{array}
$$

where we used the fact that$\| x - y \| _ { \mathfrak { s } } \leq { \frac { 1 } { 2 } } \| x , y \| _ { P }$to obtain the second bound. Again, the corresponding bounds on the distance between$\kappa _ { \gamma } f$and$\bar { \kappa } _ { \gamma } \bar { f }$follow analogously, thus concluding the proof.□

Remark 6.17 The condition α$\wedge \eta > - \mathfrak { m }$is only required in order to be able to apply Proposition 6.9. There are some situations in which, even though α$\wedge \eta < - \mathfrak { m }$, there exists a canonical element$\mathcal { R } f \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha \wedge \eta }$extending$\begin{array} { r } { \tilde { \mathcal { R } } f . } \end{array}$In such a case, Proposition 6.16 still holds and the bound (6.20) holds provided that the corresponding bound holds for $\mathcal { R } f - \bar { \mathcal { R } } \bar { f } .$

## 7 Solutions to semilinear (S)PDEs

In order to solve a typical semilinear PDE of the type

$$
\partial_ {t} u = A u + F (u), \qquad u (0) = u _ {0},
$$

a standard methodology is to rewrite it in its mild form as

$$
u (t) = S (t) u _ {0} + \int_ {0} ^ {t} S (t - s) F (u (s)) d s,
$$

where$S ( t ) = e ^ { A t }$is the semigroup generated by A. One then looks for some family of spaces$\mathcal { X } _ { T }$of space-time functions (with$\mathcal { X } _ { T }$containing functions up to time$T )$such that the map given by

$$
(\mathcal {M} u) (t) = S (t) u _ {0} + \int_ {0} ^ {t} S (t - s) F (u (s)) d s,
$$

is a contraction in$\mathcal { X } _ { T } ,$, provided that the terminal time$T$is sufficiently small.$( \mathrm { A s }$soon as$F$is nonlinear, the notion of “sufficiently small” typically depends on the choice of $u _ { 0 } ,$, thus leading to a local solution theory.) The main step of such an argument is to show that the linear map$S$given by

$$
(S v) (t) = \int_ {0} ^ {t} S (t - s) v (s) d s,
$$

can be made to have arbitrarily small norm as$T  0$as a map from some suitable space$\mathcal { \ V } _ { T }$into$\mathcal { X } _ { T }$, where$\mathcal { { V } } _ { T }$is chosen such that F is then locally Lipschitz continuous as a map from$\mathcal { X } _ { T }$to$\mathcal { { V } } _ { T }$, with some uniformity in$T \in ( 0 , 1 ]$, say.

The aim of this section is to show that, in many cases, this methodology can still be applied when looking for solutions in$\mathcal { D } _ { P } ^ { \gamma , \eta }$for suitable exponents$\gamma$and$\eta ,$and for suitable regularity structures allowing to formulate a fixed point map of the type of $\mathcal { M } _ { F }$. At this stage, all of our arguments are purely deterministic. However, they rely on a choice of model for the given regularity structure one works with, which in many interesting cases can be built using probabilistic techniques.

## 7.1 Short-time behaviour of convolution kernels

From now on, we assume that we work with$d - 1$spatial coordinates, so that the solution u we are looking for is a function on$\mathbf { R } ^ { d }$. (Or rather a subset of it.) In order to be able to reuse the results of Section 5, we also assume that$S ( t )$is given by an integral operator with kernel$G ( t , \cdot )$. For simplicity, assume that the scaling s and exponent$\beta$ are such that, as a space-time function, G furthermore satisfies the assumptions of Section 5. (Typically, one would actually write$G = K + R$, where R is smooth and a$K$satisfies the assumptions of Section 5. We will go into more details in Section 8 below.) In this section, time plays a distinguished role. We will therefore denote points in$\mathbf { R } ^ { d }$either by$( t , x )$with$t \in \mathbf { R }$and$x \in \bar { \mathbf { R } } ^ { d - 1 }$or by$z \in \mathbf { R } ^ { d }$, depending on the context.

In our setting, we have so far been working solely with modelled distributions defined on all of$\mathbf { R } ^ { d }$, so it not clear a priori how a map like S should be defined when acting on (possibly singular) modelled distributions. One natural way of reformulating it is by writing

$$
S v = G * \left(\boldsymbol {R} ^ {+} v\right),\tag{7.1}
$$

where$\pmb { R } ^ { + } : \mathbf { R } \times \mathbf { R } ^ { d - 1 }  \mathbf { R }$is given by$R ^ { + } ( t , x ) = 1$for$t > 0$and$R ^ { + } ( t , x ) = 0$ otherwise.

From now on, we always take$P \subset \mathbf { R } ^ { d }$to be the hyperplane defined by “time$0 ^ { \circ }$ namely$P = \{ ( t , x ) : t = 0 \}$, which has effective codimension${ \mathfrak { m } } = { \mathfrak { s } } _ { 1 }$. We then note that the obvious interpretation of$R ^ { + }$as a modelled distribution yields an element of $\mathcal { D } _ { P } ^ { \infty , \infty }$, whatever the details of the underlying regularity structure. Indeed, the second term in (6.2) always vanishes identically, while the first term is non-zero only for$\ell = 0$ in which case it is bounded for every choice of$\eta .$It then follows immediately from Proposition 6.12 that the map$v \mapsto R ^ { + }$v is always bounded as a map from$\mathcal { D } _ { P } ^ { \gamma , \eta }$into $\mathcal { D } _ { P } ^ { \gamma , \eta }$. Furthermore, this map does not even rely on a choice of product, since$R ^ { + }$is proportional to 1, which is always neutral for any product.

In order to avoid the problem of having to control the behaviour of functions at infinity, we will from now on assume that we have a symmetry group$\mathcal { S }$acting on$\mathbf { R } ^ { d }$ in such a way that

The time variable is left unchanged in the sense that there is an action$\tilde { T }$of$\mathcal { S }$ on$\mathbf { R } ^ { d - 1 }$such that$T _ { g } ( t , x ) = ( t , \tilde { T } _ { g } x )$

The fundamental domain K of the action$\tilde { T }$is compact in$\mathbf { R } ^ { d - 1 }$

We furthermore assume that$\mathcal { S }$acts on our regularity structure$\mathcal { T }$and that the model (Π, Γ) for$\mathcal { T }$is adapted to its action. All the modelled distributions considered in the remainder of this section will always be assumed to be symmetric, and when we write$\mathcal { D } ^ { \gamma } , \mathcal { D } _ { P } ^ { \gamma , \eta }$, etc, we always refer to the closed subspaces consisting of symmetric functions.

One final ingredient used in this section will be that the kernels arising in the context of semilinear PDEs are non-anticipative in the sense that

$$
t <   s \quad \Rightarrow \quad K ((t, x), (s, y)) = 0.
$$

We furthermore use the notations$O = [ - 1 , 2 ] \times \mathbf { R } ^ { d - 1 }$and$O _ { T } = ( - \infty , T ] \times \mathbf { R } ^ { d - 1 }$ Finally, we will use the shorthands$\| \cdot \| _ { \gamma , \eta ; T }$as a shorthand for$\Vert \cdot \Vert _ { \gamma , \eta ; O _ { T } }$, and similarly for$\| \cdot \| _ { \gamma ; T }$. The backbone of our argument is then provided by Proposition 3.31 which guarantees that one can give bounds on$\kappa _ { \gamma } f$on$O _ { T }$, solely in terms of the behaviour of f on$O _ { T }$

With all of these preliminaries in place, the main result of this subsection is the following.

Theorem 7.1 Let$\gamma > 0$and let K be a non-anticipative kernel satisfying Assumptions 5.1 and 5.4for some$\beta > 0$and$r > \gamma + \beta .$Assume furthermore that the regularity structure$\mathcal { T }$comes with an integration map of order β acting on some sector V of regularity$\alpha > - \mathfrak { s } _ { 1 }$and assume that the models$Z = ( \Pi , \Gamma )$and$\bar { Z } = ( \bar { \Pi } , \bar { \Gamma } )$both realise$K f o r \mathcal { T }$on$V .$. Then, there exists a constant$C$such that, for every$T \in ( 0 , 1 ]$ the bounds

$$
\begin{array}{c} \| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f \| _ {\gamma + \beta , \bar {\eta}; T} \leq C T ^ {\kappa / \mathfrak {s} _ {1}} \| f \| _ {\gamma , \eta ; T}, \\ \| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f; \bar {\mathcal {K}} _ {\gamma} \boldsymbol {R} ^ {+} \bar {f} \| _ {\gamma + \beta , \bar {\eta}; T} \leq C T ^ {\kappa / \mathfrak {s} _ {1}} (\| f; \bar {f} \| _ {\gamma , \eta ; T} + \| Z, \bar {Z} \| _ {\gamma ; O}), \end{array}
$$

hold, provided that$f \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V ; \Gamma )$and$\bar { f } \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V ; \bar { \Gamma } )$for some$\eta > - \mathfrak { s } _ { 1 }$. Here,$\bar { \eta }$ and κ are such that$\bar { \eta } = ( \eta \wedge \alpha ) + \beta - \kappa$and$\kappa > 0$

In the first bound, the proportionality constant depends only on$\| Z \| _ { \gamma ; O }$, while in the second bound it is also allowed to depend on$\| f \| _ { \gamma , \eta ; T } + \| \bar { f } \| _ { \gamma , \eta ; T }$

One of main ingredients of the proof is the fact that$( \mathcal { K } _ { \gamma } R _ { + } f ) ( t , x )$is well-defined using only the knowledge of f up to time t. This is a consequence of the following result, which is an improved version of Lemma$6 . 7$

Proposition 7.2 In the setting of Lemma$6 . 7 ,$and assuming that$\varphi ( 0 ) \neq 0 ,$, one has the improved bound

$$
| (\mathcal {R} f - \Pi_ {x} f (x)) (\psi_ {x} ^ {\lambda}) | \lesssim \lambda^ {\gamma} \sup _ {y, z \in \operatorname{supp}} \sup _ {\psi_ {x} ^ {\lambda}} \frac {\| f (x) - \Gamma_ {x y} f (y) \| _ {\ell}}{\| x - y \| _ {\mathfrak {s}} ^ {\gamma - \ell}},\tag{7.2}
$$

where the proportionality constant is as in Lemma$6 . 7 .$

Proof. Since the statement is linear in$f ,$we can assume without loss of generality that the right hand side of (7.2) is equal to 1. Let$\varphi$be the scaling function of a wavelet basis of$\mathbf { R } ^ { d }$and let$\varphi _ { y } ^ { n }$be defined by

$$
\varphi_ {y} ^ {n} (z) = \varphi \big (\mathcal {S} _ {\mathfrak {s}} ^ {2 ^ {- n}} (z - x) \big).
$$

Note that this is slightly different from the definition of the$\varphi _ { y } ^ { n , s }$in Section 3.1! The reason for this particular scaling is that it ensures that$\begin{array} { r } { \sum _ { y \in \Lambda _ { n } ^ { \mathfrak { s } } } \varphi _ { y } ^ { n } ( z ) = 1 } \end{array}$. Again, we have coefficients$a _ { k }$such that, similarly to (3.13),

$$
\varphi_ {y} ^ {n - 1} (z) = \sum_ {k \in \mathcal {K}} a _ {k} \varphi_ {y + 2 ^ {- n} k} ^ {n} (z),
$$

for some finite set${ \boldsymbol { \kappa } } \subset \mathbf { Z } ^ { d }$, and this time our normalisation ensures that$\textstyle \sum _ { k \in { \mathcal { K } } } a _ { k } = 1$

For every$n \geq 0 .$, define

$$
\Lambda_ {n} ^ {\psi} = \left\{y \in \Lambda_ {n} ^ {\mathfrak {s}}: \operatorname{supp} \varphi_ {y} ^ {n} \cap \operatorname{supp} \psi_ {x} ^ {\lambda} \neq \emptyset \right\},
$$

and, for any$y \in \Lambda _ { n } ^ { \psi } .$, we denote by$y | _ { n }$some point in the intersection of these two supports. There then exists some constant$C$depending only on our choice of scaling function such that$\| y - y \| _ { n } \| _ { \mathfrak { s } } \leq C 2 ^ { - n }$. Let now$R _ { n }$be defined by

$$
R _ {n} \stackrel {{\text { def }}} {{=}} \sum_ {y \in \Lambda_ {n} ^ {\psi}} (\mathcal {R} f - \Pi_ {y | _ {n}} f (y | _ {n})) (\psi_ {x} ^ {\lambda} \varphi_ {y} ^ {n})  ,
$$

and let$n _ { 0 }$be the smallest value such that$2 ^ { - n _ { 0 } } \leq \lambda$. It is then straightforward to see that one has

$$
| (\mathcal {R} f - \Pi_ {x} f (x)) (\psi_ {x} ^ {\lambda}) - R _ {n _ {0}} | = \Big | \sum_ {y \in \Lambda_ {n _ {0}} ^ {\psi}} (\Pi_ {x} f (x) - \Pi_ {y | _ {n}} f (y | _ {n})) (\psi_ {x} ^ {\lambda} \varphi_ {y} ^ {n}) \Big | \lesssim \lambda^ {\gamma}.\tag{7.3}
$$

Furthermore, using as in Section 3.1 the shortcut$z = y + 2 ^ { - n s } k$, one then has for every $n \geq 1$the identity

$$
\begin{array}{l} R _ {n - 1} = \sum_ {y \in \Lambda_ {n - 1} ^ {\psi}} \sum_ {k \in \mathcal {K}} a _ {k} (\mathcal {R} f - \Pi_ {y | _ {n - 1}} f (y | _ {n - 1})) (\psi_ {x} ^ {\lambda} \varphi_ {z} ^ {n}) \\ \quad = \sum_ {y \in \Lambda_ {n - 1} ^ {\psi}} \sum_ {k \in \mathcal {K}} a _ {k} (\mathcal {R} f - \Pi_ {z | _ {n}} f (z | _ {n})) (\psi_ {x} ^ {\lambda} \varphi_ {z} ^ {n}) \\ \quad + \sum_ {y \in \Lambda_ {n - 1} ^ {\psi}} \sum_ {k \in \mathcal {K}} a _ {k} (\Pi_ {z | _ {n}} f (z | _ {n}) - \Pi_ {y | _ {n - 1}} f (y | _ {n - 1})) (\psi_ {x} ^ {\lambda} \varphi_ {z} ^ {n}) \\ \quad = R _ {n} + \sum_ {y \in \Lambda_ {n - 1} ^ {\psi}} \sum_ {k \in \mathcal {K}} a _ {k} (\Pi_ {z | _ {n}} f (z | _ {n}) - \Pi_ {y | _ {n - 1}} f (y | _ {n - 1})) (\psi_ {x} ^ {\lambda} \varphi_ {z}^{n}). \end{array}\tag{7.4}
$$

Note now that, in (7.4), one has$\| z | _ { n } - y | _ { n - 1 } \| _ { 5 } \leq \tilde { C } 2 ^ { - n }$for some constant$\tilde { C }$. It furthermore follows from the scaling properties of our functions that if$n \geq n _ { 0 }$and $\tau \in T _ { \ell }$with$\| \tau \| = 1$, one has

$$
| (\Pi_ {y} \tau) (\psi_ {x} ^ {\lambda} \varphi_ {z} ^ {n}) | \lesssim \lambda^ {- | \mathfrak {s} |} 2 ^ {- \ell n - | \mathfrak {s} | n},
$$

with a proportionality constant that is uniform over all$y$and z such that$\| y - z \| _ { \mathfrak { s } } \le$ ${ \tilde { C } } 2 ^ { - n }$. As a consequence, each summand in the last term of$_ { ( 7 . 4 ) }$is bounded by some fixed multiple of$\lambda ^ { - | s | } 2 ^ { - \gamma n - | s | n }$. Since furthermore the number of terms in this sum is bounded by a fixed multiple of$( 2 ^ { n } \lambda ) ^ { | \mathfrak { s } | }$<sup>|</sup>, this yields the bound

$$
\left| R _ {n - 1} - R _ {n} \right| \lesssim 2 ^ {- \gamma n}.\tag{7.5}
$$

Finally, writing$S _ { n } ( \psi )$for the$2 ^ { - n }$-fattening of the support of$\psi _ { x } ^ { \lambda }$, we see that, as a consequence of Lemma 6.7 and using a similar argument to what we have just used to bound$R _ { n - 1 } - R _ { n }$, one has

$$
\left| R _ {n} \right| \lesssim 2 ^ {- \gamma n} \| f \| _ {\gamma ; S _ {n} (\psi)}.
$$

This is the only time that we use information on$f$(slightly) away from the support of$\psi _ { x } ^ { \lambda }$. This however is only used to conclude that li$\mathrm { n } _ { n  \infty } | R _ { n } | = 0$, and no explicit bound on this rate of convergence is required. Combining this with (7.5) and$( 7 . 3 )$, the stated bound follows.□

Proof of Theorem 7.1. First of all, we see that, as a consequence of Proposition 7.2, we can exploit the fact that K is non-anticipative to strengthen (6.20) to

$$
\| \mathcal {K} _ {\gamma} f; \bar {\mathcal {K}} _ {\gamma} \bar {f} \| _ {\bar {\gamma}, \bar {\eta}; T} \lesssim \| f; \bar {f} \| _ {\gamma , \eta ; T} + \| \Pi - \bar {\Pi} \| _ {\gamma ; O} + \| \Gamma - \bar {\Gamma} \| _ {\bar {\gamma}; O},\tag{7.6}
$$

in the particular case where furthermore$f ( t , x ) = 0$for$t < 0$and similarly for${ \bar { f } } .$Of course, a similar bound also holds for$\| \mathcal { K } _ { \gamma } f \| _ { \bar { \gamma } , \bar { \eta } ; T }$

The main ingredient of the proof is the following remark. Since, provided that $\eta > - \mathfrak { s } _ { 1 }$, we know that$R R ^ { + } f \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha \wedge \eta }$by Proposition 6.9, it follows that the quantity

$$
z \mapsto \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k} K (z, \bar {z}) (\mathcal {R R} ^ {+} f) (\bar {z}) d \bar {z},
$$

is continuous as soon as$| k | _ { \mathfrak { s } } < ( \alpha \wedge \eta ) + \beta _ { \mathfrak { s } }$. Furthermore, since$K$is non-anticipative and$\mathcal { R } R ^ { + } f \equiv 0$for negative times, this quantity vanishes there.

As a consequence, we can apply Lemma 6.5 which shows that the bound (7.6) can in this case be strengthened to the additional bounds

$$
\begin{array}{c} \sup _ {z \in O _ {T}} \sup _ {\ell <   \gamma + \beta} \frac {\| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f (z) \| _ {\ell}}{\| z \| _ {P} ^ {(\eta \wedge \alpha) + \beta - \ell}} \lesssim \| f \| _ {\gamma , \eta ; T}, \\ \sup _ {z \in O _ {T}} \sup _ {\ell <   \gamma + \beta} \frac {\| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f (z) - \bar {\mathcal {K}} _ {\gamma} \boldsymbol {R} ^ {+} \bar {f} (z) \| _ {\ell}}{\| z \| _ {P} ^ {(\eta \wedge \alpha) + \beta - \ell}} \lesssim \| f; \bar {f} \| _ {\gamma , \eta ; T} + \| Z, \bar {Z} \| _ {\gamma ; O}. \end{array}
$$

Since, for every$z , { \bar { z } } \in O _ { T }$, one has$\| z \| _ { P } \leq T ^ { 1 / { \mathfrak { s } } _ { 1 } }$as well as$\| z , \bar { z } \| _ { P } \leq T ^ { 1 / { \mathfrak { s } } _ { 1 } }$, we can combine these bounds with the definition of the norm$\| \cdot \| _ { \gamma + \beta , \bar { \eta } ; T }$to show that one has

$$
\| \mathcal {K} _ {\gamma} \boldsymbol {R} ^ {+} f \| _ {\gamma + \beta , \bar {\eta}; T} \lesssim T ^ {\kappa / \mathfrak {s} _ {1}} \| f \| _ {\gamma , \eta ; T},
$$

and similarly for$\| \mathcal { K } _ { \gamma } R ^ { + } f ; \bar { \mathcal { K } } _ { \gamma } R ^ { + } \bar { f } \| _ { \gamma + \beta , \bar { \eta } ; T }$, thus concluding the proof.

In all the problems we consider in this article, the Green’s function of the linear part of the equation, i.e. the kernel of${ \mathcal L } ^ { - 1 }$where$\mathcal { L }$is as in (1.2), can be split into a sum of two terms, one of which satisfies the assumptions of Section 5 and the other one of which is smooth (see Lemma 5.5). Given a smooth kernel$R \colon \mathbf { R } ^ { d } \times \mathbf { R } ^ { d }  \mathbf { R }$that is supported in$\{ ( z , \bar { z } ) : \| z - \bar { z } \| _ { \mathfrak { s } } \le L \}$for some$L > 0$, and a regularity structure$\mathcal { T }$ containing$\mathcal { T } _ { \mathfrak { s } , d }$as usual, we can define an operator$R _ { \gamma } \colon { \mathcal { C } } _ { \mathfrak { s } } ^ { \alpha }  { \mathcal { D } } ^ { \gamma }$by

$$
(R _ {\gamma} \xi) (z) = \sum_ {| k | _ {s} <   \gamma} \frac {X ^ {k}}{k !} \int_ {\mathbf {R} ^ {d}} D _ {1} ^ {k} R (z, \bar {z}) \xi (\bar {z}) d \bar {z}.\tag{7.7}
$$

(As usual, this integral should really be interpreted as$\xi ( D _ { 1 } ^ { k } R ( z , \cdot ) )$, but the above notation is much more suggestive.) The fact that this is indeed an element of$\mathcal { D } ^ { \gamma }$is a consequence of the fact that R is smooth in both variables, so that it follows from Lemma 2.12. The following result is now straightforward:

Lemma 7.3 Let R be a smooth kernel and consider a symmetric situation as above. If furthermore R is non-anticipative, then the bounds

$$
\begin{array}{c} \| R _ {\gamma} \mathcal {R} \boldsymbol {R} ^ {+} f \| _ {\gamma + \beta , \bar {\eta}; T} \leq C T \| f \| _ {\gamma , \eta ; T}, \\ \| R _ {\gamma} \mathcal {R} \boldsymbol {R} ^ {+} f; R _ {\gamma} \bar {\mathcal {R}} \boldsymbol {R} ^ {+} \bar {f} \| _ {\gamma + \beta , \bar {\eta}; T} \leq C T (\| f; \bar {f} \| _ {\gamma , \eta ; T} + \| Z; \bar {Z} \| _ {\gamma , O}), \end{array}
$$

holds uniformly over all$T \leq 1$

Proof. Since R is assumed to be non-anticipative, one has$( R _ { \gamma } \mathcal { R } R ^ { + } f ) ( t , x ) = 0$for every$t ~ \leq ~ 0$. Furthermore, the map$( t , x ) \mapsto ( R _ { \gamma } \mathcal { R } R ^ { + } f ) ( t , x )$is smooth (in the classical sense of a map taking values in a finite-dimensional vector space!), so that the claim follows at once. Actually, it would even be true with$T$replaced by an arbitrarily large power of$T$in the bound on the right hand side.□

## 7.2 The effect of the initial condition

One of the obvious features of PDEs is that they usually have some boundary data. In this article, we restrict ourselves to spatially periodic situations, but even such equations have some boundary data in the form of their initial condition. When they are considered in their mild formulation, the initial condition enters the solution to a semi-linear PDE through a term of the form$S ( t ) u _ { 0 }$for some function (or distribution)$u _ { 0 }$on $\mathbf { R } ^ { d - 1 }$and S the semigroup generated by the linear evolution.

All of the equations mentioned in the introduction are nonlinear perturbations of the heat equation. More generally, their linear part is of the form

$$
\mathcal {L} = \partial_ {t} - Q (\nabla_ {x}),
$$

where$Q$is a polynomial of even degree which is homogeneous of degree$2 q$for some scaling ¯s on$\bar { \mathbf { R } } ^ { d - 1 }$and some integer$q > 0$. (In our case, this would always be the Euclidean scaling and one has$q \ = \ 1 . )$In this case, the operator$\mathcal { L }$itself has the property that

$$
\mathcal {L} \mathcal {S} _ {\mathfrak {s}} ^ {\delta} \varphi = \delta^ {2 q} \mathcal {S} _ {\mathfrak {s}} ^ {\delta} \mathcal {L} \varphi .\tag{7.8}
$$

where s is the scaling on$\mathbf { R } ^ { d } = \mathbf { R } \times \mathbf { R } ^ { d - 1 }$given by${ \mathfrak { s } } = ( 2 q , { \bar { \mathfrak { s } } } )$. Denote by G the Green’s function$G$of  which is a distribution satisfying$\mathcal { L } G = \delta _ { 0 }$in the distributional sense and$G ( x , t ) = 0$for$t \leq 0$. Assuming that$\mathcal { L }$is such that these properties define G uniquely (which is the case if$\mathcal { L }$is hypoelliptic), it follows from (7.8) and the scaling properties of the Dirac distribution that$G$has exact scaling property

$$
G (\mathcal {S} _ {\mathfrak {s}} ^ {\delta} z) = \delta^ {| \overline {{\mathfrak {s}}} |} G (z),\tag{7.9}
$$

which is precisely of the form (5.7) with$\beta = 2 q$. Under well-understood assumptions on$Q , { \mathcal { L } }$is known to be hypoelliptic [H¨or55], so that its Green’s function$G$is smooth. In this case, the following lemma applies.

Lemma 7.4 If G satisfies (7.9), is non-anticipative, and is smooth then there exists a smoothfunction$\hat { G } \colon  { \mathbf { R } } ^ { d } \to  { \mathbf { R } }$such that one has the identity

$$
G (x, t) = t ^ {- \frac {| \bar {\mathfrak {s}} |}{2 q}} \hat {G} (\mathcal {S} _ {\bar {\mathfrak {s}}} ^ {t ^ {1 / 2 q}} x),\tag{7.10}
$$

and such that,for every$( d - 1 )$-dimensional multiindex k and every$n > 0$, there exists a constant C such that the bound

$$
\left| D ^ {k} \hat {G} (y) \right| \leq C \left(1 + | y | ^ {2}\right) ^ {- n},\tag{7.11}
$$

holds uniformly over$y \in \mathbf { R } ^ { d - 1 }$

Proof. The existence of$\hat { G }$such that (7.10) holds follows immediately from the scaling property (7.9). The bound (7.11) can be obtained by noting that, since G is smooth off the origin and satisfies$G ( x , t ) = 0$for$t \leq 0 ,$one has, for every$n > 0$, a bound of the type

$$
\left| D _ {x} ^ {k} G (x, t) \right| \lesssim t ^ {n},\tag{7.12}
$$

uniformly over all$x \in \mathbf { R } ^ { d - 1 }$with$\| x \| _ { \bar { s } } = 1$. It follows from (7.10) that

$$
D ^ {k} G (x, t) = t ^ {- \frac {| \bar {s} | + | k | _ {\bar {s}}}{2 q}} (D ^ {k} \hat {G}) (\mathcal {S} _ {\bar {s}} ^ {t ^ {1 / 2 q}} x)  .
$$

Setting$y = S _ { \bar { s } } ^ { t ^ { 1 / 2 q } }$x and noting that$\| y \| _ { \bar { \mathfrak { s } } } = 1 / t ^ { 1 / 2 q } \operatorname { i f } \| x \| _ { \bar { \mathfrak { s } } } = 1$, it remains to combine this with (7.12) to obtain the required bound.□

Given a function (or distribution)$u _ { 0 }$on$\mathbf { R } ^ { d - 1 }$with sufficiently nice behaviour at infinity, we now denote by$G u _ { 0 }$its “harmonic extension”, given by

$$
(G u _ {0}) (x, t) = \int_ {\mathbf {R} ^ {d - 1}} G (x - y, t)   u _ {0} (y)   d y  .\tag{7.13}
$$

(Of course this is to be suitably interpreted when$u _ { 0 }$is a distribution.) This expression does define a function of$( t , x )$which, thanks to Lemma 7.4, is smooth everywhere except at$t = 0$. As in Section 2.2, we can lift$G u _ { 0 }$at every point to an element of the model space T (provided of course that$\mathcal { T } _ { d , \mathfrak { s } } \subset \mathcal { T }$which we always assume to be the case) by considering its truncated Taylor expansion. We will from now on use this point of view without introducing a new notation.

We can say much more about the function$G u _ { 0 }$, namely we can find out precisely to which spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$it belongs. This is the content of the following Lemma, variants of which are commonplace in the PDE literature. However, since our spaces are not completely standard and since it is very easy to prove, we give a sketch of the proof here.

Lemma 7.5 Let$u _ { 0 } \in \mathcal { C } _ { \bar { \mathfrak { s } } } ^ { \alpha } ( \mathbf { R } ^ { d - 1 } )$) be periodic. Then, for every α$\notin \mathbf { N } ,$the function $v = G u _ { 0 }$defined in$( 7 . I 3 )$belongs to$\mathcal { D } _ { P } ^ { \gamma , \alpha }$for every$\gamma > ( \alpha \lor 0 )$

Proof. We first aim to bound the various directional derivatives of v. In the case$\alpha < 0$ it follows immediately from the scaling and decay properties of$G ,$, combined with the definition of$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$that, for any fixed$( t , x )$, one has the bound

$$
| (G u _ {0}) (x, t) | \lesssim t ^ {\frac {\alpha}{2}},
$$

valid uniformly over x (by the periodicity of$u _ { 0 } )$and over$t \in ( 0 , 1 ]$. As a consequence (exploiting the fact that, as an operator,$G$commutes with all spatial derivatives and that one has the identity$\partial _ { t } G u _ { 0 } = Q ( \nabla _ { x } ) G u _ { 0 } )$, one also obtains the bound

$$
| (D ^ {k} G u _ {0}) (x, t) | \lesssim t ^ {\frac {\alpha - | k | _ {\mathfrak {s}}}{2}},\tag{7.14}
$$

where k is any d-dimensional multiindex (i.e. we also admit time derivatives).

For$\alpha > 0$, we use the fact that elements in$\mathcal { C } _ { \bar { \mathfrak { s } } } ^ { \alpha }$can be characterised recursively as those functions whose kth distributional derivatives belong to${ \mathcal C } _ { \bar { \mathfrak { s } } } ^ { \alpha - | k | _ { \bar { \mathfrak { s } } } }$. It follows that the bound (7.14) then still holds for$| k | _ { \mathfrak { s } } > \alpha$, while one has$| ( \tilde { D } ^ { k } G u _ { 0 } ) ( x , t ) | \lesssim 1$for $| k | _ { s } < \alpha$. This shows that the first bound in (6.2) does indeed hold for every integer value ℓ as required.

In this particular case, the second bound in (6.2) is then an immediate consequence of the first by making use of the generalised Taylor expansion from Proposition A.1. Since the argument is very similar to the one already used for example in the proof of Lemma 5.18, we omit it here.□

Starting from a Green’s function$G$as above, we would like to apply the theory developed in Section 5. From now on, we will assume that we are in the situation where we have a symmetry given by a discrete subgroup$\mathcal { S }$of the group of isometries of$\mathbf { R } ^ { d - 1 }$with compact fundamental domain${ \mathcal { R } } .$. This covers the case of periodic boundary conditions, when$\mathcal { S }$is a subgroup of the group of translations, but it also covers Neumann boundary conditions in the case where$\mathcal { S }$is a reflection group.

Remark 7.6 One could even cover Dirichlet boundary conditions by reflection, but this would require a slight modification of Definition 3.33. In order to simplify the exposition, we refrain from doing so.

To conclude this subsection, we show how, in the presence of a symmetry with compact fundamental domain, a Green’s function$G$as above can be decomposed in a way similar to Lemma 5.5, but such that R is also compactly supported. We assume therefore that we are given a symmetry$\mathcal { S }$acting on$\mathbf { R } ^ { d - 1 }$with compact fundamental domain and that$G$respects this symmetry in the sense that, for every$g \in \mathcal { S }$acting on $\mathbf { R } ^ { d - 1 }$via an isometry$T _ { g } \colon x \mapsto A _ { g } x + b _ { g }$, one has the identity$G ( t , x ) = G ( t , A _ { g } x )$ We then have the following result:

Lemma 7.7 Let$G$and$\mathcal { S }$be as above. Then, there existfunctions K and R such that the identity

$$
(G * u) (z) = (K * u) (z) + (R * u) (z),\tag{7.15}
$$

holds for every symmetric function u supported in$\mathbf { R } _ { + } \times \mathbf { R } ^ { d - 1 }$and every$z \in ( - \infty , 1 ] \times$ $\mathbf { R } ^ { d - 1 }$

Furthermore, K is non-anticipative and symmetric, and satisfies Assumption 5.1 with$\beta = 2 q ,$, as well as Assumption 5.4 for some arbitrary (but fixed) value r. The function R is smooth, symmetric, non-anticipative, and compactly supported.

Proof. It follows immediately from Lemmas 5.5 and 5.24 that one can write

$$
G = K + \bar {R},
$$

where$K$has all the required properties, and$\bar { R }$is smooth, non-anticipative, and symmetric. Since u is supported on positive times and we only consider (7.15) for times $t \leq 1$, we can replace R<sup>¯</sup> by any function$\tilde { R }$which is supported in$\{ ( t , x ) : t \leq 2 \}$say, and such that$\tilde { R } ( t , x ) = \bar { R } ( t , x )$for$t \leq 1$

It remains to replace R<sup>˜</sup> by a kernel R which is compactly supported. It is wellknown [Bie11, Bie12] that any crystallographic group$\mathcal { S }$can be written as the skewproduct of a (finite) crystallographic point group$\mathcal { G }$with a lattice Γ of translations. We then fix a function$\varphi \colon \mathbf { R } ^ { d - 1 } \to [ 0$, 1] which is compactly supported in a ball of radius $C _ { \varphi }$around the origin and such that$\textstyle \sum _ { k \in \Lambda } \varphi ( x + k ) = 1$for every x. Since elements in PG leave the lattice Λ invariant, the same property holds true for the maps$x \mapsto \varphi ( A x )$ for every$A \in { \mathcal { G } }$

It then suffices to set

$$
R (t, x) = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} \sum_ {k \in \Lambda} \tilde {R} (t, x + k) \varphi (A x).
$$

The fact that R is compactly supported follows from the same property for$\varphi .$Furthermore, the above sum converges to a smooth function by Lemma 7.4. Also, using the fact that u is invariant under translations by elements in Λ by assumption, it is straightforward to verify that R<sup>˜</sup>$u = R * u$as required. Finally, for any$A _ { 0 } \in { \mathcal { G } }$, one has

$$
\begin{array}{l} R (t, A _ {0} x) = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} \sum_ {k \in \Lambda} \tilde {R} (t, A _ {0} x + k) \varphi (A A _ {0} x) \\ = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} \sum_ {k \in \Lambda} \tilde {R} (t, A _ {0} (x + k)) \varphi (A x) \\ = \frac {1}{| \mathcal {G} |} \sum_ {A \in \mathcal {G}} \sum_ {k \in \Lambda} \tilde {R} (t, x + k) \varphi (A x) = R (t, x), \end{array}
$$

so that$R$is indeed symmetric for${ \mathcal { S } }$. Here, we first exploited the fact that elements of $\mathcal { G }$leave the lattice Λ invariant, and then used the symmetry of${ \tilde { R } } .$□

## 7.3 A general fixed point map

We have now collected all the ingredients necessary for the proof of the following result, which can be viewed as one of the main abstract theorems of this article. The setting for our result is the following. As before, we assume that we have a crystallographic group$\mathcal { S }$acting on$\mathbf { R } ^ { d - 1 }$. We also write$\mathbf { R } ^ { d } = \mathbf { R } \times \mathbf { R } ^ { d - 1 }$, endow$\mathbf { R } ^ { d }$with a scaling s, and extend the action of$\mathcal { S }$to$\mathbf { R } ^ { d }$in the obvious way. Together with this data, we assume that we are given a non-anticipative kernel$G \colon \mathbf { R } ^ { d } \backslash 0  \mathbf { R }$that is smooth away from the origin, preserves the symmetry$\mathcal { S }$, and is scale-invariant with exponent$\beta - | \mathfrak { s } |$ for some fixed$\beta > 0$

Using Lemma$7 . 7 ,$we then construct a singular kernel K and a smooth compactly supported function R on$\mathbf { R } ^ { d }$such that (7.15) holds for symmetric functions u that are supported on positive times. Here, the kernel K is assumed to be again non-anticipative and symmetric, and it is chosen in such a way that it annihilates all polynomials of some arbitrary (but fixed) degree$r > 0$. We then assume that we are given a regularity structure$\mathcal { T }$containing$\mathcal { T } _ { s , d }$such that$\mathcal { S }$acts on it, and which is endowed with an abstract integration map of order$2 q \in \mathbf { N }$. (The domain of$\mathcal { T }$will be specified later.) We also assume that we have abstract differentiation maps$\mathcal { D } _ { i }$which are covariant with respect to the symmetry$\mathcal { S }$as in Remark 5.30. We also denote by$\mathcal { M } _ { \mathcal { T } } ^ { r }$the set of all models for$\mathcal { T }$which realise$K$on$T _ { r } ^ { - }$. As before, we denote by$\kappa _ { \gamma }$the concrete integration map against$K$acting on$\mathcal { D } ^ { \gamma }$and constructed in Section 5, and by$R _ { \gamma }$the integration map against R constructed in$( 7 . 7 )$

Finally, we denote by$P = \left\{ ( t , x ) \in \mathbf { R } \times \mathbf { R } ^ { d - 1 } : t = 0 \right\}$the “time$0 ^ { \circ }$hyperplane and we consider the spaces$\mathcal { D } _ { P } ^ { \gamma , \eta }$as in Section 6. Given$\gamma \geq \bar { \gamma } > 0$, a map$\bar { F } \colon \bar { \mathbf { R } } ^ { d } \times$ $T _ { \gamma }  T _ { \bar { \gamma } }$, and a map$f \colon \mathbf R ^ { d } \to T _ { \gamma }$, we denote by$F ( f )$the map given by

$$
(F (f)) (z) \stackrel {\text { def }} {=} F (z, f (z)).\tag{7.16}
$$

If it so happens that, via (7.16), F maps$\mathcal { D } _ { P } ^ { \gamma , \eta }$into$\mathcal { D } _ { P } ^ { \bar { \gamma } , \bar { \eta } }$for some$\eta , { \bar { \eta } } \in \mathbf { R }$, we say that $F$is locally Lipschitz if, for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$and every$R > 0$, there exists a constant$C > 0$such that the bound

$$
\left\| F (f) - F (g) \right\| _ {\bar {\gamma}, \bar {\eta}; \mathfrak {K}} \leq C \| f - g \| _ {\gamma , \eta ; \mathfrak {K}},
$$

holds for every$f , g \in \mathcal { D } _ { P } ^ { \gamma , \eta }$with$\| f \| _ { \gamma , \eta ; \mathbb { R } } + \| g \| _ { \gamma , \eta ; \mathbb { R } } \le R$, as well as for all models $Z$with$\| Z \| _ { \gamma ; \mathfrak { R } } \le R$. We also impose that the similar bound

$$
\llbracket F (f) - F (g) \rrbracket_ {\bar {\gamma}, \bar {\eta}; \mathfrak {K}} \leq C \llbracket f - g \rrbracket_ {\gamma , \eta ; \mathfrak {K}},\tag{7.17}
$$

holds.

We say that it is strongly locally Lipschitz if furthermore

$$
\left\| F (f); F (g) \right\| _ {\bar {\gamma}, \bar {\eta}; \mathfrak {K}} \leq C \left(\left\| f; g \right\| _ {\gamma , \eta ; \mathfrak {K}} + \left\| Z - \bar {Z} \right\| _ {\gamma ; \bar {\mathfrak {K}}}\right),
$$

for any two models$Z , { \bar { Z } }$with$\| Z \| _ { \gamma ; \bar { \mathfrak { R } } } + \| \bar { Z } \| _ { \gamma ; \bar { \mathfrak { R } } } \le R$, where this time$f \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( Z )$ $g \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( \bar { Z } )$, and K<sup>¯</sup> denotes the 1-fattening of K. Finally, given an open interval$I \subset \mathbf { R }$ we use the terminology

$$
\text { `` } u = \mathcal {K} _ {\gamma} v \quad \text { on } \quad I \quad \text { '' }
$$

to mean that the identity$u ( t , x ) = ( K _ { \gamma } v ) ( t , x )$holds for every$t \in I$and$x \in \mathbf { R } ^ { d - 1 }$ and that for those values of$( t , x )$the quantity$( \boldsymbol { \mathcal { K } } _ { \gamma } \boldsymbol { v } ) ( t , \boldsymbol { x } )$only depends on the values $v ( s , y )$for$s \in I$and$y \in \mathbf { R } ^ { d - 1 }$

With all of this terminology in place, we then have the following general result.

Theorem 7.8 Let V and$\bar { V }$be two sectors of a regularity structure$\mathcal { T }$with respective regularities$\zeta , \bar { \zeta } \in \mathbb { R }$with$\zeta \leq \bar { \zeta } + 2 q .$. In the situation described above, for some $\gamma \geq \bar { \gamma } > 0$and some$\eta \in \mathbf { R } ,$let$F \colon \mathbf { R } ^ { d } \times V _ { \gamma }  \bar { V } _ { \bar { \gamma } }$be a smooth function such that, $i f f \in \mathcal { D } _ { P } ^ { \gamma , \eta }$is symmetric with respect to${ \mathcal { S } } ,$then$F ( f )$, defined by$( 7 . I 6 ) ,$, belongs to $\mathcal { D } _ { P } ^ { \bar { \gamma } , \bar { \eta } }$and is also symmetric with respect to${ \mathcal { S } } .$. Assume furthermore that we are given an abstract integration map$\mathcal { T }$as above such that$\mathcal { Q } _ { \gamma } ^ { - } \bar { \mathcal { Z } } \bar { V } _ { \bar { \gamma } } \subset V _ { \gamma }$

$I f \eta < ( \bar { \eta } \wedge \bar { \zeta } ) + 2 q , \gamma < \bar { \gamma } + 2 q , ( \bar { \eta } \wedge \bar { \zeta } ) > - 2 q ,$and F is locally Lipschitz then,for every$v \in \mathcal { D } _ { P } ^ { \gamma , \eta }$which is symmetric with respect to${ \mathcal { S } } _ { : }$, andfor every symmetric model $Z = ( \Pi , \Gamma ) \dot { f } o r$the regularity structure$\mathcal { T }$such that is adapted to the kernel$K ,$, there exists a time$T > 0$such that the equation

$$
u = (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} F (u) + v  ,\tag{7.18}
$$

admits a unique solution$u \in \mathcal { D } _ { P } ^ { \gamma , \eta }$on$( 0 , T )$. The solution map$S _ { T } \colon ( v , Z ) \mapsto u$is jointly continuous in a neighbourhood around$( v , Z )$in the sense that, for every fixed v and$Z$as above, as well as any$\varepsilon > 0 ,$, there exists$\delta > 0$such that, denoting by u¯ the solution to thefixed point map with data v¯ and${ \bar { Z } } ,$, one has the bound

$$
\left\| u; \bar {u} \right\| _ {\gamma , \eta ; T} \leq \varepsilon  ,
$$

provided that$\begin{array} { r } { \| Z ; \bar { Z } \| _ { \gamma ; O } + \| v ; \bar { v } \| _ { \gamma , \eta ; T } \leq \delta . } \end{array}$

If furthermore$F$is strongly locally Lipschitz then the map$( v , Z ) \mapsto u$is jointly Lipschitz continuous in a neighbourhood around$( v , Z )$in the sense that$\delta$can locally be chosen proportionally to ε in the bound above.

Proof. We first consider the case of a fixed model$Z = ( \Pi , \Gamma )$, so that the space$\mathcal { D } _ { P } ^ { \gamma , \eta }$ (defined with respect to the given multiplicative map Γ) is a Banach space. In this case, denote by$\mathcal { M } _ { F } ^ { Z } ( u )$the right hand side of (7.18). Note that, even though$\mathcal { M } _ { F } ^ { Z }$appears not to depend on$Z$at first sight, it does so through the definition of$\kappa _ { \bar { \gamma } }$

It follows from Theorem 7.1 and Lemma$7 . 3 ,$, as well as our assumptions on the exponents$\gamma , \bar { \gamma } , \eta$and η¯ that there exists$\kappa > 0$such that one has the bound

$$
\left\| \mathcal {M} _ {F} ^ {Z} (u) - \mathcal {M} _ {F} ^ {Z} (\bar {u}) \right\| _ {\gamma , \eta ; T} \lesssim T ^ {\kappa} \left\| F (u) - F (\bar {u}) \right\| _ {\bar {\gamma}, \bar {\eta}; T}.
$$

It follows from the local Lipschitz continuity of$F$that, for every$R > 0$, there exists a constant$C > 0$such that

$$
\| \mathcal {M} _ {F} ^ {Z} (u) - \mathcal {M} _ {F} ^ {Z} (\bar {u}) \| _ {\gamma , \eta ; T} \leq C T ^ {\kappa} \| u - \bar {u} \| _ {\gamma , \eta ; T},
$$

uniformly over$T \in ( 0 , 1 ]$and over all u and u¯ such that$\| u \| _ { \gamma , \eta ; T } + \| \bar { u } \| _ { \gamma , \eta ; T } \le R$ Similarly, for every$R > 0$, there exists a constant$C > 0$such that one has the bound

$$
\left\| \mathcal {M} _ {F} ^ {Z} (u) \right\| _ {\gamma , \eta ; T} \leq C T ^ {\kappa} + \left\| v \right\| _ {\gamma , \eta ; T}.
$$

As a consequence, as soon as$\| v \| _ { \gamma , \eta ; T }$is finite and provided that$T$is small enough $\mathcal { M } _ { F } ^ { Z }$maps the ball of radius$\| v \| _ { \gamma , \eta ; T } + 1$in$\mathcal { D } _ { P } ^ { \gamma , \eta }$into itself and is a contraction there, so that it admits a unique fixed point. The fact that this is also the unique global fixed point for$\mathcal { M } _ { F } ^ { Z }$follows from a simple continuity argument similar to the one given in the proof of Theorem 4.8 in [Hai13].

For a fixed model Z, the local Lipschitz continuity of the map v  u for sufficiently small$T$is immediate. Regarding the dependency on the model$Z ,$we first consider the simpler case where$F$is assumed to be strongly Lipschitz continuous. In this case, the same argument as above yields the bound

$$
\left\| \mathcal {M} _ {F} ^ {Z} (u); \mathcal {M} _ {F} ^ {\bar {Z}} (\bar {u}) \right\| _ {\gamma , \eta ; T} \leq C T ^ {\kappa} \big (\left\| u; \bar {u} \right\| _ {\gamma , \eta ; T} + \left\| Z; \bar {Z} \right\| _ {\gamma ; O} \big)  ,
$$

so that the claim follows at once.

It remains to show that the solution is also locally uniformly continuous as a function of the model$Z$in situations where$F$is locally Lipschitz continuous, but not in the strong sense. Given a second model$\bar { Z } = ( \bar { \Pi } , \bar { \Gamma } )$, we denote by u¯ the corresponding solution to (7.18). We assume that$\bar { Z }$is sufficiently close to$Z$so that both$\mathcal { M } _ { F } ^ { Z }$ and$\mathcal { M } _ { F } ^ { \bar { Z } }$are strict contractions on the same ball. We also use the shorthand notations $u ^ { ( n ) } = ( \mathcal { M } _ { F } ^ { Z } ) ^ { n } ( 0 )$and$\bar { u } ^ { ( n ) } = ( \mathcal { M } _ { F } ^ { \bar { Z } } ) ^ { n } ( 0 )$. Using the strict contraction property of the two fixed point maps, we have the bound

$$
\begin{array}{c} \| u - \bar {u} \| _ {\gamma , \eta ; T} \lesssim \| u - u ^ {(n)} \| _ {\gamma , \eta ; T} + \| u ^ {(n)} - \bar {u} ^ {(n)} \| _ {\gamma , \eta ; T} + \| \bar {u} ^ {(n)} - \bar {u} \| _ {\gamma , \eta ; T} \\ \lesssim \varrho^ {n} + [   [ u ^ {(n)} - \bar {u} ^ {(n)} ]   ] _ {\gamma , \eta ; T}, \end{array}
$$

for some constant$\varrho < 1$. As a consequence of Lemma 6.5, Lemma$6 . 6 , ( 7 . 1 7 )$, Proposition$6 . 1 6 ,$and using the fact that there is a little bit of “wiggle room” between$\gamma$and $\bar { \gamma } + 2 q$, we obtain the existence of a constant$\kappa > 0$such that one has the bound

$$
\llbracket u ^ {(n)} - \bar {u} ^ {(n)} \rrbracket_ {\gamma , \eta ; T} \lesssim \| \mathcal {M} _ {F} ^ {Z} (u ^ {(n - 1)}); \mathcal {M} _ {F} ^ {\bar {Z}} (\bar {u} ^ {(n - 1)}) \| _ {\gamma , \eta ; T}
$$

$$
\begin{array}{l} \lesssim \| F (u ^ {(n - 1)}); F (\bar {u} ^ {(n - 1)}) \| _ {\bar {\gamma} - \kappa , \bar {\eta}; T} + \| Z; \bar {Z} \| _ {\gamma ; O} \\ \lesssim \llbracket F (u ^ {(n - 1)}) - F (\bar {u} ^ {(n - 1)}) \rrbracket_ {\bar {\gamma}, \bar {\eta}; T} ^ {\kappa} + \| Z; \bar {Z} \| _ {\gamma ; O} \\ \lesssim \llbracket u ^ {(n - 1)} - \bar {u} ^ {(n - 1)} \rrbracket_ {\gamma , \eta ; T} ^ {\kappa} + \| Z; \bar {Z} \| _ {\gamma ; O}  , \end{array}
$$

uniformly in$n .$By making$T$sufficiently small, one can furthermore ensure that the proportionality constant that in principle appears in this bound is bounded by 1. Since $\bar { u } ^ { 0 } = \bar { u } ^ { 0 }$, we can iterate this bound n times to obtain

$$
\| u ^ {(n)} - \bar {u} ^ {(n)} \| _ {\gamma , \eta ; T} \lesssim \| Z; \bar {Z} \| _ {\gamma ; O} ^ {\kappa^ {n}},
$$

with a proportionality constant that is bounded uniformly in n. Setting$\varepsilon = \| Z ; { \bar { Z } } \| _ { \gamma ; O }$ a simple calculation shows that the term$\varrho ^ { n }$and the term$\varepsilon ^ { \kappa ^ { n } }$are of (roughly) the same order when n log$\log \varepsilon ^ { - 1 }$, which eventually yields a bound of the type

$$
\| u; \bar {u} \| _ {\gamma , \eta ; T} \lesssim | \log \| Z; \bar {Z} \| _ {\gamma ; O} | ^ {- \nu},
$$

for some exponent$\nu > 0$, uniformly in a small neighbourhood of any initial condition and any model$Z .$While this bound is of course suboptimal in many situations, it is sufficient to yield the joint continuity of the solution map for a very large class of nonlinearities.□

Remark 7.9 The condition$( \bar { \eta } \wedge \zeta ) > - 2 q$is required in order to be able to apply Proposition 6.16. Recall however that the assumptions of that theorem can on occasion be slightly relaxed, see Remark 6.17. The relevant situation in our context is when$F$ can be rewritten as$F ( z , u ) = F _ { 0 } ( z , u ) + F _ { 1 } ( z )$, where$F _ { 0 }$satisfies the assumption of our theorem, but$F _ { 1 }$does not. If we then make sense of$( \mathcal { K } _ { \bar { \gamma } } + \mathcal { R } _ { \gamma } \mathcal { R } ) R ^ { + } F _ { 1 }$“by hand” as an element of$\mathcal { D } _ { P } ^ { \gamma , \eta }$and impose sufficient restrictions on our model$Z$such that this element is continuous as a function of$Z ,$, then we can absorb it into v so that all of our conclusions still hold.

Remark 7.10 In many situations, the map$F$has the property that

$$
\mathcal {Q} _ {\zeta + 2 q} ^ {-} \tau = \mathcal {Q} _ {\zeta + 2 q} ^ {-} \bar {\tau} \quad \Rightarrow \quad \mathcal {Q} _ {\zeta + 2 q} ^ {-} F (z, \tau) = \mathcal {Q} _ {\zeta + 2 q} ^ {-} F (z, \bar {\tau}).\tag{7.19}
$$

Denote as before by$\bar { T } \subset T$the sector spanned by abstract polynomials. Then, provided that (7.19) holds, for every$z \in \mathbf { R } ^ { d }$and every$v \in \bar { T }$, the equation

$$
\tau = \mathcal {Q} _ {\gamma} ^ {-} (\mathcal {I F} (z, \tau) + v),
$$

admits a unique solution$\mathfrak { F } ( z , v )$in$V .$. Indeed, it follows from the properties of the abstract integration map$\mathcal { T } ,$combined with (7.19), that there exists$n > 0$such that the map$F _ { z , v } : \tau \mapsto \mathcal { Q } _ { \gamma } ^ { - } ( \mathcal { T } F ( z , \tau ) + v )$has the property that$F _ { z , v } ^ { n + 1 } ( \tau ) = F _ { z , v } ^ { n } ( \tau )$

It then follows from the definitions of the operations appearing in (7.21) that, if we denote by <sup>¯</sup>u the component of u in$\bar { T } ,$one has the identity

$$
u (t, x) = \mathfrak {F} \big ((t, x), \bar {\mathcal {Q}} u (t, x) \big), \qquad t \in (0, T ],\tag{7.20}
$$

for the solution to our fixed point equation (7.21). In other words, if we interpret the$\bar { \mathcal { Q } } u ( t , x )$as a “renormalised Taylor expansion” for the solution u, then any of the components$\boldsymbol { \mathcal { Q } } _ { \zeta } \boldsymbol { u } ( t , \boldsymbol { x } )$is given by some explicit nonlinear function of the renormalised Taylor expansion up to some order depending on$\zeta .$This fact will be used to great effect in Section 9.3 below.

Before we proceed, we show that, in the situations of interest for us, the local solution maps built in Theorem 7.8 are consistent. In other words, we would like to be able to construct a “maximal solution” by piecing together local solutions. In the context considered here, it is a priori not obvious that this is possible. In order to even formulate what we mean by such a statement, we introduce the set$P _ { t } = \{ ( s , y ) ~ { : }$ $s = t \}$and write$R _ { t } ^ { + }$for the indicator function of the set$\{ ( s , y ) ~ : ~ s > t \}$, which we interpret as before as a bounded operator from$\mathcal { D } _ { P _ { t } } ^ { \gamma , \eta }$into itself for any$\gamma > 0$and $\eta \in \mathbf { R }$

From now on, we assume that G is the parabolic Green’s function of a constant coefficient parabolic differential operator on$\mathbf { R } ^ { d - 1 }$. In this way, for any distribution $u _ { 0 }$on$\mathbf { R } ^ { d - \hat { 1 } }$, the function$v = G u _ { 0 }$defined as in Lemma 7.5 is a classical solution to the equation$\partial _ { t } \boldsymbol { v } = \mathcal { L } \boldsymbol { v }$for$t > 0$. We then consider the class of equations of the type (7.18) with$v = G u _ { 0 } ,$, for some function (or possibly distribution)$u _ { 0 }$on$\mathbf { R } ^ { d - 1 }$ We furthermore assume that the sector$V$is function-like. Recall Proposition 3.28, which implies that any modelled distribution u with values in$V$is such that u is a continuous function belonging to$\mathcal { C } _ { \mathfrak { s } } ^ { \beta }$for some$\beta > 0$. In particular,$( \mathcal { R } u ) ( t , \cdot )$is then perfectly well-defined as a function on$\mathbf { R } ^ { d - 1 }$belonging to$\mathcal { C } _ { \bar { s } } ^ { \beta }$. We then have the following result:

Proposition 7.11 In the setting of Theorem$7 . 8 ,$, assume that$\zeta = 0$and$- \mathfrak { s } _ { 1 } < \eta < \beta$ with$\eta \notin \mathbf { N }$and$\beta$as above. Let$u _ { 0 } \in \mathcal { C } _ { \bar { s } } ^ { \eta } ( \mathbf { R } ^ { d - 1 } )$be symmetric and let$T > 0$be sufficiently small so that the equation

$$
u = (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} F (u) + G u _ {0},\tag{7.21}
$$

admits a unique solution$u \in \mathcal { D } _ { P } ^ { \gamma , \eta }$on (0, T ). Let furthermore$s \in ( 0 , T )$and$\bar { T } > T$ be such that

$$
\bar {u} = (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} _ {s} ^ {+} F (\bar {u}) + G u _ {s},
$$

where$\boldsymbol { u } _ { s } \overset { d e f } { = } ( \mathcal { R } \boldsymbol { u } ) ( s , \cdot )$, admits a unique solution$\bar { u } \in \mathcal { D } _ { P _ { s } } ^ { \gamma , \eta }$on$( s , \bar { T } )$

Then, one necessarily has$\bar { u } ( t , x ) = u ( t , x )$for every$x \in \mathbf { R } ^ { d - 1 }$and every$t \in$ $( s , T )$. Furthermore, the element$\hat { u } \in \mathcal { D } _ { P } ^ { \gamma , \eta }$defined by$\hat { u } ( t , x ) = u ( t , x ) f o r t \le s$and $\hat { u } ( t , x ) = \bar { u } ( t , x ) .$for$t > s$satisfies (7.21) on (0, T<sup>¯</sup>).

Proof. Setting$v = R _ { s } ^ { + } u \in \mathcal { D } _ { P _ { s } } ^ { \gamma , \eta }$, it follows from the definitions of${ \kappa } _ { \bar { \gamma } }$and$R _ { \gamma }$that one has for$t \in ( s , T ]$the identity

$$
\begin{array}{l} \langle \mathbf {1}, v (t, x) \rangle = \int_ {0} ^ {t} \int_ {\mathbf {R} ^ {d - 1}} G (t - r, x - y) (\mathcal {R} F (u)) (r, y)   d y   d r \\ \qquad + \int_ {\mathbf {R} ^ {d - 1}} G (t, x - y) u _ {0} (y)   d y \\ \qquad = \int_ {s} ^ {t} \int_ {\mathbf {R} ^ {d - 1}} G (t - r, x - y) (\mathcal {R} F (v)) (r, y)   d y   d r \\ \qquad + \int_ {\mathbf {R} ^ {d - 1}} G (t - s, x - y) u _ {s} (y)   d y  . \end{array}
$$

Here, the fact that there appears no additional term is due to the fact that$\bar { \zeta } > - 2 q$ so that the term$\langle \mathbf { 1 } , { \mathcal { I } } ( t , x ) ( F ( u ) ( t , x ) ) \rangle$cancels exactly with the corresponding term appearing in the definition of$\mathcal { N } _ { \bar { \gamma } }$. This quantity on the other hand is precisely equal to

$$
\left\langle \mathbf {1}, \left(\left(\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}\right) \boldsymbol {R} _ {s} ^ {+} F (v) + G u _ {s}\right) (t, x) \right\rangle .
$$

Setting

$$
w = (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} _ {s} ^ {+} F (v) + G u _ {s},
$$

we deduce from the definitions of the various operators appearing above that, for$\boldsymbol { \ell } \not \in \mathbf { N } ,$ one has$\mathcal { Q } _ { \ell } w ( z ) = \mathcal { Q } _ { \ell } \mathcal { T } F ( z , v ( z ) )$). However, we also know that v satisfies$\mathcal { Q } _ { \ell } v ( z ) =$ $\mathcal { Q } _ { \ell } \mathcal { I } F ( z , v ( z ) )$. We can therefore apply Proposition 3.29, which yields the identity $w = v ,$from which it immediately follows that$v = \bar { u } \mathrm { o n } ( 0 , T )$

The argument regarding uˆ is virtually identical, so we do not reproduce it here.$\boxminus$

This shows that we can patch together local solutions in exactly the same way as for “classical” solutions to nonlinear evolution equations. Furthermore, it shows that the only way in which local solutions can fail to be global is by an explosion of the$\mathcal { C } _ { \bar { \mathfrak { s } } } ^ { \eta } .$ norm of the quantity$( \mathcal { R } u ) ( t , \cdot )$. Furthermore, since the reconstruction operator  is continuous into$\mathcal { C } _ { \bar { \mathfrak { s } } } ^ { \eta }$, this norm is continuous as a function of time, so that for any cut-off value$L > 0$, there exists a (possibly infinite) first time t at which$\| u ( t , \cdot ) \| _ { \eta } = L$

Given a symmetric model$Z = ( \Pi , \Gamma )$for$\mathcal { T }$, a symmetric initial condition$u _ { 0 } \in \mathcal { C } _ { \bar { \mathfrak { s } } } ^ { \eta } .$ and some (typically large) cut-off value$L > 0$, we denote by$u = S ^ { L } ( u _ { 0 } , Z ) \in \mathcal { D } _ { P } ^ { \gamma , \eta }$ and$T = T ^ { L } ( u _ { 0 } , Z ) \in \mathbf { R } _ { + } \cup \{ + \infty \}$the (unique) modelled distribution and time such that

$$
u = (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} F (u) + G u _ {0},
$$

on$[ 0 , T ]$, such that$\| ( \mathcal { R } u ) ( t , \cdot ) \| _ { \eta } < L$for$t < T ,$, and such that$\| ( \mathcal { R } u ) ( t , \cdot ) \| _ { \eta } \geq L$for $t \geq T$. The following corollary is now straightforward:

Corollary 7.12 Let$L > 0$be fixed. In the setting of Proposition 7.11, let$S ^ { L }$and$T ^ { L }$ be defined as above and set$\overset { \cdot } { O } = [ - 1 , 2 ] \times \mathbf { R } ^ { d - \overset { \cdot } { 1 } }$. Then, for every$\varepsilon > 0$and$C > 0$ there exists$\delta > 0$such that, setting$T = 1 \land T ^ { L } ( u _ { 0 } , Z ) \land T ^ { L } ( \bar { u } _ { 0 } , \bar { Z } )$, one has the bound

$$
\left\| \mathcal {S} ^ {L} \left(u _ {0}, Z\right) - \mathcal {S} ^ {L} \left(\bar {u} _ {0}, \bar {Z}\right) \right\| _ {\gamma , \eta ; T} \leq \varepsilon ,
$$

for all$u _ { 0 } , \bar { u } _ { 0 } , Z , \bar { Z }$such that$\| Z \| _ { \gamma ; O } \leq C , \| \bar { Z } \| _ { \gamma ; O } \leq C , \| u _ { 0 } \| _ { \eta } \leq L / 2 , \| \bar { u } _ { 0 } \| _ { \eta } \leq L / 2 ,$ $\| u _ { 0 } - \bar { u } _ { 0 } \| _ { \eta } \le \delta ,$, and$\| Z ; { \bar { Z } } \| _ { \gamma ; O } \leq \delta .$

Proof. The argument is straightforward and works in exactly the same way as analogous statements in the classical theory of semilinear PDEs. The main ingredient is the fact that for every$t > 0 ,$, one can obtain an a priori bound on the number of iterations required to reach the time$t \wedge T ^ { L } ( u _ { 0 } , Z )$□

## 8 Regularity structures for semilinear (S)PDEs

In this section, we show how to apply the theory developed in this article to construct an abstract solution map to a very large class of semilinear PDEs driven by rough input data. Given Theorem$7 . 8 .$, the only task that remains is to build a sufficiently large regularity structure allowing to formulate the equation.

First, we give a relatively simple heuristic that allows one to very quickly decide whether a given problem is at all amenable to the analysis presented in this article. For the sake of conciseness, we will assume that the problem of interest can be rewritten as a fixed point problem of the type

$$
u = K * F (u, \nabla u, \xi) + \tilde {u} _ {0},\tag{8.1}
$$

where$K$is a singular integral operator that is$\beta .$-regularising on$\mathbf { R } ^ { d }$with respect to some fixed scaling${ \mathfrak { s } } , F$is a smooth function, ξ denotes the rough input data, and$\tilde { u } _ { 0 }$describes some initial condition (or possibly boundary data). In general, one might imagine that $F$also depends on derivatives of higher order (provided that$\beta$is sufficiently large) and / or that$F$itself involves some singular integral operators. We furthermore assume that $F$is affine in$\xi .$(Accommodating the general case where$F$is polynomial in$\xi$would also be possible with minor modifications, but we stick to the affine case for ease of presentation.)

It is also straightforward to deal with the situation when$F$is non-homogeneous in the sense that it depends on the (space-time) location explicitly, as long as any such dependence is sufficiently smooth. For the sake of readability, we will refrain from pre-senting such extensions and we will focus on a situation which is just general enough to be able to describe all of the examples given in the introduction.

Remark 8.1 In all the examples we are considering,$K$is the Green’s function of some differential operator${ \mathcal { L } } .$. In order to obtain optimal results, it is usually advisable to fix the scaling s in such a way that all the dominant terms in$\mathcal { L }$have the same homogeneity, when counting powers with the weights given by${ \mathfrak { s } } .$

Remark 8.2 We have seen in Section 7.1 that in general, one would really want to consider instead of (8.1) fixed point problems of the type

$$
u = \left((K + R) * \left(\boldsymbol {R} ^ {+} F (u, \nabla u, \xi)\right)\right) + \tilde {u} _ {0},\tag{8.2}
$$

where$R ^ { + }$denotes again the characteristic function of the set of positive times and$R$ is a smooth non-anticipative kernel. However, if we are able to formulate (8.1), then it is always straightforward to also formulate (8.2) in our framework, so we concentrate on (8.1) for the moment in order not to clutter the presentation.

Denoting by$\alpha < 0$the regularity of$\xi$and considering our multi-level Schauder estimate, Theorem 5.12, we then expect the regularity of the solution u to be of order at most$\beta + \alpha$, the regularity of$\nabla u$to of order at most$\beta + \alpha - 1$, etc. We then make the following assumption:

Assumption 8.3 (local subcriticality) In the formal expression of$F ,$replace$\xi$by a dummy variable$\Xi .$For any$i \in \{ 1 , \ldots , d \}$,$i f \beta + \alpha \leq { \mathfrak { s } } _ { i } ,$then replace furthermore any occurrence of ∂<sub>i</sub>u by the dummy variable$P _ { i }$. Finally,$i f \beta + \alpha \leq 0 ,$, replace any occurrence ofu by the dummy variable$U$

We then make the following two assumptions. First, we assume that the resulting expression is polynomial in the dummy variables. Second, we associate to each such monomial a homogeneity by postulating that$\Xi$has homogeneity$\alpha ,$U has homogeneity $\beta + \alpha ,$, and$P _ { i }$has homogeneity$\beta + \alpha - \mathfrak { s } _ { i } .$. (The homogeneity of a monomial then being the sum of the homogeneities of each factor.) With these notations, the assumption of local subcriticality is that terms containing Ξ do not contain the dummy variables and that the remaining monomials each have homogeneity strictly greater than α.

Whenever a problem of the type (8.1) satisfies Assumption 8.3, we say that it is locally subcritical. The role of this assumption is to ensure that, using Theorems 4.7, $4 . 1 6 ,$, and 5.12, one can reformulate (8.1) as a fixed point map in$\mathcal { D } ^ { \gamma }$for sufficiently high$\gamma$(actually any$\gamma > | \alpha |$would do) by replacing the convolution$K *$with$\kappa _ { \gamma }$ as in Theorem 5.12, replacing all products by the abstract product$\star ,$and interpreting compositions with smooth functions as in Section 4.2.

For such a formulation to make sense, we need of course to build a sufficiently rich regularity structure. This could in principle be done by repeatedly applying Proposition 4.11 and Theorem 5.14, but we will actually make use of a more explicit construction given in this section, which will also have the advantage of coming automatically with a “renormalisation group” that allows to understand the kind of convergence results mentioned in Theorem 1.11 and Theorem 1.15. Our construction suggests the following “metatheorem”, which is essentially a combination of Theorem 7.8, Theorem 4.7, Theorem 4.16, and Theorem 8.24 below.

Metatheorem 8.4 Whenever$( 8 . I )$is locally subcritical, it is possible to build a regularity structure allowing to reformulate it as a fixed point problem in <sup>γ</sup> for γ large enough. Furthermore, if the problem is parabolic on a bounded domain (say the torus), then thefixed point problem admits a unique local solution.

Before we proceed to building the family of regularity structures allowing to formulate these SPDEs, let us check that Assumption 8.3 is indeed verified for our examples (Φ<sup>4</sup>), (PAM), and (KPZ). Note first that it is immediate from Proposition 3.20 and the equivalence of moments for Gaussian random variables that white noise on$\mathbf { R } ^ { d }$with scaling s almost surely belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for every$\alpha < - { \frac { | { \boldsymbol { \mathfrak { s } } } | } { 2 } }$. (See also Lemma 10.2 below.) Furthermore, the heat kernel is 2-regularising, so that$\beta = 2$in all of the problems considered here.

In the case of$( \Phi ^ { 4 } )$in dimension$d ,$space-time is given by$\mathbf { R } ^ { d + 1 }$with scaling${ \mathfrak { s } } =$ $( 2 , 1 , \ldots , 1 )$, so that$| \mathfrak { s } | = d + 2$. This implies that$\xi$belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for every$\alpha \ <$ $\begin{array} { r } { - \frac { d + 2 } { 2 } = - 1 - \frac { d } { 2 } } \end{array}$. In this case$\begin{array} { r } { \beta + \alpha \approx 1 - \frac { d } { 2 } } \end{array}$so that, following the procedure of Assumption$8 . 3$, the monomials appearing are${ \bar { U } } ^ { 3 }$and Ξ. The homogeneity of$U ^ { 3 }$is $\begin{array} { r } { 3 ( \beta + \overline { { \alpha } } ) \approx 3 - \frac { 3 d } { 2 } } \end{array}$, which is greater than$- 1 - { \frac { d } { 2 } } { \mathrm { ~ i f ~ } }$and only if$d \digamma < \digamma 4$This is consistent with the fact that 4 is the critical dimension for Euclidean$\Phi ^ { 4 }$quantum field theory [Aiz82]. Classical fixed point arguments using purely deterministic techniques on the other hand already fail for dimension 2, where the homogeneity of u becomes negative, which is a well-known fact [GRS75]. In the particular case of$d = 2$however, provided that one defines the powers$( K * \xi ) ^ { k }$“by hand”, one can write$u = K * \xi + v ,$ and the equation for v is amenable to classical analysis, a fact that was exploited for example in [DPD03, HRW12]. In dimension 3, this breaks down, but our arguments show that one still expects to be able to reformulate$( \Phi ^ { 4 } )$as a fixed point problem in $\mathcal { D } ^ { \gamma }$, provided that$\begin{array} { r } { \gamma > \frac { 3 } { 2 } } \end{array}$. This will be done in Section 7.3 below.

For (PAM) in dimension d (and therefore space-time$\mathbf { R } ^ { d + 1 }$with the same scaling as above), spatial white noise belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for$\alpha < - \frac { d } { 2 }$. As a consequence, Assumption 8.3 does in this case boil down to the condition$2 + \alpha > 0$, which is again the case if and only if$d < 4$. This is again not surprising. Indeed, dimension 4 is precisely such that, if one considers the classical parabolic Anderson model on the lattice$\mathbf { Z } ^ { \bar { 4 } }$ and simply rescales the solutions without changing the parameters of the model, one formally converges to solutions to the continuous model (PAM). On the other hand, as a consequence of Anderson localisation, one would expect that the rescaled solution converges to an object that is “trivial” in the sense that it could only be described either by the 0 distribution or by a Dirac distribution concentrated in a random location, which is something that falls outside of the scope of the theory presented in this article. In dimensions 2 and 3 however, one expects to be able to formulate and solve a fixed point problem in$\mathcal { D } ^ { \gamma }$for$\gamma > \frac { 3 } { 2 }$This time, one also expects solutions to be global, since the equation is linear.

In the case of$( \mathrm { K P Z } )$, one can verify in a similar way that Assumption 8.3 holds. $\mathrm { A s }$before, if we consider an equation of this type in dimension$d ,$we have$| { \mathfrak { s } } | =$ $d + 2$, so that one expects the solution$u$to be of regularity just below$1 - { \textstyle { \frac { d } { 2 } } }$In this case, dimension 2 is already critical for three unrelated reasons. First, this is the dimension where u ceases to be function-valued, so that compositions with smooth functions ceases to make sense. Second, even if the functions$g _ { i }$were to be replaced by polynomials,$g _ { 4 }$would have to be constant in order to satisfy Assumption 8.3. Finally, the homogeneity of the term$| \nabla h | ^ { 2 }$is d. In dimension 2, this precisely matches the regularity$- 1 - { \frac { d } { 2 } }$of the noise term.

We finally turn to the Navier-Stokes equations (SNS), which we can write in the form (8.1) with$K$given by the heat kernel, composed with Leray’s projection onto the space of divergence-free vector fields. The situation is slightly more subtle here, as the kernel is now matrix-valued, so that we really have$d ^ { 2 }$(or rather$d ( d + 1 ) / 2$ because of the symmetry) different convolution operators. Nevertheless, the situation is similar to before and each component of K is regularity improving with$\beta = 2$. The condition for local subcriticality given by Assumption 8.3 then states that one should have$\begin{array} { r } { ( 1 - \frac { d } { 2 } ) + ( - \frac { d } { 2 } ) > - 1 - \frac { \dot { d } } { 2 } } \end{array}$, which is satisfied if and only if$d < 4$

## 8.1 General algebraic structure

The general structure arising in the abstract solution theory for semilinear SPDEs of the form$( \Phi ^ { 4 } )$, (PAM), etc is very close to the structure already mentioned in Section 4.3. The difference however is that$T$only “almost” forms a Hopf algebra, as we will see presently.

In general, we want to build a regularity structure that is sufficiently rich to allow to formulate a fixed point map for solving our SPDEs. Such a regularity structure will depend on the dimension d of the underlying space(-time), the scaling s of the linear operator, the degree$\beta$of the linear operator (which is equal to the regularising index of the corresponding Green’s function), and the regularity α of the driving noise$\xi .$. It will also depend on finer details of the equation, such as whether the nonlinearity contains derivatives of$u ,$arbitrary functions of$u ,$etc.

At the minimum, our regularity structure should contain polynomials, and it should come with an abstract integration map$\mathcal { T }$that represents integration against the Green’s function$K$of the linear operator${ \mathcal { L } } .$. (Or rather integration against a suitable cut-off version.) Furthermore, since we might want to represent derivatives of$u ,$we can introduce the integration map$\mathcal { T } _ { k }$for a multiindex k, which one should think as representing integration against$D ^ { k } K$. The “na¨ıve” way of building$T$would be then to consider all possible formal expressions$\mathcal { F }$that can be obtained from the abstract symbols$\Xi$and $\{ X _ { i } \} _ { i = 1 } ^ { d }$, as well as the abstract integration maps$\mathcal { T } _ { k }$. More formally, we can define a set$\mathcal { F }$by postulating that$\{ \mathbf { 1 } , \Xi , X _ { i } \} \subset \mathcal { F }$and, whenever$\tau , \bar { \tau } \in \mathcal { F }$, we have$\tau { \bar { \tau } } \in { \mathcal { F } }$ and$\mathcal { T } _ { k } ( \tau ) \in \mathcal { F }$. (However, we do not include any expression containing a factor of $\mathcal { T } _ { k } ( X ^ { \ell } )$, thus reflecting Assumption 5.4 at the algebraic level.) Furthermore, we postulate that the product is commutative and associative by identifying the corresponding formal expressions$( { \mathrm { i . e . ~ } } X { \mathcal { T } } ( \Xi ) = { \mathcal { T } } ( \Xi ) X , { \mathrm { e t c } } )$, and that 1 is neutral for the product.

One can then associate to each$\tau \in { \mathcal { F } }$a weight$| \tau | _ { \mathfrak { s } }$which is obtained by setting $| 1 | _ { \mathfrak { s } } = 0 .$

$$
\left| \tau \bar {\tau} \right| _ {\mathfrak {s}} = \left| \tau \right| _ {\mathfrak {s}} + \left| \tau \right| _ {\mathfrak {s}},
$$

for any two formal expressions τ and$\bar { \tau }$in${ \mathcal F }$, and such that

$$
\left| \Xi \right| _ {\mathfrak {s}} = \alpha , \quad \left| X _ {i} \right| _ {\mathfrak {s}} = \mathfrak {s} _ {i}, \quad \left| \mathcal {I} _ {k} (\tau) \right| _ {\mathfrak {s}} = \left| \tau \right| _ {\mathfrak {s}} + \beta - \left| k \right| _ {\mathfrak {s}}.
$$

Since these operations are sufficient to generate all of${ \mathcal { F } } _ { : }$, this does indeed define$| \cdot | _ { s } .$

Example 8.5 These rules yield the weights

$$
| \Xi \mathcal {I} _ {\ell} (\Xi^ {2} X ^ {k}) | _ {\mathfrak {s}} = 3 \alpha + | k | _ {\mathfrak {s}} + \beta - | \ell | _ {\mathfrak {s}}, \qquad | X ^ {k} \mathcal {I} (\Xi) ^ {2} | _ {\mathfrak {s}} = | k | _ {\mathfrak {s}} + 2 (\alpha + \beta),
$$

for any two multiindices k and$\ell .$

We could then define$T _ { \gamma }$simply as the set of all formal linear combinations of elements$\tau \in \mathcal { F }$with$| \tau | _ { \mathfrak { s } } = \gamma$. The problem with this procedure is that since$\alpha < 0$ we can build in this way expressions that have arbitrarily negative weight, so that the set of homogeneities$A \subset \mathbf { R }$would not be bounded from below anymore. (And it would possibly not even be locally finite.)

The ingredient that allows to circumvent this problem is the assumption of local subcriticality loosely formulated in Assumption$8 . 3 .$. To make this more formal, assuming again for simplicity that the right hand side$F$of our problem$_ { ( 8 . 1 ) }$depends only on$\xi , u ,$and some partial derivatives$\partial _ { i } u$, we can associate to$_ { \mathrm { ~ F ~ a ~ } }$(possibly infinite) collection${ \mathfrak { M } } _ { F }$of monomials in$\Xi , U$, and$P _ { i }$in the following way.

Definition 8.6 For any two integers m and$n ,$and multiindex$k ,$we have$\Xi ^ { m } U ^ { n } P ^ { k } \in$ ${ \mathfrak { M } } _ { F }$if$F$contains a term of the type$\xi ^ { \bar { m } } u ^ { \bar { n } } ( D u ) ^ { \bar { k } }$for$\bar { m } \ge m , \bar { n } \ge n$, and$\bar { k } \geq k$ Here, we consider arbitrary smooth functions as polynomials of “infinite order”, i.e. we formally substitute$g ( u )$by$u ^ { \infty }$and similarly for functions involving derivatives of$u .$. Note also that k and <sup>¯</sup>k are multiindices since, in general,$P$is a d-dimensional vector.

Remark 8.7 Of course,${ \mathfrak { M } } _ { F }$is not really well-defined. For example, in the case of $( \Phi ^ { 4 } )$, we have$F ( u , \xi ) = \xi - u ^ { 3 }$, so that

$$
\mathfrak {M} _ {F} = \{\Xi , U ^ {m}: m \leq 3 \}.
$$

However, we could of course have rewritten this as$F ( u , \xi ) = \xi + g ( u )$, hiding the fact that$g$actually happens to be a polynomial itself, and this would lead to adding all higher powers$\{ U ^ { n } \} _ { n > 3 }$to${ \mathfrak { M } } _ { F }$. In practice, it is usually obvious what the minimal choice of${ \mathfrak { M } } _ { F }$is.

Furthermore, especially in situations where the solution u is actually vector-valued, it might be useful to encode into our regularity structure additional structural properties of the equation, like whether a given function can be written as a gradient. (See the series of works [HM12, HW13, HMW12] for situations where this would be of importance.)

Remark 8.8 In the case of (PAM), we have

$$
\mathfrak {M} _ {F} = \{1, U, U \Xi , \Xi \},
$$

while in the more general case of$\mathbf { ( P A M g ) }$, we have

$$
\mathfrak {M} _ {F} = \left\{U ^ {n}, U ^ {n} \Xi , U ^ {n} P _ {i}, U ^ {n} P _ {i} P _ {j}: n \geq 0, i, j \in \{1, 2 \} \right\}.
$$

This and$( \Phi ^ { 4 } )$are the only examples that will be treated in full detail, but it is straightforward to see what${ \mathfrak { M } } _ { F }$would be for the remaining examples.

Remark 8.9 Throughout this whole section, we consider the case where the noise ξ driving our equation is real-valued and there is only one integral kernel required to describe the fixed point map. In general, one might also want to consider a finite family$\{ \Xi ^ { ( i ) } \}$of formal symbols describing the driving noises and a family$\{ \mathcal { T } ^ { ( i ) } \}$of symbols describing integration against various integral kernels. For example, in the case of (SNS), the integral kernel also involves the Leray projection and is therefore matrix-valued, while the driving noise is vector-valued. This is an immediate generalisation that merely requires some additional indices decorating the objects$\Xi$and and all the results obtained in the present section trivially extend to this case. One could even accommodate the situation where different components of the noise have different degrees of regularity, but it would then become awkward to state an analogue to Assumption 8.3, although it is certainly possible. Since notations are already quite heavy in the current state of things, we refrain from increasing our level of generality.

Given a set of monomials${ \mathfrak { M } } _ { F }$as in Definition 8.6, we then build subsets$\{ \mathcal { U } _ { n } \} _ { n \ge 0 } ,$ $\{ \mathcal { P } _ { n } ^ { i } \} _ { n \ge 0 }$and$\{ \mathcal { W } _ { n } \} _ { n \ge 0 }$of$\mathcal { F }$by the following algorithm. We set$\mathcal { W } _ { 0 } = \mathcal { U } _ { 0 } = \mathcal { P } _ { 0 } ^ { i } \stackrel { - } { = } \varnothing$ and, given subsets$A , B \subset { \mathcal { F } }$, we also write AB for the set of all products$\tau \bar { \tau }$with $\tau \in A$and$\bar { \tau } \in B ,$and similarly for higher order monomials. (Note that this yields the convention$A ^ { 2 } = \{ \tau \bar { \tau } : \tau , \bar { \tau } \in \bar { A } \} \neq \{ \tau ^ { 2 } : \tau \in A \} .$)

Then, we define the sets$\ w _ { w _ { n } , u _ { n } }$and$\mathcal { P } _ { n } ^ { i }$for$n > 0$recursively by

$$
\begin{array}{l} \mathcal {W} _ {n} = \mathcal {W} _ {n - 1} \cup \bigcup_ {\mathcal {Q} \in \mathfrak {M} _ {F}} \mathcal {Q} (\mathcal {U} _ {n - 1}, \mathcal {P} _ {n - 1}, \Xi)  , \\ \mathcal {U} _ {n} = \left\{X ^ {k} \right\} \cup \left\{\mathcal {I} (\tau):   \tau \in \mathcal {W} _ {n} \right\}  , \\ \mathcal {P} _ {n} ^ {i} = \left\{X ^ {k} \right\} \cup \left\{\mathcal {I} _ {i} (\tau):   \tau \in \mathcal {W} _ {n} \right\}  , \end{array}\tag{8.3}
$$

where in the set$\{ X ^ { k } \}$, k runs over all possible multiindices. In plain words, we take any of the monomials in${ \mathfrak { M } } _ { F }$and build$\mathcal { W } _ { n }$by formally substituting each occurrence of$U$by one of the expressions already obtained in$\mathcal { U } _ { n - 1 }$and each occurrence of$P _ { i }$by one of the expressions from$\mathcal { P } _ { n - 1 } ^ { i }$. We then apply the maps$\mathcal { T }$and$\mathcal { T } _ { i }$respectively to build$\mathcal { U } _ { n }$and$\mathcal { P } _ { n } ^ { i }$, ensuring further that they include all monomials involving only the symbols$X _ { i }$. With these definitions at hand, we then set

$$
\mathcal {F} _ {F} \stackrel {{\text { def }}} {{=}} \bigcup_ {n \geq 0} (\mathcal {W} _ {n} \cup \mathcal {U} _ {n})  .\tag{8.4}
$$

In situations where$F$depends on u (and not only on Du and$\xi$like in the case of the KPZ equation for example), we furthermore set

$$
\mathcal {U} _ {F} \stackrel {{\text { def }}} {{=}} \bigcup_ {n \geq 0} \mathcal {U} _ {n} .\tag{8.5}
$$

We similarly define$\begin{array} { r } { \mathcal { P } _ { F } ^ { i } = \bigcup _ { n > 0 } \mathcal { P } _ { n } ^ { i } } \end{array}$in the case when$F$depends on$\partial _ { i } u$. The idea of this construction is that$\mathcal { U } _ { F }$Scontains those elements of that are required to describe the solution u to the problem at hand,$\mathcal { P } _ { F } ^ { i }$contains the elements appearing in the description of$\partial _ { i } u$, and$\mathcal { F } _ { F }$contains the elements required to describe both the solution and the right hand side of (8.1), so that$\mathcal { F } _ { F }$is rich enough to set up the whole fixed point map.

The following result then shows that our assumption of local subcriticality, Assumption 8.3, is really the correct assumption for the theory developed in this article to apply:

Lemma 8.10 Let$\alpha < 0 .$. Then, the set$\{ \tau \in \mathcal { F } _ { F } : | \tau | _ { \mathfrak { s } } \le \gamma \}$is finite for every$\gamma \in \mathbf { R }$ if and only if Assumption 8.3 holds.

Proof. We only show that Assumption 8.3 is sufficient. Its necessity can be shown by similar arguments and is left to the reader. Set$\alpha ^ { ( n ) } = \operatorname* { i n f } \{ | \tau | _ { 5 } : \tau \in \mathcal { U } _ { n } \setminus \mathcal { U } _ { n - 1 } \}$and $\alpha _ { i } ^ { ( n ) } = \operatorname* { i n f } \{ | \tau | _ { \mathfrak { s } } : \tau \in \mathcal { P } _ { n } ^ { ( i ) } \backslash \mathcal { P } _ { n - 1 } ^ { ( i ) } \}$. We claim that under Assumption 8.3 there exists $\zeta > 0$such that$\alpha ^ { ( n ) } > \alpha ^ { ( n - 1 ) } + \zeta$and similarly for$\alpha _ { i } ^ { ( n ) }$, which then proves the claim. Note now that${ \mathcal { W } } _ { 1 } = \{ \Xi \}$, so that one has

$$
\alpha^ {(1)} = (\alpha + \beta) \wedge 0, \quad \alpha_ {i} ^ {(1)} = (\alpha + \beta - \mathfrak {s} _ {i}) \wedge 0.
$$

Furthermore, Assumption 8.3 implies that$\operatorname { i f } \Xi ^ { p } U ^ { q } P ^ { k } \in \mathfrak { M } _ { F } \setminus \{ \Xi \}$, then

$$
p \alpha + q (\alpha + \beta) + \sum_ {i} k _ {i} (\alpha + \beta - \mathfrak {s} _ {i}) > \alpha ,\tag{8.6}
$$

and$k _ { i }$is allowed to be non-zero only if$\beta > \mathfrak { s } _ { i }$. This immediately implies that one has$| \tau | _ { s } \geq \alpha$for every$\tau \in { \mathcal { F } } _ { F } , | \tau | _ { \mathfrak { s } } \geq ( \alpha + \beta ) \wedge 0$for every$\tau \in \mathcal { U } _ { F }$, and$| \tau | _ { s } \geq$ $( \alpha + \beta - { \mathfrak { s } } _ { i } ) \wedge 0$for every$\tau \in \mathcal { P } _ { F } ^ { i }$. (If this were to fail, then there would be a smallest index n at which it fails. But then, since it still holds at$n - 1$, condition$_ { ( 8 . 6 ) }$ensures that it also holds at$n _ { \colon }$thus creating a contradiction.)

Let now$\zeta > 0$be defined as

$$
\zeta = \inf _ {\Xi^ {p} U ^ {q} P ^ {k} \in \mathfrak {M} _ {F} \backslash \{\Xi \}} \left\{(p - 1) \alpha + q (\alpha + \beta) + \sum_ {i} k _ {i} (\alpha + \beta - \mathfrak {s} _ {i}) \right\}.
$$

Then we see that$\alpha ^ { ( 2 ) } \geq \alpha ^ { ( 1 ) } + \zeta$and similarly for$\alpha _ { i } ^ { ( 2 ) }$. Assume now by contradiction that there is a smallest value n such that either$\alpha ^ { ( n ) } < \alpha ^ { ( n - 1 ) } + \zeta \mathrm { o r } \alpha _ { i } ^ { ( n ) } < \alpha _ { i } ^ { ( n - 1 ) } + \zeta$ for some index i. Note first that one necessarily has$n \geq 3$and that, for any such $n ,$, one necessarily has$\alpha _ { i } ^ { ( n ) } = \alpha ^ { ( n ) } - \mathfrak { s } _ { i }$<sub>i</sub> by (8.3) so that we can assume that one has $\alpha ^ { ( n ) } < \alpha ^ { ( n - 1 ) } + \zeta$

Note now that there exists some element$\tau \in \mathcal { U } _ { n }$with$| \tau | _ { \mathfrak { s } } = \alpha ^ { ( n ) }$and that$\tau$ is necessarily of the form$\tau = \mathcal { T } ( \bar { \tau } )$with$\bar { \tau } \in \mathcal { W } _ { n } \ \backslash \ \mathcal { W } _ { n - 1 }$. In other words,$\bar { \tau }$is a product of elements in$\mathcal { U } _ { n - 1 }$and$\mathcal { P } _ { n - 1 } ^ { i }$(and possibly a factor Ξ) with at least one factor belonging to either$\mathcal { U } _ { n - 1 } \setminus \mathcal { U } _ { n - 2 } \mathrm { o r } \mathcal { P } _ { n - 1 } ^ { i } \setminus \mathcal { P } _ { n - 2 } ^ { i }$. Denote that factor by$\sigma ,$so that$\bar { \tau } = \sigma$u for some$u \in \mathcal W _ { n }$

Assume that$\sigma \in \mathcal { U } _ { n - 1 } \setminus \mathcal { U } _ { n - 2 }$, the argument being analogous if it belongs to one of the$\mathcal P _ { n - 1 } ^ { i } \setminus \mathcal P _ { n - 2 } ^ { i } .$. Then, by definition, one has$| \sigma | _ { \mathfrak { s } } \geq \alpha ^ { ( n - 1 ) }$<sup>)</sup>. Furthermore, one has$\alpha ^ { ( n - 1 ) } \geq \alpha ^ { ( n - 2 ) } + \zeta$so that there exists some element$\hat { \sigma } \in \mathcal { U } _ { n - 2 } \setminus \mathcal { U } _ { n - 3 }$with $| \hat { \sigma } | _ { \mathfrak { s } } \le | \sigma | _ { \mathfrak { s } } - \zeta$. By the same argument, one can find$\hat { u } \in \mathcal W _ { n - 1 }$with$| \hat { u } | _ { s } \le | u | _ { s } .$ Consider now the element$\hat { \tau } = \mathcal { I } ( \hat { \sigma } \hat { u } )$. By the definitions, one has$\hat { \tau } \in \mathcal { U } _ { n - 1 }$and, since $\hat { \sigma } \notin \mathcal { U } _ { n - 3 }$, one has$\hat { \tau } \notin \mathcal { U } _ { n - 2 }$. Therefore, we conclude from this that

$$
\alpha^ {(n - 1)} \leq | \hat {\tau} | _ {\mathfrak {s}} \leq | \tau | _ {\mathfrak {s}} - \zeta = \alpha^ {(n)} - \zeta ,
$$

thus yielding the contradiction required to prove our claim.

Remark 8.11 If F depends explicitly on u, then one has$U \in \mathfrak { M } _ { F }$, so that one automatically has$\mathcal { U } _ { F } \subset \mathcal { F } _ { F }$. Similarly, if$F$depends on$\partial _ { i } u .$, one has$\mathcal { P } _ { F } ^ { i } \subset \mathcal { F } _ { F }$

Remark 8.12 If$\tau \in \mathcal { F } _ { F }$is such that there exists$\tau _ { 1 }$and$\tau _ { 2 }$in$\mathcal { F }$with$\tau = \tau _ { 1 } \tau _ { 2 }$, then one also has$\tau _ { 1 } , \tau _ { 2 } \in \mathcal { F } _ { F }$. This is a consequence of the fact that, by Definition$8 . 6 ,$ whenever a monomial in${ \mathfrak { M } } _ { F }$can be written as a product of two monomials, each of these also belongs to${ \mathfrak { M } } _ { F }$

Similarly, if${ \mathcal { T } } ( \tau ) \in  { \mathcal { F } } _ { F }$or$\mathcal { T } _ { i } ( \tau ) \in \mathcal { F } _ { F }$for some$\tau \in \mathcal { F }$, then one actually has $\tau \in \mathcal { F } _ { F }$

Given any problem of the type (1.1), and under Assumption 8.3, this procedure thus allows us to build a candidate$T$for the model space of a regularity structure, by taking for$T _ { \gamma }$the formal linear combinations of elements in$\mathcal { F } _ { F }$with$| \tau | _ { s } = \gamma .$. The spaces $T _ { \gamma }$are all finite-dimensional by Lemma 8.10, so the choice of norm on$T _ { \gamma }$is irrelevant. For example, we could simply decree that the elements of$\mathcal { F } _ { F }$form an orthonormal basis. Furthermore, the natural product in$\mathcal { F }$extends to a product ⋆ on$T$by linearity, and by setting$\tau \star \bar { \tau } = 0$whenever$\tau , \bar { \tau } \in \mathcal { F } _ { F }$are such that$\tau \bar { \tau } \notin \mathcal { F } _ { F }$

While we now have a candidate for a model space$T ,$, as well as an index set A (take $A = \{ | \tau | _ { \mathfrak { s } } : \tau \in \mathcal { F } _ { F } \} )$, we have not yet constructed the structure group$G$that allows to “translate” our model from one point to another. The remainder of this subsection is devoted to this construction. In principle,$G$is completely determined by the action of the group of translations on the${ \bar { X } } ^ { k }$, the assumption that$\Gamma \Xi = \Xi$, the requirements

$$
\Gamma (\tau \bar {\tau}) = (\Gamma \tau) \star (\Gamma \bar {\tau}),
$$

for any$\tau , \bar { \tau } \in \mathcal { F } _ { F }$such that$\tau \bar { \tau } \in \mathcal { F } _ { F }$, as well as the construction of Section 5.1. However, since it has a relatively explicit construction similar to the one of Section 4.3, we give it for the sake of completeness. This also gives us a much better handle on elements of$G ,$which will be very useful in the next section. Finally, the construction of G given here exploits the natural relations between the integration maps$\mathcal { T } _ { k }$for different values of k (which are needed when considering equations involving derivatives of the solution in the right hand side), which is something that the general construction of Section 5.1 does not do.

In order to describe the structure group$G ,$we introduce three different vector spaces. First, we denote by$\mathcal { H } _ { F }$the set of finite linear combinations of elements in $\mathcal { F } _ { F }$and by the set of finite linear combinations of all elements in$\mathcal { F }$. We furthermore define a set$\mathcal { F } _ { + }$consisting of all formal expressions of the type

$$
X ^ {k} \prod_ {j} \mathcal {J} _ {k _ {j}} \tau_ {j},\tag{8.7}
$$

where the product runs over finitely many terms, the$\tau _ { j }$are elements of${ \mathcal F } ,$and the$k _ { j }$ are multiindices with the property that$| \tau _ { j } | _ { \mathfrak { s } } + \beta - | k _ { j } | _ { \mathfrak { s } } > 0$for every factor appearing in this product. We should really think of$\mathcal { T } _ { k }$as being essentially the same as$\mathcal { T } _ { k }$, so that one can alternatively think of$\mathcal { F } _ { + }$as being the set of all elements$\tau \in \mathcal { F }$such that either$\tau = 1 \mathrm { o r } | \tau | _ { \mathfrak { s } } > 0$and such that, whenever τ can be written as$\tau = \tau _ { 1 } \tau _ { 2 } .$ one also has either$\tau _ { i } = 1 \mathrm { o r } | \tau _ { i } | _ { \mathfrak { s } } > 0$. The notation$\mathcal { T } _ { k }$instead of$\mathcal { T } _ { k }$will however serve to reduce confusion in the sequel, since elements of$\mathcal { F } _ { + }$play a role that is distinct from the corresponding elements in$\mathcal { F }$. It is no coincidence that the symbol$\mathcal { I }$is the same as in Section 5 since elements of the type$\mathcal { T } _ { k } \tau$are precisely placeholders for the coefficients$\mathcal { T } ( x ) \tau$defined in (5.11). Similarly, we define$\mathcal { F } _ { F } ^ { + }$as the set of symbols as in (8.7), but with the$\tau _ { j }$assumed to belong to$\mathcal { F } _ { F }$. Expressions of the type (8.7) come with a natural notion of homogeneity, given by$\begin{array} { r } { | k | _ { s } + \mathbf { \bar { \rho } } { \bf \bar { \rho } } _ { j } ( | \tau _ { j } | _ { s } + \beta - | \bar { k _ { j } } | _ { s } ) } \end{array}$, which is always positive by definition.

We then denote by$\mathcal { H } _ { + }$the set of all finite linear combinations of all elements in$\mathcal { F } _ { + }$ and similarly for$\mathcal { H } _ { F } ^ { + }$. Note that both and$\mathcal { H } _ { + }$are algebras, by simply extending the product$( \tau , \bar { \tau } ) \mapsto \tau \bar { \tau }$in a distributive way. While$\mathcal { H } _ { F }$is a linear subspace of$\mathcal { H } ,$it is not in general a subalgebra of$\mathcal { H } .$, but this will not concern us very much since it is mostly the structure of the larger space that matters. The space$\mathcal { H } _ { F } ^ { \div }$on the other hand is an algebra. (Actually the free algebra over the symbols$\{ X _ { j } , \mathcal { J } _ { k } \dot { \tau } \}$, where$j \in \{ 1 , \ldots , d \}$ $\tau \in \mathcal { F } _ { F }$, and k is an arbitrary d-dimensional multiindex with$| k | _ { \mathfrak { s } } < | \tau | _ { \mathfrak { s } } + \beta . )$

We now describe a structure on the spaces and$\mathcal { H } _ { + }$that endows$\mathcal { H } _ { + } ~ ( \mathrm { r e s p } . ~ \mathcal { H } _ { F } ^ { + } )$ with a Hopf algebra structure and$\mathcal { H } \left( \mathrm { r e s p . ~ } \mathcal { H } _ { F } \right)$with the structure of a comodule over $\mathcal { H } _ { + } ~ ( \mathrm { r e s p . } ~ \mathcal { H } _ { F } ^ { + } )$. The purpose of these structures is to yield an explicit construction of a regularity structure that is sufficiently rich to allow to formulate fixed point maps for large classes of semilinear (stochastic) PDEs. This construction will in particular allow us to describe the structure group G in a way that is similar to the construction in Section 4.3, but with a slight twist since$T = \mathcal { H } _ { F }$itself is different from both the Hopf algebra$\mathcal { H } _ { + }$and the comodule .

We first note that for every multiindex k, we have a natural linear map$\hat { \mathcal { T } } _ { k } \colon \mathcal { H }$ $\mathcal { H } _ { + }$by setting

$$
\hat {\mathcal {J}} _ {k} (\tau) = \mathcal {J} _ {k} \tau , | k | _ {\mathfrak {s}} <   | \tau | _ {\mathfrak {s}} + \beta , \quad \hat {\mathcal {J}} _ {k} (\tau) = 0, \text { otherwise }.
$$

Since there can be no scope for confusion, we will make a slight abuse of notation and simply write again$\mathcal { T } _ { k }$instead of$\hat { \mathcal { I } } _ { k }$. We then define two linear maps$\Delta \colon { \mathcal { H } } \to { \mathcal { H } } \otimes { \mathcal { H } } _ { + }$ and$\Delta ^ { + } \colon \mathcal { H } _ { + } \to \mathcal { H } _ { + } \otimes \mathcal { H } _ { + }$by

$$
\begin{array}{l l} \Delta \mathbf {1} = \mathbf {1} \otimes \mathbf {1}, & \Delta^ {+} \mathbf {1} = \mathbf {1} \otimes \mathbf {1}, \\ \Delta X _ {i} = X _ {i} \otimes \mathbf {1} + \mathbf {1} \otimes X _ {i}, & \Delta^ {+} X _ {i} = X _ {i} \otimes \mathbf {1} + \mathbf {1} \otimes X _ {i} \\ \Delta \Xi = \Xi \otimes \mathbf {1}, \end{array}
$$

and then, recursively, by

$$
\begin{array}{l} \Delta (\tau \bar {\tau}) = (\Delta \tau) (\Delta \bar {\tau}) \\ \Delta (\mathcal {I} _ {k} \tau) = (\mathcal {I} _ {k} \otimes I) \Delta \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \otimes \frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \tau  , \end{array}\tag{8.8a}
$$

(8.8b)

as well as

$$
\Delta^ {+} (\tau \bar {\tau}) = (\Delta^ {+} \tau) (\Delta^ {+} \bar {\tau})
$$

$$
\Delta^ {+} \left(\mathcal {J} _ {k} \tau\right) = \sum_ {\ell} \left(\mathcal {J} _ {k + \ell} \otimes \frac {(- X) ^ {\ell}}{\ell !}\right) \Delta \tau + \mathbf {1} \otimes \mathcal {J} _ {k} \tau .\tag{8.9a}
$$

(8.9b)

In both cases, these sums run in principle over all possible multiindices ℓ and$m$. Note however that these sums are actually finite since, by definition, for$| \ell | _ { s }$large enough it is always the case that$\mathcal { I } _ { k + \ell } \tau = 0$

Remark 8.13 By construction, for every$\tau \in { \mathcal { F } } .$, one has the identity$\Delta \tau = \tau \otimes { \bf 1 } +$ $\begin{array} { r } { \sum _ { i } c _ { i } \tau _ { i } ^ { ( 1 ) } \otimes \tau _ { i } ^ { ( 2 ) } } \end{array}$, for some constants$c _ { i }$and some elements with$| \tau _ { i } ^ { \mathrm { ( 1 ) } } | _ { s } < | \tau | _ { s }$and $| \tau _ { i } ^ { ( \bar { 1 } ) } | _ { s } + | \tau _ { i } ^ { ( 2 ) } | _ { s } = | \tau | _ { s }$. This is a reflection in this context of the condition (2.1).

Similarly, for every$\sigma \in { \mathcal { F } } _ { + }$, one has the identity

$$
\Delta^ {+} \sigma = \sigma \otimes {\bf 1} + {\bf 1} \otimes \sigma + \sum_ {i} c _ {i} \sigma_ {i} ^ {(1)} \otimes \sigma_ {i} ^ {(2)},
$$

for some constants$c _ { i }$and some elements with$| \sigma _ { i } ^ { ( 1 ) } | _ { \mathfrak { s } } + | \sigma _ { i } ^ { ( 2 ) } | _ { \mathfrak { s } } = | \sigma | _ { \mathfrak { s } }$. Note also that (8.9) is coherent with our abuse of notation for$\hat { \mathcal { I } } _ { k }$in the sense that if τ and k are such that$\hat { \mathcal { T } } _ { k } \tau = 0$, then the right hand side automatically vanishes.

Remark 8.14 The fact that it is$\Delta$(rather than$\Delta ^ { + } )$that appears in the right hand side of (8.9b) is not a typo: there is not much choice since$\tau \in \mathcal { F }$and not in$\mathcal { F } _ { + }$. The motivation for the definitions of$\Delta$and$\Delta ^ { + }$will be given in Section$8 . 2$below where we show how it allows to canonically lift a continuous realisation$\xi$of the “noise” to a model for the regularity structure built from these algebraic objects.

Remark 8.15 In the sequel, we will use Sweedler’s notation for coproducts. Whenever we write$\Delta \tau = \sum \tau ^ { ( 1 ) } \stackrel { - } { \otimes } \tau ^ { ( 2 ) }$, this should be read as a shorthand for: “There exists a finite index set$I ,$P, non-zero constants$\{ c _ { i } \} _ { i \in I } ,$, and basis elements$\{ \tau _ { i } ^ { ( 1 ) } \} _ { i \in I } , \{ \tau _ { i } ^ { ( 2 ) } \} _ { i \in I }$ such that the identity$\begin{array} { r } { \Delta \tau = \sum _ { i \in I } c _ { i } \tau _ { i } ^ { ( 1 ) } \otimes \tau _ { i } ^ { ( 2 ) } } \end{array}$holds.” If we then later refer to a joint property of$\tau ^ { ( 1 ) }$and$\tau ^ { ( 2 ) }$P, this means that the property in question holds for every pair $( \tau _ { i } ^ { ( 1 ) } , \tau _ { i } ^ { ( 2 ) } )$appearing in the above sum.

The structure just introduced has the following nice algebraic properties.

Theorem 8.16 The space$\mathcal { H } _ { + }$is a Hopf algebra and  is a comodule over$\mathcal { H } _ { + }$. In particular, one has the identities

$$
(I \otimes \Delta^ {+}) \Delta \tau = (\Delta \otimes I) \Delta \tau ,\tag{8.10a}
$$

$$
(I \otimes \Delta^ {+}) \Delta^ {+} \tau = (\Delta^ {+} \otimes I) \Delta^ {+} \tau ,\tag{8.10b}
$$

for every$\tau \in \mathcal { H } .$. Furthermore, there exists an idempotent antipode :$\mathcal { H } _ { + } \to \mathcal { H } _ { + }$ satisfying the identity

$$
\mathcal {M} (I \otimes \mathcal {A}) \Delta^ {+} \tau = \langle \mathbf {1} ^ {*}, \tau \rangle \mathbf {1} = \mathcal {M} (\mathcal {A} \otimes I) \Delta^ {+} \tau ,\tag{8.11}
$$

where we denoted by$\mathcal { M } \colon \mathcal { H } _ { + } \otimes \mathcal { H } _ { + } \to \mathcal { H } _ { + }$the multiplication operator defined by $\mathcal { M } ( \tau \otimes \bar { \tau } ) = \tau \bar { \tau } ,$, and by 1<sup>∗</sup> the element of$\mathcal { H } _ { + } ^ { * }$such that$\left. \mathbf { 1 } ^ { * } , \mathbf { 1 } \right. = 1 a n d \left. \mathbf { 1 } ^ { * } , \tau \right. = 0$ for all$\tau \in \mathcal { F } _ { + } \setminus \{ 1 \}$

Proof. We first prove (8.10a). Both operators map 1 onto$\mathbf { 1 } \otimes \mathbf { 1 } \otimes \mathbf { 1 } , \equiv \mathrm { o n t o } \equiv \otimes \mathbf { 1 } \otimes \mathbf { 1 }$ and$X _ { i }$onto$X _ { i } \otimes \mathbf { 1 } \otimes \mathbf { 1 } + \mathbf { 1 } \otimes X _ { i } \otimes \mathbf { 1 } + \mathbf { 1 } \otimes \mathbf { 1 } \otimes X _ { i }$. Since$\mathcal { F }$is then generated by multiplication and action with$\mathcal { T } _ { k } ,$we can verify (8.10a) recursively by showing that it is stable under products and applications of the integration maps.

Assume first that, for some τ and τ¯ in${ \mathcal F } ,$, the identity (8.10a) holds when applied to both$\tau$and τ¯. By (8.8a), (8.9a), and the induction hypothesis, one then has the identity

$$
\begin{array}{c} (I \otimes \Delta^ {+}) \Delta (\tau \bar {\tau}) = (I \otimes \Delta^ {+}) (\Delta \tau \Delta \bar {\tau}) = ((I \otimes \Delta^ {+}) \Delta \tau) ((I \otimes \Delta^ {+}) \Delta \bar {\tau}) \\ = ((\Delta \otimes I) \Delta \tau) ((\Delta \otimes I) \Delta \bar {\tau}) = (\Delta \otimes I) (\Delta \tau \Delta \bar {\tau}) = (\Delta \otimes I) \Delta (\tau \bar {\tau}), \end{array}
$$

as required.

It remains to show that if (8.10a) holds for some$\tau \in \mathcal { F }$, then it also holds for$\mathcal { T } _ { k } \tau$ for every multiindex$k .$First, by (8.8b) and (8.9b), one has the identity

$$
\begin{array}{c} (I \otimes \Delta^ {+}) \Delta \mathcal {I} _ {k} \tau = (I \otimes \Delta^ {+}) (\mathcal {I} _ {k} \otimes I) \Delta \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \otimes \Delta^ {+} \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \tau \Big) \\ = (\mathcal {I} _ {k} \otimes I \otimes I) (I \otimes \Delta^ {+}) \Delta \tau \end{array}
$$

$$
+ \sum_ {\ell , m, n} \frac {X ^ {\ell}}{\ell !} \otimes \left(\frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !}\right) \Delta^ {+} \mathcal {J} _ {k + \ell + m + n} \tau ,\tag{8.12}
$$

where we used the multiplicative property of$\Delta ^ { + }$and the fact that

$$
\Delta^ {+} \frac {X ^ {k}}{k !} = \sum_ {m \leq k} \frac {X ^ {m}}{m !} \otimes \frac {X ^ {k - m}}{(k - m) !}.
$$

(Note again that the seemingly infinite sums appearing in (8.12) are actually all finite since$\mathcal { I } _ { k } \tau = 0$for k large enough. This will be the case for every expression of this type appearing below.) At this stage, we use the recursion relation (8.9b) which yields

$$
\begin{array}{r l} & {\sum_ {m, n} \Big (\frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \Big) \Delta^ {+} \mathcal {J} _ {k + m + n} \tau = \sum_ {m, n} \Big (\frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \mathcal {J} _ {k + m + n} \tau \Big)} \\ & {\qquad + \sum_ {\ell , m, n} \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m + n} \otimes \frac {X ^ {n}}{n !} \frac {(- X) ^ {\ell}}{\ell !} \Big) \Delta \tau} \\ & {\qquad = \sum_ {m, n} \Big (\frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \mathcal {J} _ {k + m + n} \tau \Big) + \sum_ {m} \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + m} \otimes I \Big) \Delta \tau .} \end{array}
$$

Here we made use of the fact that$\scriptstyle \sum _ { \ell + n = k } { \frac { X ^ { n } } { n ! } } { \frac { ( - X ) ^ { \ell } } { \ell ! } }$always vanishes, except when $k = 0$Pin which case it just yields 1. Inserting this in the above expression, we finally obtain the identity

$$
\begin{array}{l} (I \otimes \Delta^ {+}) \Delta \mathcal {I} _ {k} \tau = (\mathcal {I} _ {k} \otimes I \otimes I) (I \otimes \Delta^ {+}) \Delta \tau \\ \qquad + \sum_ {\ell , m, n} \frac {X ^ {\ell}}{\ell !} \otimes \frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \mathcal {J} _ {k + \ell + m + n} \tau \\ \qquad + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \otimes \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \otimes I \Big) \Delta \tau  . \end{array}\tag{8.13}
$$

On the other hand, using again (8.8b), (8.9b), and the binomial identity, we obtain

$$
\begin{array}{l} (\Delta \otimes I) \Delta \mathcal {I} _ {k} \tau = (\Delta \mathcal {I} _ {k} \otimes I) \Delta \tau + \sum_ {\ell , m} (\Delta \otimes I) \Big (\frac {X ^ {\ell}}{\ell !} \otimes \frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \tau \Big) \\ = (\mathcal {I} _ {k} \otimes I \otimes I) (\Delta \otimes I) \Delta \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \otimes \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \otimes I \Big) \Delta \tau \\ + \sum_ {\ell , m, n} \frac {X ^ {\ell}}{\ell !} \otimes \frac {X ^ {m}}{m !} \otimes \frac {X ^ {n}}{n !} \mathcal {J} _ {k + \ell + m + n} \tau  . \end{array}
$$

Comparing this expression with (8.13) and using the induction hypothesis, the claim follows at once.

We now turn to the proof of (8.10b). Proceeding in a similar way as before, we verify that the claim holds for$\tau = { \bf 1 } , \tau = X _ { i }$, and$\tau = \Xi$. Using the fact that$\Delta ^ { + }$is a multiplicative morphism, it follows as before that if (8.10b) holds for$\tau$and${ \bar { \tau } } ,$then it also holds for$\tau \bar { \tau }$. It remains to show that it holds for$\mathcal { T } _ { k } \tau$. One verifies, similarly to before, that one has the identity

$$
(\Delta^ {+} \otimes I) \Delta^ {+} \mathcal {J} _ {k} \tau = \mathbf {1} \otimes \mathbf {1} \otimes \mathcal {J} _ {k} \tau + \mathbf {1} \otimes \sum_ {\ell} \left(\mathcal {J} _ {k + \ell} \otimes \frac {(- X) ^ {\ell}}{\ell !}\right) \Delta \tau
$$

$$
+ \sum_ {\ell , m} \left(\mathcal {J} _ {k + \ell + m} \otimes \frac {(- X) ^ {\ell}}{\ell !} \otimes \frac {(- X) ^ {m}}{m !}\right) (\Delta \otimes I) \Delta \tau ,
$$

while one also has

$$
\begin{array}{l} (I \otimes \Delta^ {+}) \Delta^ {+} \mathcal {J} _ {k} \tau = \mathbf {1} \otimes \sum_ {\ell} \Big (\mathcal {J} _ {k + \ell} \otimes \frac {(- X) ^ {\ell}}{\ell !} \Big) \Delta \tau + \mathbf {1} \otimes \mathbf {1} \otimes \mathcal {J} _ {k} \tau \\ \qquad + \sum_ {\ell , m} \Big (\mathcal {J} _ {k + \ell + m} \otimes \frac {(- X) ^ {\ell}}{\ell !} \otimes \frac {(- X) ^ {m}}{m !} \Big) (I \otimes \Delta^ {+}) \Delta \tau . \end{array}
$$

The claim now follows from (8.10a).

It remains to show that$\mathcal { H } _ { + }$admits an antipode$\mathcal { A } \colon \mathcal { H } _ { + } \to \mathcal { H } _ { + }$. This is automatic for connected graded bialgebras but it turns out that in our case, although it admits a natural integer grading,$\mathcal { H } _ { + }$is not connected for it (i.e. there is more than one basis element with vanishing degree). It is of course connected for the grading$| \cdot | _ { s } ,$, but this is not integer-valued. The general construction of however still works in essentially the same way. The natural integer grading$| \cdot |$on$\mathcal { F } _ { + }$for this purpose is defined recursively by$| X _ { i } | = | \Xi | = | \mathbf { 1 } | = 0$, and then$| \tau \bar { \tau } | = | \tau | + | \bar { \tau } |$and$| \mathcal { I } _ { k } \tau | = | \tau | + 1$. In plain terms, it counts the number of times that an integration operator arises in the formal expression τ.

Recall that$\mathcal { A }$should be a linear map satisfying (8.11), and we furthermore want $\mathcal { A }$to be a multiplicative morphism namely, for$\tau \ = \ \tau _ { 1 } \tau _ { 2 }$, we impose that$\boldsymbol { A } \tau ~ =$ $( \boldsymbol { A \tau _ { 1 } } ) ( \boldsymbol { A \tau _ { 2 } } )$. To construct${ \mathcal { A } } ,$we start by setting

$$
\mathcal {A} X _ {i} = - X _ {i}, \quad \mathcal {A} \mathbf {1} = \mathbf {1}.\tag{8.14}
$$

Given the construction of$\mathcal { H } _ { + }$, it then remains to define on elements of the type$\mathcal { T } _ { k } \tau$ with$\tau \in \mathcal { H }$and$| \mathcal { T } _ { k } \tau | _ { \mathfrak { s } } > 0$. This should be done in such a way that one has

$$
\mathcal {M} (I \otimes \mathcal {A}) \Delta^ {+} \mathcal {J} _ {k} \tau = 0,\tag{8.15}
$$

which then guarantees that the first equality in (8.11) holds for all$\tau \in \mathcal { H } _ { + }$. This is because$\mathcal { M } ( I \otimes \mathcal { A } ) \Delta ^ { + }$is then a multiplicative morphism which vanishes on$X _ { i }$and every element of the form$\mathcal { T } _ { k } \tau$, and, except for$\tau = 1$, every element of$\mathcal { F } _ { + }$has at least one such factor.

To show that it is possible to enforce (8.15) in a coherent way, we proceed by induction. Indeed, by the definition of$\Delta ^ { + }$and the definition of$\mathcal { M } ,$, one has the identity

$$
\mathcal {M} (I \otimes \mathcal {A}) \Delta^ {+} \mathcal {J} _ {k} \tau = \sum_ {\ell} \mathcal {M} \left(\mathcal {J} _ {k + \ell} \otimes \frac {X ^ {\ell}}{\ell !} \mathcal {A}\right) \Delta \tau + \mathcal {A} \mathcal {J} _ {k} \tau .
$$

Therefore,$\mathcal { A T } _ { k } \tau$is determined by (8.15) as soon as we know$( I \otimes A ) \Delta \tau$. This can be guaranteed by iterating over$\mathcal { F }$in an order of increasing degree. (In the sense of the number of times that the integration operator appears in a formal expression, as defined above.)

We can then show recursively that the antipode also satisfies$\mathcal { M } ( \mathcal { A } \otimes I ) \Delta ^ { + } \tau$= $\mathbf { 1 } ^ { * } ( \tau ) \mathbf { 1 }$. Again, we only need to verify it inductively on elements of the form$\mathcal { T } _ { k } \tau$. One then has

$$
\mathcal {M} (\mathcal {A} \otimes I) \Delta^ {+} \mathcal {J} _ {k} \tau = \mathcal {J} _ {k} \tau + \sum_ {\ell} \frac {(- X) ^ {\ell}}{\ell !} \mathcal {M} (\mathcal {A} \mathcal {J} _ {k + \ell} \otimes I) \Delta \tau
$$

$$
\begin{array}{l} = \mathcal {J} _ {k} \tau - \sum_ {\ell , m} \frac {(- X) ^ {\ell} X ^ {m}}{\ell ! m !} \mathcal {M} (\mathcal {J} _ {k + \ell + m} \otimes \mathcal {A} \otimes I) (\Delta \otimes I) \Delta \tau \\ = \mathcal {J} _ {k} \tau - \mathcal {M} (\mathcal {J} _ {k} \otimes \mathcal {A} \otimes I) (I \otimes \Delta^ {+}) \Delta \tau  , \end{array}
$$

where we used the fact that$\begin{array} { r } { \sum _ { \ell + m = n } \frac { ( - X ) ^ { \ell } X ^ { m } } { \ell ! m ! } = 0 } \end{array}$unless$n = 0$in which case it is 1. PAt this stage, we use the fact that it is straightforward to verify inductively that

$$
(I \otimes \mathbf {1} ^ {*}) \Delta \tau = \tau ,\tag{8.16}
$$

for every$\tau \in { \mathcal { H } } .$, so that an application of our inductive hypothesis yields$\mathcal { M } ( A \otimes$ $I ) \Delta ^ { + } \mathcal { I } _ { k } \tau = \mathcal { I } _ { k } \tau - \mathcal { I } _ { k } \tau = 0$as required. The fact that$\mathcal { A } ^ { 2 } \tau = \tau$can be verified in a similar way. It is also a consequence of the fact that the Hopf algebra$\mathcal { H } _ { + }$is commutative [Swe69].□

Remark 8.17 Note that is not a Hopf module over$\mathcal { H } _ { + }$since the identity ∆(ττ¯) = $\Delta \tau \Delta ^ { + } \bar { \tau }$does in general not hold for any$\tau \in \mathcal { H }$and$\bar { \tau } \in \mathcal { H } _ { + }$. However,$\hat { \mathcal { H } } = \mathcal { H } \otimes \mathcal { H } _ { + }$ can be turned in a very natural way into a Hopf module over$\mathcal { H } _ { + }$. The module structure is given by$( \tau \otimes { \bar { \tau } _ { 1 } } ) \bar { \tau } _ { 2 } = \tau \otimes ( { \bar { \tau } _ { 1 } } { \bar { \tau } _ { 2 } } )$for$\tau \in \mathcal { H }$and$\bar { \tau } _ { 1 } , \bar { \tau } _ { 2 } \in \mathcal { H } _ { + }$, while the comodule structure ∆ :<sup>ˆ</sup>$\hat { \mathcal { H } } \to \hat { \mathcal { H } } \otimes \mathcal { H } _ { + }$is given by

$$
\hat {\Delta} (\tau \otimes \bar {\tau}) = \Delta \tau \cdot \Delta^ {+} \bar {\tau},
$$

where$( \tau _ { 1 } \otimes \tau _ { 2 } ) \cdot ( \bar { \tau } _ { 1 } \otimes \bar { \tau } _ { 2 } ) = ( \tau _ { 1 } \otimes \bar { \tau } _ { 1 } ) \otimes ( \tau _ { 2 } \bar { \tau } _ { 2 } )$for$\tau _ { 1 } ~ \in ~ \mathcal { H }$and$\tau _ { 2 } , \bar { \tau } _ { 1 } , \bar { \tau } _ { 2 } \in \mathcal { H } _ { + }$ These structures are then compatible in the sense that$( \hat { \Delta } \otimes I ) \hat { \Delta } = ( I \otimes \Delta ^ { + } ) \hat { \Delta }$and $\hat { \Delta } ( \tau \bar { \tau } ) = \hat { \Delta } \tau \cdot \Delta ^ { + } \bar { \tau }$. It is not clear at this stage whether known general results on these structures (like the fact that Hopf modules are always free) can be of use for the type of analysis performed in this article.

We are now almost ready to construct the structure group$G$in our context. First, we define a product  on$\mathcal { H } _ { + } ^ { \ast }$, the dual of$\mathcal { H } _ { + }$, by

Definition 8.18 Given two elements$g , \bar { g } \in \mathcal { H } _ { + } ^ { * }$, their product$g \circ { \bar { g } }$is given by the dual of$\Delta ^ { + }$, i.e., it is the element satisfying

$$
\left\langle g \circ \bar {g}, \tau \right\rangle = \left\langle g \otimes \bar {g}, \Delta^ {+} \tau \right\rangle ,
$$

for all$\tau \in \mathcal { H } _ { + }$

From now on, we will use the notations$\langle g , \tau \rangle , g ( \tau )$, or even$g \tau$interchangeably for the duality pairing. We also identify$X \otimes$R with X in the usual way$( x \otimes c \sim c x )$for any space X. Furthermore, to any$g \in \mathcal { H } _ { + } ^ { * }$, we associate a linear map$\Gamma _ { g } \colon { \mathcal { H } } \to { \mathcal { H } }$in essentially the same way as in (4.19), by setting

$$
\Gamma_ {g} \tau = (I \otimes g) \Delta \tau .\tag{8.17}
$$

Note that, by (8.16), one has$\Gamma _ { 1 ^ { * } } \tau = \tau$. One can also verify inductively that the co-unit 1<sup>∗</sup> is indeed the neutral element for . With these definitions at hand, we have

Proposition 8.19 For any$g , \bar { g } \in \mathcal { H } _ { + } ^ { * }$, one has$\Gamma _ { g } \Gamma _ { \bar { g } } = \Gamma _ { g \circ \bar { g } }$. Furthermore, the product is associative.

Proof. One has the identity

$$
\begin{array}{c} \Gamma_ {g} \Gamma_ {\bar {g}} \tau = \Gamma_ {g} (I \otimes \bar {g}) \Delta \tau = (I \otimes g \otimes \bar {g}) (\Delta \otimes I) \Delta \tau \\ = (I \otimes g \otimes \bar {g}) (I \otimes \Delta^ {+}) \Delta \tau = (I \otimes (g \circ \bar {g})) \Delta \tau  , \end{array}
$$

where we first used Theorem 8.16 and then the definition of the product$^ { \circ . }$The associativity of is equivalent to the coassociativity (8.10b) of$\Delta ^ { + }$, which we already proved in Theorem 8.16.□

We now have all the ingredients in place to define the structure group$G \colon$

Definition 8.20 The group$G$is given by the group-like elements$g \in \mathcal { H } _ { + } ^ { * }$, i.e. the elements such that$g ( \tau _ { 1 } \tau _ { 2 } ) = g ( \tau _ { 1 } ) g ( \tau _ { 2 } )$for any$\tau _ { i } \in \mathcal { H } _ { + }$. Its action on$\mathcal { H }$is given by $g \mapsto \Gamma _ { g } .$

This definition is indeed meaningful thanks to the following standard result:

Proposition 8.21 Given$g , { \bar { g } } \in G ,$, one has$g \circ { \bar { g } } \in G$. Furthermore, each element $g \in G$has a unique inverse$g ^ { - 1 }$

Proof. This is standard, see [Swe69]. The explicit expression for the inverse is simply $g ^ { - 1 } ( \tau ) = g ( \mathcal { A } \tau )$.□

Finally, we note that our operations behave well when restricting ourselves to the spaces$\mathcal { H } _ { F }$and$\mathcal { H } _ { F } ^ { + }$constructed as explained previously by only considering those formal expressions that are “useful” for the description of the nonlinearity$F \colon$

$$
\text { Lemma   8.22   One   has   } \Delta : \mathcal {H} _ {F} \to \mathcal {H} _ {F} \otimes \mathcal {H} _ {F} ^ {+} \text {   and   } \Delta^ {+}: \mathcal {H} _ {F} ^ {+} \to \mathcal {H} _ {F} ^ {+} \otimes \mathcal {H} _ {F} ^ {+}.
$$

Proof. We claim that actually, even more is true. Recall the definitions of the sets$\textstyle \mathcal { W } _ { n } ,$ $\mathcal { U } _ { n }$and$\mathcal { P } _ { n } ^ { i }$from (8.3) and denote by$\left. \mathcal { W } _ { n } \right.$the linear span of$\mathcal { W } _ { n }$in$\mathcal { H } _ { F }$, and similarly for$\left. \mathcal { U } _ { n } \right.$and$\langle \mathcal { P } _ { n } ^ { i } \rangle$. Then, denoting by any of these vector spaces, we claim that$\Delta$ has the property that$\Delta \mathcal { X } \subset \mathcal { X } \otimes \mathcal { H } _ { F } ^ { + }$, which in particular then also implies that the action of$G$leaves each of the spaces$\mathcal { X }$invariant. This can easily be seen by induction over n. The claim is clearly true for$n = 0$by definition. Assuming now that it holds for $\left. l _ { n - 1 } \right.$and$\langle \mathcal { P } _ { n - 1 } ^ { i } \rangle$, it follows from the definition of$\mathcal { W } _ { n }$and the morphism property of$\Delta$that the claim also holds for$\mathcal { W } _ { n }$. The identity (8.8b) then also implies that the claim is true for$\left. \mathcal { U } _ { n } \right.$and$\langle \mathcal { P } _ { n } ^ { i } \rangle$, as required.

Regarding the property$\Delta ^ { + } \colon \mathcal { H } _ { F } ^ { + } \to \mathcal { H } _ { F } ^ { + }$$\mathcal { H } _ { F } ^ { + }$, it follows from the morphism property of$\Delta ^ { + }$(and the fact that$\mathcal { H } _ { F } ^ { + }$itself is closed under multiplication) that we only need to check it on elements τ of the form$\tau = \mathcal { T } _ { k } \bar { \tau }$with$\bar { \tau } \in \mathcal { F } _ { F }$. Using (8.9b), the claim then immediately follows from the first claim.□

Remark 8.23 This shows that the action of$G$onto$\mathcal { H } _ { F }$is equivalent to the action of the quotient group$G _ { F }$obtained by identifying elements that act in the same way onto $\mathcal { H } _ { F } ^ { + }$

This concludes our construction of the regularity structure associated to a general subcritical semilinear (S)PDE, which we summarise as a theorem:

Theorem 8.24 Let F be a locally subcritical nonlinearity, let$T = \mathcal { H } _ { F }$with$T _ { \gamma } =$ $\langle \{ \tau \in \mathcal { F } _ { F } : | \tau | _ { \mathfrak { s } } = \gamma \} \rangle , A = \{ | \tau | _ { \mathfrak { s } } : \tau \in \mathcal { F } _ { F } \}$, and$G _ { F }$be defined as above. Then, $\mathcal { T } _ { F } = ( A , \mathcal { H } _ { F } , G _ { F } )$, defines a regularity structure$\mathcal { T }$. Furthermore,$\mathcal { T }$is an abstract integration map oforder$\beta f o r \mathcal { T }$

Proof. To check that$\mathcal { T } _ { F }$is a regularity structure, the only property that remains to be shown is$( 2 . 1 )$. This however follows immediately from the fact that if one writes $\begin{array} { r } { \Delta \tau = \sum \tau ^ { ( 1 ) } \otimes \tau ^ { ( 2 ) } } \end{array}$, then each of these terms satisfies$| \tau ^ { ( 1 ) } | _ { \mathfrak { s } } + | \tau ^ { ( 2 ) } | _ { \mathfrak { s } } = | \tau | _ { \mathfrak { s } }$and $| \tau ^ { ( 2 ) } | _ { \mathfrak { s } } \overline { { \geq 0 } }$. Furthermore, one verifies by induction that the term$\tau \otimes 1$appears exactly once in this sum, so that for all other terms,$\tau ^ { ( 1 ) }$is of homogeneity strictly smaller than that of$\tau .$

The map$\mathcal { T }$obviously satisfies the first two requirements of an abstract integration map by our definitions. The last property follows from the fact that

$$
\Gamma_ {g} \mathcal {I} _ {k} \tau = (I \otimes g) \Delta \mathcal {I} _ {k} \tau = (I \otimes g) (\mathcal {I} _ {k} \otimes I) \Delta \tau + \sum_ {\ell} \frac {(X - x _ {g}) ^ {\ell}}{\ell !} g (\mathcal {J} _ {k + \ell} \tau),
$$

where we defined$\boldsymbol { x } _ { q } ~ \in ~ \mathbf { R } ^ { d }$as the element with coordinates$- g ( X _ { i } )$. Noting that $( I \otimes g ) ( \mathcal { T } _ { k } \otimes I ) \Delta \tau = \mathcal { T } _ { k } \Gamma _ { g } \tau$, the claim follows.□

Remark 8.25 If some element of${ \mathfrak { M } } _ { F }$also contains a factor$\mathcal { P } _ { i }$, then one can check in the same way as above that$\mathcal { T } _ { i }$is an abstract integration map of order$\beta - \mathfrak { s } _ { i }$for$\mathcal { T }$

Remark 8.26 Given$F$as above and$r > 0$, we will sometimes write$\mathcal { T } _ { F } ^ { ( r ) }$(or simply $\mathcal { T } ^ { ( r ) }$when F is clear from the context) for the regularity structure obtained as above, but with$T _ { \gamma } = 0$for$\gamma > r$

## 8.2 Realisations of the general algebraic structure

While the results of the previous subsection provide a systematic way of constructing a regularity structure$\mathcal { T }$that is sufficiently rich to allow to reformulate (8.1) as a fixed point problem which has some local solution$U \in \mathcal { D } _ { P } ^ { \gamma , \eta }$for suitable indices γ and$\eta ,$, it does not at all address the problem of constructing a model (or family of models) (Π, Γ) such that U can be interpreted as a limit of classical solutions to some regularised version of (8.1).

It is in the construction of the model (Π, Γ) that one has to take advantage of additional knowledge about ξ (for example that it is Gaussian), which then allows to use probabilistic tools, combined with ideas from renormalisation theory, to build a “canonical mode$1 ^ { \circ }$(or in many cases actually a canonical finite-dimensional family of models) associated to it. We will see in Section 10 below how to do this in the particular cases of (PAMg) and$( \Phi ^ { 4 } )$. For any continuous realisation of the driving noise however, it is straightforward to$^ { 6 6 } \mathrm { l i f f }$it to the regularity structure that we just built, as we will see presently.

Given any continuous approximation$\xi _ { \varepsilon }$to the driving noise$\xi ,$we now show how one can build a canonical model$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$for the regularity structure$\mathcal { T }$built in the previous subsection. First, we set

$$
(\Pi_ {x} ^ {(\varepsilon)} \Xi) (y) = \xi_ {\varepsilon} (y), \quad (\Pi_ {x} ^ {\varepsilon} X ^ {k}) (y) = (y - x) ^ {k}.
$$

Then, we recursively define$\Pi _ { x } ^ { ( \varepsilon ) } \tau$by

$$
(\Pi_ {x} ^ {(\varepsilon)} \tau \bar {\tau}) (y) = (\Pi_ {x} ^ {(\varepsilon)} \tau) (y) (\Pi_ {x} ^ {(\varepsilon)} \bar {\tau}) (y),\tag{8.18}
$$

as well as

$$
(\Pi_ {x} ^ {(\varepsilon)} \mathcal {I} _ {k} \tau) (y) = \int D _ {1} ^ {k} K (y, z) (\Pi_ {x} ^ {(\varepsilon)} \tau) (z) d z + \sum_ {\ell} \frac {(y - x) ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} (\mathcal {J} _ {k + \ell} \tau).\tag{8.19}
$$

In this expression, the quantities$f _ { x } ^ { ( \varepsilon ) } ( \mathcal { T } _ { \ell } \tau )$are defined by

$$
f _ {x} ^ {(\varepsilon)} (\mathcal {J} _ {\ell} \tau) = - \int D _ {1} ^ {\ell} K (x, z) \left(\Pi_ {x} ^ {(\varepsilon)} \tau\right) (z) d z.\tag{8.20}
$$

If we furthermore impose that

$$
f _ {x} ^ {(\varepsilon)} (X _ {i}) = - x _ {i}, \qquad f _ {x} ^ {(\varepsilon)} (\tau \bar {\tau}) = \big (f _ {x} ^ {(\varepsilon)} \tau \big) \big (f _ {x} ^ {(\varepsilon)} \bar {\tau} \big),\tag{8.21}
$$

and extend this to all of$\mathcal { H } _ { F } ^ { + }$by linearity, then$f _ { x } ^ { \left( \varepsilon \right) }$defines an element of the group$G _ { F }$ given in Definition 8.20 and Remark 8.23.

Denote by$F _ { x } ^ { \left( \varepsilon \right) }$the corresponding linear operator on$\mathcal { H } _ { F }$, i.e.$F _ { x } ^ { ( \varepsilon ) } = \Gamma _ { f _ { x } ^ { ( \varepsilon ) } }$) where the map$g \mapsto \Gamma _ { g }$is given by (8.17). With these definitions at hand, we then define$\Gamma _ { x y } ^ { ( \varepsilon ) }$ by

$$
\Gamma_ {x y} ^ {(\varepsilon)} = \left(F _ {x} ^ {(\varepsilon)}\right) ^ {- 1} \circ F _ {y} ^ {(\varepsilon)}.\tag{8.22}
$$

Furthermore, for any$\tau \in \mathcal { F }$, we denote by$V _ { \tau }$the sector given by the linear span of $\{ \Gamma \tau : \Gamma \in G \}$. This is also given by the projection of$\Delta \tau$onto its first factor. We then have:

Proposition 8.27 Let K be as in Lemma 5.5 and satisfying Assumption$5 . 4 f o r$some $r > 0 .$. Let furthermore$\mathcal { T } _ { F } ^ { ( r ) }$be the regularity structure obtained from any semilinear locally subcritical problem as in Section 8.1 and Remark 8.26. Letfinally$\boldsymbol { \xi } _ { \varepsilon } \colon \mathbf { R } ^ { d }$R be a smooth function and let$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$be defined as above. Then,$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$is a model for$\mathcal { T } _ { F } ^ { ( r ) }$

Furthermore, for any$\tau \in \mathcal { F } _ { F }$such that$\mathcal { T } _ { k } \tau \in \mathcal { F } _ { F }$, the model$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$realises the abstract integration operator$\mathcal { T } _ { k }$on the sector$V _ { \tau }$

Proof. We need to verify both the algebraic relations and the analytical bounds of Definition 2.17. The fact that$\Gamma _ { x y } ^ { \left( \varepsilon \right) } \Gamma _ { y z } ^ { \left( \varepsilon \right) } = \Gamma _ { x z } ^ { \left( \varepsilon \right) }$is immediate from the definition (8.22). In view of (8.22), the identity$\Pi _ { x } ^ { ( \varepsilon ) } \Gamma _ { x y } ^ { ( \varepsilon ) } = \Pi _ { y } ^ { ( \varepsilon ) }$follows if we can show that

$$
\Pi_ {x} ^ {(\varepsilon)} (F _ {x} ^ {(\varepsilon)}) ^ {- 1} \tau = \Pi_ {y} ^ {(\varepsilon)} (F _ {y} ^ {(\varepsilon)}) ^ {- 1} \tau ,\tag{8.23}
$$

for every$\tau \in \mathcal { F } _ { F }$and any two points x and y. In order to show that this is the case, it turns out that it is easiest to simply “guess” an expression for$\Pi _ { x } ^ { ( \varepsilon ) } \big ( F _ { x } ^ { ( \varepsilon ) } \big ) ^ { - 1 } \tau$that is independent of x and to then verify recursively that our guess was correct. For this, we define a linear map Π<sup>(ε)</sup> :$\mathcal { H } _ { F } \to \mathcal { C } ( \mathbf { R } ^ { d } )$by

$$
(\mathbf {\Pi} ^ {(\varepsilon)} \mathbf {1}) (y) = 1, \qquad (\mathbf {\Pi} ^ {(\varepsilon)} X _ {i}) (y) = y _ {i}, \qquad (\mathbf {\Pi} ^ {(\varepsilon)} \Xi) (y) = \xi_ {\varepsilon} (y),
$$

and then recursively by

$$
(\mathbf {\Pi} ^ {(\varepsilon)} \tau \bar {\tau}) (y) = (\mathbf {\Pi} ^ {(\varepsilon)} \tau) (y) (\mathbf {\Pi} ^ {(\varepsilon)} \bar {\tau}) (y),\tag{8.24}
$$

as well as

$$
(\mathbf {\Pi} ^ {(\varepsilon)} \mathcal {I} _ {k} \tau) (y) = \int D _ {1} ^ {k} K (y, z) (\mathbf {\Pi} ^ {(\varepsilon)} \tau) (z) d z.\tag{8.25}
$$

We claim that one has$\Pi _ { x } ^ { ( \varepsilon ) } ( F _ { x } ^ { ( \varepsilon ) } ) ^ { - 1 } \tau = \Pi ^ { ( \varepsilon ) } \tau$for every$\tau \in \mathcal { F } _ { F }$and every$x \in \mathbf { R } ^ { d }$ Actually, it is easier to verify the equivalent identity

$$
\Pi_ {x} ^ {(\varepsilon)} \tau = \Pi^ {(\varepsilon)} F _ {x} ^ {(\varepsilon)} \tau .\tag{8.26}
$$

To show this, we proceed by induction. The identity obviously holds for$\tau = \Xi$and $\tau = 1$. For$\tau = X _ { i }$, we have by (8.21)

$$
(\mathbf {\Pi} ^ {(\varepsilon)} F _ {x} ^ {(\varepsilon)} X _ {i}) (y) = ((\mathbf {\Pi} ^ {(\varepsilon)} \otimes f _ {x} ^ {(\varepsilon)}) (X _ {i} \otimes \mathbf {1} + \mathbf {1} \otimes X _ {i})) (y) = y _ {i} - x _ {i} = (\Pi_ {x} ^ {(\varepsilon)} X _ {i}) (y)
$$

Furthermore, in view of (8.24), (8.18), and the fact that$F _ { x } ^ { \left( \varepsilon \right) }$acts as a multiplicative morphism, it holds for$\tau \bar { \tau }$if it holds for both τ and τ¯.

To complete the proof of (8.23), it remains to show that (8.26) holds for elements of the form$\mathcal { T } _ { k } \tau$if it holds for τ. It follows from the definitions that

$$
\begin{array}{l} F _ {x} ^ {(\varepsilon)} \mathcal {I} _ {k} \tau = \mathcal {I} _ {k} F _ {x} ^ {(\varepsilon)} \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} \Big (\frac {X ^ {m}}{m !} \mathcal {J} _ {k + \ell + m} \tau \Big) \\ \qquad = \mathcal {I} _ {k} F _ {x} ^ {(\varepsilon)} \tau + \sum_ {\ell , m} \frac {X ^ {\ell}}{\ell !} \frac {(- x) ^ {m}}{m !} f _ {x} ^ {(\varepsilon)} \Big (P \mathcal {J} _ {k + \ell + m} \tau \Big) \\ \qquad = \mathcal {I} _ {k} F _ {x} ^ {(\varepsilon)} \tau + \sum_ {\ell} \frac {(X - x) ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} (\mathcal {J} _ {k + \ell} \tau), \end{array}\tag{8.27}
$$

where we used (8.21), the morphism property of$f _ { x } ^ { ( \varepsilon ) }$, and the binomial identity. The above identity is precisely the abstract analogue in this context of the identity postulated in Definition 5.9.

Inserting this into (8.25), we obtain the identity

$$
(\mathbf {\Pi} ^ {(\varepsilon)} F _ {x} ^ {(\varepsilon)} \mathcal {I} _ {k} \tau) (y) = \int D _ {1} ^ {k} K (y, z) (\mathbf {\Pi} ^ {(\varepsilon)} F _ {x} ^ {(\varepsilon)} \tau) (z) d z + \sum_ {\ell} \frac {(y - x) ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} (\mathcal {J} _ {k + \ell} \tau).\tag{8.28}
$$

Since$\Pi ^ { ( \varepsilon ) } F _ { x } ^ { ( \varepsilon ) } \tau = \Pi _ { x } ^ { ( \varepsilon ) } \tau$by our induction hypothesis, this is precisely equal to the right hand side of (8.19), as required.

It remains to show that the required analytical bounds also hold. Regarding$\Pi _ { x } ^ { \left( \varepsilon \right) }$ we actually show the slightly stronger fact that$( \Pi _ { x } ^ { ( \varepsilon ) } \tau ) ( y ) \lesssim \| x - y \| _ { \mathfrak { s } } ^ { | \tau | _ { s } }$. This is obvious for$\tau = X _ { i }$as well as for$\tau = \Xi$since$| \Xi | _ { s } < 0$and we assumed that$\xi _ { \varepsilon }$is continuous. (Of course, such a bound would typically not hold uniformly in$\varepsilon ! )$Since $| \tau \bar { \tau } | _ { \mathfrak { s } } = | \tau | _ { \mathfrak { s } } + | \bar { \tau } | _ { \mathfrak { s } } ,$, it is also obvious that such a bound holds for$\tau \bar { \tau }$if it holds for both τ and τ¯. Regarding elements of the form$\mathcal { T } _ { k } \tau$, we note that the second term in (8.19) is precisely the truncated Taylor series of the first term, so that the required bound holds by Proposition A.1 or, more generally, by Theorem 5.14. To conclude the proof that $( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$is a model for our regularity structure, it remains to obtain a bound of the type (2.15) for$\Gamma _ { x y } ^ { \left( \varepsilon \right) }$. In principle, this also follows from Theorem 5.14, but we can also verify it more explicitly in this case.

Note that the required bound follows if we can show that

$$
\left| \gamma_ {x y} ^ {(\varepsilon)} (\tau) \right| \stackrel {{\text { def }}} {{=}} \left| \left(f _ {x} \mathcal {A} \otimes f _ {y}\right) \Delta^ {+} \tau \right| \lesssim \| x - y \| _ {\mathfrak {s}} ^ {| \tau | _ {\mathfrak {s}}},
$$

for all$\tau \in \mathcal { F } _ { F } ^ { + }$with$| \tau | _ { s } \leq r .$Again, this can easily be checked for$\tau = X ^ { k }$. For $\tau = \mathcal { I } _ { k } \bar { \tau }$, note that one has the identity

$$
(\mathcal {A} \otimes I) \Delta^ {+} \mathcal {J} _ {k} \bar {\tau} = \mathbf {1} \otimes \mathcal {J} _ {k} \bar {\tau} - \sum_ {\ell , m} (\mathcal {M} \otimes I) \left(\mathcal {J} _ {k + \ell + m} \otimes \frac {X ^ {\ell}}{\ell !} \mathcal {A} \otimes \frac {(- X) ^ {m}}{m !}\right) (I \otimes \Delta^ {+}) \Delta \bar {\tau}.
$$

As a consequence, we have the identity

$$
\gamma_ {x y} ^ {(\varepsilon)} (\mathcal {J} _ {k} \bar {\tau}) = f _ {y} ^ {(\varepsilon)} (\mathcal {J} _ {k} \bar {\tau}) - \sum_ {\ell} \frac {(y - x) ^ {\ell}}{\ell !} f _ {x} ^ {(\varepsilon)} (\mathcal {J} _ {k + \ell} \Gamma_ {x y} ^ {(\varepsilon)} \bar {\tau}).
$$

It now suffices to realise that this is equal to the quantity$( \Gamma _ { y x } ^ { ( \varepsilon ) } \mathcal { T } _ { x y } \bar { \tau } ) _ { k }$, where$\mathcal { I } _ { x y }$was introduced in (5.36), so that the required bound follows from Lemma 5.21. There is an unfortunate notational clash between$\mathcal { I } _ { x y }$and$\mathcal { T } _ { k }$appearing here, but since this is the only time in the article that both objects appear simultaneously, we leave it at that.

The fact that the model built in this way realises K for the abstract integration operator  (and indeed for any of the$\mathcal { T } _ { k } )$follows at once from the definition (8.19).

Remark 8.28 In general, one does not even need$\xi _ { \varepsilon } \mathrm { t o }$be continuous. One just needs it to be in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for sufficiently large (but possibly negative) α such that all the products appearing in the above construction satisfy the conditions of Proposition 4.14.

This construction motivates the following definition, where we assume that the kernel K annihilates monomials up to order r and that we are given a regularity structure $\mathcal { T } _ { F }$built from a locally subcritical nonlinearity F as above.

Definition 8.29 A model (Π, Γ) for$\mathcal { T } _ { F } ^ { ( r ) }$is admissible if it satisfies$( \Pi _ { x } X ^ { k } ) ( y ) =$ $( y - x ) ^ { k }$, as well as (8.19), (8.21), (8.22), and (8.20). We denote by$\mathcal { M } _ { F }$the set of admissible models.

Note that the set of admissible models is a closed subset of the set of all models and that the models built from canonical lifts of smooth functions$\xi ^ { ( \varepsilon ) }$are admissible by definition. Admissible models are also adapted to the integration map$K$(and suitable derivatives thereof) for the integration map$\mathcal { T }$(and the maps$\mathcal { T } _ { k }$if applicable). Actually, the converse is also true provided that we define f by (8.20). This can be shown by a suitable recursion procedure, but since we will never actually use this fact we do not provide a full proof.

Remark 8.30 It is not clear in general whether canonical lifts of smooth functions are dense in$\mathcal { M } _ { F }$. As the definitions stand, this will actually never be the case since smooth functions are not even dense in$\mathcal { C } ^ { \alpha } !$This is however an artificial problem that can easily be resolved in a manner similar to what we did in the proof of the reconstruction theorem, Theorem 3.10. (See also the note [FV06].) However, even when allowing for some weaker notion of density, it will in general not be the case that lifts of smooth functions are dense. This is because the regularity structure$\mathcal { T } _ { F } ^ { ( r ) }$ built in this section does not encode the Leibniz rule, so that it can accommodate the type of effects described in [Gub10, HM12, HK12] (or even just Itˆo’s formula in one dimension) which cannot arise when only considering lifts of smooth functions.

## 8.3 Renormalisation group associated to the general algebraic structure

There are many situations where, if we take for$\xi _ { \varepsilon }$a smooth approximation to$\xi$such that$\xi _ { \varepsilon }  \xi$in a suitable sense, the sequence$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$of models built from$\xi _ { \varepsilon }$as in the previous section fails to converge. This is somewhat different from the situation encountered in the context of the theory of rough paths where natural smooth approximations to the driving noise very often do yield finite limits without the need for renormalisation [CQ02, FV10a]. (The reason why this is so stems from the fact that if a process X is symmetric under time-reversal, then the expression$X _ { i } \partial _ { t } X _ { j }$is antisymmetric, thus introducing additional cancellations. Recall the discussion on the role of symmetries in Remark 1.9.)

In general, in order to actually build a model associated to the driving noise$\xi ,$we will need to be able to encode some kind of renormalisation procedure. In the context of the regularity structures built in this section, it turns out that they come equipped with a natural group of continuous transformations on their space of admissible models. At the abstract level, this group of transformations (which we call R) will be nothing but a finite-dimensional nilpotent Lie group – in many instances just a copy of$\mathbf { R } ^ { n }$for some $n > 0$. As already mentioned in the introduction, a renormalisation procedure then consists in finding a sequence$M _ { \varepsilon }$of elements in R such that$M _ { \varepsilon } ( \Pi ^ { \left( \varepsilon \right) } , \Gamma ^ { \left( \varepsilon \right) } )$converges to a finite limit (Π, Γ), where$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$is the bare model built in Section 8.2. As pre-viously, different renormalisation procedures yield limits that differ only by an element in R.

Remark 8.31 The construction outlined in this section, and indeed the whole methodology presented here, has a flavour that is strongly reminiscent of the theory given in [CK00, CK01]. The scope however is different: the construction presented here applies to subcritical situations in which one obtains superrenormalisable theories, so that the group R is always finite-dimensional. The construction of [CK00, CK01] on the other hand applies to critical situations and yields an infinite-dimensional renormalisation group.

Assume that we are given some model (Π, Γ) for our regularity structure$\mathcal { T }$. As before, we assume that$\Gamma _ { x y }$is provided to us in the form

$$
\Gamma_ {x y} = F _ {x} ^ {- 1} \circ F _ {y},\tag{8.29}
$$

and we denote by$f _ { x }$the group-like element in the dual of$\mathcal { H } _ { F } ^ { + }$corresponding to$F _ { x }$. As a consequence, the operator$\Pi _ { x } F _ { x } ^ { - 1 }$is independent of x and, as in Section 8.2, we will henceforth denote it simply by

$$
\Pi \stackrel {\text { def }} {=} \Pi_ {x} F _ {x} ^ {- 1} .\tag{8.30}
$$

Throughout this whole section, we will thus represent a model by the pair$( \Pi , f )$where Π is one single linear map Π :$T  S ^ { \prime } ( \mathbf { R } ^ { d } )$and f is a map on$\mathbf { R } ^ { d }$with values in the morphisms of$\mathcal { H } _ { F } ^ { + }$

We furthermore make the additional assumption that our model is admissible, so that one has the identities

$$
\boldsymbol {\Pi} \mathcal {I} _ {k} \tau = \int_ {\mathbf {R} ^ {d}} D ^ {k} K (\cdot , y) (\boldsymbol {\Pi} \tau) (d y),\tag{8.31}
$$

$$
f _ {x} \mathcal {J} _ {k} \tau = - \int_ {\mathbf {R} ^ {d}} D ^ {k} K (x, y) (\Pi_ {x} \tau) (d y),\tag{8.32}
$$

where, in view of (8.30), Π and$\Pi _ { x }$are related by

$$
\boldsymbol {\Pi} \tau = (\Pi_ {x} \otimes f _ {x} \mathcal {A}) \Delta \tau , \quad \Pi_ {x} \tau = (\boldsymbol {\Pi} \otimes f _ {x}) \Delta \tau .
$$

Note that by definition, (8.32) only ever applies to elements with$| \mathcal { T } _ { k } \tau | _ { \mathfrak { s } } > 0$, which implies that the corresponding integral actually makes sense. In view of (8.8b) and (5.12), this ensures that our model does realise K for the abstract integration operator (and, if needed, the relevant derivatives of K for the$\mathcal { T } _ { k } )$. It is crucial that any transformation that we would like to apply to our model preserves this property, since otherwise the operators$\kappa _ { \gamma }$cannot be constructed anymore for the new model.

Remark 8.32 While it is clear that$( \Pi , f )$is sufficient to determine the corresponding model by (8.29) and (8.30), the converse is not true in general if one only imposes (8.29). However, if we also impose (8.32), together with the canonical choice$f _ { x } ( X ) =$ $- x$, then$f$is uniquely determined by the model in its usual representation (Π, Γ). This shows that although the transformations constructed in this section will be given in terms of$f ,$, they do actually define maps defined on the set$\mathcal { M } _ { F }$of all admissible models.

The important feature of R is its action on elements$\tau$of negative homogeneity. It turns out that, in order to describe it, it is convenient to work on a slightly larger set $\mathcal { F } _ { 0 } \subset \mathcal { F } _ { F }$with some additional properties. Given any set$\mathcal { C } \subset \mathcal { F } _ { F }$, we will henceforth denote by$\mathrm { A l g } ( { \mathcal { C } } ) \subset { \mathcal { F } } _ { F } ^ { + }$the set of all elements in$\mathcal { F } _ { F } ^ { + }$of the form$X ^ { k } \prod _ { i } { \mathcal { T } } _ { \ell _ { i } } { \boldsymbol { \tau } } _ { i }$, for some multiindices$k$and$\ell _ { i }$such that$| { \mathcal { I } } _ { \ell _ { i } } \tau _ { i } | _ { \mathfrak { s } } > 0 .$Q, and where the elements$\tau _ { i }$all belong to . (The empty product also counts, so that one always has$X ^ { k } \in \operatorname { A l g } ( { \mathcal { C } } )$and in particular$\mathbf { 1 } \in \mathrm { A l g } ( { \mathcal { C } } ) . )$We will also use the notation for the linear span of a set. We now fix a subset$\mathcal { F } _ { 0 } \subset \mathcal { F } _ { F }$as follows.

Assumption 8.33 The set$\mathcal { F } _ { 0 } \subset \mathcal { F } _ { F }$has the following properties:

The set$\mathcal { F } _ { 0 }$contains every$\tau \in \mathcal { F } _ { F }$with$| \tau | _ { \mathfrak { s } } \le 0$

There exists$\mathcal { F } _ { \star } ~ \subset ~ \mathcal { F } _ { 0 }$such that, for every$\tau \in \mathcal { F } _ { 0 }$, one has$\Delta \tau \in \langle F _ { 0 } \rangle$⊗ $\langle \mathrm { A l g } ( \mathcal { F } _ { \star } ) \rangle$.

Remark 8.34 Similarly to before, we write$\mathcal { H } _ { 0 } = \langle \mathcal { F } _ { 0 } \rangle , \mathcal { F } _ { 0 } ^ { + } = \mathrm { A l g } ( \mathcal { F } _ { \star } )$, and$\mathcal { H } _ { 0 } ^ { + } =$ $\langle \mathcal { F } _ { 0 } ^ { + } \rangle$. Proceeding as in the proofs of Lemmas 8.38 and$8 . 3 9$below, one can verify that the second condition automatically implies that the operators$\Delta ^ { + }$and both leave$\mathcal { H } _ { 0 } ^ { + }$ invariant.

Let now$M \colon \mathcal { H } _ { 0 } \  \ \mathcal { H } _ { 0 }$be a linear map such that$M \mathbb { Z } _ { k } \tau = \mathbb { Z } _ { k } M \tau$for every $\tau \in \mathcal { F } _ { 0 }$such that$\mathcal { T } _ { k } \tau \in \mathcal { F } _ { 0 }$. Then, we would like to use the map M to build a new model$( { \mathbf { \Pi } } ^ { \phantom { \dagger } } \pi ^ { M } , f ^ { M } )$with the property that

$$
\boldsymbol {\Pi} ^ {M} \boldsymbol {\tau} = \boldsymbol {\Pi} M \boldsymbol {\tau}.\tag{8.33}
$$

(The condition$M \mathcal { L } _ { k } \tau = \mathcal { T } _ { k } M \tau$is required to guarantee that (8.31) still holds for$\mathbf { I I } ^ { M } . )$ This is not always possible, but the aim of this section is to provide conditions under which it is. In order to realise the above identity, we would like to build linear maps $\Delta ^ { M } \colon \mathcal { H } _ { 0 } \to \mathcal { H } _ { 0 } \times \mathcal { H } _ { 0 } ^ { + }$and$\hat { M } : \mathcal { H } _ { 0 } ^ { + } \to \mathcal { H } _ { 0 } ^ { + }$such that one has

$$
\Pi_ {x} ^ {M} \tau = (\Pi_ {x} \otimes f _ {x}) \Delta^ {M} \tau , \qquad f _ {x} ^ {M} \tau = f _ {x} \hat {M} \tau .\tag{8.34}
$$

Remark 8.35 One might wonder why we choose to make the ansatz (8.34). The first identity really just states that$\Pi _ { x } ^ { M } \tau$is given by a bilinear expression of the type

$$
\Pi_ {x} ^ {M} \tau = \sum_ {\tau_ {1}, \tau_ {2}} C _ {\tau} ^ {\tau_ {1}, \tau_ {2}} f _ {x} (\tau_ {1}) \Pi_ {x} \tau_ {2},
$$

which is not unreasonable since the objects appearing on the right hand side are the only objects available as “building blocks” for our construction. One might argue that the coefficients could be given by some polynomial expression in the$f _ { x } ( \tau _ { 1 } )$, but thanks to the fact that$f _ { x }$is group-like, this can always be reformulated as a linear expression. Similarly, the second expression simply states that$f _ { x } ^ { M }$is given by some arbitrary linear (or polynomial by the same argument as before) expression in the$f _ { x }$

Furthermore, we would like to ensure that if the pair (Π, f) satisfies the identities (8.31) and (8.32), then the pair$( \mathbf { I I } ^ { M } , f ^ { M } )$also satisfies them. Inserting (8.34) into (8.32), we see that this is guaranteed if we impose that

$$
\hat {M} \mathcal {J} _ {k} = \mathcal {M} (\mathcal {J} _ {k} \otimes I) \Delta^ {M},\tag{8.35a}
$$

where, as before,$\mathcal { M } \colon \mathcal { H } _ { 0 } ^ { + } \times \mathcal { H } _ { 0 } ^ { + } \to \mathcal { H } _ { 0 } ^ { + }$denotes the multiplication map. We also note that if we want to ensure that$_ { ( 8 . 3 3 ) }$holds, then we should require that, for every x $\mathbf { R } ^ { d }$, one has the identity$\mathbf { I I } \boldsymbol { M } = \bar { \Pi } _ { \boldsymbol { x } } ^ { M } ( F _ { \boldsymbol { x } } ^ { M } ) ^ { - 1 }$, which we rewrite as$\Pi _ { x } ^ { M } = \mathbf { \Pi } \mathbf { \bar { I } } \bar { M } F _ { x } ^ { M }$ Making use of the first identity of (8.34) and of the fact that$\Pi _ { x } = \Pi F _ { x }$, the left hand side of this identity can be expressed as

$$
\Pi_ {x} ^ {M} \tau = (\Pi \otimes f _ {x} \otimes f _ {x}) (\Delta \otimes I) \Delta^ {M} \tau = (\Pi \otimes f _ {x}) (I \otimes \mathcal {M}) (\Delta \otimes I) \Delta^ {M} \tau .
$$

Using the second identity of (8.34), the right hand side on the other hand can be rewritten as

$$
\boldsymbol {\Pi} M F _ {x} ^ {M} \tau = (\boldsymbol {\Pi} \otimes f _ {x} ^ {M}) (M \otimes I) \Delta \tau = (\boldsymbol {\Pi} \otimes f _ {x}) (M \otimes \hat {M}) \Delta \tau .
$$

We see that these two expressions are guaranteed to be equal for any choice of Π and $f _ { x }$if we impose the consistency condition

$$
(I \otimes \mathcal {M}) (\Delta \otimes I) \Delta^ {M} = (M \otimes \hat {M}) \Delta .\tag{8.35b}
$$

Finally, we impose that$\hat { M }$is a multiplicative morphism and that it leaves$X ^ { k }$invariant, namely that

$$
\hat {M} (\tau_ {1} \tau_ {2}) = (\hat {M} \tau_ {1}) (\hat {M} \tau_ {2}), \quad \hat {M} X ^ {k} = X ^ {k},\tag{8.35c}
$$

which is a natural condition given its interpretation. In view of (8.34), this is required to ensure that$f _ { x } ^ { M }$is again a group-like element with$f _ { x } ^ { M } ( X _ { i } ) = - x _ { i }$, which is crucial for our purpose. It then turns out that equations (8.35a)–(8.35c) are sufficient to uniquely characterise$\Delta ^ { M }$and$\hat { M }$and that it is always possible to find two operators satisfying these constraints:

Proposition 8.36 Given a linear map M as above, there exists a unique choice of M<sup>ˆ</sup> and$\Delta ^ { M }$satisfying (8.35a)–(8.35c).

In order to prove this result, it turns out to be convenient to consider the following recursive construction of elements in$\mathcal { H } _ { F }$. We define$\mathcal { F } ^ { ( 0 ) } = \emptyset$and then, recursively,

$$
\mathcal {F} ^ {(n + 1)} = \left\{\tau \in \mathcal {F} _ {F}: \Delta \tau \in \mathcal {H} _ {F} \otimes \left\langle \operatorname{Alg} (\mathcal {F} ^ {(n)}) \right\rangle \right\}.\tag{8.36}
$$

Remark 8.37 In practice, a typical choice for the set$\mathcal { F } _ { 0 }$of Assumption 8.33 is to take ${ \mathcal { F } } _ { 0 } = { \mathcal { F } } ^ { ( n ) }$and$\mathcal { F } _ { \star } = \mathcal { F } ^ { ( n - 1 ) }$for some sufficiently large$n ,$, which then automatically has the required properties by Lemma 8.38 below. In particular, this also shows that such sets do exist.

For example,$\mathcal { F } ^ { ( 1 ) }$contains all elements of the form$\Xi ^ { n } X ^ { k }$that belong to$\mathcal { F } _ { F }$, but it might contain more than that depending on the values of α and$\beta .$. The following properties of these sets are elementary:

One has$\mathcal { F } ^ { ( n - 1 ) } \subset \mathcal { F } ^ { ( n ) }$. This is shown by induction. For$n = 1$, the statement is trivially true. If it holds for some n then one has$\mathsf { A l g } ( \mathcal { F } ^ { ( n - 1 ) } ) \subset \mathsf { A l g } ( \mathcal { F } ^ { ( n ) } )$ and so, by (8.36), one also has${ \mathcal { F } } ^ { ( n ) } \subset { \mathcal { F } } ^ { ( n + 1 ) }$<sup>)</sup>, as required.

If$\tau , \bar { \tau } \in \mathcal { F } ^ { ( n ) }$are such that$\tau { \bar { \tau } } \in \mathcal { F } _ { F }$, then$\tau \bar { \tau } \in \mathcal { F } ^ { ( n ) }$as an immediate consequence of the morphism property of$\Delta$, combined with the definition of$\mathrm { A l g }$

$\mathrm { I f } \tau \in \mathcal { F } ^ { ( n ) }$and k is such that$\mathcal { T } _ { k } \tau \in \mathcal { F } _ { F }$, then$\mathcal { T } _ { k } \tau \in \mathcal { F } ^ { ( n + 1 ) }$. As a consequence of this fact, and since all elements in$\mathcal { F } _ { F }$can be generated by multiplication and integration from$\Xi$and the$X _ { i } ,$, one has$\textstyle \bigcup _ { n > 0 } { \mathcal { F } } ^ { ( n ) } = { \mathcal { F } } _ { F }$

The following consequence is slightly less obvious:

Lemma 8.38 For every$n \geq 0$and$\tau \in \mathcal { F } ^ { ( n ) }$, one has$\Delta \tau \in \langle \mathcal { F } ^ { ( n ) } \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n - 1 ) } ) \rangle$ For every$n \geq 0$and$\tau \in \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } )$, one has$\Delta ^ { + } \tau \in \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle$

Proof. We proceed by induction. For$n = 0$, both statements are trivially true, so we assume that they hold for all$n \leq k .$. Take then$\tau \in \mathcal { F } ^ { ( k + 1 ) }$and assume by contradiction that$\Delta \tau \ \not \in \ \langle { \mathcal { F } } ^ { ( k + 1 ) } \rangle \otimes \langle \mathrm { A l g } ( { \mathcal { F } } ^ { ( k ) } ) \rangle$. This then implies that$( \Delta \otimes I ) \Delta \tau \notin$ $\mathcal { H } _ { F } \otimes \left. \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \right. \otimes \left. \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \right.$. However, we have$( \Delta \otimes I ) \Delta \tau = ( I \otimes \Delta ^ { + } ) \Delta \tau$by Theorem 8.16 and$\Delta ^ { + }$maps$\langle \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \rangle$to$\langle \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \rangle$by our induction hypothesis, thus yielding the required contradiction.

It remains to show that$\Delta ^ { + }$has the desired property for$n = k + 1$. Since$\Delta ^ { + }$is a multiplicative morphism, we can assume that τ is of the form$\tau = \mathcal { T } _ { \ell } \bar { \tau }$with$\bar { \tau } \in \mathcal { F } ^ { ( k + 1 ) }$ One then has by definition

$$
\Delta^ {+} \tau = \sum_ {m} \left(\mathcal {J} _ {\ell + m} \otimes \frac {(- X) ^ {m}}{m !}\right) \Delta \bar {\tau} + \mathbf {1} \otimes \tau .
$$

By the first part of the proof, we already know that$\Delta \bar { \tau } \in \langle \mathcal { F } ^ { ( k + 1 ) } \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( k ) } ) \rangle$, so that the first term belongs to$\langle \operatorname { A l g } ( { \mathcal { F } } ^ { ( k + 1 ) } ) \rangle \otimes \langle \operatorname { A l g } ( { \mathcal { F } } ^ { ( k ) } ) \rangle$. The second term on the other hand belongs to$\big \langle \mathrm { A l g } ( \bar { \mathcal { F } } ^ { ( 0 ) } ) \big \rangle \bigotimes \big \langle \mathrm { A l g } ( \mathcal { F } ^ { ( k + 1 ) } ) \big \rangle$by definition, so that the claim follows.

A useful consequence of Lemma 8.38 is the following.

Lemma 8.39$I f \tau \in \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } )$for some$n \geq 0 ,$, then$\mathcal { A } \tau \in \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle$, where is the antipode in$\mathcal { H } _ { + }$defined in the previous subsection.

Proof. The proof goes by induction, using the relations$\mathcal { A } ( \tau \bar { \tau } ) = \mathcal { A } ( \tau ) \mathcal { A } ( \bar { \tau } )$, as well as the identity

$$
\mathcal {A} \mathcal {J} _ {k} \bar {\tau} = - \sum_ {\ell} \mathcal {M} \left(\mathcal {J} _ {k + \ell} \otimes \frac {X ^ {\ell}}{\ell !} \mathcal {A}\right) \Delta \bar {\tau},\tag{8.37}
$$

which is valid as soon as$| { \mathcal { I } } _ { k } { \bar { \tau } } | _ { \mathfrak { s } } > 0$. For$n = 0 ,$, the claim is trivially true. For arbitrary$n > 0 .$, by the multiplicative property of${ \mathcal { A } } ,$, it suffices to consider the case $\tau = \mathcal { T } _ { k } \bar { \tau }$with$\bar { \tau } \in \mathcal { F } ^ { ( n ) }$. Since$\Delta \bar { \tau } \ \in \ \langle \bar { \mathcal { F } } ^ { ( n ) } \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n - 1 ) } ) \rangle$by Lemma 8.38, it follows from our definitions and the inductive assumption that the right hand side of (8.37) does indeed belong to$\langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle$i <sup>as</sup> <sup>required.</sup>□

We now have all the ingredients in place for the

ProofofProposition 8.36. We first introduce the map$D \colon \mathcal { H } _ { 0 } \otimes \mathcal { H } _ { 0 } ^ { + } \to \mathcal { H } _ { 0 } \otimes \mathcal { H } _ { 0 } ^ { + }$given by$D = ( I \otimes \mathcal { M } ) ( \Delta \otimes I )$. It follows immediately from the definition of$\Delta$and the fact that, by Lemma 8.10, homogeneities of elements in$\mathcal { F } _ { F }$(and a fortiori of elements in $\mathcal { F } _ { \mathrm { 0 } } )$are bounded from below, that D can be written as

$$
D (\tau \otimes \bar {\tau}) = \tau \otimes \bar {\tau} - \bar {D} (\tau \otimes \bar {\tau}),
$$

for some nilpotent map$\bar { D } . \mathrm { { A s } }$a consequence,$D$is invertible with inverse given by the Neumann series$\begin{array} { r } { D ^ { - 1 } = \sum _ { k > 0 } \hat { D } ^ { k } } \end{array}$, which is always finite.

The proof of the statement then goes by induction over${ \mathcal { F } } ^ { ( n ) } \cap { \mathcal { F } } _ { 0 }$. Assume that$\hat { M }$ and$\Delta ^ { M }$are uniquely defined on$\bar { \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } \cap \mathcal { F } _ { \star } ) }$and on$\mathcal { F } ^ { ( n ) } \cap \mathcal { F } _ { 0 }$respectively which, by$( 8 . 3 5 \mathrm { c } )$, is trivially true for$n = 0$. (For$\Delta ^ { M }$this is also trivial since$\mathcal { F } ^ { ( 0 ) }$is empty.) Take then$\tau \in \mathcal { F } ^ { ( n + 1 ) } \cap \mathcal { F } _ { 0 }$. By (8.35b), one has

$$
\Delta^ {M} \tau = D ^ {- 1} (M \otimes \hat {M}) \Delta \tau .
$$

By Lemma 8.38 and Remark 8.34, the second factor of$\Delta \tau$belongs to$\langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } \cap \mathcal { F } _ { \star } ) \rangle$ on which M<sup>ˆ</sup> is already known by assumption, so that this uniquely determines$\Delta ^ { M } \tau$

On the other hand, in order to determine M<sup>ˆ</sup> on elements of$\mathrm { A l g } ( \mathcal { F } ^ { ( n + 1 ) } \cap \mathcal { F } _ { \star } )$it suffices by (8.35c) and Remark 8.34 to determine it on elements of the form$\tau = \mathcal { I } _ { k } \bar { \tau }$ with$\bar { \tau } \in \mathcal { F } ^ { ( n + 1 ) } \cap \mathcal { F } _ { \star }$. The action of M<sup>ˆ</sup> on such elements is determined by (8.35a) so that, since we already know by the first part of the proof that$\Delta ^ { M } \bar { \tau }$is uniquely determined, the proof is complete.□

Before we proceed, we introduce a final object whose utility will be clear later on. Similarly do the definition of$\Delta ^ { M }$, we define$\hat { \Delta } ^ { M } : \mathcal { H } _ { 0 } ^ { + } \to \mathcal { H } _ { 0 } ^ { + } \overset { \cdot } { \otimes } \mathcal { H } _ { 0 } ^ { + }$by the identity

$$
(\mathcal {A} \hat {M} \mathcal {A} \otimes \hat {M}) \Delta^ {+} = (I \otimes \mathcal {M}) (\Delta^ {+} \otimes I) \hat {\Delta} ^ {M}.\tag{8.38}
$$

Note that, similarly to before, one can verify that the map$D ^ { + } = ( I \otimes \mathcal { M } ) ( \Delta ^ { + } \otimes I )$is invertible on$\mathcal { H } _ { 0 } ^ { + } \otimes \mathcal { H } _ { 0 } ^ { + }$, so that this expression does indeed define$\hat { \Delta } ^ { M }$uniquely.

Remark 8.40 Note also that in the particular case when$M = I ,$, the identity, one has $\Delta ^ { M } \tau = \tau \otimes { \mathbf { 1 } } , \hat { \Delta } ^ { M } \tau = \tau \otimes { \mathbf { 1 } }$, as well as$\hat { M } = I$

With these notations at hand, we then give the following description of the “renormalisation group” R:

Definition 8.41 Let$\mathcal { F } _ { F }$and$\mathcal { F } _ { 0 }$be as above. Then the corresponding renormalisation group R consists of all linear maps$M \colon \mathcal { H } _ { 0 } \to \mathcal { H } _ { 0 }$such that M commutes with the$\mathcal { T } _ { k } .$ such that$M X ^ { k } = X ^ { k }$, and such that, for every$\tau \in \mathcal { F } _ { 0 }$and every$\hat { \tau } \in \mathcal { F } _ { 0 } ^ { + }$, one can write

$$
\Delta^ {M} \tau = \tau \otimes {\bf 1} + \sum \tau^ {(1)} \otimes \tau^ {(2)}, \quad \hat {\Delta} ^ {M} \bar {\tau} = \bar {\tau} \otimes {\bf 1} + \sum \bar {\tau} ^ {(1)} \otimes \bar {\tau} ^ {(2)},\tag{8.39}
$$

where each of the$\tau ^ { ( 1 ) } \in \mathcal { F } _ { 0 }$and$\bar { \tau } ^ { ( 1 ) } \in \mathcal { F } _ { 0 } ^ { + }$is such that$\vert \tau ^ { ( 1 ) } \vert _ { \mathfrak { s } } > \vert \tau \vert _ { \mathfrak { s } }$and$\left| \bar { \tau } ^ { ( 1 ) } \right| _ { \mathfrak { s } } > | \bar { \tau } | _ { \mathfrak { s } } .$

Remark 8.42 Note that$\hat { \Delta } ^ { M }$is automatically a multiplicative morphism. Since one has furthermore$\hat { \Delta } ^ { M } X ^ { k } = X ^ { k } \otimes$1 for every M, the second condition in (8.39) really needs to be verified only for elements of the form$\mathcal { T } _ { k } ( \tau )$with$\tau \in \mathcal { F } _ { \star }$. The reason for introducing the quantity$\hat { \Delta } ^ { M }$and defining R in this way is that these conditions appear naturally in Theorem 8.44 below where we check that the renormalised model defined by (8.34) does again satisfy the analytical bounds of Definition 2.17.

We first verify that our terminology is not misleading, namely that R really is a group:

Lemma 8.43$H f M _ { 1 } , M _ { 2 } \ \in \ \Re ,$, then$M _ { 1 } M _ { 2 } \ \in \ \Re .$. Furthermore, if$M \in \Re ,$then $M ^ { - 1 } \in \Re$

Proof. Note first that if$M = M _ { 1 } M _ { 2 }$then, due to the identity$\mathbf { I } \mathbf { I } ^ { M } = \mathbf { I } \mathbf { I } M _ { 1 } M _ { 2 }$, one obtains the model$( \mathbf { I I } ^ { M } , F ^ { M } )$by applying the group element corresponding to$M _ { 2 }$ $( \mathbf { I I } ^ { M _ { 1 } } , F ^ { M _ { 1 } } )$. As a consequence, one can “guess” the identities

$$
\Delta^ {M} = (I \otimes \mathcal {M}) (\Delta^ {M _ {1}} \otimes \hat {M} _ {1}) \Delta^ {M _ {2}},\tag{8.40a}
$$

$$
\hat {\Delta} ^ {M} = (I \otimes \mathcal {M}) (\hat {\Delta} ^ {M _ {1}} \otimes \hat {M} _ {1}) \hat {\Delta} ^ {M _ {2}},\tag{8.40b}
$$

$$
\hat {M} = \hat {M} _ {1} \hat {M} _ {2}.\tag{8.40c}
$$

Since we know that (8.35) characterises$\Delta ^ { M }$and$\hat { M }$, (8.40) can be verified by checking that$\Delta ^ { M }$and M<sup>ˆ</sup> defined in this way do indeed satisfy (8.35). The identity (8.35c) is immediate, so we concentrate on the two other ones.

For (8.35a), we have

$$
\begin{array}{c} \mathcal {M} (\mathcal {J} _ {k} \otimes I) \Delta^ {M} = \mathcal {M} ((\mathcal {J} _ {k} \otimes I) \Delta^ {M _ {1}} \otimes \hat {M} _ {1}) \Delta^ {M _ {2}} \\ = \mathcal {M} (\hat {M} _ {1} \mathcal {J} _ {k} \otimes \hat {M} _ {1}) \Delta^ {M _ {2}} \\ = \hat {M} _ {1} \mathcal {M} (\mathcal {J} _ {k} \otimes I) \Delta^ {M _ {2}} = \hat {M} _ {1} \hat {M} _ {2} \mathcal {J} _ {k}, \end{array}
$$

which is indeed the required property. Here, we made use of the morphism property of $\hat { M } _ { 1 }$to go from the second to the third line.

For (8.35b), we use (8.40a) to obtain

$$
\begin{array}{l} (I \otimes \mathcal {M}) (\Delta \otimes I) \Delta^ {M} = (I \otimes \mathcal {M}) (\Delta \otimes I) (I \otimes \mathcal {M}) (\Delta^ {M _ {1}} \otimes \hat {M _ {1}}) \Delta^ {M _ {2}} \\ \qquad = (I \otimes \mathcal {M}) ((M _ {1} \otimes \hat {M _ {1}}) \Delta \otimes \hat {M _ {1}}) \Delta^ {M _ {2}} \\ \qquad = (M _ {1} \otimes \hat {M _ {1}}) (I \otimes \mathcal {M}) (\Delta \otimes I) \Delta^ {M _ {2}} \\ \qquad = (M _ {1} \otimes \hat {M _ {1}}) (M _ {2} \otimes \hat {M _ {2}}) \Delta = (M \otimes \hat {M}) \Delta , \end{array}
$$

as required. Here, we used again the morphism property of$\hat { M } _ { 1 }$to go from the second to the third line. We also used the fact that, by assumption, (8.35b) holds for both$M _ { 1 }$ and$M _ { 2 }$. Finally, we want to verify that the expression (8.40b) for$\hat { \Delta } ^ { M }$is the correct one. For this, it suffices to proceed in virtually the same way as for$\Delta ^ { M }$, replacing$\Delta$ by ∆<sup>ˆ</sup> when needed.

To show that R is a group and not just a semigroup, we first define, for any$\kappa \in \mathbf { R }$ the projection$\mathcal { P } _ { \kappa } \colon \mathcal { H } _ { 0 } \to \mathcal { H } _ { 0 }$given by${ \mathcal { P } } _ { \kappa } \tau = 0 \mathrm { i f } | \tau | _ { \mathfrak { s } } >$κ and${ \mathcal { P } } _ { \kappa } \tau = \tau \operatorname { i f } | \tau | _ { \mathfrak { s } } \leq \kappa$ We also write$\hat { \mathcal { P } } _ { \kappa } = \mathcal { P } _ { \kappa } \otimes I$as a shorthand. We then argue by contradiction as follows. Assuming that$M ^ { - 1 } \not \in \Re$, one of the two conditions in (8.39) must be violated. Assume first that it is the first one, then there exists${ \mathrm { a } } \tau \in \mathcal { F } _ { 0 }$and a homogeneity$\kappa \leq | \tau | _ { \mathfrak { s } } ,$, such that$\Delta ^ { M ^ { - 1 } }$τ can be rewritten as

$$
\Delta^ {M ^ {- 1}} \tau = R _ {-} ^ {M} \tau + R _ {+} ^ {M} \tau ,
$$

with$\hat { \mathcal { P } } _ { \kappa } R _ { - } ^ { M } \tau = R _ { - } ^ { M } \tau \neq 0 , \hat { \mathcal { P } } _ { \kappa } R _ { + } ^ { M } \tau = 0$, and$R _ { - } ^ { M } \tau \neq \tau \otimes { \bf 1 }$. We furthermore choose for κ the smallest possible value such that such a decomposition exists, i.e. we assume that$\hat { \mathcal { P } } _ { \bar { \kappa } } R _ { - } ^ { M } \tau = 0$for every$\bar { \kappa } < \kappa$

It follows from (8.40a) that one has

$$
\hat {\mathcal {P}} _ {\kappa} (\tau \otimes \mathbf {1}) = \hat {\mathcal {P}} _ {\kappa} \Delta^ {I} \tau = (I \otimes \mathcal {M}) (\hat {\mathcal {P}} _ {\kappa} \Delta^ {M} \otimes \mathcal {M} \hat {\Delta} ^ {M}) \Delta^ {M ^ {- 1}} \tau .
$$

Since, by Definition 8.41, the identity$\hat { \mathcal { P } } _ { \kappa } \Delta ^ { M } \bar { \tau } = \hat { \mathcal { P } } _ { \kappa } ( \bar { \tau } \otimes { \bf 1 } )$holds as soon as$| \bar { \tau } | _ { \mathfrak { s } } \geq \kappa$ one eventually obtains

$$
\hat {\mathcal {P}} _ {\kappa} (\tau \otimes \mathbf {1}) = R _ {-} ^ {M} \tau ,
$$

which is a contradiction. Therefore, the only way in which one could have$M ^ { - 1 } \not \in \Re$ is by violating the second condition in (8.39). This however can also be ruled out in almost exactly the same way, by making use of (8.40b) instead of (8.40a) and exploiting the fact that one also has$\hat { \Delta } ^ { I } \tau = \tau \otimes { \bf 1 }$□

The main result in this section states that any transformation$M \ \in \ \mathfrak { R }$extends canonically to a transformation on the set of admissible models for$\mathcal { T } _ { F } ^ { ( r ) }$for arbitrary $r > 0$

Theorem 8.44 Let$M \in { \mathfrak { R } } ,$, where R is as in Definition 8.41, let$r > 0$be such that the kernel K annihilatespolynomials ofdegree$^ { r , }$and let$( \Pi , f ) \sim ( \Pi , \Gamma )$be an admissible model for$\mathcal { T } _ { F } ^ { ( r ) }$with f and Γ related as in (8.29).

Define$\bar { \Pi } _ { x } ^ { M }$and$f ^ { M }$on$\mathcal { H } _ { \mathrm { 0 } }$and$\mathcal { H } _ { 0 } ^ { + }$as in (8.34) and define$\Gamma ^ { M }$via (8.29). Then, $( \Pi ^ { M } , \dot { \Gamma } ^ { M } )$is an admissible model$f o r ~ \mathcal { T } _ { F }$on$\mathcal { H } _ { 0 } .$. Furthermore, it extends uniquely to an admissible modelfor all of$\mathcal { T } _ { F } ^ { ( r ) }$

Proof. We first verify that the renormalised model does indeed yield a model for$\mathcal { T } _ { F }$ on$\mathcal { H } _ { \mathrm { 0 } }$. For this, it suffices to show that the bounds (2.15) hold. Regarding the bound on$\Pi _ { x } ^ { M }$, recall the first identity of (8.34). As a consequence of Definition 8.41, this implies that$( \Pi _ { x } ^ { M } \tau ) ( \varphi _ { x } ^ { \lambda } )$can be written as a finite linear combination of terms of the type$( \Pi _ { x } \hat { \tau } ) ( \varphi _ { x } ^ { \lambda } )$with$| \bar { \tau } | _ { s } \geq | \tau | _ { s }$. The required scaling as a function of λ then follows at once.

Regarding the bounds on$\Gamma _ { x y } ,$recall that$\Gamma _ { x y } \tau = ( I \otimes \gamma _ { x y } ) \Delta \tau$with

$$
\gamma_ {x y} = (f _ {x} \mathcal {A} \otimes f _ {y}) \Delta^ {+},\tag{8.41}
$$

and similarly for$\gamma _ { x y } ^ { M }$. Since we know that (Π, Γ) is a model for$\mathcal { T } _ { F } ^ { ( r ) }$, this implies that one has the bound

$$
\left| \gamma_ {x y} \tau \right| \lesssim \| x - y \| _ {\mathfrak {s}} ^ {| \tau | _ {\mathfrak {s}}},\tag{8.42}
$$

and we aim to obtain a similar bound for$\gamma _ { x y } ^ { M }$. Recalling the definitions (8.41) as well as (8.34), we obtain for$\gamma _ { x y } ^ { M }$the identity

$$
\begin{array}{c} \gamma_ {x y} ^ {M} = (f _ {x} \mathcal {A} \otimes f _ {y}) (\mathcal {A} \hat {M} \mathcal {A} \otimes \hat {M}) \Delta^ {+} = (f _ {x} \mathcal {A} \otimes f _ {y}) (I \otimes \mathcal {M}) (\Delta^ {+} \otimes I) \hat {\Delta} ^ {M} \\ = (f _ {x} \mathcal {A} \otimes f _ {y} \otimes f _ {y}) (\Delta^ {+} \otimes I) \hat {\Delta} ^ {M} = (\gamma_ {x y} \otimes f _ {y}) \hat {\Delta} ^ {M}, \end{array}
$$

where the second equality is the definition of$\hat { \Delta } ^ { M }$, while the last equality uses the definition of$\gamma _ { x y }$, combined with the morphism property of$f _ { y }$. It then follows immediately from Definition 8.41 and (8.42) that the bound (8.42) also holds for$\gamma _ { x y } ^ { M }$

Finally, we have already seen that if (Π, Γ) is admissible, then$\Pi _ { x } ^ { M }$and$f _ { x } ^ { M }$satisfy the identities (8.31) and (8.32) as a consequence of (8.35a), so that they also form an admissible model. The fact that the model$( \Pi ^ { M } , \Gamma ^ { M } )$) extends uniquely (and continuously) to all of$\mathcal { T } _ { F } ^ { ( r ) }$follows from a repeated application of Theorem 5.14 and Proposition 3.31.□

Remark 8.45 In principle, the construction of R given in this section depends on the choice of a suitable set$\mathcal { F } _ { 0 }$. It is natural to conjecture that R does not actually depend on this choice (at least if$\mathcal { F } _ { 0 }$is sufficiently large), but it is not clear at this stage whether there is a simple algebraic proof of this fact.

## 9 Two concrete renormalisation procedures

In this section, we show how the regularity structure and renormalisation group built in the previous section can be used concretely to renormalise (PAMg) and$( \Phi ^ { 4 } )$.

## 9.1 Renormalisation group for (PAMg)

Consider the regularity structure generated by (PAMg) with${ \mathfrak { M } } _ { F }$as in Remark 8.8, $\beta = 2$, and$\alpha \in ( - \frac { 4 } { 3 } , - 1 )$. In this case, we can choose

$$
\mathcal {F} _ {0} = \left\{\mathbf {1}, \Xi , X _ {i} \Xi , \mathcal {I} (\Xi) \Xi , \mathcal {I} _ {i} (\Xi), \mathcal {I} _ {i} (\Xi) \mathcal {I} _ {j} (\Xi) \right\}, \quad \mathcal {F} _ {\star} = \left\{\Xi \right\},
$$

where i and j denote one of the two spatial coordinates. It is straightforward to check that this set satisfies Assumption 8.33. Indeed, provided that$\alpha \in ( - \frac { 4 } { 3 } , - 1 )$), it does contain all the elements of negative homogeneity. Furthermore, all of the elements $\tau \in \mathcal { F } _ { 0 }$satisfy$\Delta \tau = \tau \otimes { \bf 1 }$, except for$\Xi T ( \Xi )$and$X _ { i } \Xi$which satisfy

$$
\Delta (\Xi \mathcal {I} (\Xi)) = \Xi \mathcal {I} (\Xi) \otimes \mathbf {1} + \Xi \otimes \mathcal {J} (\Xi), \quad \Delta X _ {i} \Xi = X _ {i} \Xi \otimes \mathbf {1} + \Xi \otimes X _ {i}.
$$

It follows that these elements indeed satisfy$\Delta \tau \in { \mathcal { H } } _ { 0 } \otimes { \mathcal { H } } _ { 0 } ^ { + }$, as required by our assumption.

Then, for any constant$C \in \mathbf { R }$and$2 \times 2$matrix$\bar { C } ,$one can define a linear map M on the span of$\mathcal { F } _ { 0 }$by

$$
\begin{array}{c} M \big (\mathcal {I} (\Xi) \Xi \big) = \mathcal {I} (\Xi) \Xi - C \mathbf {1}  , \\ M \big (\mathcal {I} _ {i} (\Xi) \mathcal {I} _ {j} (\Xi) \big) = \mathcal {I} _ {i} (\Xi) \mathcal {I} _ {j} (\Xi) - \bar {C} _ {i j} \mathbf {1}  , \end{array}
$$

as well as$M ( \tau ) = \tau$for the remaining basis vectors in$\mathcal { F } _ { 0 }$. Denote by$\Re _ { 0 }$the set of all linear maps M of this type.

In order to verify that$\Re _ { 0 } \subset \Re$as our notation implies, we need to verify that$\Delta ^ { M }$ and$\hat { \Delta } ^ { M }$satisfy the property required by Definition 8.41. Note first that

$$
\hat {M} \mathcal {I} (\Xi) = \mathcal {I} (\Xi),
$$

as a consequence of (8.35a). Since one furthermore has$\hat { M } X _ { i } = X _ { i }$, this shows that one has

$$
(M \otimes \hat {M}) \Delta \tau = (M \otimes I) \Delta \tau ,
$$

for every$\tau \in \mathcal { F } _ { 0 }$. Furthermore, it is straightforward to verify that$( M \otimes I ) \Delta \tau = \Delta M \tau$ for every$\tau \in \mathcal { F } _ { 0 }$. Comparing this to (8.35b), we conclude that in the special case considered here we actually have the identity

$$
\Delta^ {M} \tau = (M \tau) \otimes \mathbf {1},\tag{9.1}
$$

for every$\tau \in \mathcal { F } _ { 0 }$. Indeed, when plugging (9.1) into the left hand side of (8.35b), we do recover the right hand side, which shows the desired claim since we already know that (8.35b) is sufficient to characterise$\Delta ^ { M }$. Furthermore, it is straightforward to verify that$\hat { \Delta } ^ { M } \mathcal { T } ( \Xi ) = \mathcal { T } ( \Xi )$1 so that, by Remark 8.42, this shows that$M \in \Re$for every choice of the matrix$C _ { i j }$and the constant$\bar { C }$

Furthermore, this 5-parameter subgroup of R is canonically isomorphic to$\mathbf { R } ^ { 5 }$endowed with addition as its group structure. This is the subgroup$\Re _ { 0 }$that will be used to renormalise (PAMg) in Section 9.3.

## 9.2 Renormalisation group for the dynamical$\Phi _ { 3 } ^ { 4 }$model

We now consider the regularity structure generated by$( \Phi ^ { 4 } )$, which is our second main example. Recall from Remark 8.7 that this corresponds to the case where

$$
\mathfrak {M} _ {F} = \left\{\Xi , U ^ {n}: n \leq 3 \right\},
$$

$\beta = 2$and$\alpha < - \frac { 5 } { 2 }$. In order for the relevant terms of negative homogeneity not to depend on$\alpha ,$we will choose$\alpha \in ( - \frac { 1 8 } { 7 } , - \frac { 5 } { 2 } )$. The reason for this strange-looking value$- { \frac { 1 8 } { 7 } }$is that this is precisely the value of α at which, setting$\Psi = \mathcal { I } ( \Xi )$as a shorthand, the homogeneity of the term$\Psi ^ { 2 } \mathcal { T } ( \Psi ^ { 2 } \mathcal { T } ( \Psi ^ { 3 } ) )$vanishes, so that one would have to modify our choice of$\mathcal { F } _ { 0 }$

In this particular case, it turns out that we can choose for$\mathcal { F } _ { 0 }$and$\mathcal { F } _ { \star }$the sets

$$
\begin{array}{c} \mathcal {F} _ {0} = \left\{\mathbf {1}, \Xi , \Psi , \Psi^ {2}, \Psi^ {3}, \Psi^ {2} X _ {i}, \mathcal {I} (\Psi^ {3}) \Psi , \mathcal {I} (\Psi^ {3}) \Psi^ {2}, \right. \\ \left. \mathcal {I} (\Psi^ {2}) \Psi^ {2}, \mathcal {I} (\Psi^ {2}), \mathcal {I} (\Psi) \Psi , \mathcal {I} (\Psi) \Psi^ {2}, X _ {i} \right\}, \quad \mathcal {F} _ {\star} = \left\{\Psi , \Psi^ {2}, \Psi^ {3} \right\}, \end{array}\tag{9.2}
$$

where the index i corresponds again to any of the three spatial directions.

Then, for any two constants$C _ { 1 }$and$C _ { 2 }$, we define a linear map M on$\mathcal { H } _ { \mathrm { 0 } }$by

$$
\begin{array}{c} M \Psi^ {2} = \Psi^ {2} - C _ {1} \mathbf {1}, \\ M (\Psi^ {2} X _ {i}) = \Psi^ {2} X _ {i} - C _ {1} X _ {i}, \\ M \Psi^ {3} = \Psi^ {3} - 3 C _ {1} \Psi , \\ M (\mathcal {I} (\Psi^ {2}) \Psi^ {2}) = \mathcal {I} (\Psi^ {2}) (\Psi^ {2} - C _ {1} \mathbf {1}) - C _ {2} \mathbf {1}, \\ M (\mathcal {I} (\Psi^ {3}) \Psi) = (\mathcal {I} (\Psi^ {3}) - 3 C _ {1} \mathcal {I} (\Psi)) \Psi , \\ M (\mathcal {I} (\Psi^ {3}) \Psi^ {2}) = (\mathcal {I} (\Psi^ {3}) - 3 C _ {1} \mathcal {I} (\Psi)) (\Psi^ {2} - C _ {1} \mathbf {1}) - 3 C _ {2} \Psi , \\ M (\mathcal {I} (\Psi) \Psi^ {2}) = \mathcal {I} (\Psi) (\Psi^ {2} - C _ {1} \mathbf {1}), \end{array}\tag{9.3}
$$

as well as$M \tau = \tau$for the remaining basis elements$\tau \in \mathcal { F } _ { 0 }$. We claim that one has the identity

$$
\Delta^ {M} \tau = (M \tau) \otimes \mathbf {1},\tag{9.4a}
$$

for those elements$\tau \in \mathcal { F } _ { 0 }$which do not contain a factor$\mathcal { T } ( \Psi ^ { 3 } )$. For the remaining two elements, we claim that one has

$$
\Delta^ {M} \mathcal {I} (\Psi^ {3}) \Psi = \left(M (\mathcal {I} (\Psi^ {3}) \Psi)\right) \otimes \mathbf {1} + 3 C _ {1} \Psi X _ {i} \otimes \mathcal {J} _ {i} (\Psi),\tag{9.4b}
$$

$$
\Delta^ {M} \mathcal {I} (\Psi^ {3}) \Psi^ {2} = \left(M (\mathcal {I} (\Psi^ {3}) \Psi^ {2})\right) \otimes \mathbf {1} + 3 C _ {1} \left(\Psi^ {2} - C _ {1} \mathbf {1}\right) X _ {i} \otimes \mathcal {J} _ {i} (\Psi),\tag{9.4c}
$$

where a summation over the spatial components$X _ { i }$is implicit.

For$\tau \in \{ 1 , \Xi , \Psi , \Psi ^ { 2 } , \Psi ^ { 3 } \}$, one has$\Delta \tau = \tau \otimes { \bf 1 } .$, so that$\Delta ^ { M } \tau = ( M \tau ) \otimes \mathbf { 1 }$as a consequence of$( 8 . 3 5 \mathrm { b } )$. Similarly, it can be verified that (9.4a) holds for$\Psi ^ { 2 } X _ { i }$and$X _ { i }$ by using again (8.35b). For the remaining elements, we first note that, as a consequence of this and (8.35a), one has the identities

$$
\hat {M} \mathcal {I} (\Psi^ {n}) = \mathcal {I} (M \Psi^ {n}), \qquad \hat {M} \mathcal {I} _ {i} (\Psi) = \mathcal {I} _ {i} (\Psi).\tag{9.5}
$$

All the remaining elements are of the form$\tau = \mathcal { I } ( \Psi ^ { n } ) \Psi ^ { m }$, so that (8.8) yields the identity

$$
\Delta \tau = \tau \otimes \mathbf {1} + \Psi^ {m} \otimes \mathcal {J} (\Psi^ {n}) + \delta_ {n 1} \bigl (\Psi^ {m} X _ {i} \otimes \mathcal {J} _ {i} (\Psi) + \Psi^ {m} \otimes X _ {i} \mathcal {J} _ {i} (\Psi) \bigr).
$$

As a consequence of this and of (9.5), one has

$$
(M \otimes \hat {M}) \Delta \tau = M \tau \otimes \mathbf {1} + M \Psi^ {m} \otimes \mathcal {J} (M \Psi^ {n})\tag{9.6}
$$

$$
+ \delta_ {n 1} (M \Psi^ {m} \otimes \mathbf {1}) (X _ {i} \otimes \mathcal {J} _ {i} (\Psi) + \mathbf {1} \otimes X _ {i} \mathcal {J} _ {i} (\Psi)).
$$

Furthermore, for each of these elements, one has

$$
M \tau = (M \Psi^ {m}) \mathcal {I} (M \Psi^ {n}) + \bar {\tau},\tag{9.7}
$$

where$\bar { \tau }$is an element such that$\Delta \bar { \tau } = \bar { \tau } \otimes { \bf 1 }$. Combining this with the explicit expression for$M .$, one obtains the identity

$$
\begin{array}{l} \Delta M \tau = M \tau \otimes \mathbf {1} + M \Psi^ {m} \otimes \mathcal {J} (M \Psi^ {n}) \\ \qquad + \delta_ {n 1} (M \Psi^ {m} \otimes \mathbf {1}) (X _ {i} \otimes \mathcal {J} _ {i} (\Psi) + \mathbf {1} \otimes X _ {i} \mathcal {J} _ {i} (\Psi)) \\ \qquad - 3 C _ {1} \delta_ {n 3} (M \Psi^ {m} \otimes \mathbf {1}) (X _ {i} \otimes \mathcal {J} _ {i} (\Psi) + \mathbf {1} \otimes X _ {i} \mathcal {J} _ {i} (\Psi))  . \end{array}
$$

Comparing this expression with (9.6), we conclude in view of (8.35b) that one does indeed have the identity

$$
\Delta^ {M} \tau = M \tau \otimes {\bf 1} + 3 C _ {1} \delta_ {n 3} (M \Psi^ {m}) X _ {i} \otimes \mathcal {J} _ {i} (\Psi)  ,
$$

which is precisely what we claimed. A somewhat lengthy but straightforward calculation along the same lines yields the identities

$$
\begin{array}{c} \Delta^ {+} \mathcal {J} (M \Psi^ {n}) = \mathbf {1} \otimes \mathcal {J} (M \Psi^ {n}) + \mathcal {J} (M \Psi^ {n}) \otimes \mathbf {1} - \delta_ {n 1} \big (\mathcal {J} _ {i} (\Psi) \otimes X _ {i} \big) \\ + 3 C _ {1} \delta_ {n 3} \big (\mathcal {J} _ {i} (\Psi) \otimes X _ {i} \big)  , \end{array}
$$

as well as

$$
\begin{array}{c} (\mathcal {A} \hat {M} \mathcal {A} \otimes \hat {M}) \Delta^ {+} \mathcal {J} (\Psi^ {n}) = \mathbf {1} \otimes \mathcal {J} (M \Psi^ {n}) + \mathcal {J} (M \Psi^ {n}) \otimes \mathbf {1} - \delta_ {n 1} \bigl (\mathcal {J} _ {i} (\Psi) \otimes X _ {i} \bigr) \\ - 3 C _ {1} \delta_ {n 3} \bigl (X _ {i} \mathcal {J} _ {i} (\Psi) \otimes \mathbf {1} \bigr). \end{array}
$$

Comparing these two expressions with (8.38), it follows that$\hat { \Delta } ^ { M }$is given by

$$
\hat {\Delta} ^ {M} \mathcal {J} (\Psi^ {n}) = \mathcal {J} (M \Psi^ {n}) \otimes \mathbf {1} + 3 C _ {1} \delta_ {n 3} \left(X _ {i} \otimes \mathcal {J} _ {i} (\Psi) - X _ {i} \mathcal {J} _ {i} (\Psi) \otimes \mathbf {1}\right).
$$

As a consequence of the expressions we just computed for$\Delta ^ { M }$and$\hat { \Delta } ^ { M }$and of the definition of$M$, this shows that one does indeed have$M \in \Re$. Furthermore, it is immediate to verify that this two-parameter subgroup is canonically isomorphic to${ \bf R } ^ { 2 }$ endowed with addition as its group structure. This is the subgroup$\Re _ { 0 } \subset \Re$that will be used to renormalise$( \Phi ^ { 4 } )$in Section 10.5.

## 9.3 Renormalised equations for (PAMg)

We now have all the tools required to formulate renormalisation procedures for the examples given in the introduction. We give some details only for the cases of (PAMg) and$( \Phi ^ { 4 } )$, but it is clearly possible to obtain analogous statements for all the other examples.

The precise statement of our convergence results has to account for the possibility of finite-time blow-up. (In the case of the 3D Navier-Stokes equations, the existence or absence of such a blow-up is of course a famous open problem even in the absence of forcing, which is something that we definitely do not address here.) The aim of this section is to show what the effect of the renormalisation group$\Re _ { 0 }$built in Section 9.1 is, when applied to a model used to solve (PAMg).

Recall that the right hand side of$\left( \mathrm { P A M g } \right)$is given by

$$
f _ {i j} (u) \partial_ {i} u \partial_ {j} u + g (u) \xi ,
$$

and that the set of monomials${ \mathfrak { M } } _ { F }$associated with this right hand side is given by

$$
\mathfrak {M} _ {F} = \left\{U ^ {n}, U ^ {n} \Xi , U ^ {n} \mathcal {P} _ {i}, U ^ {n} \mathcal {P} _ {i} \mathcal {P} _ {j}: n \geq 0, i, j \in \{1, 2 \} \right\}.
$$

We now let$\mathcal { T } _ { F }$be the regularity structure associated to${ \mathfrak { M } } _ { F }$via Theorem 8.24 with $d = 3 , \mathfrak { s } = ( 2 , 1 , 1 ) , \alpha = | \Xi | _ { \mathfrak { s } } \in ( - \frac { 4 } { 3 } , - 1 )$, and$\beta = 2$. As already mention when we built it, the regularity structure$\mathcal { T } _ { F }$comes with a sector$V = \langle \mathcal { U } _ { F } \rangle \subset T$which is given by the direct sum of the abstract polynomials$\bar { T }$with the image of :

$$
V = \mathcal {I} (T) \oplus \bar {T}.\tag{9.8}
$$

Since the element in$\mathcal { F } _ { F }$with the lowest homogeneity is$\Xi ,$the sector$V$is functionlike and elements$u \in { \mathcal { D } } ^ { \gamma } ( V )$with$\gamma > 0$satisfy$\mathcal { R } u \stackrel { \cdot } { \in } \mathcal { C } ^ { \gamma \wedge ( \alpha + 2 ) _ { s } }$. Furthermore, the sector$V$comes equipped with differentiation maps$\mathcal { D } _ { i }$given by$\mathcal { D } _ { i } \boldsymbol { \mathcal { T } } ( \tau ) = \boldsymbol { \mathcal { T } } _ { i } ( \tau )$and $\mathcal { D } _ { i } X ^ { k } = k _ { i } X ^ { k - e _ { i } }$. It follows immediately from the definitions that any admissible model is compatible with these differentiation maps in the sense of Definition 5.26.

Assume for simplicity that the symmetry$\mathcal { S }$is given by integer translations in${ \bf R } ^ { 2 }$ so that its action on$\mathcal { T } _ { F }$is trivial. (In other words, we consider the case of periodic boundary conditions on$[ 0 , 1 ] \times [ 0 , 1 ] . )$Fix furthermore γ$> - \alpha$and choose one of the decompositions$G = K + R$of the heat kernel given by Lemma$7 . 7$with$r > \gamma$

With all this set-up in place, we define the local map$F _ { \gamma } \colon V \to T$by

$$
F _ {\gamma} (\tau) = \hat {f} _ {i j; \gamma} (\tau) \star \mathcal {D} _ {i} \tau \star \mathcal {D} _ {i} \tau + \hat {g} _ {\gamma} (\tau) \star \Xi .\tag{9.9}
$$

Here,$\hat { f } _ { i j ; \ u \gamma }$and$\hat { g } _ { \gamma }$are defined from$f _ { i j }$and$g$as in Section 4.2. Furthermore, we have explicitly used the symbol ⋆ to emphasise the fact that this is the product in$T$. We also set as previously$P = \{ ( t , x ) : t = 0 \}$

We then have the following result:

Lemma 9.1 Assume that the functions$f _ { i j }$and g are smooth. Then, for every$\gamma > | \alpha |$ $a n d f o r \eta \in ( 0 , \alpha { + } 2 ]$, the map$\iota \mapsto F _ { \gamma } ( u )$is locally Lipschitz continuousfrom$\mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$ into$\mathcal { D } _ { P } ^ { \gamma + \alpha , \eta + \alpha }$

Remark 9.2 In fact, we only need sufficient amount of regularity for the results of Section 4.2 to apply.

Proof. Let$u \in { \mathcal { D } } _ { P } ^ { \gamma , \eta } ( V )$and note that V is function-like. By Proposition 6.15, one then has$\mathcal { D } _ { i } u \in \mathcal { D } _ { P } ^ { \gamma - 1 , \eta - 1 } ( W )$for some sector W with regularity$\alpha + 1 < 0$. This is a consequence of the fact that$\mathcal { D } _ { i } \mathbf { 1 } = 0$, so that the element of lowest homogeneity appearing in W is given by$\mathcal { T } _ { i } ( \Xi )$

Applying Proposition 6.12, we see that$\mathcal { D } _ { i } u \star \mathcal { D } _ { j } u \in \mathcal { D } _ { P } ^ { \gamma + \alpha , 2 \eta - 2 } ( \bar { W } )$, where$\bar { W }$is of regularity$2 \alpha + 2$. Since furthermore$\hat { f } _ { i j ; \gamma } ( u ) \in \mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$by Proposition 6.13 (and similarly for$\hat { g } _ { \gamma } ( u ) ,$, we can apply Proposition 6.12 once more to conclude that

$$
\hat {f} _ {i j; \gamma} (u) \star \mathcal {D} _ {i} u \star \mathcal {D} _ {i} u \in \mathcal {D} _ {P} ^ {\gamma + \alpha , 2 \eta - 2}.
$$

Similarly, note that we can view the map$z \mapsto \Xi$as an element of$\mathcal { D } _ { P } ^ { \gamma , \gamma }$for every$\gamma > 0$ but taking values in a sector of regularity α. By applying again Proposition 6.12, we conclude that one has also

$$
\hat {g} _ {\gamma} (u) \star \Xi \in \mathcal {D} _ {P} ^ {\gamma + \alpha , 2 \eta - 2}.
$$

All of these operations are easily seen to be locally Lipschitz continuous in the sense of Section 7.3, so the claim follows.□

Corollary 9.3 Denote by G the solution map for the heat equation, let$\eta > 0 ,$, α $( - \frac { 4 } { 3 } , - 1 ) , \gamma > | \alpha | ,$, and K such that it annihilates polynomials of order γ. Then, for every periodic initial condition$u _ { 0 } \in \mathcal { C } ^ { \eta }$with$\eta > 0$and every admissible model $Z \in \mathcal { M } _ { F }$, thefixed point map

$$
u = (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} F _ {\gamma} (u) + G u _ {0},\tag{9.10}
$$

where$F _ { \gamma }$is given by$( 9 . 9 ) ,$has a unique solution in$\mathcal { D } ^ { \gamma }$on$( 0 , T )$for$T > 0$sufficiently small.

Furthermore, setting${ T _ { \infty } } = T _ { \infty } ( u _ { 0 } ; Z )$to be the smallest time for which (9.10) does not have a unique solution, one has either$T _ { \infty } = \infty o r$lim$\dot { \mathbf { \eta } }  T _ { \infty } \| \mathcal { R } \boldsymbol { u } ( t , \cdot ) \| _ { \eta } =$. Finally, for every$T \ < \ T _ { \infty }$and every$\delta > 0 ,$, there exists$\varepsilon > 0$such that$i f$ $\| \bar { u } _ { 0 } - u _ { 0 } \| _ { \eta } \leq \varepsilon$and$\| Z ; { \bar { Z } } \| _ { \gamma } \leq \varepsilon ,$, one has$\| u ; \bar { u } \| _ { \gamma , \eta } \leq \delta .$

Proof. Since$\alpha > - 2$and$\eta > 0 .$, it follows from Lemma 9.1 that all of the assumptions of Theorem 7.8 and Corollary 7.12 are satisfied.□

Denote now by$S ^ { L }$the truncated solution map as given in Section$( 7 . 3 )$. On the other hand, for any (symmetric / periodic) continuous function$\xi _ { \varepsilon } : \mathbf { R } ^ { 3 } \to$R and every (symmetric / periodic)$u _ { 0 } \in \mathcal { C } ^ { \eta } ( { \bf R } ^ { 2 } )$), we can build a “classical” solution map$u _ { \varepsilon } =$ $\bar { S } ^ { L } ( u _ { 0 } , \xi _ { \varepsilon } )$for the equation

$$
\partial_ {t} u _ {\varepsilon} = \Delta u _ {\varepsilon} + f _ {i j} (u _ {\varepsilon}) \partial_ {i} u _ {\varepsilon} \partial_ {j} u _ {\varepsilon} + g (u _ {\varepsilon}) \xi_ {\varepsilon}, \qquad u _ {\varepsilon} (0, x) = u _ {0} (x),\tag{9.11}
$$

where the subscript L refers again to the fact that we stop solutions when$\| u _ { \varepsilon } ( t , \cdot ) \| _ { \eta } \geq$ $L .$Similarly to before, we also denote by$\bar { T } ^ { L } ( u _ { 0 } , \xi _ { \varepsilon } )$the first time when this happens. Here, the solution map$\bar { S } ^ { L } ( u _ { 0 } , \xi _ { \varepsilon } )$is the standard solution map for (9.11) obtained by classical PDE theory [?, Kry08].

Given an element$M \in \mathfrak { R } _ { 0 }$with the renormalisation group$\Re _ { 0 }$defined as in Section 9.1, we also define a “renormalised” solution map$u _ { \varepsilon } = \bar { S } _ { M } ^ { L } ( u _ { 0 } , \xi _ { \varepsilon } )$in exactly the same way, but replacing (9.11) by

$$
\partial_ {t} u _ {\varepsilon} = \Delta u _ {\varepsilon} + f _ {i j} (u _ {\varepsilon}) \left(\partial_ {i} u _ {\varepsilon} \partial_ {j} u _ {\varepsilon} - g ^ {2} (u _ {\varepsilon}) \bar {C} _ {i j}\right) + g (u _ {\varepsilon}) \left(\xi_ {\varepsilon} - C g ^ {\prime} (u _ {\varepsilon})\right),\tag{9.12}
$$

where$g ^ { \prime }$denotes the derivative of$g .$We then have the following result:

Proposition 9.4 Given a continuous and symmetric function$\xi _ { \varepsilon } ,$, denote by$Z _ { \varepsilon }$the associated canonical model realising$\mathcal { T } _ { F } ^ { ( r ) }$given by Proposition 8.27. Let furthermore $M \in \mathfrak { R } _ { 0 }$be as in Section 9.1. Then,for every$L > 0$and symmetric$u _ { 0 } \in \mathcal { C } ^ { \eta } ( { \mathbf { R } } ^ { 2 } )$, one has the identities

$$
\mathcal {R S} ^ {L} (u _ {0}, Z _ {\varepsilon}) = \bar {\mathcal {S}} ^ {L} (u _ {0}, \xi_ {\varepsilon}), \quad a n d \quad \mathcal {R S} ^ {L} (u _ {0}, M Z _ {\varepsilon}) = \bar {\mathcal {S}} _ {M} ^ {L} (u _ {0}, \xi_ {\varepsilon}).
$$

Proof. The fact that$\mathcal { R } S ^ { L } ( u _ { 0 } , Z _ { \varepsilon } ) = \bar { S } ^ { L } ( u _ { 0 } , \xi _ { \varepsilon } )$is relatively straightforward to see. Indeed, we have already seen in the proof of Proposition 7.11 that the function$v =$ $\mathcal { R } S ^ { L } ( u _ { 0 } , Z _ { \varepsilon } )$satisfies for$t \leq T ^ { L } ( u _ { 0 } , Z _ { \varepsilon } )$the identity

$$
v (t, x) = \int_ {0} ^ {t} \int_ {\mathbf {R} ^ {2}} G (t - s, x - y) (\mathcal {R} F _ {\gamma} (v)) (s, y) d y d s + \int_ {\mathbf {R} ^ {2}} G (t, x - y) u _ {0} (y) d y,
$$

where G denotes the heat kernel on${ \bf R } ^ { 2 }$. Furthermore, it follows from (8.18) and$\mathrm { R e } \mathrm { - }$ mark 4.13 that in the case of the canonical model$Z _ { \varepsilon }$, one has indeed the identity

$$
\left(\mathcal {R} F _ {\gamma} (v)\right) (s, y) = f _ {i j} \left(\mathcal {R} v (s, y)\right) \partial_ {i} \mathcal {R} v (s, y) \partial_ {j} \mathcal {R} v (s, y) + g (\mathcal {R} v (s, y)) \xi_ {\varepsilon} (s, y),
$$

valid for every$v \in \mathcal { D } ^ { \gamma }$with$\gamma > | \alpha | > 1$. As a consequence,$_ { \mathcal { R } v }$satisfies the same fixed point equation as the classical solution to (9.11).

It remains to find out what fixed point equation v satisfies when we consider instead the model$M Z _ { \varepsilon } .$, for which we denote the reconstruction operator by$\mathcal { R } ^ { M }$. Recall first Remark 3.15 which states that for every$w \in \mathcal { D } ^ { \gamma }$with$\gamma > 0$, one has the identity

$$
(\mathcal {R} ^ {M} w) (z) = (\Pi_ {z} ^ {M, (\varepsilon)} w (z)) (z),
$$

where we have made use of the notation$M Z _ { \varepsilon } = ( \Pi ^ { M , ( \varepsilon ) } , \Gamma ^ { M , ( \varepsilon ) } )$. Furthermore, one has$( \Pi _ { z } ^ { M , ( \varepsilon ) } \tau ) ( z ) = 0$for any element τ with$| \tau | _ { \mathfrak { s } } > 0 ;$, so that we only need to consider the coefficients of w belonging to the subspace spanned by the elements with negative (or 0) homogeneity.

It follows from Lemma 9.1 that in order to compute all components of$w = F _ { \gamma } ( v )$ with negative homogeneity, we need to know all components of v with homogeneity less than α . One can verify that as long as$\alpha > - { \frac { 4 } { 3 } } .$, the only elements in$V$with homogeneity less than α are given by$\{ \mathbf { 1 } , X _ { 1 } , X _ { 2 } , \breve { \underline { { \tau } } } ( \Xi ) \}$. Since$v ( z )$furthermore belongs to the sector$V$, we can find functions$\varphi \colon { \bf R } ^ { 3 }  { \bf R }$and$\nabla \Phi \colon \mathbf { R } ^ { 3 }  \mathbf { R } ^ { 2 }$such that

$$
v (z) = \varphi (z) \mathbf {1} + g (\varphi (z)) \mathcal {I} (\Xi) + \left\langle \nabla \varphi (z), X \right\rangle + \varrho (z),
$$

where the remainder$\varrho$consists of terms with homogeneity strictly larger than$| \alpha |$. Here, the fact that the coefficient of$\mathcal { T } ( \Xi )$is necessarily given by$g ( \varphi ( z ) )$follows from the identity (7.20), combined with an explicit calculation to determine$\mathfrak { F }$. Furthermore, we make a slight abuse of notation here by denoting by$X$the spatial coordinates of$X$ Note that in general, although$\nabla \varphi$can be interpreted as some kind of “renormalised gradient” for$\varphi ,$we do not claim any kind of relation between$\varphi$and$\nabla \varphi$. It follows that

$$
\mathcal {D} _ {i} v (z) = g (\varphi (z)) \mathcal {I} _ {i} (\Xi) + \nabla_ {i} \varphi (z) \mathbf {1} + \varrho_ {i} (z),
$$

for some remainder$\varrho _ { i }$consisting of terms with homogeneity greater than$| \alpha | - 1$

Regarding$\hat { f } _ { i j ; \gamma } ( \boldsymbol { v } )$and$\hat { g } _ { \gamma } ( v )$, we obtain from (4.11) the expansions

$$
\begin{array}{r} \hat {f} _ {i j; \gamma} (v) (z) = f _ {i j} (\varphi (z)) \mathbf {1} + f _ {i j} ^ {\prime} (\varphi (z)) g (\varphi (z)) \mathcal {I} (\Xi) + \varrho_ {f} (z), \\ \hat {g} _ {\gamma} (v) (z) = g (\varphi (z)) \mathbf {1} + g ^ {\prime} (\varphi (z)) g (\varphi (z)) \mathcal {I} (\Xi) + \varrho_ {g} (z), \end{array}
$$

where both$\varrho _ { f }$and$\varrho _ { g }$contain terms proportional to$X ,$, as well as other components of homogeneities strictly greater than$| \alpha |$. Note also that when α$> - { \frac { 4 } { 3 } }$, the elements of negative homogeneity are those in$\mathcal { F } _ { 0 }$as in Section 9.1, but that one actually has $( \Pi _ { z } ^ { M , ( \varepsilon ) } X _ { i } \Xi ) ( z ) = 0$for every$M \in \mathfrak { R } _ { 0 }$

It follows that one has the identity

$$
\begin{array}{r l} & F _ {\gamma} (v) (z) = f _ {i j} (\varphi (z)) \big (\nabla_ {i} \varphi (z) \nabla_ {j} \varphi (z) \mathbf {1} + g (\varphi (z)) \nabla_ {i} \varphi (z) \mathcal {I} _ {j} (\Xi) \\ & \qquad + g (\varphi (z)) \nabla_ {j} \varphi (z) \mathcal {I} _ {i} (\Xi) + g ^ {2} (\varphi (z)) \mathcal {I} _ {i} (\Xi) \mathcal {I} _ {j} (\Xi) \big) \\ & \qquad + g (\varphi (z)) \Xi + g ^ {\prime} (\varphi (z)) g (\varphi (z)) \mathcal {I} (\Xi) \Xi + \varrho_ {F} (z). \end{array}
$$

At this stage we use the fact that, by (9.1), one has the identity

$$
\Pi_ {z} ^ {M, (\varepsilon)} \tau = \Pi_ {z} ^ {(\varepsilon)} M \tau ,
$$

for all$\tau \in \mathcal { F } _ { 0 } .$, together with the fact that$\mathcal { R } ^ { M } v ( z ) = \varphi ( z )$. A straightforward calculation then yields the identity

$$
\mathcal {R} ^ {M} F _ {\gamma} (v) (z) = f _ {i j} (\mathcal {R} ^ {M} v (z)) \bigl (\partial_ {i} \mathcal {R} ^ {M} v (z) \partial_ {j} \mathcal {R} ^ {M} v (z) - \bar {C} _ {i j} g ^ {2} (\mathcal {R} ^ {M} v (z)) \bigr)
$$

$$
+ g (\mathcal {R} ^ {M} v (z)) \bigl (\xi_ {\varepsilon} (z) - C g ^ {\prime} (\mathcal {R} ^ {M} v (z)) \bigr),
$$

which is precisely what is required to complete the proof.

## 9.4 Solution theory for the dynamical$\Phi _ { 3 } ^ { 4 }$model

We now turn to the analysis of$( \Phi ^ { 4 } )$. In this case, one has$F = \xi - u ^ { 3 }$, so that${ \mathfrak { M } } _ { F }$is given by$\{ 1 , \Xi , U , U ^ { 2 } , U ^ { 3 } \}$. This time, spatial dimension is 3 and the scaling we consider is once again the parabolic scaling${ \mathfrak { s } } = ( 2 , 1 , 1 , 1 )$, so that the scaling dimension of space-time is 5. Since ξ denotes space-time white noise this time, we choose for α some value$\alpha = | \Xi | _ { \mathfrak { s } } < - \frac { 5 } { 2 }$. It turns out that in order to be able to choose the set$\mathcal { F } _ { 0 }$in Section 8.3 independently of$\alpha ,$, we should furthermore impose α$> - \frac { 1 8 } { 7 }$. In this case, the fixed point equation that we would like to consider is

$$
u = (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} (\Xi - u ^ {3}) + G u _ {0},\tag{9.13}
$$

with$u _ { 0 } \in \mathcal { C } _ { \bar { \mathfrak { s } } } ^ { \eta } ( \mathbf { R } ^ { 3 } ) , \eta > - \frac { 2 } { 3 } , \gamma \in ( \bar { \gamma } , \bar { \gamma } + 2 )$, and$\bar { \gamma } > 0$

We are then in a situation which is slightly outside of the scope of the general result of Corollary 7.12 for two reasons. First, Proposition 6.9 does a priori not apply to the singular modelled distribution$\pm \underline { { \ v { R } } } ^ { + } \Xi$. Second, the distribution$\mathcal { R } \mathcal { Z } ( \Xi )$is of negative order, so that there is in principle no obvious way of evaluating it at a fixed time. Fortunately, both of these problems can be solved relatively easily. For the first problem, we note that multiplying white noise by the indicator function of a set is of course not a problem at all, so we are precisely in the situation alluded to in Remark 6.17. As a consequence, all we have to make sure is that the convergence$\xi _ { \varepsilon } \to \xi$takes place in some space of distributions that allows multiplication with the relevant indicator function. Regarding the distribution (Ξ), it is also possible to verify that if ξ is space-time white noise, then$K * \xi$almost surely takes values not only in$\mathcal { C } _ { \mathfrak { s } } ^ { \eta } ( \mathbf { R } ^ { 4 } )$for $\eta < - \frac { 1 } { 2 }$, but it actually takes values in$\mathcal { C } ( \mathbf { R } , \mathcal { C } ^ { \eta } ( \mathbf { R } ^ { \mathrm { 3 } } ) )$, which is precisely what is needed to be able to evaluate it on a fixed time slice, thus enabling us to extend the argument of Proposition 7.11.

The simplest way of ensuring that the reconstruction operator yields a well-defined distribution on${ \bf R } ^ { 4 }$for$\pm \underline { { \ v { R } } } ^ { + } \Xi$is to build a suitable space of distributions “by hand” and to show that smooth approximations to space-time white noise also converge in that space. We fix again some final time, which we take to be 1 for definiteness. We then define for any$\alpha < 0$and compact K the norm

$$
\| \xi \| _ {\alpha ; \mathfrak {K}} = \sup _ {s \in \mathbf {R}} \| \xi \mathbf {1} _ {t \geq s} \| _ {\alpha ; \mathfrak {K}},
$$

and we denote by$\bar { \mathcal { C } } _ { \mathfrak { s } } ^ { \alpha }$the intersections of the completions of smooth functions under $\| \cdot \| _ { \alpha ; \mathcal { R } }$for all compacts K. One motivation for this definition is the following convergence result:

Proposition 9.5 Let ξ be white noise on$\mathbf { R } \times \mathbf { T } ^ { 3 }$, which we extend periodically to ${ \mathbf { R } } ^ { 4 }$. Let$\varrho \colon  { \mathbf { R } } ^ { 4 } \to$R be a smooth compactly supportedfunction integrating to 1, set $\varrho _ { \varepsilon } = { \cal S } _ { \mathfrak { s } } ^ { \varepsilon } \varrho ,$and define$\xi _ { \varepsilon } = \varrho _ { \varepsilon } * \xi .$. Then, for every$\alpha \in ( - 3 , - \frac { 5 } { 2 } )$, one has$\xi \in \bar { \mathcal { C } } _ { \mathfrak { s } } ^ { \alpha }$ almost surely and, for every$\eta \in ( - 1 , - \frac { 1 } { 2 } )$, one has$K * \xi \in \mathcal { C } ( \mathbf { R } , \mathcal { C } ^ { \eta } ( \mathbf { R } ^ { 3 } ) )$almost surely. Furthermore, for every compact$\mathcal { R } \subset \mathbf { R } ^ { 4 }$and every$\kappa > 0 ,$, one has

$$
\mathbf {E} \left\| \xi - \xi_ {\varepsilon} \right\| _ {\alpha ; \mathfrak {K}} \lesssim \varepsilon^ {- \frac {5}{2} - \alpha - \kappa}.\tag{9.14}
$$

Finally, for every$\bar { \kappa } \in ( 0 , - \frac { 1 } { 2 } - \eta ) .$, the bound

$$
\mathbf {E} \sup _ {t \in [ 0, 1 ]} \| (K * \xi) (t, \cdot) - (K * \xi_ {\varepsilon}) (t, \cdot) \| _ {\eta} \lesssim \varepsilon^ {\bar {\kappa}},\tag{9.15}
$$

holds uniformly over$\varepsilon \in ( 0 , 1 ]$

Proof. In order to show that$\xi \in \bar { \mathcal { C } } _ { \mathfrak { s } } ^ { \alpha }$, note first that it is immediate that$\xi { \bf 1 } _ { t \geq s } \in \mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$for every fixed$s \in \mathbf { R }$. It therefore suffices to show that the map$s \mapsto \xi \mathbf { 1 } _ { t \geq s }$is continuous in$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$. For this, we choose a wavelet basis as in Section 3.2 and, writing$\Psi _ { \star } = \Psi \cup \{ \varphi \}$ we note that for every$p > 1$, one has the bound

$$
\begin{array}{l} \mathbf {E} \| \xi \mathbf {1} _ {t \geq s} - \xi \mathbf {1} _ {t \geq 0} \| _ {\alpha ; \mathfrak {K}} ^ {2 p} \leq \sum_ {\psi \in \Psi_ {\star}} \sum_ {n \geq 0} \sum_ {x \in \Lambda_ {\mathfrak {s}} ^ {n} \cap \bar {\mathfrak {K}}} \mathbf {E} 2 ^ {2 \alpha n p + | \mathfrak {s} | n p} | \langle \xi \mathbf {1} _ {t \geq s} - \xi \mathbf {1} _ {t \geq 0}, \psi_ {x} ^ {n, \mathfrak {s}} \rangle | ^ {2 p} \\ \qquad \leq \sum_ {\psi \in \Psi_ {\star}} \sum_ {n \geq 0} \sum_ {x \in \Lambda_ {\mathfrak {s}} ^ {n} \cap \bar {\mathfrak {K}}} 2 ^ {2 \alpha n p + | \mathfrak {s} | n p} (\mathbf {E} | \langle \xi , \mathbf {1} _ {t \in [ 0, s ]} \psi_ {x} ^ {n, \mathfrak {s}} \rangle | ^ {2}) ^ {p} \\ \qquad \lesssim \sum_ {\psi \in \Psi_ {\star}} \sum_ {n \geq 0} 2 ^ {2 \alpha n p + | \mathfrak {s} | n p + | \mathfrak {s} | n} \| \mathbf {1} _ {t \in [ 0, s ]} \psi_ {x} ^ {n, \mathfrak {s}} \| _ {L ^ {2}} ^ {2 p}. \end{array}
$$

Here we wrote$\bar { \mathbf { x } }$for the 1-fattening of K and we used the equivalence of moments for Gaussian random variables to obtain the second line. We then verify that

$$
\left\| \mathbf {1} _ {t \in [ 0, s ]} \psi_ {x} ^ {n, \mathfrak {s}} \right\| _ {L ^ {2}} ^ {2} \lesssim 1 \wedge 2 ^ {2 n} s.
$$

Provided that$\alpha \in ( - \frac { 7 } { 2 } , - \frac { 5 } { 2 } )$, it then follows that

$$
\mathbf {E} \| \xi \mathbf {1} _ {t \geq s} - \xi \mathbf {1} _ {t \geq 0} \| _ {\alpha ; \mathfrak {K}} \lesssim s ^ {- \frac {5}{4} - \frac {\alpha}{2} - \frac {5}{4 p}}.
$$

Choosing first$p$sufficiently large and then applying Kolmogorov’s continuity criterion, it follows that one does indeed have$\xi \in \bar { \mathcal { C } } _ { \mathfrak { s } } ^ { \alpha }$as stated.

In order to bound the distance between$\xi$and$\xi _ { \varepsilon }$, we can proceed in exactly the same way. We then obtain the same bound, but with$\| \mathbf { 1 } _ { t \in [ 0 , s ] } \psi _ { x } ^ { n , s } \| _ { L } ^ { 2 }$<sub>2</sub> replaced by $\| \mathbf { 1 } _ { t \in [ 0 , s ] } \psi _ { x } ^ { n , 5 } - \varrho _ { \varepsilon } \ast \big ( \mathbf { 1 } _ { t \in [ 0 , s ] } \psi _ { x } ^ { n , 5 } \big ) \| _ { L ^ { 2 } } ^ { 2 }$. A straightforward calculation shows that

$$
\left\| \mathbf {1} _ {t \in [ 0, s ]} \psi_ {x} ^ {n, \mathfrak {s}} - \varrho_ {\varepsilon} * \left(\mathbf {1} _ {t \in [ 0, s ]} \psi_ {x} ^ {n, \mathfrak {s}}\right) \right\| _ {L ^ {2}} ^ {2} \lesssim 1 \wedge 2 ^ {2 n} s \wedge 2 ^ {2 n} \varepsilon^ {2}.
$$

As above, it then follows that, provided that$\alpha + \kappa > - 3$2

$$
\mathbf {E} \big \| (\xi - \xi_ {\varepsilon}) \mathbf {1} _ {t \in [ 0, s ]} \big \| _ {\alpha ; \mathfrak {K}} \lesssim \varepsilon^ {- \frac {5}{2} - \alpha - \kappa} s ^ {\frac {\kappa}{2} - \frac {5}{4 p}},
$$

so that the requested bound (9.14) follows at once by choosing p sufficiently large.

In order to show (9.15), note first that$K * \xi _ { \varepsilon } = \varrho _ { \varepsilon } * ( K * \xi )$. As a consequence, it is sufficient to find some space of distributions$\mathcal { X } \subset \mathcal { C } ( [ 0 , 1 ] , \mathcal { C } ^ { \eta } )$such that$K * \xi \in \mathcal { X }$ almost surely and such that the bound

$$
\| \varrho_ {\varepsilon} * \zeta - \zeta \| _ {\mathcal {C} ([ 0, 1 ], \mathcal {C} ^ {\eta})} \lesssim \varepsilon^ {\bar {\kappa}} \| \zeta \| _ {\mathcal {X}},\tag{9.16}
$$

holds uniformly over all$\varepsilon \in ( 0 , 1 ]$and$\zeta \in \mathcal { X }$. We claim that$\mathcal { X } = \mathcal { C } ^ { \frac { \bar { \kappa } } { 2 } } ( \mathbf { R } , \mathcal { C } ^ { \eta + \bar { \kappa } } )$is a possible choice.

To show that (9.16) holds, we use the characterisation

$$
\left\| \varrho_ {\varepsilon} * \zeta - \zeta \right\| _ {\mathcal {C} ([ 0, 1 ], \mathcal {C} ^ {\eta})}
$$

$$
= \sup _ {t \in [ 0, 1 ]} \sup _ {\lambda \in (0, 1 ]} \lambda^ {- \eta} \sup _ {\psi} \int \psi^ {\lambda} (x) \varrho_ {\varepsilon} (x - y, t - s) (\zeta (y, s) - \zeta (x, t)) d x d y d s,
$$

where the supremum runs over all test functions$\psi \in B _ { \mathfrak { s } , 0 } ^ { 1 }$(for s the Euclidean scaling). We also wrote$\psi ^ { \lambda }$for the rescaled test function as previously. One then rewrites the above expressions as a sum$T _ { 1 } + T _ { 2 }$with

$$
\begin{array}{l} T _ {1} = \int \psi^ {\lambda} (x) \varrho_ {\varepsilon} (x - y, t - s) \big (\zeta (y, s) - \zeta (y, t) \big)   d x   d y   d s  , \\ T _ {2} = \int \psi^ {\lambda} (x) \varrho_ {\varepsilon} (x - y, t - s) \big (\zeta (y, t) - \zeta (x, t) \big)   d x   d y   d s \\ = \int \big (\psi^ {\lambda} (x) - \psi^ {\lambda} (y) \big) \varrho_ {\varepsilon} (x - y, t - s) \zeta (y, t)   d x   d y   d s  . \end{array}
$$

To bound each of these terms, one considers separately the cases$\lambda \leq \varepsilon$and$\lambda > \varepsilon$ For$T _ { 1 }$, it is then straightforward to verify that$| T _ { 1 } | \lesssim ( \varepsilon ^ { \eta } \wedge \lambda ^ { \eta } ) | t - s | ^ { { \bar { \kappa } } / 2 }$. Since one has$| t - s | \lesssim \varepsilon ^ { 2 }$due to the fact that$\varrho$is compactly supported, the requested bound follows for$T _ { 1 }$. For$T _ { 2 }$, arguments similar to those used in Section 5.2 yield the bound $\left| T _ { 2 } \right| \lesssim \lambda ^ { \eta + \bar { \kappa } } \lesssim \varepsilon ^ { \bar { \kappa } } \lambda ^ { \eta }$in the case$\lambda \leq \varepsilon$and$\vert T _ { 2 } \vert \lesssim \lambda ^ { \eta + \bar { \kappa } - 1 } \varepsilon \lesssim \varepsilon ^ { \bar { \kappa } } \lambda ^ { \eta }$in the case$\varepsilon \leq \lambda$ The bound$_ { ( 9 . 1 6 ) }$then follows at once.

To show that$K * \xi$belongs to almost surely, the argument is similar. Write $\begin{array} { r } { K = \sum _ { n > 0 } K _ { n } } \end{array}$as in the assumption and set$\xi ^ { ( n ) } = K _ { n } * \xi$. We claim that it then Psuffices to show that there is$\delta > 0$such that the bound

$$
\mathbf {E} \Big (\int \psi^ {\lambda} (x) (\xi^ {(n)} (x, t) - \xi^ {(n)} (x, 0)) d x \Big) ^ {2} \lesssim 2 ^ {- \delta n} | t | ^ {\bar {\kappa} + \delta} \lambda^ {2 \eta + 2 \bar {\kappa} + \delta},\tag{9.17}
$$

holds uniformly over$n \geq 0 , \lambda \in ( 0 , 1 ]$, and test functions$\psi \in B _ { \mathfrak { s } , 0 } ^ { 1 }$. Indeed, this follows at once by combining the usual Kolmogorov continuity test (in time) with Proposition 3.20 (in space) and the equivalence of moments for Gaussian random variables.

The left hand side of (9.17) is equal to

$$
\int \left(\int \psi^ {\lambda} (x) \left(K _ {n} (x - y, t - r) - K _ {n} (x - y, - r)\right) d x\right) ^ {2} d y d r =: \| \Psi_ {n} ^ {\lambda ; t} \| _ {L ^ {2}} ^ {2}.
$$

It is immediate from the definitions and the scaling properties of the$K _ { n }$that the volume of the support of$\Psi _ { n } ^ { \lambda ; t }$is bounded by$( \lambda + 2 ^ { - n } ) ^ { 3 } 2 ^ { - 2 n }$. The values of$\Psi _ { n } ^ { \lambda ; t }$inside this support are furthermore bounded by a multiple of

$$
2 ^ {3 n} \wedge | t | 2 ^ {5 n} \wedge \lambda^ {- 3}.
$$

For$\lambda < 2 ^ { - n }$we thus obtain the bound

$$
\| \Psi_ {n} ^ {\lambda ; t} \| _ {L ^ {2}} ^ {2} \lesssim 2 ^ {- 5 n} | t | ^ {\bar {\kappa} + \delta} 2 ^ {6 n + 2 (\bar {\kappa} + \delta) n} = 2 ^ {n + 2 (\bar {\kappa} + \delta) n} | t | ^ {\bar {\kappa} + \delta},
$$

while for$\lambda \geq 2 ^ { - n }$we obtain

$$
\| \Psi_ {n} ^ {\lambda ; t} \| _ {L ^ {2}} ^ {2} \lesssim \lambda^ {3} 2 ^ {- 2 n} | t | ^ {\bar {\kappa} + \delta} \lambda^ {- 6 + \bar {\kappa} + \delta} 2 ^ {5 (\bar {\kappa} + \delta) n} = | t | ^ {\bar {\kappa} + \delta} \lambda^ {3 (\bar {\kappa} + \delta) - 3} 2 ^ {- 2 n + 5 (\bar {\kappa} + \delta) n}
$$

It follows that since$\eta$is strictly less than$- \frac { 1 } { 2 }$, it is possible to choose$\bar { \kappa }$and$\delta$sufficiently small to guarantee that the bound (9.17) holds, thus concluding the proof.□

Remark 9.6 The definition of these spaces of distributions is of course rather ad hoc, but it happens to be one that then allows us to restart solutions, which is amply sufficient to apply the same procedure as in Corollary 7.12 to define local solutions to (9.13).

As before, the regularity structure$\mathcal { T }$comes with a sector$V \subset T$which is given by$_ { ( 9 . 8 ) }$. This time however, the sector V is not function-like, but has regularity$2 +$ $\alpha \in ( - \frac { 4 } { 7 } , - \frac { 1 } { 2 } )$. Assume for simplicity that the symmetry$\mathcal { S }$is again given by integer translations in${ \mathbf { R } } ^ { 3 }$, so that its action on$\mathcal { T }$is trivial. Fix furthermore$\gamma > | 2 \alpha + 4 |$and choose one of the decompositions$G = K + R$of the heat kernel given by Lemma 7.7 with$r > \gamma$

Regarding the nonlinearity, we then have the following bound:

Lemma 9.7 For every$\gamma > | 2 \alpha + 4 |$andfor$\eta \leq \alpha + 2$, the map$u \mapsto u ^ { 3 }$is locally Lipschitz continuous in the strong sensefrom$\mathcal { D } _ { P } ^ { \gamma , \eta } ( V )$into$\mathcal { D } _ { P } ^ { \gamma + 2 \dot { \alpha } + 4 , 3 \eta }$

Proof. This is an immediate consequence of Proposition 6.12.

With these results at hand, our strategy is now as follows. First, we reformulate the fixed point map (9.13) as

$$
\begin{array}{l} u = - (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} u ^ {3} + G u _ {0} + v  , \\ v = (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} ^ {+} \Xi  . \end{array}\tag{9.18}
$$

Here, we define$\mathcal { R } R ^ { + } \Xi$as the distribution$\xi \mathbf { 1 } _ { t \geq 0 }$, which does indeed coincide with R$\pm \underline { { \ v { R } } } ^ { + } \Xi$when applied to test functions that are localised away of the singular line$t = 0$ and belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha }$by assumption. This also shows immediately that$v \in \mathcal { D } _ { P } ^ { \gamma , \eta }$for$\eta$ and$\gamma$as in Lemma 9.7. We then have the following result:

Proposition 9.8 Let$\mathcal { T } _ { F }$be the regularity structure associated as above to$( \Phi ^ { 4 } )$with $\alpha \in ( - \frac { 1 8 } { 7 } , - \frac { 5 } { 9 } ) , \beta = 2$and the formal right hand side$F ( U , \Xi , P ) = \Xi - U ^ { 3 }$. Let furthermore$\bar { \eta } \bar { \in } ( - \frac { 2 } { 3 } , \alpha + 2 )$and let$Z = ( \Pi , \Gamma ) \in \mathcal { M } _ { F }$be an admissible mode$l f o r \mathcal { T }$ with the additional properties that ξ <sup>def</sup> = Ξ belongs to$\bar { \mathcal { C } } _ { \mathfrak { s } } ^ { \alpha }$and that$K * \xi \in \mathcal { C } ( \mathbf { R } , \mathcal { C } ^ { \eta } ) .$

Then, for every$\gamma > 0$and every$L > 0 _ { : }$, one can build a maximal solution map$S ^ { L }$ for (9.18) with the same properties as in Section$7 . 3 .$. Furthermore,$\boldsymbol { S ^ { L } }$has the same continuity properties as in Corollary$7 . 1 2 ,$, provided that$Z$and$\bar { Z }$furthermore satisfy the bounds

$$
\| \xi \| _ {\alpha ; O} + \| \bar {\xi} \| _ {\alpha ; O} \leq C, \quad \sup _ {t \in [ 0, 1 ]} \left(\| (K * \xi) (t, \cdot) \| _ {\eta} + \| (K * \bar {\xi}) (t, \cdot) \| _ {\eta}\right) \leq C,\tag{9.19}
$$

as well as

$$
\llbracket \xi - \bar {\xi} \rrbracket_ {\alpha ; O} \leq \delta , \quad \sup _ {t \in [ 0, 1 ]} \left(\| (K * \xi) (t, \cdot) - (K * \bar {\xi}) (t, \cdot) \| _ {\eta}\right) \leq \delta .\tag{9.20}
$$

Here, we have set$\bar { \xi } = \bar { \mathcal { R } } \Xi$, where$\bar { \mathcal { R } }$is the reconstruction operator associated to$\bar { Z }$

Proof. We claim that, as a consequence of Lemma 9.7, the nonlinearity$F ( u ) = - u ^ { 3 }$ satisfies the assumptions of Theorem 7.8 as soon as we choose$\gamma > | 2 \alpha + 4 |$. Indeed, in this situation, V is the sector generated by all elements in$\mathcal { F } _ { F }$of the form$\boldsymbol { \mathcal { T } \tau } .$, while V<sup>¯</sup> is the span of$\mathcal { F } _ { F } \setminus \{ \Xi \}$. As a consequence, one has$\zeta = \alpha + 2$and$\bar { \zeta } = 3 ( \alpha + 2 )$, so that indeed$\zeta < \bar { \zeta } + 2$

Provided that η and γ are as in Lemma 9.7, one then has$\bar { \eta } = 3 \eta$and$\bar { \gamma } = \gamma + 2 \alpha + 4$ The condition$\eta < ( \bar { \eta } \Lambda \bar { \zeta } ) { + 2 q }$then reads$\eta < 3 \eta + 2$, which translates into the condition $\eta > - 1$, which is satisfied by assumption. The condition$\gamma < \bar { \gamma } + 2 q$reads α$> - 3 .$ which is also satisfied by assumption. Finally, the assumption$\bar { \eta } \wedge \bar { \zeta } > - 2 q$reads $\begin{array} { r } { \eta > - \frac { 2 } { 3 } } \end{array}$, which is also satisfied. As a consequence, we can apply Theorem 7.8 to get a local solution map.

To extend this local map up to the first time where$\| ( \mathcal { R } u ) ( t , \cdot ) \| _ { \eta }$blows up, the argument is virtually identical to the proof of Proposition 7.11. The only difference is that the solution u does not take values in a function-like sector. However, our local solutions are of the type$\boldsymbol { u } ( t , x ) = \boldsymbol { \mathcal { I } } \boldsymbol { \Xi } + \boldsymbol { v } ( t , x )$, with v taking values in a function-like sector. (As a matter of fact, v takes values in a sector of order$3 ( \alpha + 2 ) + 2 . )$The bounds (9.19) and (9.20) are then precisely what is required for the reconstruction operator to still be a continuous map with values in${ \mathcal { C } } ( \mathbf { R } , { \mathcal { C } } _ { \bar { \mathfrak { s } } } ^ { \eta } )$and for the fixed point equation

$$
\begin{array}{l} {u = - (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} _ {s} ^ {+} u ^ {3} + G u _ {s} + v  ,} \\ {v = (\mathcal {K} _ {\bar {\gamma}} + R _ {\gamma} \mathcal {R}) \boldsymbol {R} _ {s} ^ {+} \Xi  ,} \end{array}
$$

to make sense for all$s > 0$

Remark 9.9 The lower bound$- \frac { 2 } { 3 }$for$\eta$appearing in this theorem is probably sharp. This is because the space${ \mathcal { C } } ^ { - { \frac { 2 } { 3 } } }$is critical for the deterministic equation so that one wouldn’t even expect to have a continuous solution map for$\partial _ { t } u = \Delta u - u ^ { 3 } \mathrm { i n } \mathcal { C } ^ { - \frac { 2 } { 3 } } !$If $u ^ { 3 }$is replaced by$u ^ { 2 }$however, the critical space is${ \mathcal { C } } ^ { - 1 }$and one can build local solutions for any$\eta > - 1$

As in Section 9.3, we now identify solutions corresponding to a model that has been renormalised under the action of the group$\Re _ { 0 }$constructed in Section 9.2 with classical solutions to a modified equation. Recall that this time, elements$M \in \mathfrak { R } _ { 0 }$are characterised by two real numbers$C _ { 1 }$and$C _ { 2 }$. As before, denote by$u _ { \varepsilon } = \bar { S } ^ { L } ( u _ { 0 } , \xi _ { \varepsilon } )$ the classical solution map to the equation

$$
\partial_ {t} u _ {\varepsilon} = \Delta u _ {\varepsilon} - u _ {\varepsilon} ^ {3} + \xi_ {\varepsilon},
$$

stopped when$\| u _ { \varepsilon } ( t , \cdot ) \| _ { \eta } \geq L$. Here,$\xi _ { \varepsilon }$is a continuous function which is periodic in space, and$u _ { 0 } \in \mathcal { C } ^ { \eta } ( \mathbf { T } ^ { 3 } )$. This time, it turns out that the renormalised map$\hat { \hat { S } } _ { M } ^ { L }$is given by the classical solution map to the equation

$$
\partial_ {t} u _ {\varepsilon} = \Delta u _ {\varepsilon} + (3 C _ {1} - 9 C _ {2}) u _ {\varepsilon} - u _ {\varepsilon} ^ {3} + \xi_ {\varepsilon},\tag{9.21}
$$

stopped as before when the norm of the solution reaches L. Indeed, one has again:

Proposition 9.10 Given a continuous function$\xi _ { \varepsilon } \colon \mathbf { R } \times \mathbf { T } ^ { 3 }  \mathbf { R } ,$, denote by$Z _ { \varepsilon } ~ =$ $( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$the associated canonical model for the regularity structure$\mathcal { T } _ { F } ^ { ( r ) }$given by Proposition 8.27. Let furthermore$M \in \mathfrak { R } _ { 0 }$be as in Section 9.2. Then, for every$L > 0$ and symmetric$u _ { 0 } \in \mathcal { C } ^ { \eta } ( { \mathbf { R } } ^ { 2 } )$, one has the identities

$$
\mathcal {R S} ^ {L} (u _ {0}, Z _ {\varepsilon}) = \bar {\mathcal {S}} ^ {L} (u _ {0}, \xi_ {\varepsilon}), \quad a n d \quad \mathcal {R S} ^ {L} (u _ {0}, M Z _ {\varepsilon}) = \bar {\mathcal {S}} _ {M} ^ {L} (u _ {0}, \xi_ {\varepsilon}).
$$

Proof. The proof is similar to the proof of Proposition 9.4. Just like there, we can find periodic functions$\varphi \colon { \bf R } ^ { 4 }  { \bf R }$and$\nabla \varphi \colon { \mathbf { R } } ^ { 4 }  { \mathbf { R } } ^ { 3 }$such that, writing$\Psi = \mathcal { T } ( \Xi )$as a shorthand, the solution u to the abstract fixed point map can be expanded as

$$
u = \Psi + \varphi {\bf 1} - \mathcal {I} (\Psi^ {3}) - 3 \varphi \mathcal {I} (\Psi^ {2}) + \left\langle \nabla \varphi , X \right\rangle + \varrho_ {u},\tag{9.22}
$$

where every component of$\varrho _ { u }$has homogeneity strictly greater than$- 4 - 2 \alpha$. In particular, since$( \Pi _ { z } ^ { M , ( \varepsilon ) } \Psi ) ( z ) = ( K * \xi _ { \varepsilon } ) ( z )$, one has the identity

$$
(\mathcal {R} u) (z) = \left(K * \xi_ {\varepsilon}\right) (z) + \varphi (z),
$$

where we denote by  the reconstruction operator associated to$Z _ { \varepsilon }$. As a consequence of (9.22),$F ( u ) = \Xi - u ^ { 3 }$can be expanded in increasing degrees of homogeneity as

$$
\begin{array}{r} F (u) = \Xi - \Psi^ {3} - 3 \varphi \Psi^ {2} + 3 \Psi^ {2} \mathcal {I} (\Psi^ {3}) - 3 \varphi^ {2} \Psi + 6 \varphi \Psi \mathcal {I} (\Psi^ {3}) \\ + 9 \varphi \Psi^ {2} \mathcal {I} (\Psi^ {2}) - 3 \langle \nabla \varphi , \Psi^ {2} X \rangle - \varphi^ {3} {\bf 1} + \varrho_ {F}, \end{array}
$$

where every component of$\varrho _ { F }$has strictly positive homogeneity. This time, one has the identity$\Delta ^ { \acute { M } } \tau = \stackrel { \quad } { M } \tau \otimes { \bf 1 } + \bar { \tau } ^ { ( 1 ) } \otimes \bar { \tau } ^ { ( 2 ) }$where each of the elements$\bar { \tau } ^ { ( 1 ) }$includes at least one factor$X _ { i }$. As a consequence, just like in the case of (PAMg), one has again the identity$( \Pi _ { z } ^ { M , ( \varepsilon ) } \tau ) ( z ) = ( \Pi _ { z } ^ { ( \varepsilon ) } M \tau ) ( z )$. It follows at once that, for u as in (9.22), one has the identity

$$
\begin{array}{r l} & {(\mathcal {R} ^ {M} F (u)) (z) = \xi_ {\varepsilon} (z) - (\mathcal {R} u) (z) ^ {3} + 3 C _ {1} (K * \xi_ {\varepsilon}) (z) + 3 C _ {1} \varphi (z)} \\ & {\qquad - 9 C _ {2} (K * \xi_ {\varepsilon}) (z) - 9 C _ {2} \varphi (z)} \\ & {\qquad = \xi_ {\varepsilon} (z) - (\mathcal {R} u) (z) ^ {3} + (3 C _ {1} - 9 C _ {2}) (\mathcal {R} u) (z).} \end{array}
$$

The claim now follows in the same way as in the proof of Proposition 9.4.

Remark 9.11 We could of course have taken for$F$an arbitrary polynomial of degree 3. If we take for example$F ( u ) = \Xi - u ^ { 3 } + a u ^ { 2 }$for some real constant a, then we obtain for our renormalised equation

$$
\partial_ {t} u _ {\varepsilon} = \Delta u _ {\varepsilon} + 3 (C _ {1} - 3 C _ {2}) u _ {\varepsilon} - u _ {\varepsilon} ^ {3} + a u _ {\varepsilon} ^ {2} - a (C _ {1} - 3 C _ {2}) + \xi_ {\varepsilon} .
$$

It is very interesting to note that, again, the renormalisation procedure formally “looks like” simple Wick renormalisation, except that the renormalisation constant does not equal the variance of the linearised equation. It is not clear at this stage whether this is a coincidence or has a deeper meaning.

In the case where no term$u ^ { 3 }$appears, the renormalisation procedure is significantly simplified since none of the terms involving$\mathcal { T } ( \Psi ^ { 3 } )$) appears. This then allows to reduce the problem to the methodology of [DPD02, DPD03], see also the recent work [EJS13]. In this case, the renormalisation is the usual Wick renormalisation involving only the constant$C _ { 1 }$

## 10 Homogeneous Gaussian models

One very important class of random models for a given regularity structure is given by “Gaussian models”, where the processes$\Pi _ { x } a$and$\Gamma _ { x y } a$are built from some underlying Gaussian white noise$\xi .$. Furthermore, we are going to consider the stationary situation where, for any given test function$\varphi ,$any$\tau \in T$, and any${ \boldsymbol { h } } \in  { \mathbf { R } } ^ { d }$, the processes $x \mapsto ( \Pi _ { x } \tau ) ( \varphi _ { x } )$and$x \mapsto \Gamma _ { x , x + h }$are stationary as a function of$x .$(Here, we wrote$\varphi _ { x }$ for the function$\varphi$translated so that it is centred around$x . )$Finally, in such a situation, it will be natural to assume that the random variables$( \Pi _ { x } \tau ) ( \psi )$and$\Gamma _ { x y } \tau$belong to the (inhomogeneous) Wiener chaos of some fixed order (depending only on τ) for$\xi .$. This is indeed the case for the canonical models$Z _ { \varepsilon }$built from some continuous Gaussian process$\xi _ { \varepsilon }$as in Section 8.2, provided that$\xi _ { \varepsilon } ( z )$is a linear functional of ξ for every z. It is also the case for the renormalised model$\hat { Z } _ { \varepsilon } = M ^ { \left( \varepsilon \right) } Z _ { \varepsilon }$, where$M ^ { \left( \varepsilon \right) }$denotes any element of the renormalisation group R built in Section 8.3.

Our construction suggests that there exists a general procedure such that, by using the general renormalisation procedure described in Section 8.3, it is typically possible to build natural stationary Gaussian models that can then be used as input for the abstract solution maps built in Section 7.3. As we have seen, the corresponding solutions can then typically be interpreted as limits of classical solutions to a renormalised version of the equation as in Section 9. Such a completely general statement does unfortunately seem out of reach for the moment, although someone with a deeper knowledge of algebra and constructive quantum field theory techniques might be able to achieve this. Therefore, we will only focus on two examples, namely on the case of the dynamical$\Phi _ { 3 } ^ { 4 }$model, as well as the generalisation of the two-dimensional continuous parabolic Anderson model given in (PAMg). Several of the intermediate steps in our construction are completely generic though, and would just as well apply, mutatis mutandis, to (PAM) in dimension 3, to (KPZ), or to (SNS).

## 10.1 Wiener chaos decomposition

In all the examples mentioned in the introduction, the driving noise$\xi$was Gaussian. Actually, it was always given by white noise on some copy of$\mathbf { R } ^ { d }$which would always include the spatial variables and, except for (PAM), would include the temporal variable as well. Mathematically, white noise is described by a probability space$( \Omega , { \mathcal { F } } , \mathbf { P } )$ as well as a Hilbert space$H$(typically some$L ^ { 2 }$space) and a collection$W _ { h }$of centred jointly Gaussian random variables indexed by$h \in H$with the property that the map $h \mapsto W _ { h }$is a linear isometry from H into$L ^ { 2 } ( \Omega , { \bf P } )$. In other words, one has the identity

$$
\mathbf {E} W _ {h} W _ {\bar {h}} = \left\langle h, \bar {h} \right\rangle ,
$$

where the scalar product on the right is the scalar product in$H .$

Remark 10.1 We will usually consider a situation where some symmetry group$\mathcal { S }$ acts on$\mathbf { R } ^ { d }$. In this case, H is actually given by$L ^ { 2 } ( D )$, where$D \subset \bar { { \mathbf { R } } } ^ { d }$is the fundamental domain of the action of$\mathcal { S }$. This comes with a natural projection π :$L ^ { 2 } ( \mathbf R ^ { d } ) \to H$ given by$\begin{array} { r } { ( \pi \varphi ) ( x ) = \sum _ { g \in \mathcal { S } } \varphi ( T _ { g } x ) } \end{array}$

In the setting of the above remark, this data also yields a random distribution, which we denote by$\xi ,$defined through$\xi ( \varphi ) \ { \stackrel { \mathrm { d e f } } { = } } \ W _ { \pi \varphi }$. If we endow$\mathbf { R } ^ { d }$with some scaling s, we have the following simple consequence of Proposition 3.20.

Lemma 10.2 The random distribution ξ defined above almost surely belongs to$\mathcal { C } _ { \mathfrak { s } } ^ { \alpha } f o r$ every$\alpha < - | \mathfrak { s } | / 2$. Furthermore, let$\varrho \colon \mathbf { R } ^ { d }  \mathbf { R }$be a smooth compactly supported function integrating to one, set$\varrho _ { \varepsilon } = \mathscr { S } _ { \mathfrak { s } , 0 } ^ { \varepsilon } \varrho ,$and define$\xi _ { \varepsilon } = \varrho _ { \varepsilon } * \xi .$. Then, for every $\alpha < - { \frac { | { \mathfrak { s } } | } { 2 } }$, every$\kappa > 0 ,$, and every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$, one has the bound

$$
\mathbf {E} \| \xi_ {\varepsilon} - \xi \| _ {\alpha ; \mathfrak {K}} \lesssim \varepsilon^ {- \frac {| s |}{2} - \alpha - \kappa}.
$$

Proof. The proof is almost identical to the proof of the first part of Proposition$9 . 5$ The calculations are actually more straightforward since the indicator functions$\mathbf { 1 } _ { t \geq s }$ do not appear, so we leave this as an exercise.□

It was first remarked by Wiener [Wie38] that there exists a natural isometry between all of$L ^ { 2 } ( \Omega , { \bf P } )$and the “symmetric Fock space”

$$
\hat {H} = \bigoplus_ {k \geq 0} H ^ {\otimes_ {s} k},
$$

where$H ^ { \otimes _ { s } k }$denotes the symmetric k-fold tensor product of$H$. Here, we identify $H ^ { \otimes s k }$with$H ^ { \otimes k }$, quotiented by the equivalence relations

$$
e _ {i _ {1}} \otimes \ldots \otimes e _ {i _ {k}} \sim e _ {i _ {\sigma (1)}} \otimes \dots \otimes e _ {i _ {\sigma (k)}},
$$

where σ is an arbitrary permutation of k elements. (This extends by linearity.)

If$\{ e _ { n } \} _ { n \ge 0 }$denotes an orthonormal basis of H then, for any sequence$k _ { 0 } , k _ { 1 } , \ldots$ of positive integers with only finitely many non-zero elements, Wiener’s isometry is given by

$$
k! e _ {k} \stackrel {\mathrm{def}} {=} k! e _ {0} ^ {\otimes k _ {0}} \otimes e _ {1} ^ {\otimes k _ {1}} \otimes \dots \quad \Leftrightarrow \quad H _ {k _ {0}} (W _ {e _ {0}}) H _ {k _ {1}} (W _ {e _ {1}}) \dots ,
$$

where$H _ { n }$denotes the nth Hermite polynomial,$k ! = k _ { 0 } ! k _ { 1 } ! \cdot \cdot \cdot$, and$e _ { k }$has norm 1. Random variables in correspondence with elements in$H ^ { \otimes _ { s } m }$are said to belong to the mth homogeneous Wiener chaos. The mth inhomogeneous chaos is the sum of all the homogeneous chaoses of orders$\ell \leq m$. See also [Nua06, Ch. 1] for more details.

We have a natural projection$H ^ { \otimes m }  H ^ { \otimes _ { s } m }$: just map an element to its equivalence class. Composing this projection with Wiener’s isometry yields a natural family of maps$I _ { m } \colon H ^ { \otimes m }  L ^ { 2 } ( \Omega , { \bf P } )$with the property that

$$
\mathbf {E} (I _ {m} (f) ^ {2}) \leq \| f \| ^ {2},
$$

where$f \in H ^ { \otimes m }$is identified with an element of$L ^ { 2 } ( D ^ { d } )$, and the right hand side denotes its$L ^ { 2 }$norm. In the case of an element f that is symmetric under the permutation of its m arguments, this inequality turns into an equality. For this reason, many authors restrict themselves to symmetric functions from the start, but it turns out that allowing ourselves to work with non-symmetric functions will greatly simplify some expressions later on.

Note that in the case$m = 1$, we simply have$I _ { 1 } ( h ) = W _ { h }$. The case$m = 0$ corresponds to the natural identification of$H ^ { 0 } \sim \textbf { R }$with the constant elements of $L ^ { 2 } ( \Omega , { \bf P } )$. To state the following result, we denote by$S ( r )$the set of all permutations of r elements, and by$S ( r , m ) \subset S ( m )$the set of all “shuffles” of r and$m - r$elements, namely the set of permutations of m elements which preserves the order of the first r and of the last$m - r$elements. For$x \in D ^ { m }$and$\Sigma \in S ( m )$, we write$\Sigma ( x ) \in D ^ { m }$as a shorthand for$\Sigma ( x ) _ { i } = x _ { \Sigma ( i ) }$. For$x \in D ^ { r }$and$y \in D ^ { m - r }$, we also denote by$x \sqcup y$ the element of$D ^ { m }$given by$( x _ { 1 } , \ldots , x _ { r } , y _ { 1 } , \ldots , y _ { m - r } )$. With these notations, we then have the following formula for the product of two elements.

Lemma 10.3 Let$f \in L ^ { 2 } ( D ^ { \ell } )$and$g \in L ^ { 2 } ( D ^ { m } )$. Then, one has

$$
I _ {\ell} (f) I _ {m} (g) = \sum_ {r = 0} ^ {\ell \wedge m} I _ {\ell + m - 2 r} (f \star_ {r} g),\tag{10.1}
$$

where

$$
(f\star_{r}g)(z\sqcup \tilde{z}) = \sum_{\substack{\Sigma \in \mathcal{S}(r,\ell)\\ \tilde{\Sigma}\in \mathcal{S}(r,m)}}\sum_{\sigma \in \mathcal{S}(r)}\int_{D^{r}}f(\Sigma (x\sqcup z))g(\tilde{\Sigma} (x\sqcup \sigma (\tilde{z})))  dx  ,
$$

for all$z \in D ^ { \ell - r }$and$\tilde { z } \in D ^ { m - r }$

Proof. See [Nua06, Prop. 1.1.2].

Remark 10.4 Informally speaking, Lemma 10.3 states that in order to build the chaos decomposition of the product$I _ { \ell } ( f ) I _ { m } ( g )$, one should consider all possible ways of pairing$r$of the ℓ arguments of$f$with r of the m arguments of$g$and integrate over these paired arguments. This should really be viewed as an extension of Wick’s product formula for Gaussian random variables.

A remarkable property of the Wiener chaoses is the following equivalence of moments:

Lemma 10.5 Let$X ~ \in ~ L ^ { 2 } ( \Omega , \mathbf { P } )$be a random variable in the kth inhomogeneous Wiener chaos. Then, for every$p \geq 1$, there exists a universal constant$C _ { k , p }$such that$\mathbf { E } | X ^ { 2 p } | \leq C _ { k , p } ( \mathbf { E } X ^ { 2 } ) ^ { p }$

Proof. This is a consequence of Nelson’s hypercontractive estimate [Nel73, Gro75], combined with the fact that the Wiener chaos decomposition diagonalises the Ornstein-Uhlenbeck semigroup.□

## 10.2 Gaussian models for regularity structures

From now on, we assume that we are given a probability space$( \Omega , { \mathcal { F } } , \mathbf { P } )$, together with an abstract white noise$h \mapsto W _ { h }$over the Hilbert space$H = L ^ { 2 } ( D )$. We furthermore assume that we are given a Gaussian random distribution$\xi$which has the property that, for every test function ψ, the random variable$\xi ( \psi )$belongs to the homogeneous first Wiener chaos of$W$

Remark 10.6 One possible choice of noise$\xi$is given by$\xi ( \psi ) = W _ { \psi }$, which corresponds to white noise. While this is a very natural choice in many physical situations, this is not the only choice by far.

We furthermore assume that we are given a sequence$\xi _ { \varepsilon }$of continuous approximations to ξ with the following properties:

For every$\varepsilon > 0$, the map$x \mapsto \xi _ { \varepsilon } ( x )$is continuous almost surely.

For every$\varepsilon > 0$and every$\boldsymbol { x } \in \mathbf { R } ^ { d } , \boldsymbol { \xi } _ { \varepsilon } ( \boldsymbol { x } )$is a random variable belonging to the first Wiener chaos of W.

For every test function ψ, one has

$$
\lim _ {\varepsilon \rightarrow 0} \int_ {\mathbf {R} ^ {d}} \xi_ {\varepsilon} (x) \psi (x) d x = \xi (\psi),
$$

in$L ^ { 2 } ( \Omega , { \bf P } )$

Given such an approximation, one would ideally like to be able to show that the corresponding sequence$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$of canonical models built from$\xi _ { \varepsilon }$in Section 8.2 converges to some limit. As already mentioned several times, this is simply not the case in general, thus the need for a suitable renormalisation procedure. We will always consider renormalisation procedures based on a sequence$M _ { \varepsilon }$of elements in the renormalisation group R built in Section 8.3. We will furthermore take advantage of the fact that we know a priori that the models$( \Pi ^ { ( \varepsilon ) } , \Gamma ^ { ( \varepsilon ) } )$belong to some fixed Wiener chaos.

Indeed, we can denote by$\| \tau \|$the number of occurrences of$\Xi$in the formal expression τ. More formally, we set$\| \mathbf { 1 } \| = \| X \| = 0 , \| \Xi \| = 1$, and then recursively

$$
\left\| \tau \bar {\tau} \right\| = \left\| \tau \right\| + \left\| \bar {\tau} \right\|, \quad \left\| \mathcal {I} _ {k} \tau \right\| = \left\| \tau \right\|.
$$

Then, as an immediate consequence of Lemma 10.3, for any fixed$\boldsymbol { \tau } \in \mathcal { F } _ { F } , \boldsymbol { x } \in \mathbf { R } ^ { d }$ and smooth test function$\psi ,$the random variables$( \Pi _ { x } ^ { ( \varepsilon ) } \tau ) ( \psi )$and$\Gamma _ { x y } ^ { ( \varepsilon ) } \tau$belong to the (inhomogeneous) Wiener chaos of order$\| \tau \|$. Actually, it belongs to the sum of the homogeneous chaoses of orders$\| \tau \| - 2 n$for n a positive integer, and this is still true for the renormalised models. From now on, we denote$\mathcal { F } _ { - } = \{ \tau \in \mathcal { F } _ { F } : | \tau | _ { \mathfrak { s } } < 0 \}$ The following convergence criterion is the foundation on which all of our convergence results are built.

Theorem 10.7 Let F be a locally subcritical nonlinearity and let$\mathcal { T } _ { F } ^ { ( r ) }$be the corresponding regularity structure built in Section 8, restricted to$\{ \tau : | \tau | _ { \mathfrak { s } } \leq r \}$. Let$M _ { \varepsilon }$ be a sequence of elements in its renormalisation group R, let$\xi _ { \varepsilon }$be an approximation to$\xi$as in Lemma 10.2 with associated canonical model$Z _ { \varepsilon } ~ = ~ ( \Pi ^ { \left( \varepsilon \right) } , \Gamma ^ { \left( \varepsilon \right) } )$, and let $\hat { Z } _ { \varepsilon } = ( \hat { \Pi } ^ { ( \varepsilon ) } , \hat { \Gamma } ^ { ( \varepsilon ) } ) = M _ { \varepsilon } Z _ { \varepsilon }$be the corresponding sequence of renormalised models.

Assumefurthermore that there is$\kappa > 0$such that, for every test function$\varphi \in B _ { \mathfrak { s } , 0 } ^ { r } ,$ every$\boldsymbol { x } \in \mathbf { R } ^ { d }$, and every$\tau \in { \mathcal { F } } .$, there exists a random variable$( { \hat { \Pi } } _ { x } \tau ) ( \varphi )$belonging to the inhomogeneous Wiener chaos of order$\| \tau \|$such that

$$
\mathbf {E} | (\hat {\Pi} _ {x} \tau) (\varphi_ {x} ^ {\lambda}) | ^ {2} \lesssim \lambda^ {2 | \tau | _ {\mathfrak {s}} + \kappa},\tag{10.2}
$$

and such that, for some$\theta > 0$

$$
\mathbf {E} \big | (\hat {\Pi} _ {x} \tau - \hat {\Pi} _ {x} ^ {(\varepsilon)} \tau) (\varphi_ {x} ^ {\lambda}) \big | ^ {2} \lesssim \varepsilon^ {2 \theta} \lambda^ {2 | \tau | _ {\mathfrak {s}} + \kappa}.\tag{10.3}
$$

Then, there exists a unique admissible random model$\hat { Z } = ( \hat { \Pi } , \hat { \Gamma } ) o f \mathcal { T } _ { F } ^ { ( r ) }$such that,for every compact set$\mathcal { R } \subset \mathbf { R } ^ { d }$and every$p \geq 1$, one has the bounds

$$
\mathbf {E} \| \hat {Z} \| _ {\mathfrak {K}} ^ {p} \lesssim 1, \qquad \mathbf {E} \| \hat {Z}; \hat {Z} _ {\varepsilon} \| _ {\mathfrak {K}} ^ {p} \lesssim \varepsilon^ {\theta p}.
$$

Remark 10.8 As already seen previously, it is actually sufficient to take for$\varphi$the scaling function of some sufficiently regular compactly supported wavelet basis.

Proof. Note first that the proportionality constants appearing in (10.2) and (10.3) are independent of$x$by stationarity. Let now$\nu \subset \mathcal { F }$be any finite collection of basis vectors, let$V = \langle \nu \rangle$, and assume that$\nu$is such that$\Delta V \subset V \otimes \mathcal { H } _ { + }$, so that$V$is a sector of$\mathcal { T } _ { F }$. Then, it follows from Proposition 3.32 that, for every compact set${ \mathcal { R } } ,$one has the bound

$$
\begin{array}{l} \mathbf {E} \| \hat {\Pi} \| _ {V; \mathfrak {K}} ^ {p} \lesssim \mathbf {E} \Big ((1 + \| \Gamma \| _ {V; \mathfrak {K}}) ^ {p} \sup _ {\tau \in \mathcal {V}} \sup _ {n \geq 0} \sup _ {x \in \Lambda_ {\mathfrak {s}} ^ {n} (\bar {\mathfrak {K}})} 2 ^ {| \tau | _ {\mathfrak {s}} p n + \frac {p n | \mathfrak {s} |}{2}} | (\hat {\Pi} _ {x} \tau) (\varphi_ {x} ^ {n, \mathfrak {s}}) | ^ {p} \Big) \\ \lesssim \sqrt {\mathbf {E} (1 + \| \Gamma \| _ {V ; \mathfrak {K}}) ^ {2 p}} \sum_ {\tau \in \mathcal {V}} \sum_ {n \geq 0} 2 ^ {n | \mathfrak {s} | + | \tau | _ {\mathfrak {s}} p n + \frac {p n | \mathfrak {s} |}{2}} (\mathbf {E} | (\hat {\Pi} _ {0} \tau) (\varphi_ {0} ^ {n, \mathfrak {s}}) | ^ {2}) ^ {\frac {p}{2}}, \end{array} \tag {10.4}\tag{10.4}
$$

where the proportionality constant depends on$\mathcal { \kappa }$and the choice of$\nu .$Here, we used stationarity and Lemma 10.5 to go from the first to the second line. A similar bound also holds for$\hat { \Pi } ^ { ( \varepsilon ) }$, as well as for the difference between the two models.

The claim will now be proved by induction over${ \mathcal { F } } ^ { ( n ) }$, where${ \mathcal { F } } ^ { ( n ) }$was defined in Section 8.3. Recall that for every$n \geq 0$, the linear span$T _ { n } \ { \stackrel { \mathrm { d e f } } { = } } \ \langle { \mathcal { F } } ^ { ( n ) } \rangle$forms a sector of$\mathcal { T } _ { F }$, that these sectors exhaust all of the model space$T _ { \mathbf { \delta } }$, and that one has $\Delta T _ { n } \subset T _ { n } \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n - 1 ) } ) \rangle$. As a consequence, it is sufficient to prove that, for every $p \geq 0$, one has the bounds

$$
\mathbf {E} \| \hat {Z} \| _ {T _ {n}; \mathfrak {K}} ^ {p} \lesssim 1, \qquad \mathbf {E} \| \hat {Z}; \hat {Z} _ {\varepsilon} \| _ {T _ {n}; \mathfrak {K}} ^ {p} \lesssim \varepsilon^ {\kappa p}.
$$

The claim is trivial for$n = 0$, so we assume from now on that it holds for some $n \geq 0$. As a consequence of the definition of$\mathcal { F } ^ { ( n + 1 ) }$and the fact that we only consider admissible models, the action of${ \hat { \Gamma } } _ { x y }$on it is determined by the corresponding values $\hat { f } _ { x } ( \tau )$for$\tau \in \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } )$. Since furthermore the functionals${ \hat { f } } _ { x }$are multiplicative and, on elements of the form$\mathcal { T } _ { k } \tau$, we know from our definition of the canonical model and of the renormalisation group that (8.32) holds, we conclude from the finiteness of the set${ \mathcal { F } } ^ { ( n ) }$and from Theorem 5.14 that there exists some power k (possibly depending on n) such that the deterministic bounds

$$
\begin{array}{c} \| \hat {\Gamma} \| _ {T _ {n + 1}; \mathfrak {K}} \lesssim (1 + \| \hat {Z} \| _ {T _ {n}; \mathfrak {K}}) ^ {k}, \\ \| \hat {\Gamma} - \hat {\Gamma} ^ {(\varepsilon)} \| _ {T _ {n + 1}; \mathfrak {K}} \lesssim \| \hat {Z}; \hat {Z} _ {\varepsilon} \| _ {T _ {n}; \mathfrak {K}} (1 + \| \hat {Z} \| _ {T _ {n}; \mathfrak {K}}) ^ {k}, \end{array}
$$

hold. We now write$\mathcal { F } ^ { ( n + 1 ) } = \mathcal { F } _ { - } ^ { ( n + 1 ) } \cup \mathcal { F } _ { + } ^ { ( n + 1 ) }$, where${ \mathcal { F } } _ { - } ^ { ( n + 1 ) } = { \mathcal { F } } ^ { ( n + 1 ) } \cap { \mathcal { F } } _ { - }$-，while the second set contains the remainder. Setting$T _ { n + 1 } ^ { - } = \langle \mathcal { F } _ { - } ^ { ( n + 1 ) } \rangle$, it follows from Assumption 8.33 and (2.1) that$\Delta T _ { n + 1 } ^ { - } \subset T _ { n + 1 } ^ { - } \otimes \langle \mathrm { A l g } ( \mathcal { F } ^ { ( n ) } ) \rangle$

It thus follows from (10.4) and (10.2) that

$$
\mathbf {E} \| \hat {\Pi} \| _ {T _ {n + 1} ^ {-}; \mathfrak {K}} ^ {p} \lesssim \sqrt {\mathbf {E} (1 + \| \Gamma \| _ {T _ {n + 1} ; \mathfrak {K}}) ^ {2 p}} \sum_ {\tau \in \mathcal {V}} \sum_ {n \geq 0} 2 ^ {n | \mathfrak {s} | - \kappa p n}.
$$

Provided that$p$is large enough so that$\kappa p > | { \mathfrak { s } } |$, which is something that we can always assume without any loss of generality since p was arbitrary, it follows that Π<sup>ˆ</sup> does indeed satisfy the required bound on$T _ { n + 1 } ^ { - }$. Regarding the difference${ \hat { \Pi } } - { \hat { \Pi } } ^ { ( \varepsilon ) }$ we obtain the corresponding bound in an identical manner. In order to conclude the argument, it remains to obtain a similar bound on all of$T _ { n + 1 }$. This however follows by applying Proposition 3.31, proceeding inductively in increasing order of homogeneity. Note that each element we treat in this way has strictly positive homogeneity since we assume that only 1 has homogeneity zero, and$\Pi _ { x } \mathbf { 1 } = 1$, so nothing needs to be done there.□

We assume from now on that we are in the setting of Theorem 10.7 and therefore only need to obtain the convergence of$( \hat { \Pi } _ { x } ^ { \left( \varepsilon \right) } \tau ) ( \varphi )$to a limiting random variable $( { \hat { \Pi } } _ { x } \tau ) ( \varphi )$with the required bounds when considering rescaled versions$\mathrm { o f } \ \varphi .$. We also assume that we are in a translation invariant situation in the sense that$\mathbf { R } ^ { d }$acts onto H via a group of unitary operators$\{ S _ { x } \} _ { x \in \mathbf { R } ^ { d } }$and there exists an element$\varrho _ { \varepsilon } \in H$such that

$$
\xi_ {\varepsilon} (x) = I _ {1} (S _ {x} \varrho_ {\varepsilon})  ,
$$

where$I _ { 1 }$is as in Section 10.1. As a consequence,$\mathbf { E } | ( \hat { \Pi } _ { x } \tau ) ( \varphi _ { x } ) | ^ { 2 }$is independent of x, so that we only need to consider the case$x = 0$

Since the map$\varphi \mapsto ( \hat { \Pi } _ { x } ^ { \left( \varepsilon \right) } \tau ) ( \varphi )$is linear, one can find some functions (or possibly distributions in general)$\hat { \mathcal { W } } ^ { ( \varepsilon ; k ) } \tau$with

$$
(\hat {\mathcal {W}} ^ {(\varepsilon ; k)} \tau) (x) \in H ^ {\otimes k},\tag{10.5}
$$

where$\boldsymbol { x } \in \mathbf { R } ^ { d }$, and such that

$$
(\hat {\Pi} _ {0} ^ {(\varepsilon)} \tau) (\varphi) = \sum_ {k \leq \| \tau \|} I _ {k} \Bigl (\int_ {\mathbf {R} ^ {d}} \varphi (y) (\hat {\mathcal {W}} ^ {(\varepsilon ; k)} \tau) (y) d y \Bigr),\tag{10.6}
$$

where$I _ { k }$is as in Section 10.1. The same is of course also true of the bare model$\Pi ^ { ( \varepsilon ) }$ and we denote the corresponding functions by${ \mathscr W } ^ { ( \varepsilon ; k ) } \tau$

Remark 10.9 Regarding$\hat { \Pi } _ { x } ^ { \left( \varepsilon \right) } \tau$for$x \neq 0$, it is relatively straightforward to see that one has the identity

$$
(\hat {\Pi} _ {x} ^ {(\varepsilon)} \tau) (\varphi_ {x}) = \sum_ {k \leq \| \tau \|} I _ {k} \left(\int_ {\mathbf {R} ^ {d}} \varphi (y) S _ {x} ^ {\otimes k} (\hat {\mathcal {W}} ^ {(\varepsilon ; k)} \tau) (y) d y\right),\tag{10.7}
$$

which again implies that the law of these random variables is independent of$x _ { \ast }$

Remark 10.10 For every$x \in \mathbf { R } ^ { d } , ( \hat { \mathcal { W } } ^ { ( \varepsilon ; k ) } \tau ) ( x )$is a function on$k$copies of D. We will therefore also denote it by$( \hat { \mathcal { W } } ^ { ( \varepsilon ; k ) } \tau ) ( x ; y _ { 1 } , \dots , y _ { k } )$. Note that the dimension of x is not necessarily the same as that of the$y _ { i }$. This is the case for example in$\mathbf { ( P A M g ) }$ where the equation is formulated in${ \bf R } ^ { 3 }$(one time dimension and two space dimensions), while the driving noise$\xi$lives in the Wiener chaos over a subset of${ \bar { \mathbf { R } } } ^ { 2 }$

We then have the following preliminary result which shows that, in the kind of situations we consider here, the convergence of the models$\hat { Z } _ { \varepsilon }$to some limiting model $\hat { Z }$can often be reduced to the convergence of finitely many quite explicit kernels.

Proposition 10.11 In the situation just described, fix some$\tau \in { \mathcal { F } } .$<sub>−</sub> and assume that there exists some$\kappa > 0$such that,for every$k \leq \| \tau \|$, there existfunctions${ \hat { \mathcal { W } } } ^ { ( k ) } \tau$with values in$H ^ { \otimes k }$and such that

$$
| \langle (\hat {\mathcal {W}} ^ {(k)} \tau) (z), (\hat {\mathcal {W}} ^ {(k)} \tau) (\bar {z}) \rangle | \leq C \sum_ {\zeta} (\| z \| _ {\mathfrak {s}} + \| \bar {z} \| _ {\mathfrak {s}}) ^ {\zeta} \| z - \bar {z} \| _ {\mathfrak {s}} ^ {\kappa + 2 | \tau | _ {\mathfrak {s}} - \zeta},
$$

where the sum runs over finitely many values$\zeta \in [ 0 , 2 | \tau | _ { \mathfrak { s } } + \kappa + | \mathfrak { s } | )$. Here, we denoted $b y \left. \cdot , \cdot \right.$the scalar product in$H ^ { \otimes k }$

Assumefurthermore that there exists$\theta > 0$such that

$$
| \langle (\delta \hat {\mathcal {W}} ^ {(\varepsilon ; k)} \tau) (z), (\delta \hat {\mathcal {W}} ^ {(\varepsilon ; k)} \tau) (\bar {z}) \rangle | \leq C \varepsilon^ {2 \theta} \sum_ {\zeta} (\| z \| _ {\mathfrak {s}} + \| \bar {z} \| _ {\mathfrak {s}}) ^ {\zeta} \| z - \bar {z} \| _ {\mathfrak {s}} ^ {\kappa + 2 | \tau | _ {\mathfrak {s}} - \zeta},\tag{10.8}
$$

where we have set$\delta \hat { \mathcal { W } } ^ { ( \varepsilon ; k ) } = \hat { \mathcal { W } } ^ { ( \varepsilon ; k ) } - \hat { \mathcal { W } } ^ { ( k ) }$, and where the sum is as above.$T h e n ,$, the bounds (10.2) and (10.3) are satisfied for τ.

Proof. In view of (10.6) and (10.7) we define, for every smooth test function$\psi$and every$\boldsymbol { x } \in \mathbf { R } ^ { d }$the random variable$( { \hat { \Pi } } _ { x } \tau ) ( \psi )$by

$$
(\hat {\Pi} _ {x} \tau) (\psi) = \sum_ {k \leq \| \tau \|} (\hat {\Pi} _ {x} ^ {(k)} \tau) (\psi) = \sum_ {k \leq \| \tau \|} I _ {k} \left(\int_ {\mathbf {R} ^ {3}} \psi (z) S _ {x} ^ {\otimes k} (\hat {\mathcal {W}} ^ {(k)} \tau) (z) d z\right).\tag{10.9}
$$

We then have the bound

$$
\begin{aligned} & \mathbf{E}|(\hat{\Pi}_{x}^{(k)}\tau)(\psi_{x}^{\lambda})|^{2} = \mathbf{E}|(\hat{\Pi}_{0}^{(k)}\tau)(\psi^{\lambda})|^{2}\lesssim \left\| \int_{\mathbf{R}^{d}}\psi^{\lambda}(z)(\hat{\mathcal{W}}^{(k)}\tau)(z)  dz\right\|^{2}\\ & \qquad = \int \int \psi^{\lambda}(z)\psi^{\lambda}(\bar{z})\langle (\hat{\mathcal{W}}^{(k)}\tau)(z),(\hat{\mathcal{W}}^{(k)}\tau)(\bar{z})\rangle  dz  d\bar{z}\\ & \qquad \lesssim \lambda^{-2|\mathfrak{s}|}\sum_{\zeta}\int_{\substack{\| z\|_{\mathfrak{s}}\leq \lambda \\ \| \bar{z}\|_{\mathfrak{s}}\leq \lambda}}(\| z\|_{\mathfrak{s}} + \| \bar{z}\|_{\mathfrak{s}})^{\zeta}\| z - \bar{z}\|_{\mathfrak{s}}^{\kappa +2|\tau |_{\mathfrak{s}} - \zeta}  dz  d\bar{z}\\ & \qquad \lesssim \lambda^{-2|\mathfrak{s}|}\sum_{\zeta}\lambda^{\zeta +|\mathfrak{s}|}\int_{\| z\|_{\mathfrak{s}}\leq 2\lambda}\| z\|_{\mathfrak{s}}^{\kappa +2|\tau |_{\mathfrak{s}} - \zeta}  dz \end{aligned}
$$

$$
\lesssim \lambda^ {- 2 | \mathfrak {s} |} \sum_ {\zeta} \lambda^ {\zeta + 2 | \mathfrak {s} | + \kappa + 2 | \tau | _ {\mathfrak {s}} - \zeta} \lesssim \lambda^ {\kappa + 2 | \tau | _ {\mathfrak {s}}}.
$$

A virtually identical calculation, but making use instead of the bound on$\delta \hat { \mathcal { W } } ^ { ( \varepsilon ; k ) }$, also yields the bound

$$
\mathbf {E} | (\hat {\Pi} _ {x} ^ {(\varepsilon)} - \hat {\Pi} _ {x} \tau) (\psi_ {x} ^ {\lambda}) | ^ {2} \lesssim \varepsilon^ {2 \theta} \lambda^ {\kappa + 2 | \tau | _ {\mathfrak {s}}},
$$

as claimed.

## 10.3 Functions with prescribed singularities

Before we turn to examples of SPDEs for which the corresponding sequence of canonical models for the regularity structure$\mathcal { T } _ { F }$can be successfully renormalised, we perform a few preliminary computations on the behaviour of smooth functions having a singularity of prescribed strength at the origin.

Definition 10.12 Let s be a scaling of$\mathbf { R } ^ { d }$and let$K \colon \mathbf { R } ^ { d } \ \backslash \ \{ 0 \} \  \ \mathbf { R }$be a smooth function. We say that K is of order$\zeta$if, for every sufficiently small multiindex$k ,$there exists a constant$C$such that the bound$\begin{array} { r } { | D ^ { k } K ( x ) | \leq C \| x \| _ { \mathfrak H } ^ { \zeta - | k | , } } \end{array}$<sup>s</sup> holds for every x with$\| x \| _ { \mathfrak { s } } \leq 1$

For any$m \geq 0$, we furthermore write

$$
\| K \| _ {\zeta ; m} \stackrel {{\text { def }}} {{=}} \sup _ {| k | _ {\mathfrak {s}} \leq m} \sup _ {x \in \mathbf {R} ^ {d}} \| x \| _ {\mathfrak {s}} ^ {| k | _ {\mathfrak {s}} - \zeta} | D ^ {k} K (x) |  .
$$

Remark 10.13 Note that this is purely an upper bound on the behaviour of$K$near the origin. In particular, if K is of order$\zeta ,$then it is also of order$\bar { \zeta }$for every$\bar { \zeta } < \zeta$

Lemma 10.14 Let$K _ { 1 }$and$K _ { 2 }$be two compactly supported functions of respective orders$\zeta _ { 1 }$and$\zeta _ { 2 }$. Then$K _ { 1 } K _ { 2 }$is oforder$\zeta = \zeta _ { 1 } + \zeta _ { 2 }$and one has the bound

$$
\left\| K _ {1} K _ {2} \right\| _ {\zeta ; m} \leq C \left\| K _ {1} \right\| _ {\zeta_ {1}; m} \left\| K _ {2} \right\| _ {\zeta_ {2}; m},
$$

where C depends on the sizes ofthe supports ofthe$K _ { i }$

$I f \zeta _ { 1 } \wedge \zeta _ { 2 } > - | \mathfrak { s } |$andfurthermore$\bar { \zeta } \overset { d e f } { = } \zeta _ { 1 } + \zeta _ { 2 } + | \mathfrak { s } |$satisfies$\bar { \zeta } < 0 ,$, then$K _ { 1 } * K _ { 2 }$ is oforder$\zeta$and one has the bound

$$
\left\| K _ {1} * K _ {2} \right\| _ {\bar {\zeta}; m} \leq C \left\| K _ {1} \right\| _ {\zeta_ {1}; m} \left\| K _ {2} \right\| _ {\zeta_ {2}; m}.\tag{10.10}
$$

In both of these bounds,$m \in \mathbf { N }$is arbitrary. In general,$i f { \bar { \zeta } } \in \mathbf { R } _ { + } \setminus \mathbf { N } ,$then$K _ { 1 } * K _ { 2 }$ has derivatives of order$| k | _ { s } < \bar { \zeta }$at the origin and the function K given by

$$
K (x) = (K _ {1} * K _ {2}) (x) - \sum_ {| k | _ {\mathfrak {s}} <   \bar {\zeta}} \frac {x ^ {k}}{k !} D ^ {k} (K _ {1} * K _ {2}) (0)\tag{10.11}
$$

is oforder$\bar { \zeta } .$Furthermore, one has the bound

$$
\| K \| _ {\bar {\zeta}; m} \leq C \| K _ {1} \| _ {\zeta_ {1}; \bar {m}} \| K _ {2} \| _ {\zeta_ {2}; \bar {m}},\tag{10.12}
$$

where we set$\bar { m } = m \vee ( \lfloor \bar { \zeta } \rfloor + \operatorname* { m a x } \{ \mathfrak { s } _ { i } \} )$

Proof. The claim about the product$K _ { 1 } K _ { 2 }$is an immediate consequence of the generalised Leibniz rule, so we only need to bound$K _ { 1 } * K _ { 2 }$. We will first show that, for every$x \neq 0$and every multiindex k such that$\bar { \zeta } < | k | _ { s }$, one does have the bound

$$
| D ^ {k} (K _ {1} * K _ {2}) (x) | \lesssim \| x \| _ {\mathfrak {s}} ^ {\bar {\zeta} - | k | _ {\mathfrak {s}}} \| K _ {1} \| _ {\zeta_ {1}; | k | _ {\mathfrak {s}}} \| K _ {2} \| _ {\zeta_ {2}; | k | _ {\mathfrak {s}}},\tag{10.13}
$$

as required. From such a bound, (10.10) follows immediately. To show that (10.12) follows from (10.13), we note first that$D ^ { k } K = D ^ { k } ( K _ { 1 } * K _ { 2 } )$for every k such that $| k | _ { s } > \bar { \zeta }$, so that it remains to show that it is possible to find some numbers which we then call$D ^ { k } ( K _ { 1 } * K _ { 2 } ) ( 0 )$such that if K is defined by (10.11), then similar bounds hold for$D ^ { k } K$with$| k | _ { s } < \bar { \zeta }$

For this, we define the set of multiindices$A _ { \bar { \zeta } } = \{ k : | k | _ { \bar { \varsigma } } < \bar { \zeta } \}$and we fix a decreasing enumeration$A _ { \bar { \zeta } } = \{ k _ { 0 } , \ldots , k _ { M } \} , \mathrm { i . e . } | \bar { k } _ { m } | _ { s } \geq | k _ { n } | _ { s }$whenever$m \leq n$. We then start by setting$\bar { K } ^ { ( 0 ) } ( \bar { x } ) = ( K _ { 1 } * K _ { 2 } ) ( x )$and we build a sequence of functions $\bar { K } ^ { ( n ) } ( x )$iteratively as follows. Assume that we have the bound$| D ^ { k _ { n } + e _ { i } } K ^ { ( n ) } ( x ) | \ \lesssim$ $\| \boldsymbol { x } \| _ { \mathfrak { s } } ^ { \bar { \zeta } - | k _ { n } | _ { s } - \mathfrak { s } _ { i } }$for$i \in \{ 1 , \ldots , d \}$. (This is the case for$n = 0 \mathrm { b y } ( 1 0 . 1 3 ) . )$Proceeding as in the proof of Lemma 6.5 it then follows that one can find a real number$C _ { n }$such that$| D ^ { k _ { n } } K ^ { ( n ) } ( x ) - C _ { n } | \lesssim \| x \| _ { \mathfrak { s } } ^ { \bar { \zeta } - | k _ { n } | _ { \mathfrak { s } } }$. We then set$\begin{array} { r } { K ^ { ( n + 1 ) } ( x ) = K ^ { ( n ) } ( x ) - C _ { n } \frac { x ^ { k _ { n } } } { k _ { n } ! } } \end{array}$. It is then straightforward to verify that if we set$K ( x ) = K ^ { ( M ) } ( x )$), it has all the required properties.

It remains to show that (10.13) does indeed hold. For this, let$\varphi \colon \mathbf { R } ^ { d }$be a smooth function from$\mathbf { R } ^ { d } \mathrm { t o } [ 0 , 1 ]$such that$\varphi ( x ) = 0 \mathrm { f o r } \| x \| _ { \mathfrak { s } } \geq 1$and$\varphi ( x ) = 1$for$\| x \| _ { \mathfrak { s } } \leq \frac { 1 } { 2 }$ For$r > 0$, we also set$\varphi _ { r } ( y ) = \varphi ( S _ { \mathfrak { s } } ^ { r } y )$. Since K is bilinear in$K _ { 1 }$and$K _ { 2 } ,$, we can assume without loss of generality that$\| K _ { i } \| _ { \zeta _ { i } ; | k | _ { s } } = 1$. With these notations at hand, we can write

$$
\begin{array}{l} (K _ {1} * K _ {2}) (x) = \int_ {\mathbf {R} ^ {d}} \varphi_ {r} (y) K _ {1} (x - y) K _ {2} (y) d y + \int_ {\mathbf {R} ^ {d}} \varphi_ {r} (x - y) K _ {1} (x - y) K _ {2} (y) d y \\ \quad + \int_ {\mathbf {R} ^ {d}} \bigl (1 - \varphi_ {r} (y) - \varphi_ {r} (x - y) \bigr) K _ {1} (x - y) K _ {2} (y) d y \\ = \int_ {\mathbf {R} ^ {d}} \varphi_ {r} (y) K _ {1} (x - y) K _ {2} (y) d y + \int_ {\mathbf {R} ^ {d}} \varphi_ {r} (y) K _ {1} (y) K _ {2} (x - y) d y \\ \quad + \int_ {\mathbf {R} ^ {d}} \bigl (1 - \varphi_ {r} (y) - \varphi_ {r} (x - y) \bigr) K _ {1} (x - y) K _ {2} (y) d y, \end{array} \tag {10.14}
$$

so that, provided that$r \leq \| x \| _ { \mathfrak { s } } / 2$, say, one has the identity

$$
\begin{array}{l} D ^ {k} (K _ {1} * K _ {2}) (x) = \int_ {\mathbf {R} ^ {d}} \varphi_ {r} (y) D ^ {k} K _ {1} (x - y) K _ {2} (y) d y \\ \qquad + \int_ {\mathbf {R} ^ {d}} \varphi_ {r} (y) K _ {1} (y) D ^ {k} K _ {2} (x - y) d y \\ \qquad + \int_ {\mathbf {R} ^ {d}} (1 - \varphi_ {r} (y) - \varphi_ {r} (x - y)) D ^ {k} K _ {1} (x - y) K _ {2} (y) d y \\ \qquad - \sum_ {\ell <   k} \frac {k !}{\ell ! (k - \ell) !} \int_ {\mathbf {R} ^ {d}} D ^ {\ell} \varphi_ {r} (x - y) D ^ {k - \ell} K _ {1} (x - y) K _ {2} (y) d y. \end{array}
$$

It remains to bound these terms separately. For the first term, since the integrand is supported in the set$\{ y : \| y \| _ { \mathfrak { s } } \le \| x \| _ { \mathfrak { s } } / 2 \}$(thanks to our choice of$r )$, we can bound $\left| D ^ { k } K _ { 1 } ( x - y ) \right|$| <sup>by</sup>$C \| x \| _ { \mathfrak { s } } ^ { \zeta _ { 1 } - | k | _ { s } }$and$K _ { 2 } ( y )$by$\| y \| _ { \mathfrak { s } } ^ { \zeta _ { 2 } }$. Since, for$\zeta > - | \mathfrak { s } |$, one has the easily verifiable bound

$$
\int_ {\| y \| _ {\mathfrak {s}} \leq r} \| y \| _ {\mathfrak {s}} ^ {\zeta} d y \lesssim r ^ {| \mathfrak {s} | + \zeta},\tag{10.15}
$$

it follows that the first term in (10.14) is bounded by a multiple of$\| \boldsymbol { x } \| _ { \mathfrak { s } } ^ { \bar { \zeta } - | k | _ { s } }$, as required. The same bound holds for the second term by symmetry.

For the third term, we use the fact that its integrand is supported in the set of points y such that one has both$\| y \| _ { s } \geq \| x \| _ { s } / 4$and$\| x - y \| _ { s } \geq \| x \| _ { s } / 4$. Since$\| x - y \| _ { s } \geq$ $\left\| y \right\| _ { s } - \left\| x \right\| _ { s }$<sub>s</sub> by the triangle inequality, one has

$$
\| x - y \| _ {\mathfrak {s}} \geq \varepsilon \| y \| _ {\mathfrak {s}} + \left(\frac {1 - \varepsilon}{4} - \varepsilon\right) \| x \| _ {\mathfrak {s}}
$$

for every$\varepsilon \in [ 0 .$, 1] so that, by choosing ε small enough, one has$\| x - y \| _ { s } \geq C \| y \| _ { s }$s for some constant C. We can therefore bound the third term by a multiple of

$$
\int_ {C \geq \| y \| _ {\mathfrak {s}} \geq \| x \| _ {\mathfrak {s}} / 4} \| y \| _ {\mathfrak {s}} ^ {\zeta_ {1} + \zeta_ {2} - | k | _ {\mathfrak {s}}} d y \sim \| x \| _ {\mathfrak {s}} ^ {\bar {\zeta} - | k | _ {\mathfrak {s}}},\tag{10.16}
$$

from which the requested bound follows again at once. (Here, the upper bound on the domain of integration comes from the assumption that the$K _ { i }$are compactly supported.)

The last term is bounded in a similar way by using the scaling properties of$\varphi _ { r }$and the fact that we have chosen$r = \| x \| _ { \mathfrak { s } } / 2$□

In what follows, we will also encounter distributions that behave just as if they were functions of order$\zeta ,$but with$\zeta < - | \mathfrak { s } |$. We have the following definition:

Definition 10.15${ \mathrm { L e t } } - | { \mathfrak { s } } | - 1 < \zeta \leq - | { \mathfrak { s } } |$and let$K \colon \mathbf { R } ^ { d } \backslash \{ 0 \}  \mathbf { R }$be a smooth function of order$\zeta ,$, which is supported in a bounded set. We then define the renormalised distribution RK corresponding to$K$by

$$
(\mathcal {R} K) (\psi) = \int_ {\mathbf {R} ^ {d}} K (x) \bigl (\psi (x) - \psi (0) \bigr) d x,
$$

for every smooth compactly supported test function$\psi .$

The following result shows that these distributions behave under convolution in pretty much the same way as their unrenormalised counterparts with$\zeta > - | \mathfrak { s } |$

Lemma 10.16 Let$K _ { 1 }$and$K _ { 2 }$be two compactly supported functions of respective orders$\zeta _ { 1 }$and$\zeta _ { 2 }$with$\iota - | \mathfrak { s } | - 1 < \zeta _ { 1 } \leq - | \mathfrak { s } | a n d - 2 | \mathfrak { s } | - \zeta _ { 1 } < \zeta _ { 2 } \leq 0 .$. Then, the function$( \mathcal { R } K _ { 1 } ) * K _ { 2 }$is oforder$\bar { \zeta } = 0 \wedge ( \zeta _ { 1 } + \zeta _ { 2 } + | \mathfrak { s } | )$and the bound

$$
\left\| \left(\mathscr {R} K _ {1}\right) * K _ {2} \right\| _ {\bar {\zeta}; m} \leq C \left\| K _ {1} \right\| _ {\zeta_ {1}; m} \left\| K _ {2} \right\| _ {\zeta_ {2}; \bar {m}},
$$

holds for every m$\geq 0 ,$, where we have set$\bar { m } = m + \operatorname* { m a x } \{ \mathfrak { s } _ { i } \}$

Proof. Similarly to before, we can write

$$
D ^ {k} \big ((\mathcal {R} K _ {1}) * K _ {2} \big) (x) = \int_ {\mathbf {R} ^ {d}} \varphi_ {r} (y) D ^ {k} K _ {1} (x - y) K _ {2} (y) d y + (\mathcal {R} K _ {1}) \big (\varphi_ {r} D ^ {k} K _ {2} (x - \cdot) \big)
$$

$$
\begin{array}{l} + \int_ {\mathbf {R} ^ {d}} (1 - \varphi_ {r} (y) - \varphi_ {r} (x - y)) D ^ {k} K _ {1} (x - y) K _ {2} (y) d y \\ - \sum_ {\ell <   k} \frac {k !}{\ell ! (k - \ell) !} \int_ {\mathbf {R} ^ {d}} D ^ {\ell} \varphi_ {r} (x - y) D ^ {k - \ell} K _ {1} (x - y) K _ {2} (y) d y. \end{array}
$$

Here, we used the fact that, when tested against test functions that vanish at the origin, $\mathcal { R } K _ { 1 }$is again nothing but integration against$K _ { 1 }$. All these terms are bounded exactly as before, thus yielding the desired bounds, except for the second term. For this term, we have the identity

$$
\begin{array}{l} (\mathcal {R} K _ {1}) \big (\varphi_ {r} D ^ {k} K _ {2} (x - \cdot) \big) = \int_ {\mathbf {R} ^ {d}} K _ {1} (y) \big (\varphi_ {r} (y) D ^ {k} K _ {2} (x - y) - D ^ {k} K _ {2} (x) \big) d y \\ = \int_ {\mathbf {R} ^ {d}} K _ {1} (y) \varphi_ {r} (y) \big (D ^ {k} K _ {2} (x - y) - D ^ {k} K _ {2} (x) \big) d y \\ + D ^ {k} K _ {2} (x) \int_ {\mathbf {R} ^ {d}} K _ {1} (y) \big (1 - \varphi_ {r} (y) \big) d y. \end{array} \tag {10}\tag{10.17}
$$

For the first term, we use the fact that the integrand is supported in the region$\{ y \ :$ $\| y \| _ { s } \leq \| x \| _ { s } / 2 \}$(this is the case again by making the choice$r = \| x \| _ { s } / 2$as in the proof of Lemma 10.14). As a consequence of the gradient theorem, we then obtain the bound

$$
\left| D ^ {k} K _ {2} (x - y) - D ^ {k} K _ {2} (x) \right| \lesssim \sum_ {i = 1} ^ {d} \left| y _ {i} \right| \| x \| _ {\mathfrak {s}} ^ {\zeta_ {2} - | k | _ {\mathfrak {s}} - \mathfrak {s} _ {i}} \| K _ {2} \| _ {\zeta_ {2}; \bar {k}},
$$

where we have set${ \bar { k } } = | k | _ { \mathfrak { s } } + \operatorname* { m a x } \{ \mathfrak { s } _ { i } \}$. Observing that$| y _ { i } | \lesssim \| y \| _ { s } ^ { \mathfrak { s } _ { i } }$, the required bound then follows from$_ { ( 1 0 . 1 5 ) }$. The second term in (10.17) can be bounded similarly as in (10.16) by making use of the bounds on$K _ { 1 }$and$K _ { 2 }$□

To conclude this section, we give another two useful results regarding the behaviour of such kernels. First, we show how a class of natural regularisations of a kernel of order$\zeta$converges to it. We fix a function$\varrho \colon \mathbf { R } ^ { d }  \mathbf { R }$which is smooth, compactly supported, and integrates to 1, and we write as usual$\varrho _ { \varepsilon } ( y ) = \varepsilon ^ { - | \mathfrak { s } | } \varrho ( S _ { \mathfrak { s } } ^ { \varepsilon } y )$. Given a function$K$on$\mathbf { R } ^ { d }$, we then set

$$
K _ {\varepsilon} \stackrel {\mathrm{def}} {=} K * \varrho_ {\varepsilon}.
$$

We then have the following result:

Lemma 10.17 In the above setting, ifK is oforder$\zeta \in ( - | \mathfrak { s } | , 0 )$, then$K _ { \varepsilon }$has bounded derivatives ofall orders. Furthermore, one has the bound

$$
\left| D ^ {k} K _ {\varepsilon} (x) \right| \leq C \big (\left\| x \right\| _ {\mathfrak {s}} + \varepsilon \big) ^ {\zeta - | k | _ {\mathfrak {s}}} \left\| K \right\| _ {\zeta ; | k | _ {\mathfrak {s}}}.\tag{10.18}
$$

Finally, for all$\bar { \zeta } \in [ \zeta - 1 , \zeta )$and m$\geq 0 ,$, one has the bound

$$
\| K - K _ {\varepsilon} \| _ {\bar {\zeta}; m} \lesssim \varepsilon^ {\zeta - \bar {\zeta}} \| K \| _ {\zeta ; \bar {m}},\tag{10.19}
$$

where$\bar { m } = m + \operatorname* { m a x } \{ \mathfrak { s } _ { i } \}$

Proof. Without loss of generality, we assume that$\varrho$is supported in the set$\{ x : \| x \| _ { \mathfrak { s } } \leq$ 1 . We first obtain the bounds on$K _ { \varepsilon }$itself. For$\| \boldsymbol { x } \| _ { \mathfrak { s } } \geq 2 \varepsilon$, we can write

$$
D ^ {k} K _ {\varepsilon} (x) = \int_ {\mathbf {R} ^ {d}} D ^ {k} K (x - y) \varrho_ {\varepsilon} (y) d y.
$$

Since$\varrho _ { \varepsilon }$is supported in a ball of radius$\varepsilon ,$, it follows from the bound$\| \boldsymbol { x } \| _ { \mathfrak { s } } \geq 2 \varepsilon$that whenever the integrand is non-zero, one has$\| x - y \| _ { 5 } \geq \| x \| _ { 5 } / 2$. We can therefore bound$D ^ { k } K ( x - y ) \mathfrak { b y } \| x \| _ { \mathfrak { s } } ^ { \zeta - | k | _ { \mathfrak { s } } } \| K \| _ { \zeta ; | k | _ { \mathfrak { s } } }$, and the requested bound follows from the fact that$\varrho _ { \varepsilon }$integrates to 1.

For$\| x \| _ { \mathfrak { s } } \leq 2 \varepsilon$on the other hand, we use the fact that

$$
D ^ {k} K _ {\varepsilon} (x) = \int_ {\mathbf {R} ^ {d}} K (y) D ^ {k} \varrho_ {\varepsilon} (x - y) d y.
$$

Since$\| x \| _ { \mathfrak { s } } \leq 2 \varepsilon$, the integrand is supported in a ball of radius 3ε. Furthermore,$| D ^ { k } \varrho _ { \varepsilon } |$ is bounded by a constant multiple of$\dot { \varepsilon } ^ { - | \mathfrak { s } | - | k | }$s there, so that we have the bound

$$
| D ^ {k} K _ {\varepsilon} (x) | \lesssim \varepsilon^ {- | \mathfrak {s} | - | k | _ {\mathfrak {s}}} \| K \| _ {\zeta ; 0} \int_ {\| y \| _ {\mathfrak {s}} \leq 3 \varepsilon} \| y \| _ {\mathfrak {s}} ^ {\zeta} d y,
$$

so that (10.18) follows.

Regarding the bound on$K - K _ { \varepsilon }$, we write

$$
D ^ {k} K _ {\varepsilon} (x) - D ^ {k} K (x) = \int_ {\mathbf {R} ^ {d}} \left(D ^ {k} K (x - y) - D ^ {k} K (x)\right) \varrho_ {\varepsilon} (y) d y.
$$

For$\lVert x \rVert _ { \mathfrak { s } } \geq 2 \varepsilon$, we obtain as previously the bound

$$
\left| D ^ {k} K (x - y) - D ^ {k} K (x) \right| \lesssim \| K \| _ {\zeta ; \bar {k}} \sum_ {i = 1} ^ {d} \left| y _ {i} \right| \| x \| _ {\mathfrak {s}} ^ {\zeta - | k | _ {\mathfrak {s}} - \mathfrak {s} _ {i}},
$$

where we set$\bar { k } = | k | _ { \mathfrak { s } } +$max$\{ \mathfrak { s } _ { i } \}$. Integrating this bound against$\varrho _ { \varepsilon }$, we thus obtain

$$
| D ^ {k} K (x) - D ^ {k} K _ {\varepsilon} (x) | \lesssim \| K \| _ {\zeta ; \bar {k}} \sum_ {i = 1} ^ {d} \varepsilon^ {\mathfrak {s} _ {i}} \| x \| _ {\mathfrak {s}} ^ {\zeta - | k | _ {\mathfrak {s}} - \mathfrak {s} _ {i}} \lesssim \varepsilon^ {\zeta - \bar {\zeta}} \| K \| _ {\zeta ; \bar {k}} \| x \| _ {\mathfrak {s}} ^ {\bar {\zeta} - | k | _ {\mathfrak {s}}},
$$

where we used the fact that$\mathfrak { s } _ { i } \geq 1$for every i. For$\| x \| _ { \mathfrak { s } } \leq 2 \varepsilon$on the other hand, we make use of the bound obtained in the first part, which implies in particular that

$$
| D ^ {k} K (x) - D ^ {k} K _ {\varepsilon} (x) | \lesssim \| K \| _ {\zeta ; | k | _ {\mathfrak {s}}} \| x \| _ {\mathfrak {s}} ^ {\zeta - | k | _ {\mathfrak {s}}} \lesssim \varepsilon^ {\zeta - \bar {\zeta}} \| K \| _ {\zeta ; | k | _ {\mathfrak {s}}} \| x \| _ {\mathfrak {s}} ^ {\bar {\zeta} - | k | _ {\mathfrak {s}}},
$$

which is precisely the requested bound.

Finally, it will be useful to have a bound on the difference between the values of a singular kernel, evaluated at two different locations. The relevant bound takes the following form:

Lemma 10.18 Let K be of order$\zeta \leq 0$. Then, for every$\alpha \in [ 0 , 1 ]$, one has the bound

$$
\left| K (z) - K (\bar {z}) \right| \lesssim \| z - \bar {z} \| _ {\mathfrak {s}} ^ {\alpha} \big (\| z \| _ {\mathfrak {s}} ^ {\zeta - \alpha} + \| \bar {z} \| _ {\mathfrak {s}} ^ {\zeta - \alpha} \big) \| K \| _ {\zeta ; m},
$$

where$m = \operatorname* { s u p } _ { i } { \mathfrak { s } } _ { i } .$

Proof. For$\alpha = 0$, the bound is obvious, so we only need to show it for$\alpha = 1$; the other values then follow by interpolation.

$\begin{array} { r } { \operatorname { I f } \| z - \bar { z } \| _ { s } \geq \| z \| _ { s } \wedge \| \bar { z } \| _ { s } } \end{array}$, we use the “brutal” bound

$$
| K (z) - K (\bar {z}) | \leq | K (z) | + | K (\bar {z}) | \leq \left(\| z \| _ {\mathfrak {s}} ^ {\zeta} + \| \bar {z} \| _ {\mathfrak {s}} ^ {\zeta}\right) \| K \| _ {\zeta ; m}
$$

$$
\begin{array}{l} \leq 2 (\| z \| _ {\mathfrak {s}} ^ {\zeta} \wedge \| \bar {z} \| _ {\mathfrak {s}} ^ {\zeta}) \| K \| _ {\zeta ; m} \leq 2 \| z - \bar {z} \| (\| z \| _ {\mathfrak {s}} ^ {\zeta - 1} \wedge \| \bar {z} \| _ {\mathfrak {s}} ^ {\zeta - 1}) \| K \| _ {\zeta ; m} \\ \leq 2 \| z - \bar {z} \| (\| z \| _ {\mathfrak {s}} ^ {\zeta - 1} + \| \bar {z} \| _ {\mathfrak {s}} ^ {\zeta - 1}) \| K \| _ {\zeta ; m}, \end{array}
$$

which is precisely what is required.

To treat the case$\| z - { \bar { z } } \| _ { \mathfrak { s } } \leq \| z \| _ { \mathfrak { s } } \wedge \| { \bar { z } } \| _ { \mathfrak { s } }$, we use the identity

$$
K (z) - K (\bar {z}) = \int_ {\gamma} \left\langle \nabla K (y), d y \right\rangle ,\tag{10.20}
$$

where$\gamma$is any path connecting z¯ to z. It is straightforward to verify that it is always possible to find$\gamma$with the following properties:

1. The path$\gamma$is made of finitely many line segments that are parallel to the canonical basis vectors$\{ e _ { i } \} _ { i = 1 } ^ { d }$

2. There exists$c > 0$such that one has$\| y \| _ { s } \geq c ( \| z \| _ { s } \land \| { \bar { z } } \| _ { s } )$for every$y \mathrm { \ o n \ } \gamma$

3. There exists$C > 0$such that the total (Euclidean) length of the line segments parallel to$e _ { i }$is bounded by$C \| z - \bar { z } \| _ { \mathfrak { s } } ^ { \mathfrak { s } _ { i } }$

Here, both constants c and$C$can be chosen uniform in z and z¯. It now follows from the definition of$\| K \| _ { \zeta ; m }$that one has

$$
\left| \partial_ {i} K (y) \right| \leq \| K \| _ {\zeta ; m} \| y \| _ {\mathfrak {s}} ^ {\zeta - \mathfrak {s} _ {i}}.
$$

It follows that the total contribution to (10.20) coming from the line segments parallel to$e _ { i }$is bounded by a multiple of

$$
\| K \| _ {\zeta ; m} \| z - \bar {z} \| _ {\mathfrak {s}} ^ {\mathfrak {s} _ {i}} (\| z \| _ {\mathfrak {s}} ^ {\zeta - \mathfrak {s} _ {i}} + \| \bar {z} \| _ {\mathfrak {s}} ^ {\zeta - \mathfrak {s} _ {i}}) \leq \| K \| _ {\zeta ; m} \| z - \bar {z} \| _ {\mathfrak {s}} (\| z \| _ {\mathfrak {s}} ^ {\zeta - 1} + \| \bar {z} \| _ {\mathfrak {s}} ^ {\zeta - 1}),
$$

where, in order to obtain the inequality, we have used the fact that$\mathfrak { s } _ { i } \geq 1$and that we are considering the regime$\| z - { \bar { z } } \| _ { \mathfrak { s } } \leq \| z \| _ { \mathfrak { s } } \wedge \| { \bar { z } } \| _ { \mathfrak { s } }$□

## 10.4 Wick renormalisation and the continuous parabolic Anderson model

There is one situation in which it is possible to show without much effort that bounds of the type (10.2) and (10.3) hold, which is when$\tau = \tau _ { 1 } \tau _ { 2 }$and one has identity

$$
(\hat {\Pi} _ {z} ^ {(\varepsilon)} \tau) (\bar {z}) \approx (\hat {\Pi} _ {z} ^ {(\varepsilon)} \tau_ {1}) (\bar {z}) \diamond (\hat {\Pi} _ {z} ^ {(\varepsilon)} \tau_ {2}) (\bar {z}),
$$

either as an exact identity or as an approximate identity with a “lower-order” error term, where denotes the Wick product between elements of some fixed Wiener chaos. Recall that if$f \in H ^ { \otimes k }$and$g \in H ^ { \otimes \ell }$, then the Wick product between the corresponding random variables is defined by

$$
I _ {k} (f) \diamond I _ {\ell} (g) = I _ {k + \ell} (f \otimes g).
$$

In other words, the Wick product only keeps the “dominant” term in the product formula (10.1) and discards all the other terms.

We have seen in Section 9.3 how to associate to$\mathbf { ( P A M g ) }$a renormalisation group $\Re _ { 0 }$and how to interpret the solutions to the fixed point map associated to a renormalised model. In this section, we perform the final step, namely we show that if$\xi _ { \varepsilon }$ is a smooth approximation to our spatial white noise$\xi$and$Z _ { \varepsilon }$denotes the corresponding canonical model, then one can indeed find a sequence of elements$M _ { \varepsilon } \in \Re _ { 0 }$such that one has$M _ { \varepsilon } Z _ { \varepsilon } \to { \hat { Z } }$. Recalling that elements in$\Re _ { 0 }$are characterised by a real number$C$and a$2 \times 2$matrix$\bar { C } ,$, we show furthermore that it is possible to choose the sequence$M _ { \varepsilon }$in such a way that the corresponding constant$C$is given by a logarithmically diverging constant$C _ { \varepsilon }$, while the corresponding$2 \times 2$matrix$\bar { C }$is given by $\begin{array} { r } { \bar { C } _ { i j } = - \frac { 1 } { 2 } C _ { \varepsilon } \delta _ { i j } } \end{array}$

We are in the setting of Theorem 10.7 and Proposition 10.11 with$H = L ^ { 2 } ( \mathbf { T } ^ { 2 } )$, and where the action of$\mathbf { R } ^ { 3 }$onto H is given by translation in the spatial directions. More precisely, for$z = ( t , x ) \in \mathbf { R } \times \mathbf { R } ^ { 2 }$and$\varphi \in H$, one has

$$
(S _ {z} \varphi) (y) = \varphi (y - x).
$$

It turns out that in this case, writing as before$z = ( t , x )$and$\bar { z } = ( \bar { t } , \bar { x } )$, the random variables$( \hat { \Pi } _ { z } ^ { ( \varepsilon ) } \tau ) ( \bar { z } )$are not only independent of$t ,$, but they are also independent of$\bar { t . }$ So we really view our model as a model on${ \bf R } ^ { 2 }$endowed with the Euclidean scaling, rather than on$\mathbf { R } ^ { 3 }$endowed with the parabolic scaling. The corresponding integral kernel K<sup>¯</sup> is obtained from K by simply integrating out the temporal variable.

Since the temporal integral of the heat kernel yields the Green’s function of the Laplacian, we can choose$\breve { K }$in such a way that

$$
\bar {K} (x) = - \frac {1}{2 \pi} \log \left\| x \right\|,\tag{10.21}
$$

for values of x in some sufficiently small neighbourhood of the origin. Outside of that neighbourhood, we choose$\bar { K }$as before in such a way that it is smooth, compactly supported, and such that$\begin{array} { r } { \int _ { \mathbb { R } ^ { 2 } } x ^ { k } \bar { K } ( x ) d x = 0 } \end{array}$, for every multiindex$k$with$| k | \leq r$for Rsome fixed and sufficiently large value of$r _ { * }$These properties can always be ensured by a suitable choice for the original space-time kernel$K$. In particular,$\bar { K }$is of order$\zeta$ for every$\zeta < 0$in the sense of Definition 10.12.

Recall now that we define$\xi _ { \varepsilon }$by$\xi _ { \varepsilon } ~ = ~ \varrho _ { \varepsilon } \ast \xi .$, where ̺ is a smooth compactly supported function integrating to 1 and$\varrho _ { \varepsilon }$denotes the rescaled function as usual. From now on, we consider everything in$\mathbf { T } ^ { 2 }$, so that$\varrho \colon  { \mathbf { R } } ^ { 2 } \to  { \mathbf { R } }$. With this definition, we then have the following result, which is the last missing step for the proof of Theorem 1.11.

Theorem 10.19 Denote$b y \mathcal { T }$the regularity structure associated to$( P A M g )$with$\alpha \in$ $( - \frac { 4 } { 3 } , - 1 )$and$\beta \ = \ 2$. Let furthermore$M _ { \varepsilon }$be a sequence of elements in$\Re _ { 0 }$and define the renormalised model$\hat { Z } _ { \varepsilon } ~ = ~ M _ { \varepsilon } Z _ { \varepsilon }$. Then, there exists a limiting model$\hat { Z }$ independent of the choice of mollifier ̺, as well as a choice of$M _ { \varepsilon } \in \mathfrak { R } _ { 0 }$such that $\hat { Z } _ { \varepsilon } \to \hat { Z }$in probability. More precisely, for any$\theta < - 1 - \alpha ,$, any compact set${ \mathcal { R } } ,$and $a n y \gamma < r ,$one has the bound

$$
\mathbf {E} \| M _ {\varepsilon} Z _ {\varepsilon}; \hat {Z} \| _ {\gamma ; \mathfrak {K}} \lesssim \varepsilon^ {\theta},
$$

uniformly over$\varepsilon \in ( 0 , 1 ]$

Furthermore, it is possible to renormalise the model in such a way that the family ofall solutions to$( P A M g )$with respect to the model$\hat { Z }$formally satisfies the chain rule.

Remark 10.20 Note that we do not need to require that the mollifier$\varrho$be symmetric, although a non-symmetric choice might require a renormalisation sequence$M _ { \varepsilon }$which does not satisfy the identity$\begin{array} { r } { \bar { C } _ { i j } = - \frac { 1 } { 2 } C \delta _ { i j } } \end{array}$

Proof. As already seen in Section 9.1, the only elements in the regularity structure associated to (PAMg) that have negative homogeneity are

$$
\left\{\Xi , X _ {i} \Xi , \mathcal {I} (\Xi) \Xi , \mathcal {I} _ {i} (\Xi) \mathcal {I} _ {j} (\Xi) \right\}.
$$

By Theorem 10.7, we thus only need to identify the random variables$( \Pi _ { x } \tau ) ( \psi )$and to obtain the bounds (10.2) and (10.3) for elements$\tau$in the above set. For$\tau = \Xi$, it follows as in the proof of Proposition 9.5 that

$$
\mathbf {E} | (\hat {\Pi} _ {x} ^ {(\varepsilon)} \Xi) (\varphi_ {x} ^ {\lambda}) | ^ {2} \lesssim \lambda^ {- 2}, \qquad \mathbf {E} | (\hat {\Pi} _ {x} ^ {(\varepsilon)} \Xi - \hat {\Pi} _ {x} \Xi) (\varphi_ {x} ^ {\lambda}) | ^ {2} \lesssim \varepsilon^ {2 \theta} \lambda^ {- 2 - 2 \theta},
$$

provided that$\theta < \frac { 1 } { 2 }$, which is precisely the required bound. For$\tau = X _ { i } \Xi$, the required bound follows immediately from the corresponding bound for$\tau = \Xi$, so it only remains to consider$\tau = \mathcal { I } ( \Xi ) \Xi$and$\tau = \mathcal { T } _ { i } ( \Xi ) \mathcal { T } _ { i } ( \Xi )$

We start with$\tau = \mathcal { I } ( \Xi ) \Xi$, in which case we aim to show that

$$
\mathbf {E} | (\hat {\Pi} _ {x} ^ {(\varepsilon)} \tau) (\varphi_ {x} ^ {\lambda}) | ^ {2} \lesssim \lambda^ {- \kappa}, \qquad \mathbf {E} | (\hat {\Pi} _ {x} ^ {(\varepsilon)} \tau - \hat {\Pi} _ {x} \tau) (\varphi_ {x} ^ {\lambda}) | ^ {2} \lesssim \varepsilon^ {2 \theta} \lambda^ {- \kappa - 2 \theta}.\tag{10.22}
$$

For this value of$\tau ,$one has the identity

$$
(\hat {\Pi} _ {x} ^ {(\varepsilon)} \tau) (y) = \xi_ {\varepsilon} (y) \int (\bar {K} (y - z) - \bar {K} (x - z)) \xi_ {\varepsilon} (z) d z - C ^ {(\varepsilon)},
$$

where$C ^ { ( \varepsilon ) }$is the constant appearing in the characterisation of$M _ { \varepsilon } \in \mathfrak { R } _ { 0 }$. Note now that

$$
\mathbf {E} \xi_ {\varepsilon} (y) \xi_ {\varepsilon} (z) = \int_ {\mathbf {R} ^ {2}} \varrho_ {\varepsilon} (y - x) \varrho_ {\varepsilon} (z - x) d x \stackrel {{\mathrm{def}}} {{=}} \varrho_ {\varepsilon} ^ {\star 2} (y - z),
$$

and define the kernel$\bar { K } _ { \varepsilon }$by

$$
\bar {K} _ {\varepsilon} (y) = \int \varrho_ {\varepsilon} (y - z) \bar {K} (z) d z.
$$

With this notation, provided that we make the choice$C ^ { ( \varepsilon ) } = \langle \varrho _ { \varepsilon } , \bar { K } _ { \varepsilon } \rangle$, we have the identity

$$
(\hat {\Pi} _ {x} ^ {(\varepsilon)} \tau) (y) = \int (\bar {K} (y - z) - \bar {K} (x - z)) (\xi_ {\varepsilon} (z) \diamond \xi_ {\varepsilon} (y)) d z - \int \varrho_ {\varepsilon} ^ {\star 2} (y - z) \bar {K} (x - z) d z.
$$

In the notation of Proposition 10.11, we thus have

$$
\begin{array}{r} (\hat {\mathcal {W}} ^ {(\varepsilon ; 0)} \tau) (y) = (\varrho_ {\varepsilon} * \bar {K} _ {\varepsilon}) (y), \\ (\hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (y; z _ {1}, z _ {2}) = \varrho_ {\varepsilon} (z _ {2} - y) (\bar {K} _ {\varepsilon} (y - z _ {1}) - \bar {K} _ {\varepsilon} (- z _ {1})). \end{array}
$$

This suggests that one should define the$L ^ { 2 }$-valued distributions

$$
\begin{array}{c} (\hat {\mathcal {W}} ^ {(0)} \tau) (y) = \bar {K} (y), \\ (\hat {\mathcal {W}} ^ {(2)} \tau) (y; z _ {1}, z _ {2}) = \delta (z _ {2} - y) \big (\bar {K} (y - z _ {1}) - \bar {K} (- z _ {1}) \big), \end{array}\tag{10.23}
$$

and use them to define the limiting random variables$( \hat { \Pi } _ { x } ^ { ( k ) } \tau ) ( \psi )$via (10.9).

A simple calculation then shows that, for any two points y and$\bar { y }$in${ \bf R } ^ { 2 }$, one has

$$
\langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (y), (\hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (\bar {y}) \rangle
$$

$$
\begin{array}{l} = \varrho_ {\varepsilon} ^ {\star 2} (y - \bar {y}) \int (\bar {K} _ {\varepsilon} (y - z) - \bar {K} _ {\varepsilon} (- z)) (\bar {K} _ {\varepsilon} (\bar {y} - z) - \bar {K} _ {\varepsilon} (- z)) d z \\ \stackrel {{\mathrm{def}}} {{=}} \varrho_ {\varepsilon} ^ {\star 2} (y - \bar {y}) W _ {\varepsilon} (y, \bar {y}). \end{array} \tag {10.24}
$$

Writing$\begin{array} { r } { Q _ { \varepsilon } ( y ) \stackrel { \mathrm { d e f } } { = } \int \bar { K } ( y - z ) K _ { \varepsilon } ( - z ) } \end{array}$dz and using furthermore the shorthand notation

$$
\hat {Q} _ {\varepsilon} (y) \stackrel {\mathrm{def}} {=} Q _ {\varepsilon} (y) - Q _ {\varepsilon} (0) - \left<   y, \nabla Q _ {\varepsilon} (0) \right > ,\tag{10.25}
$$

we obtain

$$
W _ {\varepsilon} (y, \bar {y}) = \hat {Q} _ {\varepsilon} (y - \bar {y}) - \hat {Q} _ {\varepsilon} (y) - \hat {Q} _ {\varepsilon} (- \bar {y}).
$$

As a consequence of Lemmas 10.14 and 10.17, we obtain for any$\delta > 0$the bound $\begin{array} { r } { \vert \hat { Q } _ { \varepsilon } ( z ) \vert \lesssim \vert \vert \dot { z } \vert \vert ^ { 2 - \delta } } \end{array}$uniformly over$\varepsilon \in ( 0 , 1 ]$. This then immediately implies that

$$
| W _ {\varepsilon} (y, \bar {y}) | \lesssim \| y \| ^ {2 - \delta} + \| \bar {y} \| ^ {2 - \delta},
$$

uniformly over$\varepsilon \in ( 0 , 1 ]$

It follows immediately from these bounds that

$$
\left| \int \langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (y), (\hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (\bar {y}) \rangle \psi^ {\lambda} (y) \psi^ {\lambda} (\bar {y}) d y d \bar {y} \right| \lesssim \lambda^ {- \delta},
$$

uniformly over$\varepsilon \in ( 0 , 1 ]$. In the same way, it is straightforward to obtain an analogous bound on$\hat { \mathcal { W } } ^ { ( 2 ) } \tau$, so it remains to find similar bounds on the quantity

$$
(\delta \hat {\Pi} _ {x} ^ {(\varepsilon ; 2)} \tau) (\psi^ {\lambda}) \stackrel {\mathrm{def}} {=} (\hat {\Pi} _ {x} ^ {(\varepsilon ; 2)} \tau) (\psi^ {\lambda}) - (\hat {\Pi} _ {x} ^ {(2)} \tau) (\psi^ {\lambda}).
$$

Writing$\delta \hat { \mathcal { W } } ^ { ( \varepsilon ; 2 ) } \tau = \hat { \mathcal { W } } ^ { ( \varepsilon ; 2 ) } \tau - \hat { \mathcal { W } } ^ { ( 2 ) } \tau$, we can decompose this as

$$
\begin{array}{r l} & {(\delta \hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (y; z _ {1}, z _ {2}) = (\delta (z _ {2} - y) - \varrho_ {\varepsilon} (z _ {2} - y)) (\bar {K} (y - z _ {1}) - \bar {K} (- z _ {1}))} \\ & {\qquad + \varrho_ {\varepsilon} (z _ {2} - y) (\delta \bar {K} _ {\varepsilon} (y - z _ {1}) - \delta \bar {K} _ {\varepsilon} (- z _ {1}))} \\ & {\stackrel {\mathrm{def}} {=} (\delta \hat {\mathcal {W}} _ {1} ^ {(\varepsilon ; 2)} \tau) (y; z _ {1}, z _ {2}) + (\delta \hat {\mathcal {W}} _ {2} ^ {(\varepsilon ; 2)} \tau) (y; z _ {1}, z _ {2}).} \end{array}
$$

where we have set$\delta \bar { K } _ { \varepsilon } = \bar { K } - \bar { K } _ { \varepsilon }$. Accordingly, at the level of the corresponding random variables, we can write

$$
\delta \hat {\Pi} _ {x} ^ {(\varepsilon ; 2)} \tau = \delta \hat {\Pi} _ {x; 1} ^ {(\varepsilon ; 2)} \tau + \delta \hat {\Pi} _ {x; 2} ^ {(\varepsilon ; 2)} \tau ,
$$

and it suffices to bound each of these separately. Regarding$\delta \hat { \Pi } _ { x ; 2 } ^ { ( \varepsilon ; 2 ) } \tau$, it is straightforward to bound it exactly as above, but making use of Lemma 10.17 in order to bound $\delta \bar { K } _ { \varepsilon }$. The result of this calculation is that the second bound in (10.22) does indeed hold for δΠ<sup>ˆ</sup>$\dot { \mathrm { I } } _ { x ; 2 } ^ { ( \varepsilon ; 2 ) }$, for every$\begin{array} { r } { \theta < \frac { 1 } { 2 } } \end{array}$and$\kappa > 0$, uniformly over ε,$\lambda \in ( 0 , 1 ]$

Let us then turn to$\delta \hat { \Pi } _ { x ; 1 } ^ { ( \varepsilon ; 2 ) } \tau$. It follows from the definitions that one has the identity

$$
\begin{array}{r l} & {\langle (\delta \hat {\mathcal {W}} _ {0; 1} ^ {(\varepsilon ; 2)} \tau) (y), (\delta \hat {\mathcal {W}} _ {0; 1} ^ {(\varepsilon ; 2)} \tau) (\bar {y}) \rangle} \\ & {\qquad = (\delta (y - \bar {y}) - \varrho_ {\varepsilon} (\bar {y} - y) - \varrho_ {\varepsilon} (y - \bar {y}) + \varrho_ {\varepsilon} ^ {\star 2} (y - \bar {y})) W (y, \bar {y}).} \end{array}
$$

At this stage, we note that we can decompose this as a sum of$9$terms of the form

$$
\big (\delta (y - \bar {y}) - \tilde {\varrho} _ {\varepsilon} (y - \bar {y}) \big) \hat {Q} (x),\tag{10.26}
$$

where$\tilde { \varrho } _ { \varepsilon }$is one of$\varrho _ { \varepsilon } ^ { \star 2 } , \varrho _ { \varepsilon } , \mathrm { o r } \varrho _ { \varepsilon } ( - \cdot )$, x is one of$y , \bar { y }$and$y - { \bar { y } } .$, and$\hat { Q }$is defined analogously to (10.25). Let us consider the case$x = y$. One then has the identity

$$
\begin{array}{l} \int (\tilde {\varrho} _ {\varepsilon} (y - \bar {y}) - \delta (y - \bar {y})) \hat {Q} (y) \psi^ {\lambda} (y) \psi^ {\lambda} (\bar {y}) d y d \bar {y} \\ = \int \tilde {\varrho} _ {\varepsilon} (h) \hat {Q} (y) \psi^ {\lambda} (y) (\psi^ {\lambda} (y - h) - \psi^ {\lambda} (y)) d y d h. \end{array} \tag {10}\tag{10.27}
$$

Since the integrand vanishes as soon as$\| h \| \gtrsim \varepsilon$, we have the bound$| \psi ^ { \lambda } ( y - h ) -$ $\psi ^ { \lambda } ( y ) | \lesssim \lambda ^ { - 3 } \varepsilon$. Combining this with the bound on$\hat { Q }$obtained previously, this immediately yields for any such term the bound$\varepsilon \lambda ^ { - 1 - \delta }$, provided that$\varepsilon \leq \lambda$. However, a bound proportional to$\lambda ^ { - \delta }$can be obtained by simply bounding each term in (10.27) separately, so that for every$\theta \ < \ \frac { 1 } { 2 }$, one has again a bound of the type$\varepsilon ^ { 2 \theta } \lambda ^ { - 2 \theta - \kappa }$ uniformly over all$\varepsilon , \lambda \in ( 0 , 1 ]$

The case$x \ = \ \bar { y }$is analogous by symmetry, so it remains to consider the case $x = y - \bar { y }$. In this case however, (10.27) reduces to

$$
\int \varrho_ {\varepsilon} (y - \bar {y}) \hat {Q} (y - \bar {y}) \psi^ {\lambda} (y) \psi^ {\lambda} (\bar {y}) d y d \bar {y},
$$

which is even bounded by$\varepsilon ^ { 2 - \delta } \lambda ^ { - 2 }$, so that the requested bound follows again. This concludes our treatment of the component in the second Wiener chaos for$\tau = \mathcal { I } ( \Xi ) \Xi$

Regarding the term$\hat { \mathcal { W } } ^ { ( \varepsilon ; 0 ) } \tau$in the 0th Wiener chaos, it follows immediately from Lemma 10.17 that, for any$\delta > 0$, one has the uniform bound

$$
\left| \int \langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 0)} \tau) (y), (\hat {\mathcal {W}} ^ {(\varepsilon ; 0)} \tau) (\bar {y}) \rangle \psi^ {\lambda} (y) \psi^ {\lambda} (\bar {y}) d y d \bar {y} \right| \lesssim \lambda^ {- \delta},
$$

as required. For the difference$\delta \hat { \mathcal { W } } ^ { ( \varepsilon ; 0 ) } \tau$, we obtain immediately from Lemma 10.17 that, for any$\kappa < 1$and$\delta > 0$, one has indeed the bound

$$
\left| \int \langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 0)} \tau) (y), (\hat {\mathcal {W}} ^ {(\varepsilon ; 0)} \tau) (\bar {y}) \rangle \psi^ {\lambda} (y) \psi^ {\lambda} (\bar {y}) d y d \bar {y} \right| \lesssim \varepsilon^ {\kappa - \delta} \lambda^ {- \kappa},
$$

uniformly over$\varepsilon , \lambda \in ( 0 , 1 ]$. This time, the corresponding bound on the difference between$\hat { \mathcal { W } } ^ { ( \varepsilon ; 0 ) } \tau$and$\hat { \mathscr { W } } ^ { ( 0 ) } \tau$is an immediate consequence of Lemma 10.17.

We now turn to the case$\tau = \mathcal { I } _ { i } ( \Xi ) \mathcal { I } _ { j } ( \Xi )$. This is actually the easier case, noting that one has the identity

$$
(\hat {\Pi} _ {x} ^ {(\varepsilon)} \tau) (y) = \int \partial_ {i} \bar {K} (y - z) \xi_ {\varepsilon} (z) d z \int \partial_ {j} \bar {K} (y - z) \xi_ {\varepsilon} (z) d z - \bar {C} _ {i j} ^ {(\varepsilon)},
$$

independently of$x .$If we now choose$\bar { C } _ { i j } ^ { ( \varepsilon ) } = \langle \partial _ { i } \bar { K } _ { \varepsilon } , \partial _ { j } \bar { K } _ { \varepsilon } \rangle$, one has similarly to before the identity

$$
(\hat {\Pi} _ {x} ^ {(\varepsilon)} \tau) (y) = \int \partial_ {i} \bar {K} (y - z _ {1}) \partial_ {j} \bar {K} (y - z _ {2}) \big (\xi_ {\varepsilon} (z _ {1}) \diamond \xi_ {\varepsilon} (z _ {2}) \big) d z _ {1} d z _ {2},
$$

so that in this case$( \hat { \Pi } _ { x } ^ { ( \varepsilon ) } \tau ) ( y )$belongs to the homogeneous chaos of order 2 with

$$
(\hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (y; z _ {1}, z _ {2}) = \partial_ {i} \bar {K} _ {\varepsilon} (y - z _ {1}) \partial_ {i} \bar {K} _ {\varepsilon} (y - z _ {2}).
$$

It then follows at once from Lemma 10.17 that the required bounds (10.2) and (10.3) do hold in this case as well.

Let us recapitulate what we have shown so far. If we choose the renormalisation map$M _ { \varepsilon }$associated to$C ^ { ( \varepsilon ) } = \langle \varrho _ { \varepsilon } , \bar { K } _ { \varepsilon } \rangle$and$\bar { C } _ { i j } ^ { ( \varepsilon ) } = \langle \partial _ { i } \bar { K } _ { \varepsilon } , \partial _ { j } \bar { K } _ { \varepsilon } \rangle$, which certainly does depend on the choice of mollifier$\varrho ,$then the renormalised model$\hat { Z } _ { \varepsilon }$converges in probability to a limiting model$\hat { Z }$that is independent of$\varrho .$. However, this is not the only possible choice for$M _ { \varepsilon } \mathrm { : }$we could just as well have added to$C ^ { ( \varepsilon ) }$and$\bar { C } _ { i j } ^ { ( \varepsilon ) }$some constants independent of$\varepsilon$and$\varrho$(or converging to such a limit as$\varepsilon  0 )$and we would have obtained a different limiting model$\breve { \hat { Z } } ,$, so that we do in principle obtain a 4-parameter family of possible limiting models.

We now lift some of this indeterminacy by imposing that the limiting model yields a family of solutions to (PAMg) which obeys the usual chain rule. As we have seen in $( 1 . 5 )$, this is the case if we obtain$\hat { Z }$as a limit of renormalised models where$\bar { C } _ { i j } =$ $- \textstyle { \frac { 1 } { 2 } } C \delta _ { i j }$, thus yielding a one-parameter family of models. Since we already know that with the choices mentioned above the limiting model is independent of$\varrho ,$it suffices to find some$\varrho$such that the constants$E _ { i j }$defined by

$$
E _ {i j} = - \lim _ {\varepsilon \rightarrow 0} \left(\bar {C} _ {i j} ^ {(\varepsilon)} + \frac {1}{2} C ^ {(\varepsilon)} \delta_ {i j}\right),\tag{10.28}
$$

are finite. If we then define the model$\tilde { Z }$by$\boldsymbol { \tilde { Z } } = \boldsymbol { M _ { E } } \boldsymbol { \hat { Z } } ,$, where$M _ { E }$denotes the action of the element of$\Re _ { 0 }$determined by$C = 0$and$\bar { C } _ { i j } = E _ { i j }$, then the model$\tilde { Z }$leads to a solution theory for (PAMg) that does obey the chain rule.

It turns out that in order to show that the limits (10.28) exist and are finite, it is convenient to choose a mollifier$\varrho$which has sufficiently many symmetries so that

$$
\varrho (x _ {1}, x _ {2}) = \varrho (x _ {2}, x _ {1}) = \varrho (x _ {1}, - x _ {2}) = \varrho (- x _ {1}, x _ {2}),\tag{10.29}
$$

for all$\boldsymbol { x } \in \mathbf { R } ^ { 2 }$. (For example, choosing a$\varrho$that is radially symmetric will do.) Indeed, by the symmetry of the singularity of$\bar { K }$given by (10.21), it follows in this case that

$$
\partial_ {1} \bar {K} _ {\varepsilon} (x _ {1}, x _ {2}) = - \partial_ {1} \bar {K} _ {\varepsilon} (- x _ {1}, x _ {2}) = \partial_ {1} \bar {K} _ {\varepsilon} (x _ {1}, - x _ {2}),
$$

for$x$in some sufficiently small neighbourhood of the origin, and similarly for$\partial _ { 2 } \bar { K } _ { \varepsilon }$ As a consequence, the function$\partial _ { 1 } \bar { K } _ { \varepsilon } \partial _ { 2 } \bar { K }$integrates to 0 in any sufficiently small symmetric neighbourhood of the origin. It follows at once that in this case, one has

$$
\lim _ {\varepsilon \to 0} C _ {1 2} ^ {(\varepsilon)} = \int_ {\| x \| \geq \delta} \partial_ {1} \bar {K} (x)   \partial_ {2} \bar {K} (x)   d x  ,\tag{10.30}
$$

which is indeed finite (and independent of$\delta > 0$, provided that it is sufficiently small) since the integrand is a smooth function.

It remains to treat the on-diagonal elements. For this, note that one has

$$
\int \left(\left(\partial_ {1} \bar {K} _ {\varepsilon} (x)\right) ^ {2} + \left(\partial_ {2} \bar {K} _ {\varepsilon} (x)\right) ^ {2}\right) d x = - \int \bar {K} _ {\varepsilon} (x) \Delta \bar {K} _ {\varepsilon} (x) d x.
$$

It follows from (10.21) that, as a distribution, one has the identity$\Delta \bar { K } = \delta _ { 0 } + \bar { R }$, where $\bar { R }$is a smooth function. As a consequence, we obtain the identity

$$
\langle \partial_ {1} \bar {K} _ {\varepsilon}, \partial_ {1} \bar {K} _ {\varepsilon} \rangle + \langle \partial_ {2} \bar {K} _ {\varepsilon}, \partial_ {2} \bar {K} _ {\varepsilon} \rangle = - \langle \bar {K} _ {\varepsilon}, \varrho_ {\varepsilon} \rangle + \int \bar {K} _ {\varepsilon} (x) (\varrho_ {\varepsilon} * \bar {R}) (x) d x,
$$

so that

$$
\lim _ {\varepsilon \to 0} (\langle \partial_ {1} \bar {K} _ {\varepsilon}, \partial_ {1} \bar {K} _ {\varepsilon} \rangle + \langle \partial_ {2} \bar {K} _ {\varepsilon}, \partial_ {2} \bar {K} _ {\varepsilon} \rangle + \langle \bar {K} _ {\varepsilon}, \varrho_ {\varepsilon} \rangle) = \langle \bar {K}, \bar {R} \rangle .\tag{10.31}
$$

On the other hand, writing$( x _ { 1 } , x _ { 2 } ) ^ { \perp } = ( x _ { 2 } , x _ { 1 } )$, it follows from (10.21) and the symmetries of$\varrho$that$\bar { K } _ { \varepsilon } ( x ^ { \perp } ) = \bar { K } _ { \varepsilon } ( x )$for all values of x in a sufficiently small neighbourhood of the origin, so that$( \partial _ { 1 } \bar { K } _ { \varepsilon } ) ^ { 2 } - ( \partial _ { 2 } \bar { K } _ { \varepsilon } ) ^ { 2 }$integrates to 0 there. It follows that

$$
\lim _ {\varepsilon \rightarrow 0} \left(\left\langle \partial_ {1} \bar {K} _ {\varepsilon}, \partial_ {1} \bar {K} _ {\varepsilon} \right\rangle - \left\langle \partial_ {2} \bar {K} _ {\varepsilon}, \partial_ {2} \bar {K} _ {\varepsilon} \right\rangle\right) = \int_ {\| x \| \geq \delta} \left(\left(\partial_ {1} \bar {K} (x)\right) ^ {2} - \left(\partial_ {2} \bar {K} (x)\right) ^ {2}\right) d x.
$$

Combining this with (10.31) and (10.30), it immediately follows that the right hand side of (10.28) does indeed converge to a finite limit. Furthermore, since the singularity is avoided in all of the above expressions, the convergence rate is of order$\varepsilon .$□

Remark 10.21 The value$C ^ { ( \varepsilon ) }$can be computed very easily. Indeed, for ε small enough, one has the identity

$$
\begin{array}{r l} & C ^ {(\varepsilon)} = \int \varrho_ {\varepsilon} ^ {\star 2} (z) \bar {K} (z) d z = - \frac {1}{2 \pi} \int \varrho_ {\varepsilon} ^ {\star 2} (z) \log \| z \| d z \\ & \qquad = - \frac {1}{\pi} \log \varepsilon - \frac {1}{2 \pi} \int \varrho^ {\star 2} (z) \log \| z \| d z, \end{array}\tag{10.32}
$$

which shows that only the finite part of$C ^ { ( \varepsilon ) }$actually depends on the choice of$\varrho .$Since this expression does not depend explicitly on K either, it also shows that in this case there is a unique canonical choice of renormalised model$\hat { Z } .$This is unlike in case of the dynamical$\Phi _ { 3 } ^ { 4 }$model where no such canonical choice exists.

## 10.5 The dynamical Φ<sup>4</sup><sub>3</sub> model

We now finally turn to the analysis of the renormalisation procedure for$( \Phi ^ { 4 } )$in dimension 3. The setting is very similar to the previous section, but this time we work in full space-time, so that the ambient space is${ \mathbf { R } } ^ { 4 }$, endowed with the parabolic scaling ${ \mathfrak { s } } = ( 2 , 1 , 1 , 1 )$. Our starting point is the canonical model built from$\xi _ { \varepsilon } = \varrho _ { \varepsilon } * \xi _ { \varepsilon }$, where $\xi$denotes space-time white noise on$\mathbf { R } \times \mathbf { T } ^ { 3 }$and$\varrho _ { \varepsilon }$is a parabolically rescaled mollifier similarly to before.

We are then again in the setting of Theorem 10.7 and Proposition 10.11 but with $H = L ^ { 2 } ( \mathbf { R } \times \mathbf { T } ^ { 3 } )$. This time, the kernel$K$used for building the canonical model is obtained by excising the singularity from the heat kernel, so we can choose it in such a way that

$$
K (t, x) = \frac {\mathbf {1} _ {t > 0}}{(4 \pi t) ^ {\frac {3}{2}}} \exp \left(- \frac {\| x \| ^ {2}}{4 t}\right),
$$

for$( t , x )$sufficiently close to the origin. Again, we extend this to all of${ \bf R } ^ { 4 }$in a way which is compactly supported and smooth away from the origin, and such that it annihilates all polynomials up to some degree$r > 2$. The following convergence result is the last missing ingredient for the proof of Theorem 1.15.

Theorem 10.22 Let$\mathcal { T } _ { F }$be the regularity structure associated to the dynamical$\Phi _ { 3 } ^ { 4 }$ modelfor$\beta = 2$and some$\alpha \in ( - \frac { 1 8 } { 7 } , - \frac { 5 } { 2 } )$, let$\xi _ { \varepsilon }$as above, and let$Z _ { \varepsilon }$be the associated canonical model, where the kernel K is as above. Then, there exists a random model$\hat { Z }$ independent of the choice of mollifier ̺ and elements$M _ { \varepsilon } \in \Re _ { 0 }$such that$M _ { \varepsilon } Z _ { \varepsilon } \to \hat { Z }$ in probability.

More precisely, for any$\textstyle \theta < - { \frac { 5 } { 2 } } - \alpha ,$, any compact set${ \mathcal { R } } ,$and any$\gamma < r ,$, one has the bound

$$
\mathbf {E} \| M _ {\varepsilon} Z _ {\varepsilon}; \hat {Z} \| _ {\gamma ; \mathfrak {K}} \lesssim \varepsilon^ {\theta},
$$

uniformly over$\varepsilon \in ( 0 , 1 ]$

Proof. Again, we are in the setting of Theorem 10.7, so we only need to show that the suitably renormalised model converges for those elements$\tau \in \mathcal { F } _ { F }$with non-positive homogeneity. It can be verified that in the case of the dynamical$\Phi _ { 3 } ^ { 4 }$model, these elements are given by

$$
\mathcal {F} _ {-} = \left\{\Xi , \Psi , \Psi^ {2}, \Psi^ {3}, \Psi^ {2} X _ {i}, \mathcal {I} (\Psi^ {3}) \Psi , \mathcal {I} (\Psi^ {2}) \Psi^ {2}, \mathcal {I} (\Psi^ {3}) \Psi^ {2} \right\}.
$$

Regarding$\tau = \Xi .$, the claim follows exactly as in the proof of Theorem 10.19. Regarding$\tau = \Psi = \mathcal { I } ( \Xi )$, the relevant bound follows at once from Proposition 10.11 and Lemma 10.17, noting that$( \hat { \Pi } _ { z } ^ { ( \varepsilon ) } \Psi ) ( \bar { z } ) = ( \Pi _ { z } ^ { ( \varepsilon ) } \Psi ) ( \bar { z } )$belongs to the first Wiener chaos with

$$
(\hat {\mathcal {W}} ^ {(\varepsilon ; 1)} \Psi) (z, \bar {z}) = K _ {\varepsilon} (\bar {z} - z),
$$

where we have set similarly to before$K _ { \varepsilon } = \varrho _ { \varepsilon } * K$. This is because$| \Psi | _ { \mathfrak { s } } < 0$, so that the second term appearing in (5.12) vanishes in this case. In particular,$( \hat { \Pi } _ { z } ^ { ( \varepsilon ) } \Psi ) ( \bar { z } )$is independent of z, so we also denote this random variable by$( \hat { \Pi } ^ { ( \varepsilon ) } \Psi ) ( \bar { z } )$. Here, we used the fact that both$K$and$K _ { \varepsilon }$are of order$- 3$

The cases$\tau = \Psi ^ { 2 }$and$\tau = \Psi ^ { 3 }$then follow very easily. Indeed, denote by$C _ { 1 } ^ { ( \varepsilon ) }$and $C _ { 2 } ^ { ( \varepsilon ) }$the two constants characterising the element$M _ { \varepsilon } \in \mathfrak { R } _ { 0 }$used to renormalise our model. Then, provided that we make the choice

$$
C _ {1} ^ {(\varepsilon)} = \int_ {\mathbf {R} ^ {4}} (K _ {\varepsilon} (z)) ^ {2} d z,\tag{10.33}
$$

we do have the identities

$$
(\hat {\Pi} ^ {(\varepsilon)} \Psi^ {2}) (z) = (\hat {\Pi} ^ {(\varepsilon)} \Psi) (z) \diamond (\hat {\Pi} ^ {(\varepsilon)} \Psi) (z), \qquad (\hat {\Pi} ^ {(\varepsilon)} \Psi^ {3}) (z) = (\hat {\Pi} ^ {(\varepsilon)} \Psi) (z) ^ {\diamond 3}.
$$

As a consequence,$( \hat { \Pi } ^ { ( \varepsilon ) } \Psi ^ { k } ) ( z )$belongs to the kth homogeneous Wiener chaos and one has

$$
(\hat {\mathcal {W}} ^ {(\varepsilon ; k)} \Psi^ {k}) (z; \bar {z} _ {1}, \ldots , \bar {z} _ {k}) = K _ {\varepsilon} (\bar {z} _ {1} - z) \dots K _ {\varepsilon} (\bar {z} _ {k} - z),\tag{10.34}
$$

for$k \in \{ 2 , 3 \}$so that the relevant bounds follow again from Proposition 10.11 and Lemma 10.17. Regarding$\tau = \Psi ^ { 2 } X _ { i }$, the corresponding bound follows again at once from those for$\tau = \Psi ^ { 2 }$

In order to treat the remaining terms, it will be convenient to introduce the following graphical notation, which associates a function to a graph with two types of edges. The first type of edge, drawn as , represents a factor$K$, while the second type of edge, drawn as$\cdots - \cdot$, represents a factor$K _ { \varepsilon }$. Each vertex of the graph denotes a variable in ${ \mathbf { R } } ^ { 4 }$, and the kernel is always evaluated at the difference between the variable that the arrow points from and the one that it points to. For example,$z _ { 1 } \xrightarrow { } - \mathbf { \hat { \Pi } } \mathbf { \hat { \Pi } } \xrightarrow { } z _ { 2 }$is a shorthand for$K ( z _ { 1 } - z _ { 2 } )$. Finally, we use the convention that if a vertex is drawn in grey, then the corresponding variable is integrated out. As an example, the identity (10.34) with $k = 3$and the identity (10.33) translate into

$$
(\hat {\mathcal {W}} ^ {(\varepsilon ; 3)} \Psi^ {3}) (z) = \bigoplus_ {z} ^ {\bullet}, \quad C _ {1} ^ {(\varepsilon)} = \bigcirc .\tag{10.35}
$$

Here, we made a slight abuse of notation, since the second picture actually defines a function of one variable, but this function is constant by translation invariance. With this graphical notation, Lemma 10.3 has a very natural graphical interpretation as follows. The function$f$is given by a graph with ℓ unlabelled black vertices and similarly for$g$with$m$of them. Then, the contribution of$I _ { \ell } ( f ) I _ { m } ( g )$in the$( \ell + m - 2 r ) \mathrm { t h }$ Wiener chaos is obtained by summing over all possible ways of contracting r vertices of$f$with r vertices of$g$

We now treat the case$\tau = \mathcal { T } ( \Psi ^ { 3 } ) \Psi$. Combining the comment we just made on the interpretation of Lemma 10.3 with (9.4b) and the definition (10.35) of$C _ { 1 } ^ { ( \varepsilon ) }$, we then have

![](images/page_166_image_2.jpg)

while the contribution to the second Wiener chaos is given by

$$
(\hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (z) = 3 \bigg (\bigvee_ {z} - \bigvee_ {0} z \bigg) \stackrel {{\text {def}}} {{=}} 3 \left(\hat {\mathcal {W}} _ {1} ^ {(\varepsilon ; 2)} \tau - \hat {\mathcal {W}} _ {2} ^ {(\varepsilon ; 2)} \tau\right).\tag{10.36}
$$

The reason why no contractions appear between the top vertices is that, thanks to the definition of$\dot { C } _ { 1 } ^ { ( \varepsilon ) }$in (10.35), these have been taken care of by our renormalisation procedure.

We first treat the quantity${ \hat { W } } ^ { ( \varepsilon ; 4 ) } \tau .$. The obvious guess is that, in a suitable sense, one has the convergence$\hat { \mathcal { W } } ^ { ( \bar { \varepsilon } ; 4 ) } \tau \to \hat { \mathcal { W } } ^ { ( 4 ) } \tau$τ, where

$$
(\hat {\mathcal {W}} ^ {(4)} \tau) (z) = \begin{array}{c} \bullet \\ \downarrow \\ z \end{array} - \begin{array}{c} \bullet \\ \downarrow \\ 0 \end{array} \begin{array}{c} \bullet \\ \downarrow \\ z \end{array} .
$$

In order to apply Proposition 10.11, we first need to obtain uniform bounds on the quantity$\langle ( \hat { \mathcal { W } } ^ { ( \varepsilon ; 4 ) } \tau ) ( z ) , ( \hat { \mathcal { W } } ^ { ( \varepsilon ; 4 ) } \tau ) ( \bar { z } ) \rangle$. This can be obtained in a way similar to what we did for bounding${ \hat { \mathcal { W } } } ^ { ( \varepsilon ; 2 ) } { \mathcal { T } } ( \Xi ) { \Xi }$in Theorem 10.19. Defining kernels$Q _ { \varepsilon } ^ { ( 3 ) }$and$P _ { \varepsilon }$by

$$
Q _ {\varepsilon} ^ {(3)} (z - \bar {z}) = z \bullet \longleftarrow \bigtriangleup \dots \longrightarrow \bullet \bar {z}, \quad P _ {\varepsilon} (z - \bar {z}) = z \bullet \longleftarrow \dots \longrightarrow \bullet \bar {z},
$$

we have the identity

$$
\langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 4)} \tau) (z), (\hat {\mathcal {W}} ^ {(\varepsilon ; 4)} \tau) (\bar {z}) \rangle = P _ {\varepsilon} (z - \bar {z}) \delta^ {(2)} Q _ {\varepsilon} ^ {(3)} (z, \bar {z}),
$$

where, for any function$Q$of two variables, we have set

$$
\delta^ {(2)} Q (z, \bar {z}) = Q (z, \bar {z}) - Q (z, 0) - Q (0, \bar {z}) + Q (0, 0).
$$

(Here, we have also identified a function of one variable with a function of two variables by$Q ( z , \bar { z } )  Q ( z - \bar { z } ) . )$It follows again from a combination of Lemmas 10.14 and 10.17 that, for every$\delta > 0$, one has the bounds

$$
| Q _ {\varepsilon} ^ {(3)} (z) - Q _ {\varepsilon} ^ {(3)} (0) | \lesssim \| z \| _ {\mathfrak {s}} ^ {1 - \delta}, \qquad | P _ {\varepsilon} (z) | \lesssim \| z \| _ {\mathfrak {s}} ^ {- 1}.
$$

Here, in the first term, we used the notation$z = ( t , x )$and we write$\nabla _ { x }$for the spatial gradient. As a consequence, we have the desired a priori bounds for$\hat { \mathcal { W } } ^ { ( \varepsilon ; 4 ) } \tau$, namely

$$
| \langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 4)} \tau) (z), (\hat {\mathcal {W}} ^ {(\varepsilon ; 4)} \tau) (\bar {z}) \rangle | \lesssim \| z - \bar {z} \| _ {\mathfrak {s}} ^ {- 1} \big (\| z - \bar {z} \| _ {\mathfrak {s}} ^ {1 - \delta} + \| z \| _ {\mathfrak {s}} ^ {1 - \delta} + \| \bar {z} \| _ {\mathfrak {s}} ^ {1 - \delta} \big)  ,
$$

which is valid for every$\delta > 0$

To obtain the required bounds on$\delta \hat { \mathcal { W } } ^ { ( \varepsilon ; 4 ) } \tau$, we proceed in a similar manner. For completeness, we provide some details for this term. Once suitable a priori bounds are established, all subsequent terms of the type$\delta \hat { \mathcal { W } } ^ { ( . . . ) } \tau$can be bounded in a similar manner, so we will no longer treat them in detail. Let us introduce a third kind of arrow, denoted by , which represents the kernel$K - K _ { \varepsilon }$. With this notation, one has the identity

$$
\begin{array}{l} (\delta \hat {\mathcal {W}} ^ {(\varepsilon ; 4)} \tau) (z) = \left( \begin{array}{c c c} & - & \\ z & & 0 \end{array} \right) + \left( \begin{array}{c c c} & - & \\ z & & 0 \end{array} \right) \\ + \left( \begin{array}{c c c} & - & \\ z & & 0 \end{array} \right) + \left( \begin{array}{c c c} & - & \\ z & & 0 \end{array} \right) \stackrel {{\mathrm{def}}} {{=}} \sum_ {i = 1} ^ {4} (\delta \hat {\mathcal {W}} _ {i} ^ {(\varepsilon ; 4)} \tau) (z). \end{array}
$$

It thus remains to show that each of the four terms$( \delta \hat { W } _ { i } ^ { ( \varepsilon ; 4 ) } \tau ) ( z )$satisfies a bound of the type (10.8). Note now that each term is of exactly the same form as$( \hat { \mathcal { W } } ^ { ( \varepsilon ; 4 ) } \tau ) ( z )$ except that some of the factors$K _ { \varepsilon }$are replaced by a factor$K$and exactly one factor$K _ { \varepsilon }$ is replaced by a factor$( K - K _ { \varepsilon } )$. Proceeding as above, but making use of the bound (10.19), we then obtain for each i the bound

$$
\begin{array}{r l} & {| \langle (\delta \hat {\mathcal {W}} _ {i} ^ {(\varepsilon ; 4)} \tau) (z), (\delta \hat {\mathcal {W}} _ {i} ^ {(\varepsilon ; 4)} \tau) (\bar {z}) \rangle |} \\ & {\qquad \lesssim \varepsilon^ {2 \theta} \| z - \bar {z} \| _ {\mathfrak {s}} ^ {- 1} (\| z - \bar {z} \| _ {\mathfrak {s}} ^ {1 - 2 \theta - \kappa} + \| z \| _ {\mathfrak {s}} ^ {1 - 2 \theta - \kappa} + \| \bar {z} \| _ {\mathfrak {s}} ^ {1 - 2 \theta - \kappa}),} \end{array}
$$

which is valid uniformly over$\varepsilon \in ( 0 , 1 ]$, provided that$\theta < 1$and that$\kappa > 0$. Here, we made use of (10.19) and the fact that each of these terms always contains exactly two factors$( K - K _ { \varepsilon } )$

We now turn to$\hat { \mathcal { W } } ^ { ( \varepsilon ; 2 ) } \tau$, which we decompose according to (10.36). For the first term, it follows from Lemmas 10.14 and 10.17 that we have the bound

$$
| \langle (\hat {\mathcal {W}} _ {1} ^ {(\varepsilon ; 2)} \tau) (z), (\hat {\mathcal {W}} _ {1} ^ {(\varepsilon ; 2)} \tau) (\bar {z}) \rangle | = \left| z \bullet \overbrace {\longleftrightarrow} ^ {\bullet} \bullet \overbrace {\longleftrightarrow} ^ {\bullet} \bullet \bar {z} \right| \lesssim \| z - \bar {z} \| _ {\mathfrak {s}} ^ {- \delta},
$$

valid for every$\delta > 0$. (Recall that both$K$and$K _ { \varepsilon }$are of order$- 3 ,$with norms uniform in$\varepsilon . )$In order to bound$\hat { \mathcal { W } } _ { 2 } ^ { ( \varepsilon ; 2 ) } \tau$, we introduce the notation$z \bullet \mathrm { - } \big \infty \mathrm { - } \bullet \bar { z }$as a shorthand for $\| z - \bar { z } \| _ { \mathfrak { s } } ^ { \alpha } \mathbf { 1 } _ { \| z - \bar { z } \| _ { \mathfrak { s } } \le C }$for an unspecified constant$C .$. (Such an expression will always appear as a bound and means that there exists a choice of$C$for which the bound holds true.) We will also make use of the inequalities

$$
\| z \| _ {\mathfrak {s}} ^ {- \alpha} \| \bar {z} \| _ {\mathfrak {s}} ^ {- \beta} \lesssim \| z \| _ {\mathfrak {s}} ^ {- \alpha - \beta} + \| \bar {z} \| _ {\mathfrak {s}} ^ {- \alpha - \beta},\tag{10.37a}
$$

$$
\left\| z \right\| _ {\mathfrak {s}} ^ {- \alpha} \left\| \bar {z} \right\| _ {\mathfrak {s}} ^ {- \alpha} \lesssim \left\| z - \bar {z} \right\| _ {\mathfrak {s}} ^ {- \alpha} \left(\left\| z \right\| _ {\mathfrak {s}} ^ {- \alpha} + \left\| \bar {z} \right\| _ {\mathfrak {s}} ^ {- \alpha}\right),\tag{10.37b}
$$

which are valid for every$z , \bar { z }$in${ \bf R } ^ { 4 }$and any two exponents$\alpha , \beta > 0$. The first bound is just a reformulation of Young’s inequality. The second bound follows immediately from the fact that$\begin{array} { r } { \| z \| _ { \mathfrak { s } } \vee \| \bar { z } \| _ { \mathfrak { s } } \geq \frac { 1 } { 2 } \| z - \bar { z } \| _ { \mathfrak { s } } } \end{array}$

With these bounds at hand, we obtain for every$\delta \in ( 0 , 1 )$the bound

$$
| \langle (\hat {\mathcal {W}} _ {2} ^ {(\varepsilon ; 2)} \tau) (z), (\hat {\mathcal {W}} _ {2} ^ {(\varepsilon ; 2)} \tau) (\bar {z}) \rangle | \lesssim \left| \begin{array}{c} 0 \bullet \\ z \bullet \end{array} \right. \begin{array}{c} - 3 \\ - 1 \end{array} \begin{array}{c} - 3 \\ - 3 \\ - 3 \end{array} \begin{array}{c} - 3 \\ - 3 \\ - 3 \end{array} \begin{array}{c} - 3 \\ - 1 \\ - 1 \end{array} \begin{array}{c} 0 \\ \bullet \\ \bullet \\ \bar {z} \end{array}\tag{10.38}
$$

$$
\lesssim \| z \| _ {\mathfrak {s}} ^ {- \delta} \bigl (G (z) + G (\bar {z}) + G (z - \bar {z}) + G (0) \bigr),
$$

where the function$G$is given by

![](images/page_168_image_2.jpg)

Here, in order to go from the first to the second line in (10.38), we used (10.37b) with $\alpha = \delta ,$followed by (10.37a). As a consequence of Lemma 10.14, the function G is bounded, so that the required bound follows from (10.38). Defining as previously $\hat { \mathcal { W } } _ { i } ^ { ( 2 ) } \mathcal { \tau }$τ like$\hat { \mathcal { W } } _ { i } ^ { ( \varepsilon ; 2 ) } \tau$but with each instance of$K _ { \varepsilon }$replaced by K, one then also obtains as before the bound

$$
| \langle (\delta \hat {\mathcal {W}} _ {i} ^ {(\varepsilon ; 2)} \tau) (z), (\delta \hat {\mathcal {W}} _ {i} ^ {(\varepsilon ; 2)} \tau) (\bar {z}) \rangle | \lesssim \varepsilon^ {2 \theta} \big (\| z \| _ {\mathfrak {s}} ^ {- 2 \theta - \kappa} + \| \bar {z} \| _ {\mathfrak {s}} ^ {- 2 \theta - \kappa} + \| \bar {z} - z \| _ {\mathfrak {s}} ^ {- 2 \theta - \kappa} \big),
$$

which is exactly what we require.

We now turn to the case$\tau = \mathcal { I } ( \Psi ^ { 2 } ) \Psi ^ { 2 }$. Denoting by$\psi _ { \varepsilon }$the random function $\psi _ { \varepsilon } ( z ) = ( K * \xi _ { \varepsilon } ) ( z ) = ( K _ { \varepsilon } * \xi ) ( z )$, one has the identity

$$
(\hat {\Pi} _ {0} \tau) (z) = ((K * \psi_ {\varepsilon} ^ {\diamond 2}) (z) - (K * \psi_ {\varepsilon} ^ {\diamond 2}) (0)) \cdot (\psi_ {\varepsilon} (z) \diamond \psi_ {\varepsilon} (z)) - C _ {2} ^ {(\varepsilon)}.\tag{10.39}
$$

Regarding$\hat { \mathcal { W } } ^ { ( \varepsilon ; 4 ) } \tau$, we therefore obtain similarly to before the identity

![](images/page_168_image_9.jpg)

Similarly to above, we then have the identity

$$
\langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 4)} \tau) (z), (\hat {\mathcal {W}} ^ {(\varepsilon ; 4)} \tau) (\bar {z}) \rangle = P _ {\varepsilon} ^ {2} (z - \bar {z}) \delta^ {(2)} Q _ {\varepsilon} ^ {(2)} (z, \bar {z}),
$$

where$P _ { \varepsilon }$is as above and${ Q } _ { \varepsilon } ^ { \left( 2 \right) }$is defined by

![](images/page_168_image_13.jpg)

This time, it follows from Lemmas 10.14 and 10.17 that

$$
| Q _ {\varepsilon} ^ {(2)} (z) - Q _ {\varepsilon} ^ {(2)} (0) - \langle x, \nabla_ {x} Q _ {\varepsilon} ^ {(2)} (0) \rangle | \lesssim \| z \| _ {\mathfrak {s}} ^ {2 - \delta},
$$

for arbitrarily small$\delta > 0$and otherwise the same notations as above. Combining this with the bound already obtained for$P _ { \varepsilon }$immediately yields the bound

$$
| \langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 4)} \tau) (z), (\hat {\mathcal {W}} ^ {(\varepsilon ; 4)} \tau) (\bar {z}) \rangle | \lesssim \| z - \bar {z} \| _ {\mathfrak {s}} ^ {- \delta},
$$

as required. Again, the corresponding bound on$\delta \hat { \mathcal { W } } ^ { ( \varepsilon ; 4 ) }$then follows in exactly the same fashion as before.

Regarding$\hat { \mathcal { W } } ^ { ( \varepsilon ; 2 ) } \tau .$, it follows from Lemma 10.3 and (10.39) that one has the identity

![](images/page_168_image_20.jpg)

We then obtain somewhat similarly to above

$$
\langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (z), (\hat {\mathcal {W}} ^ {(\varepsilon ; 2)} \tau) (\bar {z}) \rangle = P _ {\varepsilon} (z - \bar {z})   \delta^ {(2)} Q _ {z, \bar {z}} ^ {\varepsilon} (z, \bar {z})  ,
$$

where we have set

$$
Q _ {z, \bar {z}} ^ {\varepsilon} (a, b) = a \bullet \xleftarrow {} \bullet \xrightarrow {} \bullet \xrightarrow {} \bullet \xrightarrow {} \bullet \overline {{z}}.
$$

At this stage, we make use of Lemma 10.18. Combining it with Lemma 10.14, this immediately yields, for any$\alpha \in [ 0 , 1 ]$, the bound

$$
| \delta^ {(2)} Q _ {z, \bar {z}} ^ {\varepsilon} (z, \bar {z}) | \lesssim \| z \| _ {\mathfrak {s}} ^ {\alpha} \| \bar {z} \| _ {\mathfrak {s}} ^ {\alpha} \bigl (G (z, \bar {z}) + G (z, 0) + G (0, \bar {z}) + G (0, 0) \bigr),
$$

where this time the function G is given by

$$
G (a, b) = \begin{array}{c} z \\ a \end{array} \begin{array}{c} - 1 \\ - 3 - \alpha \end{array} \begin{array}{c} - 1 \\ - 1 \end{array} \begin{array}{c} - 1 \\ - 3 - \alpha \end{array} \begin{array}{c} \bar {z} \\ b \end{array} .
$$

As a consequence of Lemma 10.14, we see that$G$is bounded as soon as$\alpha < \textstyle { \frac { 1 } { 2 } }$, which yields the required bound. The corresponding bound on$\delta \hat { \mathcal { W } } ^ { ( \varepsilon ; 2 ) } \tau$is obtained as usual.

Still considering$\tau = \mathcal { I } ( \Psi ^ { 2 } ) \Psi ^ { 2 }$, we now turn to$\hat { \mathcal { W } } ^ { ( \varepsilon ; 0 ) } \tau .$, the component in the 0th Wiener chaos. From the expression (10.39) and the definition of the Wick product, we deduce that

$$
(\hat {\mathcal {W}} ^ {(\varepsilon ; 0)} \tau) (z) = 2 \left(\bullet \overbrace {\bigstar \bigstar} ^ {\bullet} - 0 \bullet \overbrace {\bigstar \bigstar} ^ {\bullet} z\right) - C _ {2} ^ {(\varepsilon)}.\tag{10.40}
$$

The factor two appearing in this expression arises because there are two equivalent ways of pairing the two${ \mathrm { ^ { 6 6 } t o p } } ^ { \prime 3 }$arrows with the two “bottom” arrows. At this stage, it becomes clear why we need the second renormalisation constant$C _ { 2 } ^ { ( \varepsilon ) }$: the first term in this expression diverges as$\varepsilon \to 0$and needs to be cancelled out. (Here, we omitted the label z for the first term since it doesn’t depend on it by translation invariance.) This suggests the choice

$$
C _ {2} ^ {(\varepsilon)} = 2 \leftarrow ,\tag{10.41}
$$

which then reduces (10.40) to

$$
- \frac {1}{2} (\hat {\mathcal {W}} ^ {(\varepsilon ; 0)} \tau) (z) = 0 \bullet \longleftarrow \bigstar \bigstar \bigstar z.\tag{10.42}
$$

This expression is straightforward to deal with, and it follows immediately from Lemmas 10.14 and 10.17 that we have the bound$| ( \hat { \mathcal { W } } ^ { ( \varepsilon ; 0 ) } \tau ) ( z ) | \lesssim \| z \| _ { s } ^ { - \delta }$for every exponent$\delta > 0$

This time, we postulate that$\hat { \mathscr W } ^ { ( 0 ) } \tau$is given by$_ { ( 1 0 . 4 2 ) }$with every occurrence of$K _ { \varepsilon }$ replaced by K. The corresponding bound on$\delta \hat { \mathcal { W } } ^ { ( \varepsilon ; 0 ) } \tau$is then again obtained as above. This concludes our treatment of the term$\tau = \mathcal { I } ( \Psi ^ { 2 } ) \Psi ^ { 2 }$

We now turn to the last element with negative homogeneity, which is$\tau = \mathcal { I } ( \Psi ^ { 3 } ) \Psi ^ { 2 }$ This is treated in a way which is very similar to the previous term; in particular one has an identity similar to (10.39), but with$\psi _ { \varepsilon } ^ { \circ 2 }$replaced by$\psi _ { \varepsilon } ^ { \circ 3 }$and$C _ { 2 } ^ { ( \bar { \varepsilon } ) }$replaced by $3 C _ { 2 } ^ { ( \varepsilon ) } \psi _ { \varepsilon } ( z )$. One verifies that one has the identity

$$
\langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 5)} \tau) (z), (\hat {\mathcal {W}} ^ {(\varepsilon ; 5)} \tau) (\bar {z}) \rangle = P _ {\varepsilon} ^ {2} (z - \bar {z}) \delta^ {(2)} Q _ {\varepsilon} ^ {(3)} (z, \bar {z}),
$$

where both$P _ { \varepsilon }$and$Q _ { \varepsilon } ^ { ( 3 ) }$were defined earlier. The relevant bounds then follow at once from the previously obtained bounds.

The component in the third Wiener chaos is also very similar to what was obtained previously. Indeed, one has the identity

$$
(\hat {\mathcal {W}} ^ {(\varepsilon ; 3)} \tau) (z) = 6 \left( \begin{array}{c c} \bullet & \bullet \\ \bullet & \downarrow \\ z & - \end{array} - \begin{array}{c c} \bullet & \bullet \\ \bullet & \downarrow \\ 0 & z \end{array} \right),
$$

so that

$$
\langle (\hat {\mathcal {W}} ^ {(\varepsilon ; 3)} \tau) (z), (\hat {\mathcal {W}} ^ {(\varepsilon ; 3)} \tau) (\bar {z}) \rangle = P _ {\varepsilon} (z - \bar {z}) \delta^ {(2)} \tilde {Q} _ {z, \bar {z}} ^ {\varepsilon} (z, \bar {z}),
$$

where we have set

$$
\tilde {Q} _ {z, \bar {z}} ^ {\varepsilon} (a, b) = a \bullet \xleftarrow {} \bullet \xrightarrow {} \bullet b.
$$

This time however, we simply use (10.37a) in conjunction with Lemmas 10.14 and 10.17 to obtain the bound

$$
| \tilde {Q} _ {z, \bar {z}} ^ {\varepsilon} (a, b) | \lesssim \| z - \bar {z} \| _ {\mathfrak {s}} ^ {- \delta} + \| z - b \| _ {\mathfrak {s}} ^ {- \delta} + \| a - \bar {z} \| _ {\mathfrak {s}} ^ {- \delta} + \| b - a \| _ {\mathfrak {s}} ^ {- \delta}.
$$

The required a priori bound then follows at once, and the corresponding bounds on $\delta \hat { \mathcal { W } } ^ { ( \varepsilon ; 3 ) } \tau$are obtained as usual.

It remains to bound the component in the first Wiener chaos. For this, one verifies the identity

$$
\begin{array}{l} (\hat {\mathcal {W}} ^ {(\varepsilon ; 1)} \tau) (z) = \left(6 \bigoplus_ {z} - 3 C _ {2} ^ {(\varepsilon)} \bigoplus_ {z}\right) - \bigoplus_ {0} ^ {\bullet} \\ \stackrel {{\mathrm{def}}} {{=}} 6   (\hat {\mathcal {W}} _ {1} ^ {(\varepsilon ; 1)} \tau) (z) - (\hat {\mathcal {W}} _ {2} ^ {(\varepsilon ; 1)} \tau) (z)  . \end{array}
$$

Recalling that we chose$C _ { 2 } ^ { ( \varepsilon ) }$as in (10.41), we see that

$$
(\hat {\mathcal {W}} _ {1} ^ {(\varepsilon ; 1)} \tau) (z; \bar {z}) = ((\mathscr {R} L _ {\varepsilon}) * K _ {\varepsilon}) (\bar {z} - z),
$$

where the kernel$L _ { \varepsilon }$is given by$L _ { \varepsilon } ( z ) = P _ { \varepsilon } ^ { 2 } ( z ) K ( z )$. It follows from Lemma 10.16 that, for every$\delta > 0$, the bound

$$
| \langle (\hat {\mathcal {W}} _ {1} ^ {(\varepsilon ; 1)} \tau) (z), (\hat {\mathcal {W}} _ {1} ^ {(\varepsilon ; 1)} \tau) (\bar {z}) \rangle | \lesssim \| z - \bar {z} \| _ {\mathfrak {s}} ^ {- 1 - \delta},
$$

holds uniformly for$\varepsilon \in ( 0 , 1 ]$as required. Regarding$\hat { \mathcal { W } } _ { 2 } ^ { ( \varepsilon ; 1 ) } \tau$, we can again apply the bounds (10.37) to obtain

$$
| \langle (\hat {\mathcal {W}} _ {2} ^ {(\varepsilon ; 1)} \tau) (z), (\hat {\mathcal {W}} _ {2} ^ {(\varepsilon ; 1)} \tau) (\bar {z}) \rangle | \lesssim \| z \| _ {\mathfrak {s}} ^ {- \frac {1}{2} - \delta} \| \bar {z} \| _ {\mathfrak {s}} ^ {- \frac {1}{2} - \delta},
$$

as required. Regarding$\hat { \mathcal { W } } ^ { ( 1 ) } \tau$, we define it as

$$
\hat {\mathcal {W}} ^ {(1)} \tau = \hat {\mathcal {W}} _ {1} ^ {(1)} \tau + \hat {\mathcal {W}} _ {2} ^ {(1)} \tau ,
$$

where$\hat { \mathcal { W } } _ { 2 } ^ { ( 1 ) } \tau$is defined like$\hat { \mathcal { W } } _ { 2 } ^ { ( 1 ) } \tau$, but with$K _ { \varepsilon }$replaced by$K ,$, and where

$$
(\hat {\mathcal {W}} _ {1} ^ {(1)} \tau) (z; \bar {z}) = ((\mathscr {R} L) * K) (\bar {z} - z).
$$

Again,$\delta \hat { \mathcal { W } } ^ { ( 1 ) } \tau$can be bounded in a manner similar to before, thus concluding the proof.

Remark 10.23 It is possible to show that$C _ { 1 } ^ { ( \varepsilon ) } \sim \varepsilon ^ { - 1 }$and$C _ { 2 } ^ { ( \varepsilon ) } \sim \log \varepsilon$, but the precise values of these constants do not really matter here. See [Fel74, FO76] for an expression for these constants in a slightly different context.

## Appendix A A generalised Taylor formula

Classically, Taylor’s formula for functions on$\mathbf { R } ^ { d }$is obtained by applying the onedimensional formula to the function obtained by evaluating the original function on a line connecting the start and endpoints. This however does not yield the “right” formula if one is interested in obtaining the correct scaling behaviour when applying it to functions with inhomogeneous scalings. In this section, we provide a version of Taylor’s formula with a remainder term having the correct scaling behaviour for any non-trivial scaling s of$\mathbf { R } ^ { d }$. Although it is hard to believe that this formula isn’t known (see [Bon09] for some formulae with a very similar flavour) it seems difficult to find it in the literature in the form stated here. Furthermore, it is of course very easy to prove, so we provide a complete proof.

In order to formulate our result, we introduce the following kernels on R:

$$
\mu_ {\ell} (x, d y) = \mathbf {1} _ {[ 0, x ]} (y) \frac {(x - y) ^ {\ell - 1}}{(\ell - 1) !} d y, \quad \mu_ {\star} (x, d y) = \delta_ {0} (d y).
$$

For$\ell = 0 .$, we extend this in a natural way by setting$\mu _ { 0 } ( x , d y ) = \delta _ { x } ( d y )$. With these notations at hand, any multiindex$k \in \mathbf { N } ^ { d }$gives rise to a kernel$\mathcal { Q } ^ { k }$on$\mathbf R ^ { d } \mathrm { { b y } }$

$$
\mathcal {Q} ^ {k} (x, d y) = \prod_ {i = 1} ^ {d} \mu_ {i} ^ {k} (x _ {i}, d y _ {i}),\tag{A.1}
$$

where we define

$$
\mu_ {i} ^ {k} (z, \cdot) = \left\{ \begin{array}{c l} \mu_ {k _ {i}} (z, \cdot) & \text { if } i \leq \mathfrak {m} (k), \\ \frac {z ^ {k _ {i}}}{k _ {i} !} \mu_ {\star} (z, \cdot) & \text { otherwise }, \end{array} \right.
$$

where we defined the quantity

$$
\mathfrak {m} (k) = \min \{j: k _ {j} \neq 0 \}.
$$

Note that, in any case, one has the identity$\begin{array} { r } { \mu _ { i } ^ { k } ( z , { \bf R } ) = \frac { z ^ { k _ { i } } } { k _ { i } ! } } \end{array}$, so that

$$
\mathcal {Q} ^ {k} (x, \mathbf {R} ^ {d}) = \frac {x ^ {k}}{k !}.
$$

Recall furthermore that$\mathbf { N } ^ { d }$is endowed with a natural partial order by saying that $k \ \leq \ \ell$if$k _ { i } \ \leq \ \ell _ { i }$for every$i \in \{ 1 , \ldots , d \}$. Given$k \in \mathbf { N } ^ { d }$, we use the shorthand $k _ { < } = \{ \ell \neq k : \ell \leq k \}$

Proposition A.1 Let$A \subset \mathbf { N } ^ { d }$be such that$k \in A \Rightarrow k _ { < } \subset A$and define$\partial A = \{ k \notin$ $A : k - e _ { \mathfrak { m } ( k ) } \in A \}$. Then, the identity

$$
f (x) = \sum_ {k \in A} \frac {D ^ {k} f (0)}{k !} x ^ {k} + \sum_ {k \in \partial A} \int_ {\mathbf {R} ^ {d}} D ^ {k} f (y) \mathcal {Q} ^ {k} (x, d y),\tag{A.2}
$$

holds for every smooth function$f$on$\mathbf { R } ^ { d }$.

Proof. The case$A = \{ 0 \}$is straightforward to verify “by hand”. Note then that, for every set A as in the statement, one can find a sequence$\left\{ A _ { n } \right\}$of sets such as in the statement with$A _ { a } = \{ 0 \} , A _ { | A | } = A$, and$A _ { n + 1 } = A _ { n } \cup \{ k _ { n } \}$for some$k _ { n } \in \partial A _ { n }$. It is therefore sufficient to show that if$( \mathrm { A } . 2 )$holds for some set A, then it also holds for ${ \bar { A } } = A \cup \{ \ell \}$for any$\ell \in \partial A$

Assume from now on that (A.2) holds for some A and we choose some$\ell \in \partial A$ Inserting the first-order Taylor expansion$( \mathrm { i } . \mathrm { e } . \ ( \mathrm { A } . 2 )$with$A = \{ 0 \} )$into the term involving$D ^ { \ell } f$and using (A.1), we then obtain the identity

$$
\begin{array}{l} f (x) = \sum_ {k \in \bar {A}} \frac {D ^ {k} f (0)}{k !} x ^ {k} + \sum_ {k \in \partial A \setminus \{\ell \}} \int_ {\mathbf {R} ^ {d}} D ^ {k} f (y)   \mathcal {Q} ^ {k} (x, d y) \\ \qquad + \sum_ {i = 1} ^ {d} \int_ {\mathbf {R} ^ {d}} D ^ {\ell + e _ {i}} f (y)   (\mathcal {Q} ^ {e _ {i}} \star \mathcal {Q} ^ {\ell}) (x, d y)  . \end{array}
$$

It is straightforward to check that one has the identities

$$
\mu_ {m} \star \mu_ {n} = \mu_ {m + n}, (\mu_ {\star} \star \mu_ {n}) (x, \cdot) = \frac {x ^ {n}}{n !} \mu_ {\star}, \mu_ {\star} \star \mu_ {\star} = \mu_ {\star}, \mu_ {n} \star \mu_ {\star} = 0,
$$

valid for every$m , n \geq 0$. As a consequence, it follows from the definition of$\mathcal { Q } ^ { k }$that one has the identity

$$
\mathcal {Q} ^ {e _ {i}} \star \mathcal {Q} ^ {\ell} = \left\{ \begin{array}{c l} \mathcal {Q} ^ {\ell + e _ {i}} & \text { if } i \leq \mathfrak {m} (\ell), \\ 0 & \text { otherwise }. \end{array} \right.
$$

The claim now follows from the fact that, by definition, ∂A<sup>¯</sup> is precisely given by$( \partial A \backslash$ $\{ \ell \} ) \cup \{ \ell + e _ { i } : i \leq \mathfrak { m } ( \ell ) \}$□

## Appendix B Symbolic index

In this appendix, we collect the most used symbols of the article, together with their meaning and the page where they were first introduced.

| Symbol | Meaning | Page |
| --- | --- | --- |
| 1 | Unit element in $T$ | 18 |
| $1^*$ | Projection onto 1 | 120 |
| $\|\cdot\|_{\mathfrak{s}}$ | Scaled degree of a multiindex | 22 |
| $\\\|\cdot\\\|_{\mathfrak{s}}$ | Scaled distance on $\mathbf{R}^{d}$ | 24 |
| $\\\|\cdot\\\|_{\gamma;\mathfrak{K}}$ | “Norm” of a model / modelled distribution | 27, 30 |
| ○ | Dual of $\Delta^{+}$ | 123 |
| ★ | Generic product on $T$ | 48 |
| * | Convolution of distributions on $\mathbf{R}^{d}$ | 63 |
| A | Set of possible homogeneities for $T$ | 18 |
| A | Antipode of $\mathcal{H}_{+}$ | 120 |
| Alg(C) | Subalgebra of $\mathcal{H}_{+}$ determined by C | 130 |
| β | Regularity improvement of K | 63 |
| $\mathcal{C}_{\mathfrak{s}}^{\alpha}$ | α-Hölder continuous functions with scaling s | 24 |
| D | Abstract gradient | 83 |
| $\mathcal{D}^{\gamma}$ | Modelled distributions of regularity γ | 30 |
| $\mathcal{D}_{P}^{\gamma,\eta}$ | Singular modelled distributions of regularity γ | 85 |
| Δ | Comodule structure of H over $\mathcal{H}_{+}$ | 119 |
| $\Delta^{+}$ | Coproduct in $\mathcal{H}_{+}$ | 119 |
| $\Delta^{M}$ | Action of M on Π | 130 |
| $\hat{\Delta}^{M}$ | Action of M on Γ | 133 |
| F | Nonlinearity of the SPDE under consideration | 3 |
| $F_{x}$ | Factor in $\Gamma_{xy} = F_{x}^{-1}F_{y}$ | 129 |
| F | All formal expressions for the model space | 116 |
| $\mathcal{F}_{+}$ | All formal expressions representing Taylor coefficients | 116 |
| $\mathcal{F}_{F}$ | Subset of F generated by F | 116 |
| $\mathcal{F}_{F}^{+}$ | Subset of $\mathcal{F}_{+}$ generated by F | 116 |
| G | Structure group | 18 |
| $\Gamma_{g}$ | Action of $\mathcal{H}_{+}^{*}$ onto H | 123 |
| $\mathcal{H}_{+}^{*}$ | Dual of $\mathcal{H}_{+}$ | 123 |
| $\mathcal{H}_{+}$ | Linear span of $\mathcal{F}_{+}$ | 119 |
| $\mathcal{H}_{F}^{+}$ | Linear span of $\mathcal{F}_{F}^{+}$ | 119 |
| H | Linear span of F | 119 |
| I | Abstract integration map for K | 66 |
| $\mathcal{I}_{k}$ | Abstract integration map for $D^{k}K$ | 114 |
| $\mathcal{J}(x)$ | Taylor expansion of $K * \Pi_{x}$ | 67 |
| $\mathcal{J}_{k}\tau$ | Abstract placeholder for Taylor coefficients of $\Pi_{x}\tau$ | 118 |
| K | Generic compact set in $\mathbf{R}^{d}$ | 24 |
| K | Truncated Green’s function of L | 63, 65 |
| $K_{n}$ | Contribution of K at scale $2^{-n}$ | 63 |
| $K_{n,xy}^{\alpha}$ | Remainder of Taylor expansion of $K_n$ | 67 |
| $\mathcal{K},\mathcal{K}_{\gamma}$ | Operator such that $\mathcal{R}\mathcal{K}f = K * \mathcal{R}f$ | 63 |
| $\mathcal{L}$ | Linearisation of the SPDE under consideration | 3 |
| $\Lambda_{n}^{\mathfrak{s}}$ | Diadic grid at level n for scaling s | 35 |
| $\mathcal{M}$ | Multiplication operator on $\mathcal{H}_+$ | 120 |
| M | Renormalisation map | 130 |
| $\hat{M}$ | Action of M on f | 130 |
| $M_g$ | Action of S on T | 47 |
| $\mathfrak{M}_F$ | Basic building blocks of F | 115 |
| $\mathcal{M}_\mathcal{T}$ | All models for T | 27 |
| $\mathcal{M}_F$ | All admissible models associated to F | 128 |
| $\mathcal{N}_{\gamma}$ | Operator such that $\mathcal{K}_{\gamma} = \mathcal{I} + \mathcal{J} + \mathcal{N}_{\gamma}$ | 68 |
| $(\Pi, f)$ | Alternative representation of an admissible model | 129 |
| $(\Pi^M, f^M)$ | Renormalised model | 130 |
| $(\Pi, \Gamma)$ | Model for a regularity structure | 25 |
| $\varphi_x^n$ | Scaling function at level n around x | 34 |
| $\psi_x^n$ | Wavelet at level n around x | 34 |
| P | Time 0 hyperplane | 99 |
| $\mathcal{P}_F$ | Formal expressions required to represent $\partial u$ | 116 |
| $\mathcal{Q}_{\alpha}$ | Projection onto $T_{\alpha}$ | 20 |
| $\mathcal{Q}_{\alpha}^-$ | Projection onto $T_{\alpha}^-$ | 20 |
| $\boldsymbol{R}^{+}$ | Restriction to positive times | 99 |
| R | Smooth function such that “G = K + R” | 105 |
| $R_{\gamma}$ | Convolution by R on $\mathcal{D}^{\gamma}$ | 103 |
| $\mathcal{R}$ | Reconstruction operator | 31 |
| $\mathfrak{R}$ | Renormalisation group | 133 |
| s | Scaling of $\mathbf{R}^d$ | 22 |
| $\mathcal{S}_{\mathfrak{s},x}^{\delta}$ | Scaling by δ around x | 25 |
| $\mathcal{S}_P^\delta$ | Scaling by δ in directions normal to P | 86 |
| $\mathcal{S}$ | Discrete symmetry group | 47 |
| T | Model space | 18 |
| $T_{\alpha}$ | Elements of T of homogeneity α | 18 |
| $T_{\alpha}^{+}$ | Elements of T of homogeneity α and higher | 20 |
| $T_{\alpha}^-$ | Elements of T of homogeneity strictly less than α | 20 |
| $T_g$ | Action of S on $\mathbf{R}^d$ | 47 |
| $\bar{T}$ | Abstract Taylor polynomials in T | 27 |
| $\mathcal{T}$ | Generic regularity structure $\mathcal{T} = (A, T, G)$ | 18 |
| $\mathcal{T}_{\beta}$ | Classical Taylor expansion of order β | 23 |
| $\mathcal{U}_F$ | Formal expressions required to represent u | 116 |
| V,W | Generic sector of T | 20 |
| $X^k$ | Abstract symbol representing Taylor monomials | 21 |
| $\Xi$ | Abstract symbol for the noise | 54 |

## References

[AC90] S. ALBEVERIO and A. B. CRUZEIRO. Global flows with invariant (Gibbs) measures for Euler and Navier-Stokes two-dimensional fluids. Comm. Math. Phys. 129, no. 3, (1990), 431–444.

[AF04] S. ALBEVERIO and B. FERRARIO. Uniqueness of solutions of the stochastic Navier-Stokes equation with invariant measure given by the enstrophy. Ann. Probab. 32, no. 2, (2004), 1632–1649.

[Aiz82] M. AIZENMAN. Geometric analysis of$\varphi ^ { 4 }$fields and Ising models. I, II. Comm. Math. Phys. 86, no. 1, (1982), 1–48.

[ALZ06] S. ALBEVERIO, S. LIANG, and B. ZEGARLINSKI. Remark on the integration by parts formula for the ϕ<sup>4</sup><sub>3</sub>-quantum field model. Infin. Dimens. Anal. Quantum Probab. Relat. Top. 9, no. 1, (2006), 149–154.

[AR91] S. ALBEVERIO and M. ROCKNER¨ . Stochastic differential equations in infinite dimensions: solutions via Dirichlet forms. Probab. Theory Related Fields 89, no. 3, (1991), 347–386.

[BCD11] H. BAHOURI, J.-Y. CHEMIN, and R. DANCHIN. Fourier analysis and nonlinear partial differential equations, vol. 343 of Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences]. Springer, Heidelberg, 2011.

[BDP97] F. E. BENTH, T. DECK, and J. POTTHOFF. A white noise approach to a class of non-linear stochastic heat equations. J. Funct. Anal. 146, no. 2, (1997), 382–415.

[BG97] L. BERTINI and G. GIACOMIN. Stochastic Burgers and KPZ equations from particle systems. Comm. Math. Phys. 183, no. 3, (1997), 571–607.

[BGJ12] Z. BRZEZNIAK´ , B. GOLDYS, and T. JEGARAJ. Weak solutions of a stochastic Landau-Lifshitz-Gilbert equation. Appl. Math. Res. Express. AMRX 2012, (2012), Art. ID abs009, 33.

[BGJ13] C. BERNARDIN, P. GONC¸ ALVES, and M. JARA. Private communication, 2013.

[Bie11] L. BIEBERBACH. Uber die Bewegungsgruppen der Euklidischen R¨aume. <sup>¨</sup> Math. Ann. 70, no. 3, (1911), 297–336.

[Bie12] L. BIEBERBACH. Uber die Bewegungsgruppen der Euklidischen R¨aume (Zweite <sup>¨</sup> Abhandlung.) Die Gruppen mit einem endlichen Fundamentalbereich. Math. Ann. 72, no. 3, (1912), 400–412.

[BMN10] A. B <sup>´</sup> ENYI ´ , D. MALDONADO, and V. NAIBO. What is . . . a paraproduct? Notices Amer. Math. Soc. 57, no. 7, (2010), 858–860.

[Bon81] J.-M. BONY. Calcul symbolique et propagation des singularit´es pour les ´equations aux d´eriv´ees partielles non lin´eaires. Ann. Sci. Ecole Norm. Sup. (4)<sup>´</sup> 14, no. 2, (1981), 209–246.

[Bon09] A. BONFIGLIOLI. Taylor formula for homogeneous groups and applications. Math. Z. 262, no. 2, (2009), 255–279.

[BPRS93] L. BERTINI, E. PRESUTTI, B. RUDIGER ¨ , and E. SAADA. Dynamical fluctuations at the critical point: convergence to a nonlinear stochastic PDE. Teor. Veroyatnost. i Primenen. 38, no. 4, (1993), 689–741.

[Bro04] C. BROUDER. Trees, renormalization and differential equations. BIT 44, no. 3, (2004), 425–438.

[But72] J. C. BUTCHER. An algebraic theory of integration methods. Math. Comp. 26, (1972), 79–106.

[CFO11] M. CARUANA, P. K. FRIZ, and H. OBERHAUSER. A (rough) pathwise approach to a class of non-linear stochastic partial differential equations. Ann. Inst. H. Poincar´e Anal. Non Lin´eaire 28, no. 1, (2011), 27–46.

[Cha00] T. CHAN. Scaling limits of Wick ordered KPZ equation. Comm. Math. Phys. 209, no. 3, (2000), 671–690.

[Che54] K.-T. CHEN. Iterated integrals and exponential homomorphisms. Proc. London Math. Soc. (3) 4, (1954), 502–512.

[CK00] A. CONNES and D. KREIMER. Renormalization in quantum field theory and the Riemann-Hilbert problem. I. The Hopf algebra structure of graphs and the main theorem. Comm. Math. Phys. 210, no. 1, (2000), 249–273.

[CK01] A. CONNES and D. KREIMER. Renormalization in quantum field theory and the Riemann-Hilbert problem. II. The β-function, diffeomorphisms and the renormalization group. Comm. Math. Phys. 216, no. 1, (2001), 215–241.

[CM94] R. A. CARMONA and S. A. MOLCHANOV. Parabolic Anderson problem and intermittency. Mem. Amer. Math. Soc. 108, no. 518, (1994), viii+125.

[Col51] J. D. COLE. On a quasi-linear parabolic equation occurring in aerodynamics. Quart. Appl. Math. 9, (1951), 225–236.

[Col83] J.-F. COLOMBEAU. A multiplication of distributions. J. Math. Anal. Appl. 94, no. 1, (1983), 96–115.

[Col84] J.-F. COLOMBEAU. New generalized functions and multiplication of distributions, vol. 84 of North-Holland Mathematics Studies. North-Holland Publishing Co., Am sterdam, 1984. Notas de Matem´atica [Mathematical Notes], 90.

[CQ02] L. COUTIN and Z. QIAN. Stochastic analysis, rough path analysis and fractional Brownian motions. Probab. Theory Related Fields 122, no. 1, (2002), 108–140.

[Dau88] I. DAUBECHIES. Orthonormal bases of compactly supported wavelets. Comm. Pure Appl. Math. 41, no. 7, (1988), 909–996.

[Dau92] I. DAUBECHIES. Ten lectures on wavelets, vol. 61 of CBMS-NSF Regional Conference Series in Applied Mathematics. Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA, 1992.

[Dav08] A. M. DAVIE. Differential equations driven by rough paths: an approach via discrete approximation. Appl. Math. Res. Express. AMRX 2008, (2008), Art. ID abm009, 40.

[Del04] B. DELAMOTTE. A hint of renormalization. Amer. J. Phys. 72, no. 2, (2004), 170.

[DPD02] G. DA PRATO and A. DEBUSSCHE. Two-dimensional Navier-Stokes equations driven by a space-time white noise. J. Funct. Anal. 196, no. 1, (2002), 180–210.

[DPD03] G. DA PRATO and A. DEBUSSCHE. Strong solutions to the stochastic quantization equations. Ann. Probab. 31, no. 4, (2003), 1900–1916.

[DPDT07] G. DA PRATO, A. DEBUSSCHE, and L. TUBARO. A modified Kardar-Parisi-Zhang model. Electron. Comm. Probab. 12, (2007), 442–453 (electronic).

[EJS13] W. E, A. JENTZEN, and H. SHEN. Renormalized powers of Ornstein-Uhlenbeck processes and well-posedness of stochastic Ginzburg-Landau equations. ArXiv eprints (2013). arXiv:1302.5930.

[EO71] J.-P. ECKMANN and K. OSTERWALDER. On the uniqueness of the Hamiltionian and of the representation of the CCR for the quartic boson interaction in three dimensions. Helv. Phys. Acta 44, (1971), 884–909.

[FdLP06] D. FEYEL and A. DE LA PRADELLE. Curvilinear integrals along enriched paths. Electron. J. Probab. 11, (2006), no. 34, 860–892 (electronic).

[Fel74] J. FELDMAN. The λϕ<sup>4</sup><sub>3</sub> field theory in a finite volume. Comm. Math. Phys. 37, (1974), 93–120.

[FO76] J. S. FELDMAN and K. OSTERWALDER. The Wightman axioms and the mass gap for weakly coupled (Φ<sup>4</sup>)<sub>3</sub> quantum field theories. Ann. Physics 97, no. 1, (1976), 80–135.

[Fr¨o82] J. FROHLICH ¨ . On the triviality of λϕ<sup>4</sup><sub>d</sub> theories and the approach to the critical point in d > 4 dimensions. Nuclear Phys. B 200, no. 2, (1982), 281–296.

[Fun92] T. FUNAKI. A stochastic partial differential equation with values in a manifold. J. Funct. Anal. 109, no. 2, (1992), 257–288.

[FV06] P. FRIZ and N. VICTOIR. A note on the notion of geometric rough paths. Probab. Theory Related Fields 136, no. 3, (2006), 395–416.

[FV10a] P. FRIZ and N. VICTOIR. Differential equations driven by Gaussian signals. Ann. Inst. Henri Poincar´e Probab. Stat. 46, no. 2, (2010), 369–413.

[FV10b] P. K. FRIZ and N. B. VICTOIR. Multidimensional stochastic processes as rough paths, vol. 120 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2010. Theory and applications.

[GIP12] M. GUBINELLI, P. IMKELLER, and N. PERKOWSKI. Paraproducts, rough paths and controlled distributions. ArXiv e-prints (2012). arXiv:1210.2684.

[GJ73] J. GLIMM and A. JAFFE. Positivity of the ϕ<sup>4</sup><sub>3</sub> Hamiltonian. Fortschr. Physik 21, (1973), 327–376.

[GJ87] J. GLIMM and A. JAFFE. Quantum physics. Springer-Verlag, New York, second ed., 1987. A functional integral point of view.

[Gli68] J. GLIMM. Boson fields with the :Φ<sup>4</sup>: interaction in three dimensions. Comm. Math. Phys. 10, (1968), 1–47.

[GLP99] G. GIACOMIN, J. L. LEBOWITZ, and E. PRESUTTI. Deterministic and stochastic hydrodynamic equations arising from simple microscopic model systems. In Stochastic partial differential equations: six perspectives, vol. 64 of Math. Surveys Monogr., 107–152. Amer. Math. Soc., Providence, RI, 1999.

[Gro75] L. GROSS. Logarithmic Sobolev inequalities. Amer. J. Math. 97, no. 4, (1975), 1061–1083.

[GRS75] F. GUERRA, L. ROSEN, and B. SIMON. The P(ϕ)<sub>2</sub> Euclidean quantum field theory as classical statistical mechanics. I, II. Ann. ofMath. (2) 101, (1975), 111–189; ibid. (2) 101 (1975), 191–259.

[GT10] M. GUBINELLI and S. TINDEL. Rough evolution equations. Ann. Probab. 38, no. 1, (2010), 1–75.

[Gub04] M. GUBINELLI. Controlling rough paths. J. Funct. Anal. 216, no. 1, (2004), 86–140.

[Gub10] M. GUBINELLI. Ramification of rough paths. J. Differential Equations 248, no. 4, (2010), 693–721.

[Hai09] M. HAIRER. An Introduction to Stochastic PDEs. ArXiv e-prints (2009). arXiv:0907.4178.

[Hai11] M. HAIRER. Rough stochastic PDEs. Comm. Pure Appl. Math. 64, no. 11, (2011), 1547–1585.

[Hai12] M. HAIRER. Singular perturbations to semilinear stochastic heat equations. Probab. Theory Related Fields 152, no. 1-2, (2012), 265–297.

[Hai13] M. HAIRER. Solving the KPZ equation. Ann. Math. (2013). To appear.

[Hid75] T. HIDA. Analysis of Brownian functionals. Carleton Univ., Ottawa, Ont., 1975. Carleton Mathematical Lecture Notes, No. 13.

[HK12] M. HAIRER and D. KELLY. Geometric versus non-geometric rough paths. ArXiv e-prints (2012). arXiv:1210.6294.

[HM12] M. HAIRER and J. MAAS. A spatial version of the Itˆo-Stratonovich correction. Ann. Probab. 40, no. 4, (2012), 1675–1714.

[HMW12] M. HAIRER, J. MAAS, and H. WEBER. Approximating rough stochastic PDEs. ArXiv e-prints (2012). arXiv:1202.3094.

[Hop50] E. HOPF. The partial differential equation$u _ { t } + u u _ { x } = \mu u _ { x x } .$. Comm. Pure Appl. Math. 3, (1950), 201–230.

[H¨or55] L. HORMANDER¨ . On the theory of general partial differential operators. Acta Math. 94, (1955), 161–248.

[HØUZ10] H. HOLDEN, B. ØKSENDAL, J. UBØE, and T. ZHANG. Stochastic partial differential equations. Universitext. Springer, New York, second ed., 2010. A modeling, white noise functional approach.

[HP90] T. HIDA and J. POTTHOFF. White noise analysis—an overview. In White noise analysis (Bielefeld, 1989), 140–165. World Sci. Publ., River Edge, NJ, 1990.

[HP13] M. HAIRER and N. PILLAI. Regularity of laws and ergodicity of hypoelliptic sdes driven by rough paths. Ann. Probab. (2013). To appear.

[HRW12] M. HAIRER, M. D. RYSER, and H. WEBER. Triviality of the 2D stochastic Allen-Cahn equation. Electron. J. Probab. 17, (2012), no. 39, 14.

[HV11] M. HAIRER and J. VOSS. Approximations to the stochastic Burgers equation. J. Nonlinear Sci. 21, no. 6, (2011), 897–920.

[HW74] E. HAIRER and G. WANNER. On the Butcher group and general multi-value methods. Computing (Arch. Elektron. Rechnen) 13, no. 1, (1974), 1–15.

[HW13] M. HAIRER and H. WEBER. Rough Burgers-like equations with multiplicative noise. Probab. Theory Related Fields 1–56.

[IPP08] B. IFTIMIE, E. P<sup>´</sup> ARDOUX, and A. PIATNITSKI. Homogenization of a singular random one-dimensional PDE. Ann. Inst. Henri Poincar´e Probab. Stat. 44, no. 3, (2008), 519–543.

[JLM85] G. JONA-LASINIO and P. K. MITTER. On the stochastic quantization of field theory. Comm. Math. Phys. 101, no. 3, (1985), 409–436.

[KE83] J. R. KLAUDER and H. EZAWA. Remarks on a stochastic quantization of scalar fields. Progr. Theoret. Phys. 69, no. 2, (1983), 664–673.

[KPZ86] M. KARDAR, G. PARISI, and Y.-C. ZHANG. Dynamic scaling of growing interfaces. Phys. Rev. Lett. 56, no. 9, (1986), 889–892.

[Kry08] N. V. KRYLOV. Lectures on elliptic and parabolic equations in Sobolev spaces, vol. 96 of Graduate Studies in Mathematics. American Mathematical Society, Providence, RI, 2008.

[LCL07] T. J. LYONS, M. CARUANA, and T. LEVY ´ . Differential equations driven by rough paths, vol. 1908 of Lecture Notes in Mathematics. Springer, Berlin, 2007. Lectures from the 34th Summer School on Probability Theory held in Saint-Flour, July 6–24, 2004, With an introduction concerning the Summer School by Jean Picard.

[LQ02] T. LYONS and Z. QIAN. System control and rough paths. Oxford Mathematical Monographs. Oxford University Press, Oxford, 2002. Oxford Science Publications.

[LS69] R. G. LARSON and M. E. SWEEDLER. An associative orthogonal bilinear form for Hopf algebras. Amer. J. Math. 91, (1969), 75–94.

[LV07] T. LYONS and N. VICTOIR. An extension theorem to rough paths. Ann. Inst. H. Poincar´e Anal. Non Lin´eaire 24, no. 5, (2007), 835–847.

[Lyo98] T. J. LYONS. Differential equations driven by rough signals. Rev. Mat. Iberoamericana 14, no. 2, (1998), 215–310.

[Mey92] Y. MEYER. Wavelets and operators, vol. 37 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 1992. Translated from the 1990 French original by D. H. Salinger.

[MM65] J. W. MILNOR and J. C. MOORE. On the structure of Hopf algebras. Ann. ofMath. (2) 81, (1965), 211–264.

[MR04] R. MIKULEVICIUS and B. L. ROZOVSKII. Stochastic Navier-Stokes equations for turbulent flows. SIAM J. Math. Anal. 35, no. 5, (2004), 1250–1310.

[Nel73] E. NELSON. The free Markoff field. J. Functional Analysis 12, (1973), 211–227.

[Nua06] D. NUALART. The Malliavin calculus and related topics. Probability and its Applications (New York). Springer-Verlag, Berlin, second ed., 2006.

[Pin02] M. A. PINSKY. Introduction to Fourier analysis and wavelets. Brooks/Cole Series in Advanced Mathematics. Brooks/Cole, Pacific Grove, CA, 2002.

[PW81] G. PARISI and Y. S. WU. Perturbation theory without gauge fixing. Sci. Sinica 24, no. 4, (1981), 483–496.

[Reu93] C. REUTENAUER. Free Lie algebras, vol. 7 of London Mathematical Society Monographs. New Series. The Clarendon Press Oxford University Press, New York, 1993. Oxford Science Publications.

[RY91]D. REVUZ and M. YOR. Continuous martingales and Brownian motion, vol. 293 of Grundlehren der Mathematischen Wissenschaften [Fundamental Principles ofMathematical Sciences]. Springer-Verlag, Berlin, 1991.

[Sch54] L. SCHWARTZ. Sur l’impossibilit´e de la multiplication des distributions. C. R. Acad. Sci. Paris 239, (1954), 847–848.

[Sim97] L. SIMON. Schauder estimates by scaling. Calc. Var. Partial Differential Equations 5, no. 5, (1997), 391–407.

[Swe67] M. E. SWEEDLER. Cocommutative Hopf algebras with antipode. Bull. Amer. Math. Soc. 73, (1967), 126–128.

[Swe69] M. E. SWEEDLER. Hopf algebras. Mathematics Lecture Note Series. W. A. Benjamin, Inc., New York, 1969.

[Tei11] J. TEICHMANN. Another approach to some rough and stochastic partial differential equations. Stoch. Dyn. 11, no. 2-3, (2011), 535–550.

[Unt10] J. UNTERBERGER. H¨older-continuous rough paths by Fourier normal ordering. Comm. Math. Phys. 298, no. 1, (2010), 1–36.

[Wal86] J. B. WALSH. An introduction to stochastic partial differential equations. In Ecole<sup>´</sup> d’´et´e de probabilit´es de Saint-Flour, XIV—1984, vol. 1180 of Lecture Notes in Math., 265–439. Springer, Berlin, 1986.

[Wie38] N. WIENER. The Homogeneous Chaos. Amer. J. Math. 60, no. 4, (1938), 897–936.

[You36] L. C. YOUNG. An inequality of the H¨older type, connected with Stieltjes integration. Acta Math. 67, no. 1, (1936), 251–282.