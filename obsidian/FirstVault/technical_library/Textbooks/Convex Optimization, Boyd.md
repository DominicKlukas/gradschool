Author: Stephen Boyd
### Chapter 1
#### 1.2-1.3
- We defined at least squares, linear programming, and convex optimization, and looked at some use cases/problems which can be formulated as such problems.
- Of particular interest for linear programming is the Chebyshev approximation problem.
- Convex optimization problems are the topic of the book, and in particular, knowing which problems are convex optimization problems/can be formulated as convex optimization problems is often difficult.
#### 1.4
- Often, convex optimization can be used to help with nonlinear optimization (which need not be convex), where approximations of the function we are trying to optimize can give us good starting points, or convex approximations of the constraints can give us bounds for the global optimal value.
### 1.5-1.6
- Cool application of Riesz representation theorem: Any linear function from S^k -> R can be written as tr(CX), where C, X \in S^k. Let the reader understand.
- Some non-standard notation: R+, R++
- Inequalities between matrices? Is this component-wise? No, Lowner order. It basically means that their difference is positive semi-definite, and it applies for symmetric matrices (so they have an orthogonal basis).
- Reflecting on chapter 1.5: Convex optimization seems to show up a lot, so having it down pat is likely just as useful as having linear algebra down pat.
### Chapter 2
Chapter 2 seems to look at some standard convex sets that are good to consider as examples... *why aren't we looking at convex functions*? Perhaps that's the next chapter. Looking forward to working with these mathematical objects!

#### 2.1
We looked at convex sets. A couple things I learned:
- To get the affine hull, think of it as x_0 + span(S - x_0).
- The restricted interior considers points x such that B(x, r) \cap aff S \subset S, instead of B(x, r) \subset S... it "flattens" the interior, so to speak, so it lives inside the right affine set to make sense in the context of S.
- You can also deal with integrals!$\int _C p(x)x dx$  where $x \in \mathbb{R}^{n}$, for some subset $C$ of $\mathbb{R}^{n}$, where p(x) is over C and is equal to 1. Imagine instead of taking linear combinations of a finite number of points, we take, for example, this integral over the unit circle. Then, we can fill in the circle with different choices for p over the "vectors" making up the circle.
- Conic combination removes the requirement that $\sum_{i} \theta_{i} = 1$
#### 2.2
- Hyperplanes: solution to a single equation. You can think of it as vectors whose dot product with the "normal vector" to the plane result in a specific value. Divides R^n into two halves.
- Cones and ellipsoids are quite intuitive, but perhaps recall their definition if needed.
- Simplex's are the affine hull of affine independent vectors. The unit simplex and the probability simplex are very common, very useful mathematical objects.
- We can also think about convexity living in other spaces, like the space of matrices for instance: PSD matrices are a convex space when thought of in the context of the space of matrices.
#### 2.3
- We look at transformations that preserve convexity. There is a whole zoo of them, mostly intuitive and obvious.
- Perspective functions: interesting way to "project" R^(n+1) onto R^n. *Linear fractional*functions, have an interesting interpretation: take an element from R^n, bring it to R^n+1 as a conical ray, then do a linear transformation on this ray, and take it to R^m. May have to review this if it shows up again.
#### 2.4
- General inequalities, are a weak inequality where an element of $\mathbb{R}^{n}$ is bigger than some other element if you take a specific cone, zero it at the "smaller" number, and the bigger number is then in this translated cone. I.e. y-x \in K, where K is a proper cone. (Proper cones are nice, solid in R^n, convex cones).
#### 2.5
- If we take the point of smallest distance between two disjoint convex sets, we can always create a plane perpendicular to the line segment joining these two points that separates the two sets.
#### 2.6
- Dual cone is defined to be the intersection of the halfspaces intersecting the origin with the rays in the original cone as their normal vectors.
- For dual inequalities: we have this really cool idea. The dual cone produces a constraint: $x \leq_K y$ if and only if $\lambda^T x \leq \lambda^T y$ for all $\lambda \geq_K^* 0$. Take two vectors, x and y, and see that the dual cone contains all vectors up to the ones that are orthogonal to y-x, but no further! Dual cones can be thought of as sharper if the original cone is wider.
- This characterization of the minimum also lets us cook up a better idea for the minimizer of a set. An element in a non-convex set S can be minimal without minimizing the inequality. But a minimizing element will satisfy $\lambda^T$ is minimized.

