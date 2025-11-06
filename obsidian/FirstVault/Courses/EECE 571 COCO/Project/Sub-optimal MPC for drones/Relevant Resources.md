Papers:
https://arxiv.org/html/2508.01103v1
https://www.sciencedirect.com/science/article/pii/S2405896319301934
Simulation:
https://github.com/utiasDSL/gym-pybullet-drones
https://github.com/zsayem30/lsy_drone_racing
Links:
https://github.com/acados/acados
https://www.mathworks.com/help/mpc/ug/simulate-mpc-controller-using-suboptimal-solution.html



---
## Dominic's Notes

### Numerical Optimization
#### Chapter 17
If we have a constrained optimization problem, one way we might want to deal with the constraints, is by "regularizing"... defining a new loss function which we seek to minimize.
$$
Q(x, \mu) = f(x) + \mu \sum c_{i}^{2}
$$
where $f$ is the cost function, and $c_{i}$ are the constraints. This is called "Penalty Augmented".
The problem here is that $f(x)$ will go for points that are not on the constraint, since for small deviations from the constraint we won't necessarily be penalized very much yet, since it is quadratic penalty (small for $c < 1$). The first theorem says, we can consider a sequence of solutions as $\mu \to \infty$, and can prove that limit points of such sequences will converge to an optimal solution.

In the case where we have both inequalities $c_{i} \geq 0, i \in \mathcal{E}$, and equalities $c_{i} = 0, i \in \mathcal{I}$ we may want to work with the $\ell_{1}$ norm instead. Then, we have:
$$
Q(x, \mu) = f(x) +\mu \sum_{i \in \mathcal{E}} [c_{i}]^{-} + \mu \sum_{i \in \mathcal{I}} c_{i}
$$
There is a proof that shows, that the amount that we are straying away from the constraint is $c_{i}(x) \approx -\frac{\lambda_{i}}{\mu}$ if we use these quadratic methods, where $\lambda$ is the Legrange multiplier of the function.
Therefore, if we minimize a function that takes this into account, then we will have a much closer estimate. This is called the Augmented Legrangian:
$$
\mathcal{L}_{A}(x, \lambda; \mu) = f(x) - \sum_{i \in \mathcal{E}} \lambda_{i} c_{i}(x) + \frac{\mu}{2} \sum_{i \in \mathcal{E}} c_{i}^{2}(x)
$$
Now, this idea is actually very important if we want to understand sequential quadratic programming (apparently).

#### Chapter 18
We consider two ways of getting the SQD solution.
In the first, we formulate a multi-dimensional KKT problem. We solve the problem (by taking gradients) but then realize that we can solve for the optimality condition using Newton's method, so we go ahead and take gradients again (a Jacobian in this case, since we are in the multi-dimensional case). Newton's method then gives us the result that we want!
There is another way we can get to this problem:

![[Screenshot2025-10-23_17-53-47.png]]
The above equations just make intuitive geometric sense as a quadratic programming problem. We are trying to take the step $p$ that linearly gets us from where we are $x_{k}$, and moves us such that our constraint $c_{k}$ moves to zero, since it evolves linearly in $A_{k} p$ since $A_{k}$ is the Jacobian of $c(x)$ at $x_{k}$.
18.7a, then says that we want to minimize $f(x)$ (which we should) but the hessian term includes the amount that $c(x)$ will change (non-Linearly), which is then avoided as well!

![[Screenshot2025-10-23_17-53-55.png]]
Then here, we simply treat it as a KKT problem in $p$, which we then solve (with $l$ being the KKT problem in this one).

### Sequential $\ell_{1}$ Quadratic Programming for Nonlinear Model Predictive Control
https://www.sciencedirect.com/science/article/pii/S2405896319301934

- Bolza: Form of problem where the function we are trying to minimize is the sum of an integral integral (sum) of some function over the timescale and then a function of the ending time/location.
- Shooting solution to ODE: Having fixed u(t_0) = u_0, you try around different values for u'(t_0) until you get the desired u(t_1) which then solves the boundary condition for the specified values u_0 and u_1. 
- Multiple shooting: you break apart the problem into time steps. You solve a bunch of shooting problems simultaneously, updating your guesses for the y values where your shots get stitched together. (Might have to do more reading if you haven't before this isn't a sufficient explanation I think).
- Trust Region Algorithms: Unlike line search where we fix a direction and then choose how far we want to go along it, here we fix a step size and choose the direction we want to go. The sensitive computation determines how far this step size should be.

### Improving Drone Racing Performance Through Iterative Learning MPC
#### Abstract
Some terms I would like to hammer down
- Real-time compatible: You compute your next control step in time for the state change
- Time optimal traversal: you aren't just optimizing over a small amount of time, but rather over the entire track
- Safe traversal: computing constraints is difficult and expensive, costs time.
- Centerline Adherance: making sure your path goes through the centers of the corridors
- Adaptive cost function: Your (For instance) LQR optimality function can change and adapt over time
- Safe set: set of states from which you know a safe trajectory to the goal exists.
##### Frenet-Serret Formulas
- If you have a differentiable curve, instantaneously, the curve lies in a plane (unless it is a line, in which case it lies in infinitely many planes). There are three vectors of interest: the vector tangent to the curve, $T$, the vector perpendicular to the tangent in the plane, $N$, and the vector perpendicular to both of these, $B$.
- There are intuitive formulas which descirbe how to derive these, and how to derive them from each other.
	- $\vec{T} = \frac{d \vec{r}}{ds}$
	- $\vec{N} = \frac{\frac{d \vec{T}}{ds}}{\left\lvert  \frac{d \vec{T}}{ds}  \right\rvert}$
	- $\vec{B} = \vec{T} \times \vec{N}$
	- The curvature $\kappa$ is simply defined as $\| \frac{d \vec{T}}{ds} \|$.
	- The center of curvature can then be computed as $r(s) + \frac{1}{\kappa (s)^{2}} \vec{T}'(s)$.
	- The torsion is defined as $\tau = - \frac{d\vec{N}}{ds} \cdot (\vec{T} \times \vec{N})$, and it shows how quickly the curve is twisting in space (so that the plane that the curve is in is changing.)
- Then, the Frenet-Serret formulas are given by:
  
  ![[Pasted image 20251018125658.png]]
- (Relatively intuitive)

- Back to the paper: “A Cartesian-based formulation that accommodates safety constraints without the singularities or integration errors associated with Frenet-frame transformations.”
	- If we are in the Frenet frame, our co-ordinate is centered at the point on the track we are trying to follow that we are hoping to be at. This is $s$. Then, we measure our deviation along $\vec{N}$ and $\vec{B}$, for the deviations $d$ and $h$, which we are trying to minimize.
	- In order to compute $s$, we have to integrate along the curve to figure out how far along it we are, which leads to deviations.
	- Finally, Frenet frames in general have the problem that when your curve is a strait line, then you have zero curvature and so you can't really comptue $\vec{N}$ or $\vec{B}$: you get a singularity.

