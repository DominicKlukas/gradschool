Paper on [world models](https://www.cl.cam.ac.uk/~ey204/teaching/ACS/R244_2022_2023/papers/ha_arXiv_2018.pdf)
## Motivation
Cyrus gave us 6 potential (rough) research ideas on the first day. After some quick chats with GPT, the physics side of things seemed most interested to me. In particular,"developing physics-aware foundation models" struck my attention.

I wanted to understand a little bit the context of the research, so I asked ChatGPT to make a map for me of the different types of research that are going on this field.

Model based RL

System identification: I don't know everything about the real world, and fill the gaps with 
### Context for Physics Aware ML Research
Scientific Machine Learning / AI for Science
└── Physics-Aware Machine Learning (PaML)
	├─ Physical Data-Guided ML (System Identification?)
    ├─ Physics-Informed ML
    ├─ Physics-Embedded ML
    │   ├─ Hamiltonian / Lagrangian NNs
    │   ├─ Port-Hamiltonian NNs
    │   ├─ Neural SDEs
    │   ├─ Neural Operators (FNO, DeepONet, etc.)
    │   ├─ Physics-Aware Foundation Models
    │   └─ Geometric Deep Learning (GDL)
    └─ Hybrid Learning

Here are my personal summaries based on the chats I had, for each of these fields.
1. Physical Data-Guided ML
   Use: Physics simulations.
   Methodology: Doesn't use any prior knowledge of physics: this is merely ML applied to physics systems to learn models from lots of good data.
2. Physics-Informed ML
   Use: Physics simulations/Equation solutions
   Methodology: Uses physics in the loss function. You can use a traditional solver for the inputs you do know to train the network and then in other cases ML extrapolates.
3. Physics Embedded ML
   Use: Dynamical Systems
   Methodologies: Carefully choose architecture to fit well with the use case in question.
4. Physics-Aware Hybrid Learning.
   Use: Physics simulations
   Methodology: In various ways use both results for traditional solvers and ML. For example, in a mechanics simulation use traditional solution for liquids and ML for solid. You might use traditional as a rough guess and ML for refinement. Many different ways stuff might get put together.

I added more bullet points onto Physics Embedded ML, since a lot of Cyrus's papers in the past seem to revolve around this topic.

### Context for RL
These physics aware ML models can then be used as world models, to simulate the state-transition function used in the RL model, that is, $s_t = f(s_t, a_t)$, more accurately to be able to predict future rewards and create better policies.
## Physics-Informed AI course (CPSC 532Z)
### Objective
Next, I want to determine what the Physics-Informed AI course has to offer. That is, what each of the papers that they are reading touches on/is about.

1. [Hu+ 2019] Difftaichi: Differentiable programming for physical simulation  
2. [Macklin 2024] Warp: Differentiable Spatial Computing for Python  
3. [Raissi+ 2019] Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations  
4. [Sharp+ 2023] Data-Free Learning of Reduced-Order Kinematics  
5. [Sanchez Gonzalez+ 2020] Learning to simulate complex physics with graph networks  
6. [Li+ 2020] Fourier neural operator for parametric partial differential equations  
7. [Holzschuh+ 2025] PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations.  
8. [Li+ 2023] PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification  
9. [Xie+ 2024] PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics  
10. [Holderrieth+ 2025] Introduction to Flow Matching and Diffusion Models  
11. [Bai+ 2025] Impossible Videos  
12. [Geng+ 2025] Motion Prompting: Controlling Video Generation with Motion Trajectories  
13. [Li+ 2025] WonderPlay: Dynamic 3D Scene Generation from a Single Image and Actions  
14. [Lu+ 2025] The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

Different topics/use cases covered:
- Differentiable simulators
	- Difftaichi
	- Warp
- Solutions to PDEs
	- PINNs
	- Fourier Neural Operator
	- Data Free Learning of Reduced Order Kinematics
- Numerical physics simulators
	- Sanchez Gonzales GNNs
	- Accurate Physics Simulations from multiple cameras
		- PAC-NeRF
		- PhysGaussian
	- Li 2025, WonderPlay: Dynamic 3D Scene Generation from Single Images and Actions
	- Generating Videos
		- Motion Prompting: Controlling Video Generation
- LLM Performance Analysis
	- Lu 2025: The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery
	- Bai 2025: Impossible Videos
- PDE problem modified to fit inside of a transformer

### Cyrus Papers
1. How to Learn and Generalize From Three Minutes of Data: Physics-Constrained and Uncertainty-Aware Neural Stochastic Differential Equations
   In this paper, the diffusion function in the SDE as well as the parameters (and sometimes form as well) of the drift term are learned.

## Goal: Get a mapping of papers on PAC Nerf

First step: Get up to speed on the papers Cyrus and Sayem are reading.
[[2024_Chakra_PhysEmbodiedGaussianSplattingForRobotics]]
[[2025_Jiang_PhysTwin]]
