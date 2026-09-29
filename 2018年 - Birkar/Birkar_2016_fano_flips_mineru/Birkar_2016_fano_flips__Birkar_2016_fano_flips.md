# A penalized method for multivariate concave least squares with application to productivity analysis

Abolfazl Keshvari

Aalto University School of Business, Helsinki, Finland abolfazl.keshvari@aalto.fi, tel: 00358503120915

To appear in the European Journal of Operational Research

## Abstract

We propose a penalized method for the least squares estimator of a multivariate concave regression function. This estimator is formulated as a quadratic programming (QP) problem with �(�<sup>2</sup>) constraints, where � is the number of observations. Computing such an estimator is a very timeconsuming task, and the computational burden rises dramatically as the number of observations increases. By introducing a quadratic penalty function, we reformulate the concave least squares estimator as a QP with only non-negativity constraints. This reformulation can be adapted for estimating variants of shape restricted least squares, i.e. the monotonic-concave/convex least squares. The experimental results and an empirical study show that the reformulated problem and its dual are solved significantly faster than the original problem. The Matlab and R codes for implementing the penalized problems are provided in the paper.

Keywords: concave regression, convex regression, penalization method, production function.

## 1. Introduction

This paper is concerned with the shape restricted least squares problem, which is used to estimate a concave or convex regression function. Such an estimator is used in different disciplines: such as productivity analysis (Keshvari & Kuosmanen, 2013; Kuosmanen, 2012; H. Varian, 1984), econometrics (Aït-Sahalia & Duarte, 2003; H. R. Varian, 1982), statistics (Birke & Dette, 2007; Hanson & Pledger, 1976; Hildreth, 1954), and operations research (Badinelli, 1986; Zhou & Lange, 2013).

The estimated function is selected among all the possible functions satisfying the shape assumption. The function is shown to be a piecewise linear function, and it is formulated as a quadratic programming (QP) problem (Kuosmanen, 2008). The finite sample properties of the shape restricted least squares estimator are known. For example, it is known that it satisfies the orthogonality condition, and the mean of fitted values is equal to the mean of the responses. The properties and characteristics are studied by several researchers (see for example Groeneboom, Jongbloed, &

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup> © 2016 This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/</span></small>

Wellner, 2001; Hanson & Pledger, 1976; Kuosmanen, 2008; Mammen, 1991; Meyer, 2003, 2006; Nemirovskii, Polyak, & Tsybakov, 1985; Seijo & Sen, 2011).

Single variate problems are relatively easy to solve and several methods are proposed to compute the estimator (Dykstra & Robertson, 1982; Dykstra, 1983; Hanson & Pledger, 1976; Hildreth, 1954). However, dealing with a multivariate problem is difficult and it is very time consuming. The main source of the computational burden is the number of constraints that is of order$O ( n ^ { 2 } )$and rises very quickly as the number of observations (�) increases. To solve this problem, Holloway (1979) proposed an iterative algorithm that approximates the regression function, and it is applied on small size samples. Another approach is proposed by Fraser & Massam (1989) and Meyer (1999) that is a mixed primal–dual algorithm to find a least squares regression estimate over the closed convex cone defined by the constraints. Goldman and Ruud (1993) also propose a generalization to the algorithms of Hildreth (1954) and Dykstra (1983). However, these algorithms are not practical for multi-input problems.

The least squares concave or convex function is piecewise linear consisting of several linear segments. In applications, only a relatively small percentage of the constraints of the related QP are binding and as a result, the number of linear segments is smaller than the number of observations. This result is recently used as the basis for two methods. One of the methods is to preprocess the problem based on the Dantzig’s relaxations method (G. B. Dantzig, Fulkerson, & Johnson, 1959; G. Dantzig, Fulkerson, & Johnson, 1954) and to iteratively eliminate some of the nonbinding constraints (Lee, Johnson, Moreno-Centeno, & Kuosmanen, 2013). Based on the pairwise distance between observations, in every iteration a subset of constraints is selected and then a QP is solve to get the solution of the relaxed problem. The other method is to find acceptable partitions of the input space, and to estimate the linear segments for the partitions (Hannah & Dunson, 2013), which may end up with an approximation of the optimal solution. Both of these methods are iterative algorithms and it is required to implement special codes for using them.

In this paper, a reformulation to the QP problem is proposed. In this method, the constraints, except the signs of the variables, are eliminated and the objective function is penalized by the constraints violations. The final problem is a QP with only sign constraints, and it is solved in a reasonably shorter time than the original problem. To this end, first we convert the original problem into a QP with equality constraints, and categorize the constraints into � blocks of equations. Then the errors are estimated from the first block, and the objective is penalized by the sum of the quadratic values of violations. The dual of the penalized problem is also developed. The dual problem is a separable QP and it is solved significantly faster than the penalized and the original problems. Moreover, a similar approach is used to develop the penalized problem and its dual for estimating variants of shape restricted least squares functions, i.e. the (monotonic) convex and concave least squares.

Since the seminal work of Fiacco and McCormick (1968), the penalty method is well studied in the literature of optimization (e.g. Di Pillo & Grippo, 1989; Hu & Ralph, 2004; Li, Yin, Jiang, & Zhang, 2013). Penalty method is used to solve a wide range of regression problems. For example, Ridge regression (Hoerl & Kennard, 1970) is a penalty method that regularizes coefficients to control their variances. Lasso (Tibshirani, 1996) is a shrinkage and selection method that enhances the outof-sample interpretability of a regression problem. Moreover, various penalty methods are developed to solve constrained optimization problems, such as in bilevel programming problems (Marcotte & Zhu, 1996), options pricing (D’Halluin, Forsyth, & Labahn, 2004), and portfolio optimization (Corazza, Fasano, & Gusso, 2013). To the best of our knowledge, this paper is the first application of penalty method to solve shape restricted least squares.

To compare the efficiency of the penalized problem and its dual, a number of Monte Carlo simulations is used. The results show the superiority of the penalized shape restricted least squares and the dual problem over the conventional formulation in terms of the computational time. The results show that solving the dual problem is the most efficient approach.

The rest of the paper is organized as follows. Section 2 contains the main results of the paper. It starts with a review on the monotonic concave least squares problem. The steps to build the penalty term, the penalized and the dual problems are explained in this section. The optimality of the penalized problem is also discussed. Moreover, the penalization method for estimating a concave function is developed. To simplify the algebraic calculations, this paper uses succinct matrix forms of the problem. The summation form of the dual problem is also presented in this section. The results of the numerical Monte Carlo simulations are presented in Section 3. An empirical application is presented in Section 4, in which the penalized method is used to analyze the room rates of a sample of hotels in Finland. The paper has three appendices. The first appendix presents the detailed analytical computations to obtain the matrix form of the QP. This appendix also includes the steps to compute the reformulated problem. The second appendix contains the proofs of the theorems. Appendix 3 presents the Matlab and R codes for solving the penalized monotonic concave least squares and the dual problem.

## 2. Penalized monotonic concave least squares

Our focus in this paper is on the concave least squares (CLS) problem under monotonicity assumption $( \mathrm { { M C L S } } ) . ^ { 2 }$One of the applications of this problem is to estimate a non-parametric production function that is monotonic and concave (Andor & Hesse, 2014; Cheng, Bjørndal, & Bjørndal, 2014; Eskelinen & Kuosmanen, 2013; Keshvari & Kuosmanen, 2013; Kuosmanen, 2011, 2012; Wang, Wang, Dang, & Ge, 2014).

## 2.1 Monotonic concave least squares (MCLS)

MCLS is a least squares approach to construct a non-parametric multivariate regression model. In this model, a function$f \colon  { \mathbb { R } } ^ { m } \to  { \mathbb { R } }$is estimated as$y _ { i } = f ( \mathbf { x } _ { i } ) + \varepsilon _ { i } ( i = 1 , \dots , n )$, where � is the number of observations,$y _ { i } \in \mathbb { R }$and$\mathbf { x } _ { i } \in \mathbb { R } ^ { m } ( i = 1 , \ldots , n )$are response and explanatory variables, respectively, and$\varepsilon _ { i } ( i = 1 , \ldots , n )$is a random variable with mean 0. Moreover,$f \in \mathbb { F }$, where � is the set of all monotonic concave functions. Hence the problem is:

$$
\begin{array}{r l} & {\underset {\varepsilon , f} {\min} \frac {1}{2} \sum_ {i = 1} ^ {n} \varepsilon_ {i} ^ {2}} \\ & {s. t.} \\ & {y _ {i} = f (\mathbf {x} _ {i}) + \varepsilon_ {i}, i = 1, \ldots , n,} \\ & {f \in \mathbb {F}.} \end{array}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup> MCLS function is also known as convex nonparametric least squares (CNLS).</span></small>

The set � is infinite-dimensional. However, it is shown that a piecewise linear function generates the best fit (Hildreth, 1954; Kuosmanen, 2008), and it is estimated by the following problem

$$
\begin{array}{r l} & {\underset {\pmb {\varepsilon}, \pmb {\alpha}, \pmb {\beta}} {\min} \frac {1}{2} \sum_ {i = 1} ^ {n} \varepsilon_ {i} ^ {2}} \\ & {s. t.} \\ & {y _ {i} = \alpha_ {i} + \mathbf {x} _ {i} \pmb {\beta} _ {i} ^ {\prime} + \varepsilon_ {i}, i = 1, \dots n,} \\ & {\alpha_ {i} + \mathbf {x} _ {i} \pmb {\beta} _ {i} ^ {\prime} \leq \alpha_ {j} + \mathbf {x} _ {i} \pmb {\beta} _ {j} ^ {\prime}, i, j = 1, \dots , n,} \\ & {\pmb {\beta} _ {i} \geq \pmb {0}, i = 1, \dots , n,} \end{array}\tag{1}
$$

where$\mathbf { x } _ { i }$and$\mathbf { \beta } _ { i }$are the �-th rows of � and �, respectively:

$$
\mathbf {X} = \left(x _ {i p}\right) _ {n \times m} = \left( \begin{array}{c c c c} x _ {1 1} & x _ {1 2} & \ldots & x _ {1 m} \\ x _ {2 1} & x _ {2 2} & \ldots & x _ {2 m} \\ & & \ddots & \\ x _ {n 1} & x _ {n 2} & \ldots & x _ {n m} \end{array} \right), \mathbf {B} = \left(\beta_ {i p}\right) _ {n \times m} = \left( \begin{array}{c c c c} \beta_ {1 1} & \beta_ {1 2} & \ldots & \beta_ {1 m} \\ \beta_ {2 1} & \beta_ {2 2} & \ldots & \beta_ {2 m} \\ & & \ddots & \\ \beta_ {n 1} & \beta_ {n 2} & \ldots & \beta_ {n m} \end{array} \right),
$$

In problem (1), the first constraint specifies a hyperplane for every observation, with intercept$\alpha _ { i }$ and slope variable$\mathbf { \beta } _ { i }$. The second and the third constraints enforces concavity and monotonicity, respectively. Problem (1) is a basis to obtain variants of shape restricted least squares. For example, a CLS function can be estimated by problem (1) when the non-negativity constraint is relaxed (see sub-section 2.4). Figure 1 depicts examples of estimated CLS and MCLS functions.<sup>3</sup>

![](images/page_3_chart_5.jpg)

![](images/page_3_chart_6.jpg)

Figure 1. Examples of two-variate shape restricted least squares. Left panel: CLS estimator, right panel: MCLS estimator.

## 2.2 Penalization method

There are$O ( n ^ { 2 } )$constraints in problem (1), and to the best of our knowledge this is the main reason that solving (1) is very time consuming (Hannah & Dunson, 2013; Lee et al., 2013). Our approach to handle the large number of constraints is to eliminate all expect the non-negativities, and to penalize the objective function with constraints’ violations. The penalty method consists of three steps: a) using the equality constraints to eliminate the intercept variables$( \alpha _ { i } ) _ { \cdot }$, b) transforming the remaining constraints into equalities by adding slack variables, c) penalizing the objective function by the quadratic violations of the equality constraints. The reformulated problem is a penalized QP with only non-negativity constraints and it is solved quicker than the original problem (see Section 3). This problem is solved efficiently with off-the-shelf solvers (such as CPLEX and Mosek) and there is no need to develop a customized solver.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup> For the sake of simplicity of the figure, we generated the data over a grid in the inputs space.</span></small>

To start, consider that the intercept variables$\alpha _ { i } ( i = 1 , \ldots , n )$are eliminated by combining$\alpha _ { i } =$ $y _ { i } - \mathbf { x } _ { i } \mathbf { \beta } _ { i } ^ { \prime } - \varepsilon _ { i }$and the second constraint. By adding the slack variables$\pmb { \mathscr { s } } _ { i } = ( \mathscr { s } _ { i 1 } , \dots , \mathscr { s } _ { i n } ) ^ { \prime }$, this problem is written as:

$$
\begin{array}{r l} & {\underset {\pmb {\varepsilon}, \pmb {\beta}, \pmb {s}} {\min} \frac {1}{2} \sum_ {i = 1} ^ {n} \varepsilon_ {i} ^ {2}} \\ & {s. t.} \\ & {y _ {j} - y _ {i} = \varepsilon_ {j} - \varepsilon_ {i} + (\mathbf {x} _ {j} - \mathbf {x} _ {i}) \pmb {\beta} _ {j} ^ {\prime} + s _ {i j}, i, j = 1, \dots , n,} \\ & {s _ {i j} \geq 0, \pmb {\beta} _ {i} \geq \pmb {0}, i = 1, \dots , n.} \end{array}\tag{2}
$$

The algebraic calculations of the penalty term is simplified if the problem is presented in a succinct matrix form. To this end, a vector of variables is defined as:

$$
\pmb {\psi} = (\pmb {\beta} ^ {1}, \pmb {\beta} ^ {2}, \dots , \pmb {\beta} ^ {m}, \mathbf {s} _ {1}, \mathbf {s} _ {2}, \dots , \mathbf {s} _ {\mathrm{n}}) ^ {\prime},
$$

where the slopes and slacks are stacked together to form a vector of size$m n + n ^ { 2 }$. Hereafter the superscript � denotes the �-th column of matrices. Auxiliary matrices$\mathbf { E } _ { i } , \boldsymbol { x } _ { i } .$, and invertible$\mathbf { A } _ { i }$are defined in Appendix 1 in such a way that the second constraint of problem (2) is$( \mathbf { I } - \mathbf { E } _ { i } ) \mathbf { y } = \mathbf { A } _ { i } \pmb { \varepsilon } +$ $\pmb { \mathcal { X } } _ { i } \Psi \left( i = 1 , \ldots , n \right)$, where � is the identity matrix of order �. Thus � is calculated by the following equation for any$i = 1 , \ldots , n$

$$
\pmb {\varepsilon} = - \mathbf {A} _ {i} ^ {- 1} \pmb {\mathcal {X}} _ {i} \pmb {\psi} + \mathbf {A} _ {i} ^ {- 1} (\mathbf {I} - \mathbf {E} _ {i}) \mathbf {y}.\tag{3}
$$

Theorem 1 calculates the objective function by using$i = 1$

Theorem 1.$\begin{array} { r } { \varepsilon ^ { \prime } \varepsilon = \Psi ^ { \prime } \mathcal { X } _ { 1 } ^ { \prime } \texttt A _ { 1 } ^ { - 1 \prime } \texttt A _ { 1 } ^ { - 1 } \mathcal { X } _ { 1 } \Psi - 2 \mathbf { y } ^ { \prime } \left( \mathbf { I } - \frac { 1 } { n } \mathbf { 1 } \right) \texttt A _ { 1 } ^ { - 1 } \mathcal { X } _ { 1 } \Psi + \mathbf { y } ^ { \prime } \left( \mathbf { I } - \frac { 1 } { n } \mathbf { 1 } \right) \mathbf { y } } \end{array}$, where � is a$n \times$ � matrix of ones.

## Proof. See Appendix 2.

In a similar approach, Theorem 2 calculates a penalty term as the sum of the quadratic violations of the constraints of (2).

$$
\begin{array}{r l} & {\mathrm{Theorem2.} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \left(\left(y _ {j} - y _ {i}\right) - \left(\varepsilon_ {j} - \varepsilon_ {i} + \left(\mathbf {x} _ {j} - \mathbf {x} _ {i}\right) \pmb {\beta} _ {j} ^ {\prime} + s _ {i j}\right)\right) ^ {2} =} \\ & {\qquad \qquad \qquad \qquad \qquad \Psi^ {\prime} (\sum_ {i = 2} ^ {n} (\pmb {\mathscr {X}} _ {1} - \mathbf {A} _ {1} \mathbf {A} _ {i} ^ {- 1} \pmb {\mathscr {X}} _ {i}) ^ {\prime} (\pmb {\mathscr {X}} _ {1} - \mathbf {A} _ {1} \mathbf {A} _ {i} ^ {- 1} \pmb {\mathscr {X}} _ {i})) \Psi .} \end{array}
$$

## Proof. See Appendix 2.

Combining the results of theorems, penalized MCLS is defined as:

$$
\begin{array}{l} \min _ {\boldsymbol {\psi}} \frac {1}{2} \boldsymbol {\psi} ^ {\prime} \mathbf {H} \boldsymbol {\psi} + \mathbf {c} \boldsymbol {\psi} \\ s. t. \\ \boldsymbol {\psi} \geq \mathbf {0}, \end{array}\tag{4}
$$

where$\mathbf { H } = \mathbf { Q } + M ^ { 2 } \mathbf { V } .$, � is a large positive number, and there are

$$
\begin{array}{r l} & {\mathbf {Q} = \mathcal {X} _ {1} ^ {\prime} \mathbf {A} _ {1} ^ {- 1 \prime} \mathbf {A} _ {1} ^ {- 1} \mathcal {X} _ {1},} \\ & {\mathbf {V} = \sum_ {i = 2} ^ {n} (\mathcal {X} _ {1} - \mathbf {A} _ {1} \mathbf {A} _ {i} ^ {- 1} \mathcal {X} _ {i}) ^ {\prime} (\mathcal {X} _ {1} - \mathbf {A} _ {1} \mathbf {A} _ {i} ^ {- 1} \mathcal {X} _ {i}),} \\ & {\mathbf {c} = - \mathbf {y} ^ {\prime} \left(\mathbf {I} - \frac {1}{n} \mathbf {1}\right) \mathbf {A} _ {1} ^ {- 1} \mathcal {X} _ {1},} \\ & {\gamma = \mathbf {y} ^ {\prime} \left(\mathbf {I} - \frac {1}{n} \mathbf {1}\right) \mathbf {y}.} \end{array}
$$

The objective of problem (4) is not the sum of squared errors (SSR) of the original problem. SSR is computed by Theorem 1, or simply by the following equation:

$$
\sum_ {i = 1} ^ {n} \hat {\varepsilon} _ {i} ^ {2} = \pmb {\psi} ^ {* \prime} \pmb {\mathbf {Q}} \pmb {\psi} ^ {*} + 2 \pmb {\mathbf {c}} \pmb {\psi} ^ {*} + \gamma ,\tag{5}
$$

where �̂ is the error and$\Psi ^ { * }$is the optimal solution to (4).

The solution to (4) converges to the optimal solution of (2) when � increases to infinity. The conventional algorithm for choosing a sufficiently large � is to start by an initial value and iteratively increasing it until the convergence is satisfactory. This result is shown in Theorem 3 below. In applications, the magnitude of penalty should depend on the magnitude of the problem data. We may use a large enough � such that$\boldsymbol { \Psi } ^ { * \prime } \boldsymbol { \mathbf { V } } \boldsymbol { \Psi } ^ { * }$be as close as possible to zero.

Theorem 3. The following properties hold:

a) Problem (4) has an optimal solution for any given$M \geq 0$

b) Let$\Psi ^ { * }$and$\Psi ^ { * } ( M )$be the optimal solutions to problems (2) and (4), respectively. Then $\Psi ^ { * } ( M ) \to \Psi ^ { * } \operatorname { a s } M \to \infty$

Proof. See Appendix 2.

As it is shown in Theorem 3, optimal solution to (4) is convergent to the optimal solution to (2), and theoretically, a very large � does not cause an issue in the convergence. However, a very large value of M may cause numerical instability, which is mainly due to rounding errors. In practice, the value of the penalty term in (4) tends to zero if a very big � is used, and thus the solution to (4) is in a tight neighborhood of feasible region of (2). The behavior of big � and a rule for choosing a proper � are explained in Appendix 2.

Penalized MCLS (4) is a non-negative unconstrained QP, which is solved by available QP solvers. Matrices �, �, and vector � are sparse and readily computable. A number of simplifications for the calculations are discussed in Appendix 1.

## 2.3 Dual of penalized MCLS

The matrices in the dual of problem (4) are less dense, and this sensibly reduces the solution time. It is straightforward to obtain the Lagrangian dual of penalized MCLS as follows (see Appendix 2):

$$
\begin{array}{l} \min \frac {1}{2} \mathbf {w} ^ {\prime} \mathbf {w} \\ s. t. \\ \mathbf {F} ^ {\prime} \mathbf {w} + \mathbf {c} ^ {\prime} \geq \mathbf {0}, \end{array}\tag{6}
$$

where � is a$n ^ { 2 } .$-vector of dual variables. There is$\mathbf { H } = \mathbf { F ^ { \prime } } \mathbf { F }$and$\mathbf { F } = \left( \mathbf { A } _ { 1 } ^ { - 1 } \pmb { \mathcal { X } } _ { 1 } , \mathbf { \Delta } M ( \pmb { \mathcal { X } } _ { 2 } - \mathbf { A } _ { 2 } \mathbf { A } _ { 1 } ^ { - 1 } \pmb { \mathcal { X } } _ { 1 } ) \right.$ $M ( { \pmb X } _ { n } - { \pmb A } _ { n } { \pmb A } _ { 1 } ^ { - 1 } { \pmb X } _ { 1 } ) \big )$. The estimated error term is computed by${ \widehat { \pmb { \varepsilon } } } = - \mathbf { W } ^ { * } + \left( \mathbf { I } - { \frac { 1 } { n } } \mathbf { 1 } \right) \mathbf { y }$, where $\mathbf { w } ^ { * }$is the optimal solution to (6).

There are several advantages to use (6). This problem is separable and matrix � is sparse, hence it is expected to be solved faster than problem (4) (Vanderbei, 2001, sec. 23). The experimental results in Section 3 show the superior performance of problem (6). Moreover, building problem (4) starts by making � and then computing$\mathbf { F ^ { \prime } } \mathbf { F }$to form �. By avoiding this matrix multiplication, fewer computations are needed and one source of numerical errors is removed. Another advantage is that matrix � is less dense than matrix � and hence, the memory usage decreases.

Problem (6) can directly be used in Matlab and R in its current matrix form. However, mathematical programming software, such as GAMS, AIMMS and AMPL, use the summation forms. To be able to use such software we present the summation form of problem (6) below. The performance of the solver does not depend on the programming language or the format of the problem. In practice, the solution time of problem (6) and its summation form (problem 7) with the same solver are the same.<sup>4</sup> The error is estimated by$\hat { \varepsilon } _ { i } = y _ { i } - \bar { y } - w _ { 1 i } / \sqrt { 2 }$, where �̅ is the average of response variables.

$$
\begin{array}{r l} & {\min \frac {1}{2} \sum_ {i, j = 1} ^ {n} w _ {i j} ^ {2}} \\ & {s. t. \qquad \qquad \qquad \qquad (7)} \\ & {\sum_ {i \geq 2} \big (x _ {1 p} - x _ {i p} \big) \sum_ {j \geq 2} w _ {i j} \geq 0, p = 1, \dots , m,} \\ & {\frac {\sqrt {2}}{n} \big (x _ {1 p} - x _ {i p} \big) \big (\sum_ {j} w _ {1 j} - n w _ {1 i} \big) - M \sum_ {j \geq 2} \big (x _ {1 p} - x _ {j p} \big) w _ {j i} + 2 (y _ {i} - \bar {y}) \big (x _ {1 p} - x _ {i p} \big) \geq} \\ & {0, p = 1, \dots , m, i = 2, \dots , n,} \\ & {\frac {\sqrt {2}}{n} \sum_ {i} w _ {1 i} + M \sum_ {i \geq 2} w _ {i 1} \geq 0,} \\ & {- \frac {\sqrt {2}}{n} \big (\sum_ {j} w _ {1 j} + n w _ {1 i} \big) + M \sum_ {j \geq 2} w _ {j i} - 2 (y _ {i} - \bar {y}) \geq 0, i = 2, \dots , n,} \\ & {\sum_ {j \geq 2} w _ {i j} \geq 0, i = 2, \dots , n,} \\ & {w _ {i j} \leq 0, i, j = 2, \dots , n, i \neq j,} \\ & {w _ {i 1} \leq 0, i = 2, \dots , n.} \end{array}
$$

In order to increase the speed of the problem, the relaxation method proposed by Lee et al. (2013) can be combined with the reformulated problem proposed in this paper. Using this method<sup>5</sup>, the second constraint of problem (1) is relaxed for some pairs of$( i , j )$. Let � be the set of pairs$( i , j )$of the seconds constraint of problem (1), which is determined in an iteration of the method of Lee et al. (2013). Let$K _ { I } = \{ k \colon k > n m$and$k \neq ( n m + ( i - 1 ) n + j )$and$( i , j ) \in I \}$as a subset of $\{ 1 , \dots , n m + n ^ { 2 } \}$. The QP of Lee et al. (2013) can be replaced by problem (4) when$\psi _ { k } = 0 , k \in K _ { I }$ Similarly, problem (6) can be used by removing row$k \in K _ { I }$of$\mathbf { F } ^ { \prime } \mathbf { w } + \mathbf { c } ^ { \prime } \geq \mathbf { 0 }$

