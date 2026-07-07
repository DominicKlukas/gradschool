## Difficulties with Robotics Manipulators

### Planning/RL Gap
- Nothing beats a classical controller when it comes to the low-level robotics problem.
- If you do use RL to train your model end to end, it can be hard to have good planning unless your model and data are both huge.
- Creating an interface between a low-level RL controller and a planner is difficult.
- Sim to real is difficult... requires really good robots, engineering, and lots of compute.
In summary: the best hope is lots of data/good robots with small sim-to-real gap.

Drones are easier...
- Drones don't struggle with singularities.
- There are many interesting non-military applications: forest fighting, weather, and lifeguards.