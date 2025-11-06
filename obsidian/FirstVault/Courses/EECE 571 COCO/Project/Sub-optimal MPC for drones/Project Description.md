## Real-Time Iteration for Aggressive Drone Maneuvers 

Main Idea: Control a drone to follow a complex curvy path as fast as possible 


**The Sub-optimal Angle:** Implement the **Real-Time Iteration (RTI)** scheme, also known as Sequential Quadratic Programming (SQP) for NMPC. The idea is to do most of the hard computational work (linearizing the model, calculating derivatives) _before_ you get the latest state measurement. Once you get the measurement, you only need to solve one QP, making it extremely fast. This is sub-optimal because it's based on a slightly old state, but it's often very effective.