## 2.4 Variants of shape restricted least squares

A concave function is estimated by problem (1) if slope variables are free of sign, i.e. by removing $\pmb { \beta } _ { i } \geq 0 \ ( i = 1 , \ldots , n )$. Furthermore, if the direction of inequalities is reversed, this problem estimates a convex least squares function. The reformulated problem (problem 4) and its dual (problem 6) can be easily adapted to solve different variants of the shape restricted least squares.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup> The generation times of the problems may differ, and they are depended to the programming language.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup> Method of Lee et al. (2013) is implemented in Ray, Kumbhakar, & Dua (2015).</span></small>

In this sub-section, problems (4) and (6) are adapted for estimating a CLS function. The difference between CLS and MCLS is that the regression hyperplanes of CLS, which are defined by the first constraint of problem (1), are free of sign. This is shown by$\Psi _ { i } \geq \mathbf { 0 } ~ ( i > m n )$in penalized CLS problem as follows:

$$
\begin{array}{l} \min \frac {1}{2} \pmb {\psi} ^ {\prime} \pmb {H} \pmb {\psi} + \mathbf {c} \pmb {\psi} \\ s. t. \\ \pmb {\psi} _ {i} \geq 0, j > m n, \end{array}
$$

where � and � are the same as in problem (4). The dual of penalized CLS is also developed similarly:

$$
\begin{array}{l} \min \frac {1}{2} \mathbf {w} ^ {\prime} \mathbf {w} \\ s. t. \\ \mathbf {F} ^ {\prime} \mathbf {w} + \mathbf {c} ^ {\prime} = \boldsymbol {\mu}, \\ \boldsymbol {\mu} _ {j} \geq 0, j > m n. \end{array}\tag{8}
$$

Adapting problems (4) and (6) to solve a convex problem is straightforward and it is done by reversing the signs of the slack variables of problem (1).

## 3. Experimental results

In this section, an experiment is designed to analyze the computational performance of (1), (4), and (6). The aim is to benchmark the penalization method (problems 4 and 6) against the original problem. The problems are solved on a laptop computer running Windows with an Intel Core i5 CPU 2.6 GHz and 8 gigabytes of RAM. The methods are implemented in Matlab, and Mosek 7 solves the QP problems. The measure of performance in this experiment is the average mean squared error (AMSE):

$$
A M S E ^ {\omega} = \frac {1}{T} \sum_ {t = 1} ^ {T} \sqrt {\frac {S S R _ {t} ^ {\omega}}{n}}, S S R _ {t} ^ {\omega} = \sum_ {i = 1} ^ {N} (y _ {i} - y _ {i} ^ {\omega}) ^ {2},
$$

where � is the number of simulations, � is the number of observations, and$\omega \in$ {MCLS, PMCLS, dual of PMCLS} where

MCLS: Problem (1), the original formulation of monotonic concave least squares,

PMCLS: Penalized MCLS, problem (4),

Dual of PMCLS: Dual of penalized MCLS, problem (6).

A measure for the goodness of fit of (1) is the coefficient of determination,$R ^ { 2 }$, which is one minus the ratio of SSR to the total sum of squares:$\begin{array} { r } { S S T = \sum _ { i = 1 } ^ { n } ( y _ { i } - \bar { y } ) ^ { 2 } } \end{array}$, where �̅ is the mean value of �. Let$R _ { 4 } ^ { 2 }$be the coefficient of determination that is computed from the optimal solution to problem (4), and$\rho = 1 - ( \Psi ^ { \ast \prime } \mathbf { H } \Psi ^ { \ast } + 2 \mathbf { c } \Psi ^ { \ast } + \gamma ) / S S T$. In case of no violation, there is$R ^ { 2 } = R _ { 4 } ^ { 2 } = \rho$. Since problem (2) allows for violations,$R _ { 4 } ^ { 2 }$is an upper bound for$R ^ { 2 } ~ ( R ^ { 2 } \leq R _ { 4 } ^ { 2 } )$. In case there are some violations,$R _ { 4 } ^ { 2 } = \rho + M ^ { 2 } R _ { a u g } ^ { 2 }$where$R _ { a u g } ^ { 2 } = \Psi ^ { * \prime } \mathbf { V } \Psi ^ { * } / S S T$. If$R _ { a u g } ^ { 2 }  0$then$\rho \to R ^ { 2 } . \ : R _ { a u g } ^ { 2 }$is the amount by which$R ^ { 2 }$is augmented when some violations exist. It is unit free (like$R ^ { 2 } )$and it is used to measure the accuracy of (4) and (6). It is computed even if the solution to problem (1) is not calculated.$R _ { a u g } ^ { 2 }$is desired to be close to zero.

Similar to Lee et al. (2012), data is generated from the function$y = \Pi _ { r = 1 } ^ { m } x _ { r } ^ { 0 . 5 / m } + \varepsilon$, where inputs are drawn from a uniform distribution in the interval [10,100]. The error term is generated from a normal distribution with mean zero and standard deviation of 10. There are totally 98 scenarios, with different number of observations from 50 to 700, and different number of inputs from 2 to 8. Each scenario is simulated 20 times to compute the average solution time. Figure 1 compares the solution times for solving the problems with four inputs using three formulations presented in this paper.

![](images/page_8_chart_2.jpg)

Figure 2. Comparison of solution times for the scenario with four inputs. MCLS cannot be solved for problems with more than 150 observations via (1).

As Figure 2 depicts, a problem with 4 inputs and more than 100 observations cannot be solved via (1), while it is solved in a relatively short time via (4) and (6). For example, a problem with 700 observations is solved in around four minutes via (4) and in around eleven minutes via (6). The solution times are presented in Table 1. Both (4) and (6) solve larger problems in a manageable time. As we expected from the discussion in sub-section 2.4, the dual problem is solved significantly faster.

Table 1. The solution times in seconds for dual of PMCLS (D. PMCLS), PMCLS and MCLS. The standard deviations are in parenthesis. Maximum running time of solver is one hour.

<table><tr><td>Inputs</td><td colspan="3">2</td><td colspan="3">3</td><td colspan="3">4</td><td colspan="3">5</td><td colspan="3">6</td><td colspan="3">7</td><td colspan="3">8</td></tr><tr><td>Obs.</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td></tr><tr><td>50</td><td>0.1(0)</td><td>0.3(0.1)</td><td>9.1(1.6)</td><td>0.2(0.1)</td><td>0.5(0.3)</td><td>9.2(1.6)</td><td>0.5(0.2)</td><td>0.7(0.4)</td><td>9.4(0.6)</td><td>0.5(0.3)</td><td>0.8(0.4)</td><td>10.5(2.6)</td><td>0.6(0.2)</td><td>0.9(0.4)</td><td>11.0(3.5)</td><td>0.6(0.3)</td><td>1.2(0.4)</td><td>13.2(2.9)</td><td>0.6(0.2)</td><td>1.3(0.2)</td><td>15.0(2.7)</td></tr><tr><td>100</td><td>0.7(0.1)</td><td>1.1(0.1)</td><td>1.6(0.5)</td><td>0.7(0.2)</td><td>1.4(0.6)</td><td>704.4(45.4)</td><td>0.9(0.4)</td><td>2.2(1.1)</td><td>707.9(49)</td><td>1.0(0.7)</td><td>3.0(1.6)</td><td>958.8(66.7)</td><td>1.1(0.5)</td><td>3.1(0.8)</td><td>1163.0(94.9)</td><td>1.1(0.5)</td><td>4.4(1.6)</td><td></td><td>1.5(0.6)</td><td>6.1(1.5)</td><td></td></tr><tr><td>150</td><td>1.5(0.3)</td><td>2.8(0.7)</td><td>3.0(0.7)</td><td>1.6(0.9)</td><td>3.9(1)</td><td>1928.4(96.4)</td><td>2.0(0.5)</td><td>8.0(2.5)</td><td>2245.6(113.4)</td><td>3.9(1.8)</td><td>9.0(3)</td><td></td><td>4.0(1.4)</td><td>11.9(2.8)</td><td></td><td>5.4(2.5)</td><td>14.1(2.8)</td><td></td><td>5.7(1.2)</td><td>18.8(2.7)</td><td></td></tr><tr><td>200</td><td>2.3(1.1)</td><td>7.4(1.5)</td><td>8.2(0.9)</td><td>2.9(1.3)</td><td>11.7(1.7)</td><td>3532.5(187.6)</td><td>4.4(0.8)</td><td>15.4(2.2)</td><td></td><td>5.1(1.8)</td><td>16.1(3.4)</td><td></td><td>8.4(3.1)</td><td>26.8(5.1)</td><td></td><td>8.9(2.2)</td><td>33.1(3.8)</td><td></td><td>10.5(3.4)</td><td>48.6(5.4)</td><td></td></tr><tr><td>250</td><td>4.3(1.1)</td><td>15.2(3.4)</td><td>21.1(6.7)</td><td>5.4(2.1)</td><td>23.3(2.1)</td><td></td><td>8.9(1.2)</td><td>28.5(7.9)</td><td></td><td>12.8(2.8)</td><td>39.2(7.2)</td><td></td><td>13.8(8)</td><td>52.9(8.4)</td><td></td><td>15.7(5.1)</td><td>65.5(4.6)</td><td></td><td>17.4(4.1)</td><td>98.2(8.3)</td><td></td></tr><tr><td>300</td><td>9.2(2.5)</td><td>25.1(5.8)</td><td>32.5(6.9)</td><td>10.5(1.7)</td><td>36.0(9.5)</td><td></td><td>14.8(3.1)</td><td>52.0(4.9)</td><td></td><td>15.6(4.7)</td><td>57.6(9.3)</td><td></td><td>21.0(3)</td><td>91.2(10.9)</td><td></td><td>29.7(7.4)</td><td>141.5(14.1)</td><td></td><td>29.8(9.8)</td><td>202.3(15.5)</td><td></td></tr><tr><td>350</td><td>16.2(3.1)</td><td>39.9(6.4)</td><td>55.1(1.1)</td><td>19.1(5.2)</td><td>53.9(13.7)</td><td></td><td>20.8(3)</td><td>67.3(5.5)</td><td></td><td>30.0(11.3)</td><td>107.9(18.5)</td><td></td><td>44.5(14.7)</td><td>175.9(5.9)</td><td></td><td>56.9(14.9)</td><td>210.5(10.9)</td><td></td><td>56.4(13.8)</td><td>293.6(15.6)</td><td></td></tr><tr><td>400</td><td>23.5(3.7)</td><td>54.6(5.6)</td><td>94.5(8.5)</td><td>31.2(3.1)</td><td>96.8(12.2)</td><td></td><td>33.0(5.2)</td><td>119.7(31.7)</td><td></td><td>48.1(6.1)</td><td>182.4(19)</td><td></td><td>65.5(20.5)</td><td>257.3(28.5)</td><td></td><td>77.9(23.8)</td><td>353.9(41.5)</td><td></td><td>104.7(26.9)</td><td>472.7(33.7)</td><td></td></tr><tr><td>450</td><td>32.8(4.8)</td><td>90.1(11.9)</td><td>157.9(8.9)</td><td>48.1(4.4)</td><td>134.1(10.3)</td><td></td><td>56.5(7.9)</td><td>172.2(25)</td><td></td><td>64.8(9.5)</td><td>277.8(26.2)</td><td></td><td>83.2(8)</td><td>356.9(31.3)</td><td></td><td>83.2(0.8)</td><td>464.8(38.9)</td><td></td><td>120.3(28.5)</td><td>678.8(83)</td><td></td></tr><tr><td>500</td><td>49.1(5.4)</td><td>141.1(13.2)</td><td>251.6(17.2)</td><td>60.0(7.8)</td><td>206.9(33.2)</td><td></td><td>75.3(11.8)</td><td>238.3(19.2)</td><td></td><td>105.2(14.1)</td><td>339.0(47.8)</td><td></td><td>120.9(14)</td><td>466.4(26.2)</td><td></td><td>139.7(16.5)</td><td>684.9(50.9)</td><td></td><td>179.9(67.8)</td><td>781.6(3.3)</td><td></td></tr><tr><td>550</td><td>75.8(4)</td><td>203.8(31.6)</td><td>365.4(20.6)</td><td>81.1(11.1)</td><td>270.2(41.9)</td><td></td><td>109.7(13.2)</td><td>343.6(19.4)</td><td></td><td>132.4(11.2)</td><td>502.2(66.7)</td><td></td><td>195.0(62.9)</td><td>626.2(55.6)</td><td></td><td>194.4(13.8)</td><td>949.8(83.7)</td><td></td><td>256.4(87.4)</td><td>981.4(125.4)</td><td></td></tr><tr><td>600</td><td>88.3(22.8)</td><td>244.8(30)</td><td>479.6(39.9)</td><td>122.6(13.6)</td><td>338.9(10.7)</td><td></td><td>154.2(23.9)</td><td>450.7(74.5)</td><td></td><td>183.4(52.2)</td><td>627.3(50)</td><td></td><td>244.8(7.9)</td><td>1021.5(96.9)</td><td></td><td>330.0(97.5)</td><td>1114.1(96.4)</td><td></td><td>422.2(147.6)</td><td>1629.0(217.9)</td><td></td></tr><tr><td>650</td><td>123.7(25.4)</td><td>341.4(46.3)</td><td>665.8(28.4)</td><td>143.3(16.4)</td><td>466.1(13)</td><td></td><td>187.0(39.5)</td><td>550.1(66.1)</td><td></td><td>226.4(12.8)</td><td>727.7(22.2)</td><td></td><td>339.1(93.9)</td><td>1132.4(43.3)</td><td></td><td>447.5(87.2)</td><td>1372.9(373.3)</td><td></td><td>485.1(99.6)</td><td>1990.8(290.6)</td><td></td></tr><tr><td>700</td><td>144.2(12.1)</td><td>402.0(38.3)</td><td>867.0(51.1)</td><td>220.6(12.9)</td><td>550.9(25.9)</td><td></td><td>245.7(22.4)</td><td>650.5(94.6)</td><td></td><td>316.9(42.6)</td><td>948.2(91.9)</td><td></td><td>412.2(45.9)</td><td>1368.0(85.4)</td><td></td><td>571.1(41.4)</td><td>1586.6(677)</td><td></td><td>629.1(10.6)</td><td>2757.3(323.8)</td><td></td></tr></table>

