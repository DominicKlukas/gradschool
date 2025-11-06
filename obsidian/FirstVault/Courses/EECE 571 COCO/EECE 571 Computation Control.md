There were a set of topics that I wanted to look into, that were mentioned in the first lecture. I would at least like to have a basic idea of what it is about.
### Unknown Terms
- Optimal Control
- Centralized Control
- Model Predictive Control
- Bang Bang Control
- PID Control
- Feed forward Control
- Distributed Control
- Multi-Agent Control


# Engineering Flowchart

See on Google drive.
## Weeks 1-2
We are going to be looking at convex optimization. I started by reading [[Convex Optimization, Boyd]] by Stephen Boyd.

## Convex Optimization
What are computers good at?
- Linear algebra
- Fixed point iterations: $x^* = f(x^*)$.
What is an optimization problem?
$$ \text{minimize}_{x \in \mathbb{R}^n} f(x)$$
$$\text{subject to } x \in \mathcal{X}$$
Here, $\mathcal{X}$ is called the constraint set. It is typically described in terms of inequalities/equalities.

Next, we look at convex functions. Must have a convex domain to be well defined and then satisfies the obvious definition.
We define level sets and sublevel sets:
$$ L_c = \{x | g(x) = c\}$$$$ S_c = \{ x | g(x) \leq c\} $$
If we have a constraint domain, then it is enough to show $\nabla f(x*)(y - x*) >= 0$ for all $y$ within our constraint set.

This course is not about convex optimization: we will take them for granted. The keywords are
- Iterative gradient-based algorithms
- Interior point algorithms
- Lagrangian: function whose saddle-point solves KKT
- Iterative algorithms to solve (KKT)

## State Space Models
Optimization variables are $x_t$ and $u_t$, for $t = 0, 1, ..., T$.
The constraints are linear: $x_{t+1} = A x_t + B u_t$.
The cost function is $$ \sum_{t=0}^{T - 1}(x_t^T Q x_t + u_t^T R u_t)  + x_T^T S x_T$$
Open loop control: all of your actions are determined at the start, so if something changes or goes wrong then your solution is no longer valid.

What is a state space model?
$$ x_{t+1} = f(x_t, u_t)$$
$$y_t = h(x_t, u_t)$$
$x_t \in \mathbb{R}^n$ is the state, which tells you everything you need to know about the system (internally, so measured quantities). $u_t \in \mathbb{R}^n$ is the input (external drive). $y_t \in \mathbb{R}^p$ is the output, so these are the things that you measure.
Markov means that the future states depend only on $x_t$ and $u_t$.

Parallel interconnection and series interconnection are both single input single output. Feedback interconnection is multiple input multiple output.
We can compute such a trajectory iteratively.
LTI systems are linear and time invariant. They are given by matrices.

Computing trajectories of a linear time invariant system is a potential final exam problem.

Equilibria: $x_e = f(x_e, u_e)$. Then, $y_e = h(x_e, u_e)$. However, we can have stable and unstable equilibria. We have a formal mathematical way of describing this: $\forall \epsilon > 0, \exists \delta > 0$ such that $|| x_0 || < \delta \implies ||x_t || < \epsilon \forall t \geq 0$. Asymtotically stable if stable and $\lim_{t \to \infty} || x_t || = 0$. Let $V$ be a real-valued function such that $V(0)$ and $V(x) > 0$ for all $x \neq 0$. Then $V(f(x)) < V(x)$ for all  $x$.

What are the equilibrium conditions for LTI systems?