The biggest thing I got out of this was the intuition afforded by cones, dual cones, and restricted interiors.

### Chapter 3
#### 3.1
- A convex function is convex when restricted to a line t | x + vt, for vectors x and v: useful to use this to try and break convexity
- We can extend the domain of f by letting it be infinite on places not on its original domain (and since the original domain was convex) the new function will also be convex. Also useful for dealing with sums of convex functions, especially when they are defined on different domains, not having to deal with extra argument about what the domain is (infinity will sweep away $D_1 \triangle D_2$)
- Indicator functions of convex sets also have $I_C(x) = 0$ for $x \in C$ and infinite otherwise.
- Useful property: first order Taylor approximation is a global under-estimator of a differentiable convex function. Simple to prove. n dimensional case proved by first constructing a 1 dimensional function along a line. Second order condition: $\nabla^2 f(x) \geq 0$, semi-positive definite.
- We look at some interesting examples of convex sets. Interesting: max, and log sum exp function. Log sum exp function is a differentiable approximation to the max function.
- Geometric mean: side length of square that has same area as rectangle. Matches arithmetic mean when x=y.
- Epigraph: set of points in the graph of a function above the function. Convex iff function is convex.
- Multi-dimensional, and integral convex combinations also make sense for convex functions. (See "convex" integrals and convex combinations in chapter 2).
#### 3.2
- Another zoo of operations that conserve convexity.
- In particular the max of convex functions is convex. The function that is the sum of the max r of n components of a vector can be written as the maximum of a bunch of linear functions.
- Will skip most of this section for now. Perhaps composition/other examples will be interesting at some point.
- The infemum of a convex set w.r.t. one of its components is just the projection of the epigraph of the set onto that component. In chapter 2 we saw that projection of convex sets leads to another convex set. Let the reader understand.
#### 3.3
- The conjugate of a function $\mathbb{R}^{n} \to \mathbb{R}$ is given by $f^{*}(y) = \text{sup}_{x \in \text{dom} f} (y^{T}x - f(x))$, when it exists. This won't exist for all $y$, since it sweeps over all of $x$ in the domain.
- This conjugate is going to be a convex function, because it is the max/sup of convex functions (affine sets).
- If $f$ is differentiable, then we have that the value of the conjugate at $y$ is given by  $y = \nabla f(x^{*})$ for some $x^{*}$ which maximizes this function. Geometrically, we can think then of $f^{*}(y)$ as the function that maximizes the distance between the lines $yx$ and the tangent of the function at $x$, and then the value of the function is the gap between the lines.
- You can think about it as the intercept of the "highest" plane with slope y (generalize to dot product if in higher dimensions) 
- The conjugate of the conjugate is the function itself after we apply some conditions... figure out what these conditions are: The conditions are that the function is convex. Try an example to see that when not convex, none of the planes which come up to meet the function will ever hit the points that are in the non-convex locations. So, if you take the conjugate of a conjugate, it will just make a function that is linear over those areas.
#### 3.4.
Quasi convex: if the sublevel sets are all convex. Recall that the sublevel sets are defined as $\{ x : f(x) \leq \alpha \}$.
Quasi concave if $-f$ is quasi convex. If both then quasilinear.
Essentially, if it is decreasing away from a point and increasing toward it then it is quasi convex and if it is increasing/decreasing then it is quasilinear.
$$
f(y) \leq f(x) \implies \nabla f(x)^{T}(y-x) \leq 0
$$
This is a way to write this when you are in a higher dimensional space.