The accuracy of the solutions is assessed by the AMSE statistic and$R _ { a u g } ^ { 2 }$on Table 2. The results indicate that the methods have similar performances, while dual of PMCLS performs slightly better. The value of$R _ { a u g } ^ { 2 }$for the dual of PMCLS and PMCLS in all scenarios is less than$1 0 ^ { - 7 }$. Therefore, PMCLS and its dual obtain the optimal solution to MCLS in a reasonably shorter time. The dual problem is solved significantly faster than PMCLS, and its performance with regard to the AMSE statistic is slightly better, therefore the dual of PMCLS is the preferred formulation for solving a monotonic concave least squares problem.

Table 2. AMSE of the three formulations. The value of$R _ { a u g } ^ { 2 }$for D.PMCLS and PMCLS in all scenarios is less than$\pmb { 1 0 } ^ { - 7 }$

<table><tr><td>Inputs</td><td colspan="3">2</td><td colspan="3">3</td><td colspan="3">4</td><td colspan="3">5</td><td colspan="3">6</td><td colspan="3">7</td><td colspan="3">8</td></tr><tr><td>Obs.</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td><td>D. PMCLS</td><td>PMCLS</td><td>MCLS</td></tr><tr><td>50</td><td>8.78</td><td>8.79</td><td>8.79</td><td>7.68</td><td>7.71</td><td>7.72</td><td>7.19</td><td>7.19</td><td>7.19</td><td>6.18</td><td>6.23</td><td>6.23</td><td>6.19</td><td>6.21</td><td>6.22</td><td>5.95</td><td>6.00</td><td>6.00</td><td>7.27</td><td>7.30</td><td>7.30</td></tr><tr><td>100</td><td>9.55</td><td>9.55</td><td>9.62</td><td>8.44</td><td>8.45</td><td>8.45</td><td>8.31</td><td>8.31</td><td>8.31</td><td>7.22</td><td>7.22</td><td>7.23</td><td>7.08</td><td>7.12</td><td>7.14</td><td>7.58</td><td>7.60</td><td></td><td>6.82</td><td>6.83</td><td></td></tr><tr><td>150</td><td>9.99</td><td>9.99</td><td>9.99</td><td>8.60</td><td>8.60</td><td>8.60</td><td>8.69</td><td>8.69</td><td>8.70</td><td>7.48</td><td>7.49</td><td></td><td>7.87</td><td>7.90</td><td></td><td>7.88</td><td>7.92</td><td></td><td>7.27</td><td>7.31</td><td></td></tr><tr><td>200</td><td>9.47</td><td>9.48</td><td>9.48</td><td>9.20</td><td>9.20</td><td>9.20</td><td>8.70</td><td>8.71</td><td></td><td>8.25</td><td>8.26</td><td></td><td>7.81</td><td>7.83</td><td></td><td>8.01</td><td>8.06</td><td></td><td>7.94</td><td>7.96</td><td></td></tr><tr><td>250</td><td>9.42</td><td>9.43</td><td>9.43</td><td>9.03</td><td>9.03</td><td></td><td>8.99</td><td>9.00</td><td></td><td>8.43</td><td>8.47</td><td></td><td>8.24</td><td>8.27</td><td></td><td>8.43</td><td>8.44</td><td></td><td>7.72</td><td>7.74</td><td></td></tr><tr><td>300</td><td>9.38</td><td>9.39</td><td>9.39</td><td>9.72</td><td>9.73</td><td></td><td>8.97</td><td>8.97</td><td></td><td>8.51</td><td>8.52</td><td></td><td>8.36</td><td>8.39</td><td></td><td>8.58</td><td>8.61</td><td></td><td>8.73</td><td>8.76</td><td></td></tr><tr><td>350</td><td>9.79</td><td>9.80</td><td>9.80</td><td>9.59</td><td>9.61</td><td></td><td>9.15</td><td>9.16</td><td></td><td>8.71</td><td>8.74</td><td></td><td>8.86</td><td>8.88</td><td></td><td>8.87</td><td>8.89</td><td></td><td>8.30</td><td>8.33</td><td></td></tr><tr><td>400</td><td>9.35</td><td>9.37</td><td>9.36</td><td>9.47</td><td>9.48</td><td></td><td>9.41</td><td>9.42</td><td></td><td>9.07</td><td>9.10</td><td></td><td>8.91</td><td>8.95</td><td></td><td>8.60</td><td>8.63</td><td></td><td>8.17</td><td>8.23</td><td></td></tr><tr><td>450</td><td>9.81</td><td>9.83</td><td>9.82</td><td>9.45</td><td>9.46</td><td></td><td>9.17</td><td>9.19</td><td></td><td>8.78</td><td>8.80</td><td></td><td>8.94</td><td>8.97</td><td></td><td>8.75</td><td>8.76</td><td></td><td>8.46</td><td>8.49</td><td></td></tr><tr><td>500</td><td>9.51</td><td>9.52</td><td>9.52</td><td>9.62</td><td>9.62</td><td></td><td>9.30</td><td>9.32</td><td></td><td>8.99</td><td>9.01</td><td></td><td>8.47</td><td>8.49</td><td></td><td>8.61</td><td>8.64</td><td></td><td>8.76</td><td>8.77</td><td></td></tr><tr><td>550</td><td>9.98</td><td>9.99</td><td>9.99</td><td>9.43</td><td>9.44</td><td></td><td>9.28</td><td>9.29</td><td></td><td>8.72</td><td>8.76</td><td></td><td>9.03</td><td>9.05</td><td></td><td>8.76</td><td>8.81</td><td></td><td>8.76</td><td>8.78</td><td></td></tr><tr><td>600</td><td>10.06</td><td>10.07</td><td>10.07</td><td>9.78</td><td>9.80</td><td></td><td>9.39</td><td>9.41</td><td></td><td>9.16</td><td>9.17</td><td></td><td>9.02</td><td>9.05</td><td></td><td>8.77</td><td>8.81</td><td></td><td>8.85</td><td>8.89</td><td></td></tr><tr><td>650</td><td>9.84</td><td>9.85</td><td>9.84</td><td>9.68</td><td>9.69</td><td></td><td>9.48</td><td>9.50</td><td></td><td>9.02</td><td>9.05</td><td></td><td>9.14</td><td>9.17</td><td></td><td>8.85</td><td>8.89</td><td></td><td>8.81</td><td>8.87</td><td></td></tr><tr><td>700</td><td>9.77</td><td>9.77</td><td>9.77</td><td>9.45</td><td>9.47</td><td></td><td>9.20</td><td>9.23</td><td></td><td>9.01</td><td>9.04</td><td></td><td>8.94</td><td>8.98</td><td></td><td>8.96</td><td>9.07</td><td></td><td>9.96</td><td>10.00</td><td></td></tr></table>

Combining the results of the experiment together, we conclude that PMCLS and its dual are computationally more efficient than the original formulation of the problem, and the dual of PMCLS has the best performance in running times.

Furthermore, the performance of the methods is tested on large problems by simulating scenarios with thousands of observations. The starting number of observations is 1000 with increment of 500, and the maximum running time is five hours for every simulation. Every scenario is simulated 5 times. The results are reported in Table 3. The largest problem that is solved via problem (6) has 2500 observations. The average solution time of the dual of PMCLS for problems with 2500 observations is around 187 minutes. The largest problem that problem (4) solved has 2000 observation and the average solution time is 264 minutes. The maximum$R _ { a u g } ^ { 2 }$in all scenarios is$1 0 ^ { - 4 }$. The original formulation (problem 1) cannot solve any of the large problems in the time limit.

Table 3. The solution times in seconds for problems with more than 1000 observations.

|  | D. PMCLS | PMCLS | MCLS |
| --- | --- | --- | --- |
| 1000 | 914(143) | 2204(301) | - |
| 1500 | 2966(423) | 8284(792) | - |
| 2000 | 7258(1226) | 15856(1785) | - |
| 2500 | 11259(1988) | - | - |

By using penalized MCLS and its dual multivariate concave and convex least squares functions can be estimated for problems with several thousands of observations. As we discussed in the introduction section, the computation time is one of the major difficulties in using shape restricted least squares, which can be effectively eliminated by using problems (4) and (6).

## 4. Empirical study

The computation advantages of problem (6) over problem (1) is used in this section to analyze the room rates of a sample of hotels. The data consists of the average room rates and 12 hotel attributes of 126 hotels with minimum star rating of 2 in Finland. The data set is collected from Expedia.com in January 2016. The conventional approach to explain the price based on the attributes of the hotel is to use the hedonic pricing analysis (see for example Chen & Rothschild, 2010; Espinet, Saez, Coenders, & Fluvia, 2003; Rigall-I-Torrent & Fluvià, 2011; Semere, 2014; Thrane, 2007). In this section, we first show that a monotonic concave function generates a better fit than a linear function. This is not however a surprise because set ℱ includes linear functions and a linear hedonic function is a restricted case of a piecewise linear function. Secondly, we estimate an efficient frontier that shows the maximum of room rate for every hotel if their pricing strategy is efficient in comparison with the hotels in the sample. Hotel attributes are explained in Table 4. The selection of attributes is based on similar researches.

Table 4. Descriptions of attributes for the hotels in the sample (� = ���).

| Attribute | Description | Mean | Std. Dev. |
| --- | --- | --- | --- |
| Average rate | Average room rate, logged | 5.14 | 0.38 |
| Rooms | Number of rooms | 162.33 | 96.24 |
| Stars | Star rating of hotel | 3.64 | 0.64 |
| Distance | Distance to central railway station (KM) | 2.53 | 3.69 |
| Chain | Hotel is associated with a chain (binary) | 0.75 | 0.44 |
| Breakfast | Free breakfast is included (binary) | 0.56 | 0.5 |
| Business | Business facilities, such as meeting rooms, are available (binary) | 0.65 | 0.48 |
| Fitness | Fitness facilities is present at hotel (binary) | 0.66 | 0.48 |
| Parking | Free parking is included (binary) | 0.21 | 0.41 |
| Hair dryer | Hair dryer is present at hotel (binary) | 0.75 | 0.44 |
| Pool | Pool is present at hotel (binary) | 0.45 | 0.5 |
| Sauna | Sauna is present at hotel (binary) | 0.82 | 0.39 |
| Spa | Spa is present as hotel (binary) | 0.87 | 0.34 |

Let$\mathbf { R } _ { i }$be a � vector of attributes of hotel$i , p ( { \bf R } _ { i } )$be the room rate, and$y _ { i }$be the logarithm of the average room rate. The natural logarithm of the average room rates are used to maintain a more nearly linear function (Gelman & Hill, 2007). Thus$y _ { i } = p ( \mathbf { R } _ { i } ) + \varepsilon _ { i }$where$\varepsilon _ { i }$is an error term. While the dual of PMCLS (problem 6) obtains the optimal solution in around 2 seconds, problem (1) cannot be solved for this sample of hotels within a one-hour limit$( n = 1 2 6 , m = 1 2 )$

The linear hedonic function is also estimated and the$R ^ { 2 }$coefficients of both models are reported in Table 5. As it is shown, the estimated monotonic concave function generates a better fit. The$R ^ { 2 }$ of MCLS is 66% which is 1.8 times of$R ^ { 2 }$of a linear function. Therefore, it is concluded that a monotonic piecewise linear function explains more of the variations of the room rates. However, problem (1) cannot be practically used to estimate such a piecewise linear function due to the lack of memory in the computer and to the lengthy solution times.