$$x_{k+1} = Ax_k + Bu_k$$
Recall for linear algebra that if $x_t = A^t x_0$, then we know that the system is stable if the max eigenvalue is less than 1 (this is different than the spectral radius). A way to check that this is the case, is to show that for any positive definite matrix $Q$, there exists some positive definite matrix $P$ such that $A^T P A - P = - Q$. The way to think about this formula, is $Q$ conceptually describes the rate of energy loss as we take 1 step in the direction of A, for any vector $x$ (it's a quadratic operator). Then, $P$ is a potential function, telling us what this energy will be. Them being positive definite means that the energy only increases as you go away from the origin. So, there is a potential function which mimics the behavior of A (and so is stable). The energy is given by $x^T P x$ (a quadratic function) and so $(Ax)^T P (Ax) - x^T P x$ will give us a one step change in energy.

# COCO Tutorial
See the notebooks on the Dropbox page.

# Dynamic Programming and LQR
- We consider optimal control, and ways to solve it.
- We consider dynamic programming, and Bellman's principle: the optimal path, whatever the first step, will have the second step onwards be optimal considering you start from the state the first step gets you to.
- You solve by doing backwards induction, after breaking the problem into stage problems.
- If the decision set $U_t$ is convex, and $g_t$ is convex in $u_t$, then $V_{t+1} \circ f_t$ is convex in $u_t$, and we have an easy problem to solve!
### Linear Quadratic Regulators
Suppose we have decision variables ${x_t}_{t=1, 2, 3, 4..., T}$ and ${u_t}_{t=0, 1, 2, ..., T-1}$. The constraints are then $x_{t + 1} = Ax_t + Bu_t$. The cost function will be written as follows

$$ \sum_{t = 0}^{T - 1} (x_t^T Q x_t + u_t^T R u_t) + x_T^T S x_T $$
where Q, S are positive semi-definite, and R is positive definite, so we have no sub-spaces where u may be zero in some dimensions.

We have that for the very last step, our reward is just V = x^T S x.
Then, we can do recursion, by plugging in x_{t-1} into the expression x_{t}, and plug and chug, computing a gradient w.r.t. u to get the minimum, to show that optimal cost V is a quadratic.
It gives us a nasty expression, but it is recursive, and then it can be computed.

If f(x, u) is convex in (x, u), then if we define a function $\varphi(x) = \min_u f(x, u)$, then the function is convex in x. This is a theorem that quickly proves that V_t is convex, but proving it algebraically plops out the Ricatti equation, which computes the optimal reward functions with respect to $x_t$.

We look into the computation cost of such a solution method.

We can analyze these solutions with LTI system theory (arguing about things like stability).

#### Infinite Horizon
Now, our decision variables are infinite. How we define this? Also, we worry about the convergence of our cost function.
A system $x_{t+1} = Ax_t + Bu_t$ is stabilizable if $\exists K \in \mathbb{R}^{n \times m}$ such that $\rho (A + BK) < 1$.
This means, there exists a feedback law $K$ such that the closed loop system with feedback $u_t = Kx_t$ will give us a system that is stable. In particular, this will give us the system equations $x_{t+1} = (A + BK)x_t$. Then, we prove that there is a sequence of inputs with finite cost. We simply plug the expression for $x_t$ and $u_t$ into our cost expression.
After we play around with the C.S. inequality, we proceed to prove that the cost terms are bounded by a geometric series (after some point) and then will converge.
How do we compute this in real life? We do iteration!

We argue about the computational cost.

We need to have costs on unstable modes, otherwise we will have unstable systems.


# Model Predictive Control
- Rated, in a survey of controls experts, MPC is going to be the type of control which will grow the most in terms of use and importance in the future.
- You simulate the horizon into the future for different future actions, and then you take the action which results in the best final outcome.
- Once that action is taken, you start again, computing the new trajectory.
MPC is a static, nonlinear, time-invariant feedback control law
- Static means no memory. 
- Nonlinear - in principle, not a linear function. Will look at interesting cases.
- Time invariant: if you start from the same $x$, then at any time $k$ you will get the same solution.
- If you don't have an integrator in the loop you can't have zero tracking error. Can we have zero tracking error with MPC?
One silly case is the following problem:
$$ \min_{x,u} \sum_{k=0}^{K-1}a^k|u_k|^2 + |x(K)|^2, |a| <1$$ It turns out, that here, $u_k = 0$ for all $k$ until $K-2$, since we don't want to act (since it is more expensive than acting later). Since $K$ steps away is always updated, this never comes and we don't solve optimality!
Be careful when you set up your cost and constraints.
How to compare them with LQR?
- Finite vs infinite horizon

Now, we can compute $u_0^* (\cdot )$ offline or online. Offline is often intractable because of how many values you have to store. Online only works if your solver's timescale is smaller than the timescale of your iterations.

We explicitly compute an MPC problem.
Explicit computation, means that for every input $x$ we compute the output that the MPC would have us do. The problem with this, is that there are many combinations of slack/tight constraints that we have to try. We have to break down every single one of those regions, and solve the solve optimally for each of them. This can be very expensive, as there are exponentially many regions as we add more and more constraints.

Next, we look at the stability of MPC. We go back to Lyapunov. Essentially, if we can show that there exists a function describing some sort of pseudo-energy of our state that decreases along trajectories, and has a minimum, then we can use analysis to show that this function is stable at that minimum.
In the context of MPC, a convenient function is the infinite horizon const function (which isn't used in the algorithm, but can be used to prove stability as a Lyapunov function), after sufficient constraints are applied.
We can also consider systems where the dynamics leads us to 0 after $K$ steps, but this is a strong requirement and won't apply for all systems.

If we have steady state disturbance, we can add an integrator after our MPC. What this does, is that the input dynamics are given by $u_{k+1} = u_{k} + \Delta u_{k}$. They are connected in parallel, in this way, so that this is the result of our action. If we know what the steady state is beforehand, we can simply do a change of co-ordinates. This works just as well. Also, if you have a state you want the system to go to, you can set it to be like that in your cost function.

If you have disturbances and errors in your measurement, you can add these into your model, such as your dynamics model, or by creating an estimator which then adjusts your steady state goal in order to get your controller to try to make it to the right place.

## Economic MPC
We can have a system: $$
\text{Steady-state optimization} \to \text{MPC} \leftrightarrow \text{Plant}
$$
Here, we solve a problem that takes a long time (the steady state problem) before optimizing in the short term with MPC.

Often, we have many goals in our problem.
- Economic aspects
- Regulatory Specifications
- Use of resources
Our problem may not be quadratic either!

How can we motivate our formulation? The steady state motivation can be to solve a long term trajectory, and the MPC stays on the trajectory.
Pros and cons:
- Offline or slower time scale for the steady state optimization
- Fragile: cost not reduced during transients. (suboptimal cost of the system trajectory).

Economic MPC
- Basically, instead of having a reference trajectory we are trying to minimize the distance from, (which our cost is a quadratic function of), we have more complicated functions of the trajectory which we are trying to minimize, which tells us the cost of a given trajectory.

Robust MPC
- Often you will get exogenous disturbances
- Exogenous - relating to external factors


## Identification 
When we know what our model is (taken directly from physics) then the previous control schemes work well. But if we don't, we have to figure out what our system is from data.

For instance, for LQR we needed the ABCD matrices. In physical systems we can derive from first principles the Markovian state variables (capacitance (charge), current, voltage) or position and velocity.

But often this is difficult. Suppose we are doing an operation on a human. What should our states be? There are many number of factors which could affect our system.

### System Identification

Suppose we are given (told) that there is some state space model underlying our system.
We are given an input sequence $\{ u_{t} \}_{t=0}^{T}$ and the corresponding output sequence $\{ y_{t} \}_{t=0}^{T}$.
Find a system
$$
x_{t+1} = Ax_{t} + Bu_{t}, y_{t} = C x_{t}
$$
Consider the scalar, single-input, single-output system $x_{t+1} = x_{t} + u_{t}$, $y_{t}= x_{t}$.
What happens if we change the units (or coordinates) of the state?
The system is the same, so the input-output behavior doesn't change.

Given data, which co-ordinate system should I choose? It actually doesn't matter. But we should definitely choose a co-ordinate system such that the matrices are easy to work with.

#### SISO
If we are using LTI systems, we can use the impulse response in order to find the total behavior of the system! Since we can simply take the superposition (by LTI) of many time shifted deltas in order to reconstruct any signal, it suffices!

How can we see if two systems, with two different co-ordinate bases, are the same?
So, set $x_{0}=0$ and $u_{t} = \delta_{t}$. Set $\xi_{0} = 0$ and $u_{t} = \delta_{t}$.

By the definition of our system, $x_{1} = B$, and at time 2, we have $x_{2} = AB$, and $x_{n} = A^{n-1}B$. Also, we have $y_{n} = CA^{n-1}B$.

But a similar calculation with our co-ordinate changed system gives us: $\xi_{n} = T^{-1}A^{n-1}B$, where $x_n = T \xi_{n}$. Similarly, even with the different co-ordinates, the matrices cancel out, so that we get $y_{n} = CA^{n-1}B$.

What of it, if we have a different basis for every output?
Instead of fixing a basis, and getting a system for every basis, we can instead consider just the impulse response, and then to compute the system, we do a convolution with the specific input, to get the response for all time.
The problem with this, is that we have to store the impulse response for every point in time!
#### MIMO System
We take the impulse response with respect to delta functions at each input co-ordinate, and we can use this to "build up" the matrices that describe the response of the system, one column at a time.

### Controllability and Observability
Consider the problem driving the system from $x_{0} = 0$ to a target state $\bar{x} \in \mathbb{R}^{n}$. Consider the single input system
$$
x_{t+1} = \begin{pmatrix}
0 & 0 & 0 \\ 1 &  0 & 0\\ 0 & 1 & 0
\end{pmatrix} x_{t} + \begin{pmatrix}
1 \\ 0 \\ 0
\end{pmatrix} u_{t}
$$
What states can we reach by applying $k$ consecutive inputs from $x_{0} = 0$ applying any input?
In this case, all of $\mathbb{R}^{3}$, for instance by applying $(c, 0, 0)$, $(b, 0, 0)$, $(a, 0 ,0)$ consecutively.
We only need to check $n$ powers by the Cayley Hamilton theorem.

Now, how can we get to our target state?
$$
x_{n} = \begin{bmatrix}
B & AB & \dots & A^{n-1}B
\end{bmatrix} \begin{bmatrix}
u_{n-1} \\
u_{n-2}  \\
\vdots  \\
u_{0}
\end{bmatrix}
$$
This matrix has dimension $n \times n \cdot m$. This makes sense, because if the dimension of the input is greater than $1$, then we have more options for the columns we may have.

Also, we can think too about which states can be observed with $y$. $y$ is computed with the matrix $C$. So, we can only detect states which are in the 

---
Recall: we want observability and controllability.
$x_{t+1} = A x_{t} + Bu_{t}, y_{t} = C x_{t}$.
We say that a system is controllable if the rank of the matrix $[B \, AB, \dots, \ A^{n-1}B]$ is $n$.

Suppose we have the Markov parameters of the system. How does one compute a state-space model (integer $n$ and matrices $A, B, C$)? This is called realizing the system.

History: in the past, control theory and circuits were closely connected. So, people would have a desired system response, and they wanted to "realize" the system, finding the resistors/capacitors/inductors which would create this system.

Suppose we have the system:
$$
y_{t} = c_{1} u_{t-1} + c_{2} u_{t-2} + c_{3} u_{t-3}
$$
 We want to find $n \in \mathbb{N}$ and $A \in \mathbb{R}^{n \times n}$, $B \in \mathbb{R}^{n \times 1}$, $c \in \mathbb{R}^{n \times 1}$ such that
 $$
x_{t+1} = A x_{t} + B u_{t}
$$
$$
y = C x_{t}
$$

We potentially have $y_{t} = [c_{1}, c_{2}, c_{3}] \cdot [u_{t-1}, u_{t-2}, u_{t-3}]$.
So, if we take $C = [c_{1}, c_{2}, c_{3}]$, then we are fixing $n = 3$.
In particular, this would require:
$$
\begin{bmatrix}
u_{t}\\
u_{t-1}\\
u_{t-2}
\end{bmatrix}
= \begin{bmatrix}
0 & 0 & 0 \\
1 & 0 & 0\\
0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
u_{t-1}\\
u_{t-2} \\
u_{t-3}
\end{bmatrix}
+
\begin{bmatrix}
1 \\
0  \\
0
\end{bmatrix}
u_{t}
$$
Is the system minimal?
- We need to check whether the two rank conditions we expressed in the previous slide are satisfied.
- Recall that the controllability matrix is given by
$$
\mathcal{C} = [B \, AB \, A^2 B] = \begin{bmatrix}
1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1
\end{bmatrix}
= I
$$
- so this is full rank and we are done! What about the observability matrix?
$$
\mathcal{O} = \begin{bmatrix}
C \\
CA \\
CA^2
\end{bmatrix} = \begin{bmatrix}
c_{1} & c_{2} & c_{3} \\
c_{2} & c_{3} & 0 \\
c_{3} & 0 & 0
\end{bmatrix}
$$
This is full column rank if and only if $c_{3} \neq 0$.

Now, this will work invariably for finite impulse response systems (because we have a finite number of these coefficients $c_{i}$).

### Hankel Matrices
Suppose we have a sequence $u_{1}, \dots, u_{T}$.
Then, the corresponding Hankel matrix is:
$$
H = \begin{bmatrix}
u_{1} & u_{2} & \dots & u_{T - d+1} \\
u_{2} & u_{3} & \dots & u_{T - d + 2}\\
\dots & \dots & \dots & \dots  \\
u_{d} & u_{d+1} & \dots & u_{T}
\end{bmatrix}
$$
What if we have the signal: $u_{t} = \begin{bmatrix} a^{t} \\ b^{t} \end{bmatrix}$. In this case, it would be a 3 by 6 matrix if we had $T = 3$.
Thinking about the dimension, we would get that $\mathcal{H}$ has dimension $p \cdot n \times n \cdot m$.
Each of the elements of the column can be written as the observability matrix times $B$.
But then,
$$
\mathcal{H} = \begin{bmatrix}
C  \\
CA \\
\vdots  \\
CA^{n-1}
\end{bmatrix}
\begin{bmatrix}
B & AB & \dots & A^{n-1} B
\end{bmatrix}
$$
Therefore, $\mathcal{H} = \mathcal{O} \mathcal{C}$! The rank of this Hankel matrix will tell us the dimension! If the system is controllable and observable (or minimial) then the rank of the matrix $\mathcal{H}$ is $n$.

**Minimal** means both controllable and observable, and no other system of smaller dimension is controllable and observable.

The very first element doesn't tell us anything about the matrix $A$, though, observe. Somehow, how many data points that you have.
Now, given a sequence $\{ G_{k} \}_{k \in \mathbb{N}}$ define the extended Hankel matrix:
$$
\mathcal{H}_{k, l} = \begin{bmatrix}
G_{1} & G_{2} & \dots & G_{l} \\
\vdots & \dots & \dots & \vdots  \\
G_{k} & \dots & \dots & G_{l + k}
\end{bmatrix}
$$
How does one factorize $\mathcal{H}$ as $\mathcal{O}$ and $\mathcal{C}$?
You are always entitled to multiply $\mathcal{H} = \mathcal{O} T T^{-1} \mathcal{C}$, so long as $T$ is invertible. This amounts to a change of basis in your state space!

We can take the singular value decomposition of the Hankel matrix to figure stuff out.

How can we determine what our observability and controlabillity matrices are?
One way we can do it is by taking the SVD, taking the square root of the diagonal matrix in the decomposition, and then have:
$$
\mathcal{H}_{k, l} = U_{1} \Sigma_{1}^{1 / 2} \Sigma_{1}^{1 / 2} V_{1}^{T}
$$

By definition of the Observability matrix, the first $p$ rows of the observability matrix is the $C$ matrix, and the first m columns of the $O$ matrix is the B matrix.

The shifted Hankel matrix is given by
$$
\mathcal{H}_{k ,l}^{\uparrow} = \begin{bmatrix}
G_{2} & G_{3} & G_{4} & \dots & G_{l+1} \\
\dots & \dots & \dots & \dots & \dots  \\
G_{k} & G_{k+1} & \dots & \dots & G_{k + l}
\end{bmatrix}
= \begin{bmatrix}
CAB & CA^{2}B & CA^{3}B & \dots \\
CA^{2}B & CA^{3}B & CA^{4}B & \dots  \\
\dots  &  \dots  & \dots & \dots 
\end{bmatrix}
$$
But we can see that this is just $\mathcal{H}_{k, l}^{\uparrow} = \mathcal{O}_{k} A \mathcal{C}_{l}$. This can be seen by writing it all out. Multiply by right inverse of $\mathcal{C}_{l}$ on the right  and the left inverse of $\mathcal{O}_{k}$ on the left.

This is the Kalman-Ho algorithm. We assume that there exists a real LTI finite-dimensional system. We assumed that there is no noise.

## Data-Driven Prediction Control

We started with three dogmas
- Underlying Markovian state
- We know the initial condition
- We have an objective that is quadratic and summable
In those assumptions it was fruitful to study LTI systems and we could compute controllers.
Our next task, was to look at impulse responses, and then try and identify the ABCD matrices of the LTI system.

Now, we are going to challenge the assumption that we need an ABCD system. We can go straight from data to actions.

Systems can be thought of as subspaces (planes in an $\mathbb{R}^{n}$-like space).

If we want to consider how a system evolves through time, (with it's ABCD matrices) then we take an initial state, $x_{0}$, a sequence of inputs at each point in time, $u_{0}, u_{1}, u_{2}, \dots$, and we will get a sequence of outputs, $y_{0}, y_{1}, \dots$.
Then, we will get:
$$
\begin{bmatrix}
y_{0} \\
y_{1} \\
y_{2} \\
\vdots
\end{bmatrix}
= 
\begin{bmatrix}
C \\
CA \\
CA^{2} \\
\vdots
\end{bmatrix}
x_{0}
+ \begin{bmatrix}
D & 0  & 0 & \dots \\
CB & D & 0 & \dots \\
CAB  & CB & D & \dots \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}
\vec{u}
$$
In particular, we can write a matrix for the vector $\begin{bmatrix}u_{0} & u_{1} & \dots & u_{L-1} | & y_{0} & y_{1} & \dots & y_{L-1}\end{bmatrix}^{T}$ as a function of $\begin{bmatrix}u_{0}  &  u_{1} &  \dots  & u_{L-1} | & x_{0}\end{bmatrix}$ by having the identity on top, and then this matrix above on the bottom, as in $\begin{bmatrix} I & 0 \\ C & B\end{bmatrix}$. We will call this the $M$ matrix. Whatever lies in the image of this matrix is a valid trajectory.

Trajectories are admissible if
$\vec{y}_{L} - \mathcal{T}_{L} \vec{u}_{L} =_{?} \mathcal{O}_{L}x_{0}$. This can be solved only when $\vec{y}_{L} - \mathcal{T}_{L} \vec{u}_{L}$ is in the image of $\mathcal{O}_{L}$.

J. C. Willems
- You can see a system as state space equations
- You can see as a result of latent variables (x, ABCD)
- Sets of trajectories that are compatible with the system.

We write: $\begin{bmatrix} \vec{u}_{n} \\ \vec{y}_{n}\end{bmatrix} = \begin{bmatrix} I_{n}  &  0 \\ \mathcal{T}_{n}  &  \mathcal{O}_{n}\end{bmatrix} \begin{bmatrix} \vec{u}_{n} \\ x_{0}\end{bmatrix}$
$M_{n}$ has dimension $2n \times 2n$. $\mathcal{O}_{n}$ has rank $n$ (observability) $\implies$ $M_{n}$ has rank $2n \implies M_{n}$ is invertible. We want this matrix to be invertible so that we can find the initial state that will give us a desired output/input combination.
