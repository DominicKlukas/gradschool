---
tags:
  - technical_library
title: "Physically Embodied Gaussian Splatting: A VisuallyLearnt and Physically Grounded 3D Representationfor Robotics"
authors: Jad Abou-Chakra, Krishan Rana, Feras Dayoub, Niko Sunderhauf
bibtex:
pretty_cite:
link: https://openreview.net/pdf?id=AEq0onGrN2
topics: Physics, Simulation, Robotics
reading_lists:
projects: Physics Aware Learning
type:
to_read: false
stars:
---
# Introduction
- Physics in a robot's world obeys laws, which gives us useful information, but most world representations don't encode/obey those laws.
- Particle based physics simulators do. In this paper, we initialize a particle based simulator with RGBD camera, and run the simulation, correcting it with RGB camera observations.
- 3D Gaussians are used to render the images from the model, which then allows us to compare images and correct error.
- Here, the loss is computed with renderings. Only RGB is used to compute loss at times after t=0. At t = 0, RGBD camera is used to initialize the particle simulator.
- Differs from the previous paper in the physics simulations that they use. Here, constraints are enforced: we guess the new positions based on the forces we know, and when constraints are violated, we add "corrective" forces. There, a simple spring model is used to compute forces/acceleration (spring coefficient, damping coefficient, rest length, external force on particle, all must be learned) which then update the velocity. External force includes collisions and gravity.
- User labels the first images into "instance masks", so that particles in the depth map are partitioned to the correct object. The way that the model for the individual items is built up is quite interesting: After segmenting, a "bounding box" for the different objects is generated. This is filled with 3D Gaussians, and which are then removed in order to minimize difference of rendered images from ground truth... therefore, unobserved regions of the objects will be filled with Gaussians. Interesting. Not sure what happens to them after: paper says opacity can be decreased.
- The Gaussian's positions are continually being updated from the RGB images.