Table 5. The coefficients of determination of the estimated linear and monotonic piecewise linear functions

| Function | Linear | Monotonic piecewise linear |
| --- | --- | --- |
| $R^{2}$ | 36% | 66% |

Let$\hat { p } ( \mathbf { R } _ { i } )$be the estimated price for hotel � via problem (6). The variation of$y _ { i }$from$\hat { p } (  { \mathbf { R } } _ { i } )$may be either due to the performance of the pricing strategy of the hotel or it may be because of a random noise. The method of StoNED provides a basis to estimate the performance of the pricing strategy of the hotel. This method is well studied in several publications, for example see Keshvari and Kuosmanen, (2013) and Kuosmanen and Kortelainen (2012). By using StoNED, the error term (�) is decomposed into a noise part (�) and an asymmetric inefficiency part$( u > 0 )$such that$\varepsilon _ { i } = u _ { i } -$ $v _ { i }$. The inefficiency term$u _ { i }$is assumed to be half-normally distributed with the variance$\sigma _ { u } ^ { 2 }$, and the noise term$v _ { i }$is assumed to be normally distributed with the zero mean and the variance$\sigma _ { v } ^ { 2 }$. By using the method of moments the standard deviation of the inefficiency term is estimated as$\hat { \sigma } _ { u } =$ $\sqrt [ 3 ] { \widehat { M } _ { 3 } / \left[ \sqrt { 2 / \pi } \left( 4 / \pi - 1 \right) \right] }$where$\textstyle { \widehat { M } } _ { 3 } = \sum _ { i = 1 } ^ { n } \varepsilon _ { i } ^ { 3 } / n$is the estimated third central moment of �. The expected room rate in then estimated by$\hat { y } _ { i } = \hat { p } ( \mathbf { R } _ { i } ) + \hat { \sigma } _ { u } \sqrt { 2 / \pi }$. The difference between the room rate and the estimated room rate via StoNED shows the amount by which the hotel can adjust the room rate to be efficient in the sample.

Figure 3 shows histogram of the estimated adjustments of room rate, i.e.$y _ { i } - \hat { y } _ { i }$. According to this figure, 45 hotels have a negative adjustment value, which means that based on this sample of hotels, there are some potentials for them to increase their room rate. Most of these hotels (34) may increase the prices by up to 50 euros, and two of the hotels have the adjustment value of 150 euros. On the other hand, there are 14 hotels with a positive adjustment value. It is suggested that 9 hotels decrease the prices by up to 50 euros and there are also some hotels that may decrease their room rates by up to 250 or 300 euros. This analysis of the room rate is based on the frontier analysis and further research is required to investigate and analyze the drivers of the room rates of the hotels in the sample. However, as Table 5 shows, this method gives a better fit than a traditional hedonic pricing analysis which is currently the main method for explaining the relations between the room rate and hotel attributes.

![](images/page_13_chart_0.jpg)

Figure 3. Histogram of the room rates and the estimated room rates.

## 5. Conclusions

In this paper, we proposed an alternative formulation for concave and convex regression via least squares. Despite the interesting properties and wide range of applications of such estimators, solving the problem is very time consuming. One major source of complexity is the number of constraints in the QP problems. In our proposal, we reformulate the problem as a non-negative unconstrained QP. This problem can be solved by using available QP solvers. The numerical tests show that our penalized monotonic concave regression and its dual perform significantly better than the original problem. To analyze the pricing strategies of a sample of 126 hotels in Finland, we estimate a piecewise linear concave function. While this problem cannot be solved via the original formulation of MCLS in one hour, it is solved in around two seconds via the dual of PMCLS. The results show that MCLS is a better fit than a linear function. The Matlab and R codes for solving the reformulated problems are also provided in this paper.

## Acknowledgements

The author would like to thank Professor Timo Kuosmanen (Aalto University) and Professor Andrew L. Johnson (Texas A&M University) for the helpful discussions and comments.

## References

Aït-Sahalia, Y., & Duarte, J. (2003). Nonparametric option pricing under shape restrictions. Journal of Econometrics (Vol. 116).

Andor, M., & Hesse, F. (2014). The StoNED age: The departure into a new era of efficiency analysis? A monte carlo comparison of StoNED and the “oldies” (SFA and DEA). Journal of Productivity Analysis, 41, 85–109.

Badinelli, R. D. (1986). Optimal safety stock investment through subjective evaluation of stockout costs. Decision Sciences, 17(3), 312–328.

Birke, M., & Dette, H. (2007). Estimating a convex function in nonparametric regression. Scandinavian Journal of Statistics, 34, 384–404.

Chen, C. F., & Rothschild, R. (2010). An application of hedonic pricing analysis to the case of hotel rooms in Taipei. Tourism Economics, 16(3), 685–694.

Cheng, X., Bjørndal, E., & Bjørndal, M. (2014). Cost Efficiency Analysis based on The DEA and StoNED Models : Case of Norwegian Electricity Distribution Companies. European Energy Market (EEM), 11th International Conference IEEE, 1–6.

Corazza, M., Fasano, G., & Gusso, R. (2013). Particle Swarm Optimization with non-smooth penalty reformulation, for a complex portfolio selection problem. Applied Mathematics and Computation, 224, 611–624.

D’Halluin, Y., Forsyth, P. A., & Labahn, G. (2004). A penalty method for American options with jump diffusion processes. Numerische Mathematik, 97(2), 321–352.

Dantzig, G. B., Fulkerson, D. R., & Johnson, S. M. (1959). On a linear-programming, combinatorial approach to the traveling-salesman problem. Operations Research, 7(1), 58–66.

Dantzig, G., Fulkerson, R., & Johnson, S. (1954). Solution of a Large-Scale Traveling Salesman Problem. Journal of the Operations Research Society of America, 393–403.

Di Pillo, G., & Grippo, L. (1989). Exact Penalty Functions in Constrained Optimization. SIAM Journal on Control and Optimization, 27(6), 1333–1360.

Dykstra, R. L. (1983). An Algorithm for Restricted Least Squares Regression. Journal of the American Statistical Association, 78(384), 837–842.

Dykstra, R. L., & Robertson, T. (1982). An algorithm for isotonic regression for two or more independent variables. The Annals of Statistics, 10(3), 708–716.

Eskelinen, J., & Kuosmanen, T. (2013). Intertemporal efficiency analysis of sales teams of a bank: Stochastic semi-nonparametric approach. Journal of Banking & Finance, 37(12), 5163–5175.

Espinet, J. M., Saez, M., Coenders, G., & Fluvia, M. (2003). Effect on prices of the attributes of holiday hotels: A hedonic prices approach. Tourism Economics, 9(2), 165–177.

Fiacco, A. V., & McCormick, G. P. (1968). Nonlinear programming: sequential unconstrained minimization techniques. Classics in Applied Mathematics (Vol. 4). Philadelphia, PA: SIAM.

Fraser, D. A., & Massam, H. (1989). A mixed primal-dual bases algorithm for regression under inequality constraints. Application to concave regression. Scandinavian Journal of Statistics, 65–74.

Gelman, A., & Hill, J. (2007). Data analysis using regression and multilevel/hierarchical models. New York: Cambridge University Press: Cambridge.

Goldman, S. M., & Ruud, P. a. (1993). Nonparametric Multivariate Regression Subject to Constraint, 1–16.

Groeneboom, P., Jongbloed, G., & Wellner, J. a. (2001). Estimation of a convex function: Characterizations and asymptotic theory. Annals of Statistics, 29(6), 1653–1698.

Hannah, L. A., & Dunson, D. B. (2013). Multivariate convex regression with adaptive partitioning. The Journal of Machine Learning Research, 14, 3261–3294.

Hanson, D., & Pledger, G. (1976). Consistency in concave regression. The Annals of Statistics, 4(6), 1038–1050.

Hildreth, C. (1954). Point estimates of ordinates of concave functions. Journal of the American Statistical Association, 49(267), 598–619.

Hoerl, A. E., & Kennard, R. W. (1970). Ridge Regression: Biased Estimation for Nonorthogonal Problems. Technometrics, 12(1), 55–67.

Holloway, C. A. (1979). On the estimation of convex functions. Operations Research, 27(2), 401–407.

Hu, X. M., & Ralph, D. (2004). Convergence of a penalty method for mathematical programming with complementarity constraints. Journal of Optimization Theory and Applications, 123(2), 365–390.

Keshvari, A., & Kuosmanen, T. (2013). Stochastic non-convex envelopment of data: Applying isotonic regression to frontier estimation. European Journal of Operational Research, 231(2), 481–491.

Kuosmanen, T. (2008). Representation theorem for convex nonparametric least squares. Econometrics Journal, 11(2), 308–325.

Kuosmanen, T. (2011). Cost efficiency analysis of electricity distribution networks: Application of the StoNED method in the Finnish regulatory model.

Kuosmanen, T. (2012). Stochastic semi-nonparametric frontier estimation of electricity distribution networks: Application of the StoNED method in the Finnish regulatory model. Energy Economics, 34(6), 2189–2199.

Kuosmanen, T., & Kortelainen, M. (2012). Stochastic non-smooth envelopment of data: semi-parametric frontier estimation subject to shape constraints. Journal of Productivity Analysis, 38(1), 11–28.

Lee, C. Y., Johnson, A. L., Moreno-Centeno, E., & Kuosmanen, T. (2013). A more efficient algorithm for Convex Nonparametric Least Squares. European Journal of Operational Research, 227(2), 391–400.

Li, C., Yin, W., Jiang, H., & Zhang, Y. (2013). An efficient augmented Lagrangian method with applications to total variation minimization. Computational Optimization and Applications, 56(3), 507–530.

Mammen, E. (1991). Nonparametric Regression Under Qualitative Smoothness Assumptions. The Annals of Statistics, 19(2), 741–759.

Marcotte, P., & Zhu, D. L. (1996). Exact and inexact penalty methods for the generalized bilevel programming problem. Mathematical Programming, 74, 141–157.

Meyer, M. C. (1999). An extension of the mixed primal–dual bases algorithm to the case of more constraints than dimensions. Journal of Statistical Planning and Inference, 81, 13–31.

Meyer, M. C. (2003). A test for linear versus convex regression function using shape-restricted regression. Biometrika, 90(1), 223–232.

Meyer, M. C. (2006). Consistency and power in tests with shape-restricted alternatives. Journal of Statistical Planning and Inference, 136, 3931–3947.

Nemirovskii, A. S., Polyak, B. T., & Tsybakov, A. B. (1985). Convergence Rate of Nonparametric Estimates of Maximum-Likelihood Type. Problems of Information Transmission, 21, 258–271.

Ray, S. C., Kumbhakar, S. C., & Dua, P. (Eds.). (2015). Benchmarking for Performance Evaluation. Springer.

Rigall-I-Torrent, R., & Fluvià, M. (2011). Managing tourism products and destinations embedding public good components: A hedonic approach. Tourism Management, 32(2), 244–255.

Seijo, E., & Sen, B. (2011). Nonparametric least squares estimation of a multivariate convex regression function. Annals of Statistics, 39(3), 1633–1657.

Semere, M. (2014). Determinants of Hotel Room Rates in Stockholm : A Hedonic Pricing Approach. Södertörn University.

Thrane, C. (2007). Examining the Determinants of Room Rates for Hotels in Capital Cities: The Oslo Experience. Journal of Revenue and Pricing Management, 5(4), 315–323.

Tibshirani, R. (1996). Regression Shrinkage and Selection via the Lasso. Journal of the Royal Statistical Society. Series B (Methodological), 58(1), 267–288.

Vanderbei, R. J. (2001). Linear Programming: Foundations and Extensions. Journal of the Operational Research Society (Vol. 49).

Wang, Y., Wang, S., Dang, C., & Ge, W. (2014). Nonparametric quantile frontier estimation under shape restriction. European Journal of Operational Research, 232(3), 671–678.

Varian, H. (1984). The nonparametric approach to production analysis. Econometrica: Journal of the Econometric Society.

Varian, H. R. (1982). The nonparametric approach to demand analysis. Econometrica, 50(4), 945–973.

Zhou, H., & Lange, K. (2013). A Path Algorithm for Constrained Estimation. Journal of Computational and Graphical Statistics, 22(2), 261–283.

## Appendix 1. Developing matrix form of MCLS

Note that problem (2) has$n ^ { 2 } - n$constraints. By adding the condition$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \varepsilon _ { i } = 0 } \end{array}$to problem (2) and repeating it � times, there are$n ^ { 2 }$constraints. The condition$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \varepsilon _ { i } = 0 } \end{array}$is one of the finite sample properties of shape restricted regression estimator (see for example Seijo & Sen, 2011). Here we present an alternative proof to this property in Proposition 1.

Proposition 1: In the optimal solution to problem (1), the sum of residuals is zero.

Proof. See the Appendix 2.

Having this property, we categorize the constraints in (2) into � blocks as follows:

$$
\begin{array}{l} \text {Block i (i = 1,\ldots,n):} \\ y _ {j} - y _ {i} = \varepsilon_ {j} - \varepsilon_ {i} + (\pmb {x} _ {j} - \pmb {x} _ {i}) \pmb {\beta} _ {j} + s _ {i j}, j = 1, \ldots , n, j \neq i, \\ \sum_ {i = 1} ^ {n} \varepsilon_ {i} = 0, \end{array}
$$

where$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \varepsilon _ { i } = 0 } \end{array}$is appended to all blocks such that there are � constraints in every block. Here, our aim is to develop the matrix form of block �. To accomplish this purpose we use the following auxiliary matrices:

$$
\begin{array}{r l} & {\mathbf {0} _ {c \times d} = \mathrm{matrixofzerosofsize} c \times d,} \\ & {\mathbf {1} _ {c \times 1} = \mathrm{vectorofonesofsize} c,} \\ & {\mathbf {1} = \mathrm{matrixofonesofsize} n \times n,} \\ & {\mathbf {I} = \mathrm{theidentitymatrixofsize} n,} \\ & {\mathbf {E} _ {i} = [ \mathbf {0} _ {n \times (i - 1)} \mathbf {1} _ {n \times 1} \mathbf {0} _ {n \times (n - i)} ],} \\ & {\mathbf {A} _ {i} = \mathbf {I} - \mathbf {E} _ {i} + \mathbf {E} _ {i} ^ {\prime},} \\ & {\mathcal {X} _ {i} = (\mathbf {d} _ {1}, \dots , \mathbf {d} _ {m}, \mathbf {0} _ {n \times n (i - 1)}, \mathbf {I}, \mathbf {0} _ {n \times n (n - i)}),} \\ & {\mathbf {d} _ {p} = d i a g (\mathbf {x} ^ {p}) - x _ {i p} \mathbf {I}, p = 1, \dots , m,} \end{array}
$$

where$d i a g ( \pmb { x } ^ { p } )$refers to the diagonal matrix of vector$x ^ { p } . \ x _ { i }$is a sparse matrix of data, which is made of$m + n$sub-matrices. The first � sub-matrices$( { \bf { d } } _ { p } )$are diagonal matrices. The next � submatrices of$x _ { i }$consist of$n - 1$zero matrices and one identity matrix. The identity matrix is placed such that$\begin{array} { r } { \pmb { \mathcal { X } } _ { i } \Psi = \sum _ { p = 1 } ^ { m } \bigl ( d i a g ( \pmb { x } ^ { p } ) - x _ { i p } \mathbf { I } \bigr ) \pmb { \beta } ^ { p } + \pmb { s } _ { i } } \end{array}$

With the help of the auxiliary matrices, the �-th block of matrices is written as

$$
(\mathbf {I} - \mathbf {E} _ {i}) \mathbf {y} = \mathbf {A} _ {i} \pmb {\varepsilon} + \pmb {\mathcal {X}} _ {i} \pmb {\psi},\tag{A1}
$$

where${ \pmb \varepsilon } = ( \varepsilon _ { 1 } , \varepsilon _ { 2 } , \ldots , \varepsilon _ { n } ) ^ { \prime }$. Consider that constraint$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \varepsilon _ { i } = 0 } \end{array}$is placed as the �-th equality in (A1). By using equation (A1), problem (2) is written as$\left\{ \operatorname* { m i n } _ { \pmb { \varepsilon } , \Psi } \frac { 1 } { 2 } \pmb { \varepsilon } ^ { \prime } \pmb { \varepsilon } \right.$�. �.$( \mathbf { I } - \mathbf { E } _ { i } ) \mathbf { y } = \mathbf { A } _ { i } \pmb { \varepsilon } + \pmb { \chi } _ { i } \Psi , \ i =$ $1 , \ldots , n , \Psi \geq \mathbf { 0 } { \Big \} } .$. Building the matrices �, �, and the vector � are heavily based on the auxiliary matrices. To simplify the calculations, we summarize the necessary operations in the following proposition.

Proposition 2. Matrix$\mathbf { A } _ { i }$is invertible. Moreover, the following properties hold for the auxiliary matrices:

a)$\begin{array} { r } { \mathbf A _ { i } ^ { - 1 } = \mathbf I - \frac { 1 } { n } \mathbf { 1 } + \frac { 2 } { n } \mathbf E _ { i } - \mathbf e _ { i i } , } \end{array}$

b)$\begin{array} { r } { \mathbf { A } _ { i } ^ { - 1 } ( \mathbf { I } - \mathbf { E } _ { i } ) = \mathbf { I } - \frac { 1 } { \mathrm { n } } \mathbf { 1 } , } \end{array}$

$$
\mathbf {c}) \mathbf {A} _ {i} ^ {- 1 \prime} \mathbf {A} _ {i} ^ {- 1} = \mathbf {I} - \frac {1}{n} \mathbf {1} + \frac {1}{n} (\mathbf {E} _ {i} + \mathbf {E} _ {i} ^ {\prime}) - \mathbf {e} _ {i i},
$$

$$
\mathrm{d}) \mathbf {A} _ {1} \mathbf {A} _ {i} ^ {- 1} = \mathbf {I} - \mathbf {E} _ {1} - \mathbf {e} _ {i i} + \mathbf {e} _ {1 i},
$$

$$
\mathbf {\Phi} _ {e)} \left(\mathbf {I} - \frac {1}{n} \mathbf {1}\right) \mathbf {A} _ {1} ^ {- 1} = \mathbf {I} - \frac {1}{n} \mathbf {1} + \frac {1}{n} \mathbf {E} _ {1} - \mathbf {e} _ {1 1},
$$

where$\mathbf { e } _ { i j }$is an$n \times n$matrix whose$( i , j )$element is 1 and other elements are zero.

## Proof. See the Appendix 2.

Proposition 2 proves that matrix$\mathbf { A } _ { i }$is invertible. Hence, we calculate the closed form definition of the error vector � as the following:

$$
\pmb {\varepsilon} = - \mathbf {A} _ {i} ^ {- 1} \pmb {\mathcal {X}} _ {i} \pmb {\Psi} + \left(\mathbf {I} - \frac {1}{\mathrm{n}} \mathbf {1}\right) \mathbf {y}, i = 1, \ldots , n.\tag{A2}
$$

To estimate the residuals we use the first block of equation (A2), i.e. � = 1, but this choice is arbitrary and any of the blocks may be used. Equation (A2) is used in theorems 1 and 2 to obtain the penalty term.

Note that matrices$\mathbf { A } _ { 1 } ^ { - 1 \prime } \mathbf { A } _ { 1 } ^ { - 1 } , \mathbf { A } _ { 1 } \mathbf { A } _ { i } ^ { - 1 }$and$\begin{array} { r } { \left( \mathbf { I } - \frac { 1 } { n } \mathbf { 1 } \right) \mathbf { A } _ { 1 } ^ { - 1 } } \end{array}$that are used in the calculations of the penalized problem, have closed form definitions in Proposition 2. These matrices depend only to the number of observations and not to the problem data. Hence, we may compute them prior to solve the problem. Such matrices may be used to enhance the speed of computations in large-scale problems.

## Appendix 2. Proofs and algebraic computations

Proposition 1: In the optimal solution to problem (1), the sum of residuals is zero.

Proof. To prove this proposition we use the optimality conditions of problem (1) based on the Karush–Kuhn–Tucker (KKT) conditions. Suppose$( \varepsilon _ { i } ^ { * } , \alpha _ { i } ^ { * } , \beta _ { i } ^ { * } ) , i = 1 , \ldots , n$is a global minimizer of problem (1). Hence, there exist parameters$\lambda _ { i } , \mu _ { i j } , \gamma _ { i } = ( \gamma _ { i 1 } , \ldots , \gamma _ { i m } ) ^ { \prime } ( i , j = 1 , \ldots , n )$that satisfy the following conditions:

KKT conditions for the CLS problem

$$
- 2 \varepsilon_ {i} = \lambda_ {i}, i = 1, \dots , n,\tag{A3}
$$

$$
\lambda_ {i} + \sum_ {j = 1} ^ {n} \mu_ {i j} - \sum_ {j = 1} ^ {n} \mu_ {j i} = 0, i = 1, \dots , n,\tag{A4}
$$

$$
\mathbf {x} _ {i} ^ {\prime} \lambda_ {i} + \sum_ {j = 1} ^ {n} \mathbf {x} _ {i} ^ {\prime} \mu_ {i j} - \sum_ {j = 1} ^ {n} \mathbf {x} _ {i} ^ {\prime} \mu_ {j i} + \pmb {\gamma} _ {i} = 0, i = 1, \dots , n,
$$

$$
\pmb {\gamma} _ {i} ^ {\prime} \pmb {\beta} _ {i} = 0, i = 1, \dots , n,
$$

$$
\mu_ {i j} \big (\alpha_ {i} + {\bf x} _ {i} {\pmb \beta} _ {i} - \alpha_ {j} - {\bf x} _ {i} {\pmb \beta} _ {j} \big) = 0, i, j = 1, \ldots , n,
$$

$$
\pmb {\gamma} _ {i} \geq \mathbf {0}, \mu_ {i j} \geq 0, i, j = 1, \dots , n,
$$

$$
y _ {i} = \alpha_ {i} + \mathbf {x} _ {i} \pmb {\beta} _ {i} ^ {\prime} + \varepsilon_ {i}, i = 1, \dots n,
$$

$$
\alpha_ {i} + \mathbf {x} _ {i} \pmb {\beta} _ {i} ^ {\prime} \leq \alpha_ {j} + \mathbf {x} _ {i} \pmb {\beta} _ {j} ^ {\prime}, i, j = 1, \dots , n,
$$

$$
\pmb {\beta} _ {i} \geq \mathbf {0}, i = 1, \dots , n,
$$

where$\lambda _ { i }$and$\mu _ { i j }$are Lagrange multipliers of the first and the second constraints of the CLS problem, respectively, and$\pmb { \gamma } _ { i }$is the vector of Lagrange multipliers of the nonnegativity constraints.

Among all the conditions above, we need (A3) and (A4). Consider that$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \mu _ { i j } = } \end{array}$ $\textstyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \mu _ { j i }$. Hence, we have$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \lambda _ { i } = 0 } \end{array}$from condition (A4). Consequently, there is$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \varepsilon _ { i } = 0 } \end{array}$ from condition (A3). ■

Proposition 2. Matrix$\mathbf { A } _ { i }$is invertible. Moreover, the following properties hold for the auxiliary matrices in (6):

a)$\begin{array} { r } { \mathbf A _ { i } ^ { - 1 } = \mathbf I - \frac { 1 } { n } \mathbf { 1 } + \frac { 2 } { n } \mathbf E _ { i } - \mathbf e _ { i i } , } \end{array}$

b)$\begin{array} { r } { \mathbf { A } _ { i } ^ { - 1 } ( \mathbf { I } - \mathbf { E } _ { i } ) = \mathbf { I } - \frac { 1 } { \mathrm { n } } \mathbf { 1 } , } \end{array}$

$$
\mathbf {A} _ {i} ^ {- 1 \prime} \mathbf {A} _ {i} ^ {- 1} = \mathbf {I} - \frac {1}{n} \mathbf {1} + \frac {1}{n} (\mathbf {E} _ {i} + \mathbf {E} _ {i} ^ {\prime}) - \mathbf {e} _ {i i},
$$

d)$\mathbf { A } _ { 1 } \mathbf { A } _ { i } ^ { - 1 } = \mathbf { I } - \mathbf { E } _ { 1 } - \mathbf { e } _ { i i } + \mathbf { e } _ { 1 i }$

$$
\left(\mathbf {I} - \frac {1}{n} \mathbf {1}\right) \mathbf {A} _ {1} ^ {- 1} = \mathbf {I} - \frac {1}{n} \mathbf {1} + \frac {1}{n} \mathbf {E} _ {1} - \mathbf {e} _ {1 1},
$$

where$\mathbf { \boldsymbol { e } } _ { i j }$is an � × � matrix which its$( i , j )$element is 1 and other elements are zero.

## Proof.

First, we show$\mathbf { A } _ { i }$is positive definite, and hence it is invertible. Let � be a nonzero vector of size �.

There is$\mathbf { q } ^ { \prime } \mathbf { A } _ { i } \mathbf { q } = \mathbf { q } ^ { \prime } ( \mathbf { I } - \mathbf { E } _ { i } + \mathbf { E } _ { i } ^ { \prime } ) \mathbf { q } = \mathbf { q } ^ { \prime } \mathbf { q } > 0 .$

To prove the other statements, we use the following equalities:

$$
\begin{array}{l} \mathbf {1 E} _ {i} = n \mathbf {E} _ {i}, \mathbf {1 E} _ {i} ^ {\prime} = \mathbf {1}, \mathbf {1 e} _ {i i} = \mathbf {E} _ {i}, \mathbf {1 1} = n \mathbf {1}, \mathbf {E} _ {i} \mathbf {E} _ {i} = \mathbf {E} _ {i}, \mathbf {E} _ {i} \mathbf {E} _ {i} ^ {\prime} = \mathbf {1}, \mathbf {E} _ {i} ^ {\prime} \mathbf {E} _ {i} = n \mathbf {e} _ {i i}, \mathbf {e} _ {i i} \mathbf {E} _ {i} = \mathbf {e} _ {i i}, \mathbf {E} _ {i} \mathbf {e} _ {i i} = \\ \mathbf {E} _ {i}, \mathbf {e} _ {i i} \mathbf {e} _ {i i} = \mathbf {e} _ {i i}, \end{array}
$$

and for$2 \leq i \leq n \colon \mathbf { E } _ { 1 } \mathbf { E } _ { i } = \mathbf { E } _ { i } , \mathbf { E } _ { i } ^ { \prime } \mathbf { E } _ { 1 } = n \mathbf { e } _ { i 1 } , \mathbf { E } _ { 1 } \mathbf { e } _ { i i } = \mathbf { 0 } , \mathbf { E } _ { 1 } ^ { \prime } \mathbf { e } _ { i i } = \mathbf { e } _ { 1 i } .$

$$
\text { Theorem   1. } \varepsilon^ {\prime} \varepsilon = \psi^ {\prime} \mathcal {X} _ {1} ^ {\prime} \mathrm{A} _ {1} ^ {- 1 ^ {\prime}} \mathrm{A} _ {1} ^ {- 1} \mathcal {X} _ {1} \psi - 2 \mathrm{y} ^ {\prime} \left(\mathrm{I} - \frac {1}{n} \mathrm{1}\right) \mathrm{A} _ {1} ^ {- 1} \mathcal {X} _ {1} \psi + \mathrm{y} ^ {\prime} \left(\mathrm{I} - \frac {1}{n} \mathrm{1}\right) \mathrm{y}
$$

Proof.

By using equation (6), the proof is straightforward. ■

Theorem 2.$\begin{array} { r } { \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \Big ( \varepsilon _ { j } - \varepsilon _ { i } + \big ( \mathbf { x } _ { j } - \mathbf { x } _ { i } \big ) \big \beta _ { j } ^ { \prime } + s _ { i j } - \big ( y _ { j } - y _ { i } \big ) \Big ) ^ { 2 } = } \end{array}$

$$
\pmb {\Psi} ^ {\prime} (\sum_ {i = 2} ^ {n} (\pmb {\mathscr {X}} _ {1} - \mathbf {A} _ {1} \mathbf {A} _ {i} ^ {- 1} \pmb {\mathscr {X}} _ {i}) ^ {\prime} (\pmb {\mathscr {X}} _ {1} - \mathbf {A} _ {1} \mathbf {A} _ {i} ^ {- 1} \pmb {\mathscr {X}} _ {i})) \pmb {\Psi}.
$$

Proof.

The error is calculated by equation (3) for all blocks of constraints. To satisfy the constraints, we calculate the error vector for block$i ( i \geq 2 )$by equation (3) and use it in block 1$( i = 1 )$by equation (A1). Therefore, the following equation must hold for$i = 2 , \ldots , n \colon$

$$
\left(\boldsymbol {\mathcal {X}} _ {1} - \mathbf {A} _ {1} \mathbf {A} _ {i} ^ {- 1} \boldsymbol {\mathcal {X}} _ {i}\right) \boldsymbol {\Psi} = \left(\mathbf {I} - \mathbf {E} _ {1} - \mathbf {A} _ {1} \left(\mathbf {I} - \frac {1}{n} \mathbf {1}\right)\right) \mathbf {y}.
$$

Using Proposition 2, there is$\begin{array} { r } { \mathbf { A } _ { 1 } ^ { - 1 } ( \mathbf { I } - \mathbf { E } _ { 1 } ) = \mathbf { I } - \frac { 1 } { \mathrm { n } } \mathbf { 1 } } \end{array}$. Hence, the right hand side of the above equation is$\mathbf { I } - \mathbf { E } _ { 1 } - \mathbf { A } _ { 1 } \mathbf { A } _ { 1 } ^ { - 1 } ( \mathbf { I } - \mathbf { E } _ { 1 } ) = \mathbf { 0 }$. Using this result, we reframe the block of constraints (A1) as$( { \pmb { \mathscr X } } _ { 1 } - { \pmb A } _ { 1 } { \pmb A } _ { i } ^ { - 1 } { \pmb \mathscr X } _ { i } ) { \pmb \psi } = { \pmb 0 }$. Note that the left hand side of this equation shows the violation, and the penalty is defined as sum of the quadratic violations.■

Theorem 3. The following properties hold:

a) Problem (4) has an optimal solution for any given$M \geq 0$

b) Let$\Psi ^ { * }$and$\Psi ^ { * } ( M )$be the optimal solutions to problems (2) and (4), respectively. Then $\Psi ^ { * } ( M ) \to \Psi ^ { * } \mathrm { a s } M \to \infty .$

Proof.

a) We show that matrix � is positive semidefinite. Matrix � can be written as$\mathbf { Q } = 2 \mathbf { T } ^ { \prime } \mathbf { T }$, where$\mathbf { T } =$ $\pmb { \mathrm { A } } _ { 1 } ^ { - 1 } \pmb { \mathcal { X } } _ { 1 }$. Let � be a nonzero vector of size$n m + n ^ { 2 }$. Hence,$\mathbf { q } ^ { \prime } \mathbf { T } ^ { \prime } \mathbf { T } \mathbf { q } \geq 0$, and therefore � is positive semidefinite. Similarly, matrix � is positive semidefinite, and hence � is positive semidefinite. Therefore, for any$M > 0$problem (4) is convex and it has a global minimizer.

b) First, assume that$\Psi ^ { * } ( M )$is a feasible solution to problem (2). This means that all the constraints are satisfied and$\boldsymbol { \Psi } ^ { * \prime } \boldsymbol { \mathbf { V } } \boldsymbol { \Psi } ^ { * } = 0$. In this case, the objective function of (4) is equal to the objective function of (2) minus the scalar value of$\gamma .$. Therefore, the optimal solutions of (2) and (4) are the same:$\boldsymbol { \Psi } ^ { * } ( M ) = \boldsymbol { \Psi } ^ { * }$

Now assume that$\Psi ^ { * } ( M )$is outside of the feasible region of (2). Let$\{ M _ { k } \} , k = 1 , 2 , \dots , \infty$be an increasing sequence of nonnegative numbers, and let us use a more simple notation for the optimal solution of (4) as$\Psi ^ { ( k ) } = \Psi ^ { * } ( M _ { k } )$. Optimality of$\Psi ^ { ( k + 1 ) }$and$\Psi ^ { ( k ) }$implies that:

$$
\frac {1}{2} \pmb {\psi} ^ {(k) \prime} (\mathbf {Q} + M _ {k} \mathbf {V}) \pmb {\psi} ^ {(k)} + \mathbf {c} \pmb {\psi} ^ {(k)} \leq \frac {1}{2} \pmb {\psi} ^ {(k + 1) \prime} (\mathbf {Q} + M _ {k} \mathbf {V}) \pmb {\psi} ^ {(k + 1)} + \mathbf {c} \pmb {\psi} ^ {(k + 1)},
$$

$$
\frac {1}{2} \pmb {\psi} ^ {(k + 1) \prime} (\mathbf {Q} + M _ {k + 1} \mathbf {V}) \pmb {\psi} ^ {(k + 1)} + \mathbf {c} \pmb {\psi} ^ {(k + 1)} \leq \frac {1}{2} \pmb {\psi} ^ {(k) \prime} (\mathbf {Q} + M _ {k + 1} \mathbf {V}) \pmb {\psi} ^ {(k)} + \mathbf {c} \pmb {\psi} ^ {(k)}.
$$

By adding these two inequalities and rearranging the terms, we have

$$
(M _ {k + 1} - M _ {k}) \big (\boldsymbol {\Psi} ^ {(k + 1) \prime} \mathbf {V} \boldsymbol {\Psi} ^ {(k + 1)} - \boldsymbol {\Psi} ^ {(k) \prime} \mathbf {V} \boldsymbol {\Psi} ^ {(k)} \big) \leq 0,
$$

As$M _ { k + 1 } - M _ { k } \geq 0$, there is$0 \leq \Psi ^ { ( k + 1 ) \prime } \mathbf { V } \Psi ^ { ( k + 1 ) } \leq \Psi ^ { ( k ) \prime } \mathbf { V } \Psi ^ { ( k ) }$. Hence,$\begin{array} { r } { \psi ^ { ( k ) \prime } \mathbf { V } \Psi ^ { ( k ) } \to 0 } \end{array}$as$k$ $\infty .$, which means that the value of penalty term at the optimal solution to (4) decreases if$M  \infty$ Therefore for a large$M , \Psi ^ { * } ( M )$is in a tight neighborhood of the feasible region of (2), and it gets closer to the feasible region if the value of � increases. As a result,$\Psi ^ { * } ( M ) \to \Psi ^ { * }$as$M \to \infty . \mathbf { \mathbb { m } }$

## Some discussions about big �

The penalty term in problem (4) is zero if the solution is feasible to problem (2). Therefore at any step of the solving process, if a feasible solution is obtained then the penalty is zero and the magnitude of � is not important. However, there are some concerns for the value of � in practice, which are related to the numerical precisions of the solver and the computer. Solvers usually use two tolerance thresholds for the numerical computations of a QP: optimality tolerance (OT), and feasibility tolerance (FT). The precision (PT) of the computer is also important since it causes rounding biases.

A rule of thumb for the value of � is explained here. Let � be a solution to (4), and let$f$be an upper limit for${ \scriptstyle { \frac { 1 } { 2 } } } \Psi ^ { \prime } \mathbf { Q } \Psi + \mathbf { C } \Psi$and � be the value of${ \frac { 1 } { 2 } } M ^ { 2 } \Psi ^ { \prime } \mathbf { V } \Psi$. If there exists some violation then there should be$g > | f |$. Let assume there is a small violation$( \delta > F T )$in every constraint of (2). Thus$g$is approximated by$n ^ { 2 } M ^ { 2 } \delta / 2$, and there is$M > \sqrt { \frac { 2 \vert f \vert } { n ^ { 2 } \delta } }$which approximates the lower bound of �. The value of � can be approximated from the objective value of a linear regression problem. For example, assume$n = 1 0 0 , F T = 1 0 ^ { - 8 } , \delta = 1 0 ^ { - 5 }$, and an approximation for � is$- 1 0 ^ { 3 }$(note that optimal value of � is negative). Using this role of thumb, there is$M \cong 1 4 0$

In case an extremely big � is used, at the optimal solution to (4) there is$\boldsymbol { \Psi } ^ { * \prime } \boldsymbol { \mathbf { V } } \boldsymbol { \Psi } ^ { * } \cong 0$but the value of${ \textstyle \frac { 1 } { 2 } } \Psi ^ { * \prime } M ^ { 2 } \mathbf { V } \Psi ^ { * }$may be still larger than$\textstyle { \frac { 1 } { 2 } } \Psi ^ { * \prime } \mathbf { Q } \Psi ^ { * } + \mathbf { C } \Psi ^ { * }$. If this case happens, the current solution to (4) is thus hold the concavity condition. Therefore the estimated function is piecewise linear and concave, which may be equivalent to a linear regression line, the average line (average of � values), or a piecewise linear function that is not necessarily the best fit.

## Dual of penalized monotonic CLS

Let � be the Lagrange multiplier of nonnegativity constraint in problem (4). We build the Lagrange function$\begin{array} { r } { L ( \Psi , \mu ) = \frac { 1 } { 2 } \Psi ^ { \prime } \mathbf { H } \Psi - ( \mu ^ { \prime } - \mathbf { c } ) \Psi } \end{array}$and minimize it in$\Psi .$. This is an unconstrained optimization and the function is convex and differentiable, hence the minimum is given by$\nabla _ { \Psi } L = 0$ Therefore,$\mathbf { H } \boldsymbol { \Psi } = ( \mathbf { \boldsymbol { \mu } } - \mathbf { \boldsymbol { \mathbf { c } } } ^ { \prime } )$and$\Psi = \mathbf { H } ^ { - 1 } ( \mu - \mathbf { c } ^ { \prime } )$. By substituting � into the Lagrange function, we get the following dual function:

$$
L (\pmb {\mu}) = - \frac {1}{2} (\pmb {\mu} - \pmb {c ^ {\prime}}) ^ {\prime} \mathbf {H} ^ {- 1} (\pmb {\mu} - \pmb {c ^ {\prime}}),
$$

and the dual problem is obtained by maximizing � subject to nonnegative �. We perform the following two steps to obtain dual of penalized monotonic CLS as presented in (6):

i.Define$\mathbf { z } = \mathbf { H } ^ { - 1 } ( \boldsymbol { \mu } - \mathbf { c } ^ { \prime } )$, and obtain${ \mathbf { \mu } } -  { \mathbf { c } } ^ { \prime } =  { \mathbf { H \pi } }$. Hence, the dual problem is to maximize$- { \frac { 1 } { 2 } } \mathbf { z } ^ { \prime } \mathbf { H } \mathbf { z }$subject to$\mathbf { H } \mathbf { z } + \mathbf { c } ^ { \prime } \geq \mathbf { 0 }$

ii.Use$\mathbf { H } = \mathbf { F ^ { \prime } } \mathbf { F }$and define$\mathbf { w } = \mathbf { F } \mathbf { Z }$. Hence, the dual problem is to maximize$\begin{array} { r } { - \frac { 1 } { 2 } \mathbf { w } ^ { \prime } \mathbf { w } } \end{array}$subject to$\mathbf { F } ^ { \prime } \mathbf { w } + \mathbf { c } ^ { \prime } \geq 0$

To obtain the dual of penalized CLS (8), consider that the Lagrange multipliers of the first �� elements of � are free of sign.■

## Appendix 3.

In this appendix we present two functions: Dual\_PMCLS(x,y) and PMCLS(x,y), and one auxiliary function to generate matrix$x _ { i }$(function make\_X). To call the functions use the command as:

```txt
Matlab: [SSR, eps] = Dual_PMCLS(x, y), R: sol < -Dual_PMCLS(x, y)
```

where x is an � × � matrix of input values, y is a vector of outputs, SSR is the estimated SSR, and eps is the error. The function make\_X must be in the same folder as the main functions. In R, sol is a list containing SSR and eps.

## Part 1. Matlab codes

## MATLAB code for dual of penalized MCLS

```matlab
function [SSR,eps]=Dual_PMCLS(x,y)
%This function refers to dual of penalized monotonic CLS
%Please cite this paper if you use this function
n= size(x,1); m= size(x,2);
ai=sparse(eye(n));
E=@(i) sparse([zeros(n,(i-1)),ones(n,1),zeros(n,(n-i))]);
ei=@(i) sparse([zeros(n,(i-1)),ai(:,i),zeros(n,(n-i))]);
eil=@(i) sparse([zeros((i-1),n);ai(1,:);zeros((n-i),n)]);
ainv=@(i) sparse(ai-(1/n)*ones(n)+(2/n)*E(i)-ei(i));%Inverse of matrix A(i)

X=@(i) make_X(i,m,n,x,ai,1);%We make matrix X via a separate function
Q=X(1)'*sparse((ai-(1/n)*ones(n)+(1/n)*(E(1)+E(1)')-ei(1)));
Q=Q*X(1);
C=-2*y'*(ai-(1/n)*ones(n)+(1/n)*E(1)-ei(1))*X(1);

%Building matrix F
r=cell(n,1);c=cell(n,1);v=cell(n,1);
for i=2:n
    [r{i},c{i},v{i}]=find(sparse((ai-E(1)+ei1(i)'-ei(i))*X(i)-X(1)));
    r{i}=(i-1)*n+r{i};
end;
r=cell2mat(r);
c=cell2mat(c);
v=cell2mat(v); v=round(v,8);
F=sparse(r,c,v,n^2,n^2+n*m);
H= sparse(1:n^2,1:n^2,ones(n^2,1),n^2 ,n^2 );
F=100*F;
F(1:n,1:n*m+n^2)=sparse(sqrt(2)*(ainv(1)*X(1)));

% We use MOSEK to solve the problem. The reader may choose to use quadprog
% or other solvers instead.
param = [];
param.MSK_IPAR_LOG=0;
[res]=mskqpopt(H,zeros(n^2 ,1),F',[],C', [],[],param );

psi=-res.sol.itr.y;%Optimal values of psi variables
eps =sparse(eye(n)-(1/n)*ones(n,n))*y-ainv(1)*(X(1))*psi;
SSR=eps'*eps;
end
```

```matlab
MATLAB code for penalized MCLS

function [SSR, eps]=PMCLS(x,y)

%This function refers to penalized monotonic CLS

%Please cite this paper if you use this function

n= size(x,1); m= size(x,2);

ai=sparse(eye(n));

E=@(i) sparse([zeros(n,(i-1)),ones(n,1),zeros(n,(n-i))]);

ei=@(i) sparse([zeros(n,(i-1)),ai(:,i),zeros(n,(n-i))]);

eil=@(i) sparse([zeros((i-1),n);ai(1,:);zeros((n-i),n)]);
ainv=@(i) sparse(ai-(1/n)*ones(n)+(2/n)*E(i)-ei(i));%Inverse of matrix A(i)

X=@(i) make_X(i,m,n,x,ai,1);%We make matrix X via a separate function
Q=X(1)'*sparse((ai-(1/n)*ones(n)+(1/n)*(E(1)+E(1)')-ei(1)));
Q=Q*X(1);
C=-2*y*(ai-(1/n)*ones(n)+(1/n)*E(1)-ei(1))*X(1);

%Building matrix F

r=cell(n,1);c=cell(n,1);v=cell(n,1);

for i=2:n
    [r{i},c{i},v{i}]=find(sparse((ai-E(1)+ei1(i)'-ei(i))*X(i)-X(1)));
    r{i}=(i-1)*n+r{i};

end;

r=cell2mat(r);

c=cell2mat(c);

v=cell2mat(v); v=round(v,8);

F=sparse(r,c,v,n^2,n^2+n*m);

V=F'*F;
H=2*Q+V*10000 ;H=round(H,8);

% We use MOSEK to solve the problem. The reader may choose to use quadprog
% or other solvers instead.

param = 居

param.MSK_IPAR_LOG=0;

[res]=mskqpopt(H,C',zeros(1,size(C,2)),[],[],zeros(size(C,2),1),[] ,param);

psi=res.sol.itr.xx;%Optimal values of psi variables
eps =sparse(eye(n)-(1/n)*ones(n,n))*y-ainv(1)*(X(1))*psi;
SSR=eps'*eps;

end
```

## MATLAB code for making matrix �

```matlab
function X=make_X(i,m,n,x,ai,slacks)
d=@(i,p) sparse(diag(x(:,p))-x(i,p)*ai);
r=cell(m);c=cell(m);v=cell(m);
for p=1:m
    [r{p},c{p},v{p}]=find(d(i,p));c{p}=c{p}+n*(p-1);
end;
r=cell2mat(r);c=cell2mat(c);v=cell2mat(v);
X=sparse(r,c,v,n,n*m);
if slacks==1
    r=1:n;
    c=m*n+n*(i-1)+1:m*n+n*(i-1)+n;
    X2=sparse(r,c,ones(n,1),n,m*n+n^2);
    X2(:,1:m*n)=X;
    X=X2;
end;
end
```

## Part 2. R codes

```r
R code for dual of penalized MCLS
Dual_PMCLS = function(m,n,x,y) {
    # This function refers to dual of penalized monotonic CLS
    # Please cite this paper if you use this function

    require(slam)
    require(quadprog)
    source("make_X.R")  # the code for this script is available in the paper
    ai <- diag(n)
    E <- function(i) return(cbind(matrix(0,n,i-1),matrix(1,n,1),matrix(0,n,n-i)))
    ei <- function(i) return(cbind(matrix(0, n, i-1),ai[, i],matrix(0, n, n-i)))
    ei1 <- function(i) return(rbind(matrix(0, i-1, n),ai[1, ],matrix(0, n-i, n)))
    ainv <- function(i) return(ai-matrix(1,n,n)/n +2*E(i)/n-ei(i))#Inverse of A(i)
    X <- function(i) make_X(i,m,n,x,ai,1)
    Q <- t(X(1)) %** (ai-(1/n)*matrix(1, n, n)+(1/n)*(E(1)+t(E(1))-ei(1)))
    Q <- Q %** X(1)
    C <- -2*t(y) %** (ai-(1/n)*matrix(1, n, n)+(1/n)*E(1)-ei(1))%**X(1)

    #Building matrix F
    r <- list(); c <- list(); v <- list()
    for (i in 2:n){
    temp <- (ai-E(1)+t(eil(i))-ei(i))%**X(i)-X(1)
    rc <- which(temp!=0,arr.ind = T)
    r[[i]] <- rc[,1]; c[[i]] <- rc[,2]; v[[i]] <- temp[rc];
    r[[i]] <- (i-1)*n + r[[i]];
    }
    r <- unlist(r); c <- unlist(c); v <- unlist(v);v <- round(v,8);
    F <- matrix(simple_triplet_matrix(r,c,v,n^2,n^2+n*m),n^2,n^2+n*m)
    H <- matrix(simple_triplet_matrix(1:n^2,1:n^2,matrix(1,n^2,1),n^2,n^2),n^2,n^2)
    F <- 100*F  #big M = 100
    F[1:n,1:(n*m+n^2)] <- (sqrt(2)*(ainv(1) %** X(1)))

    # Solve by using solve.QP in R. This works but a more efficient solver such as
    # CPLEX, Gurobi or Mosel is preferred
    H <- H + diag(0.000000001,dim(H)[1],dim(H)[2])
    res <- solve.QP(H, c(rep(0,n^2)), (-F), (-C), meq=0, factorized=F)

    psi <- res$Lagrangian #Optimal values of psi variables
    eps <- (ai-(1/n)*matrix(1,n,n))%**y-ainv(1)%**(X(1))%**psi;
    SSR=t(eps) %** eps
    return(list(SSR, eps))
}

R code for penalized MCLS
PMCLS=function(x,y) {
    # This function refers to penalized monotonic CLS
    # Please cite this paper if you use this function

    require(slam)
    require(quadprog)
    source("make_X.R")  # the code for this script is available in the paper
    n <- dim(x)[1]; m <- dim(x)[2];
    ai <- diag(n)
    E <- function(i) return(cbind(matrix(0,n,i-1),matrix(1,n,1),matrix(0,n,n-i)))
    ei <- function(i) return(cbind(matrix(0, n, i-1),ai[, i],matrix(0, n, n-i)))
    ei1 <- function(i) return(rbind(matrix(0, i-1, n),ai[1, ],matrix(0, n- i, n)))
    ainv <- function(i) return(ai-matrix(1,n,n)/n +2*E(i)/n-ei(i))#Inverse of A(i)
    X <- function(i) return(make_X(i,m,n,x,ai,1))
```

```r
Q <- t(X(1)) %*% (ai-(1/n)*matrix(1, n, n)+(1/n)*(E(1)+t(E(1))-ei(1)))
Q <- Q %*% X(1)
C <- -2*t(y) %*% (ai-(1/n)*matrix(1, n, n)+(1/n)*E(1)-ei(1))%*%X(1)

#Building matrix F
r <- list(); c <- list(); v <- list()
for (i in 2:n){
    temp <- (ai-E(1)+t(ei1(i))-ei(i))%*%X(i)-X(1)
    rc <- which(temp!=0,arr.ind = T)
    r[[i]] <- rc[,1]; c[[i]] <- rc[,2]; v[[i]] <- temp[rc];
    r[[i]] <- (i-1)*n + r[[i]];
}

r <- unlist(r); c <- unlist(c); v <- unlist(v);v <- round(v,8);
F <- matrix(simple_triplet_matrix(r,c,v,n^2,n^2+n*m),n^2,n^2+n*m)
V <- t(F)%*%F;
H <- 2*Q+V*10000 ;H=round(H,8); # big M = 100

# Solve by using solve.QP in R. This works but a more efficient solver such as
# CPLEX, Gurobi or Mosel is preferred
H <- H + diag(0.000001,dim(H)[1],dim(H)[2])
res <- solve.QP(H,-t(C),diag(1,dim(H)[1]),c(rep(0,dim(H)[1])), meq=0,factorized=F)

psi <- res$solution #Optimal values of psi variables
eps <- (ai-(1/n)*matrix(1,n,n))%*%y -ainv(1)%*(X(1))%*%psi;
SSR=t(eps) %*% eps
return(list(SSR, eps))
```

## R code for making matrix �

```r
make_X = function(i,m,n,x,ai,slacks=0) {
    d <- function(i,p) return(diag(x[,p]) - x[i,p] * ai)
    r <- list()
    c <- list()
    v <- list()
    for (p in 1:m) {
    rc <- which(d(i,p)!=0,arr.ind = T)
    r[[p]] <- rc[,1]
    c[[p]] <- rc[,2]
    v[[p]] <- d(i,p)[rc]
    }
    r <- unlist(r)
    c <- unlist(c)
    v <- unlist(v)
    X <- matrix(simple_triplet_matrix(r,c,v,n,n*m),n,n*m)
    if (slacks==1) {
    r <- 1:n
    c <- (m*n+n*(i-1)+1):(m*n+n*(i-1)+n)
    X2 <- matrix(simple_triplet_matrix(r,c,matrix(1,n,1),n,m*n+n^2),n,m*n+n^2)
    X2[,1:(m*n)] <- X
    X <- X2;
    }
    return(X)
}
```