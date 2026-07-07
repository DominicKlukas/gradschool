Here, I want to write out my complete understanding of equivariance, where it stands, and the problems associated with it.

Right now, in applications that suffer from small amounts of data, high sample efficiency and generalization is required. Sample efficiency relates to how much data you need to learn a specific policy/train a model, and generalization deals with how well data in one domain can help you train a model that succeeds in domains that you have never seen before.

If global symmetries are present in the statement of your learning class, so that you have a simple mathematical (typically linear) description of the way your symmetry acts on your input space, and on your output space, with a finite group, you can then construct a network by using a lifting convolution, and then group convolutions between group equivariant non-linear layers to construct your networks so they strictly obey symmetries as an inductive bias.

If your symmetry is not represented by a finite group, then in certain cases, there are analytical ways of decomposing your signal into a basis where the continuous group behaves nicely. (Steerable Kernels)

The problem with this, is that these symmetries are nice when they exist in the wild, but often they do not, or they may not be so simple. Dian Wang's lab looks at such applications, but again they are restrictive.

What are the main problems?
- Finding new symmetries that apply more broadly that will result in larger sample efficiency/generalization gains.
- Having a more clear definition for partially equivariant environments.


Can we fine tune the mapping between joint space and Cartesian space? How can we deal with situations where the relationship between the joint space and the observed environment is really complicated, but we are trusting the neural network to abstract away nuisance information in a nice way? Can we apply the principles of latent symmetry being present and using equivariant networks somehow there anyways?

Can we apply lie groups described by vector fields to multi-agent reinforcement learning, perhaps to enable individual agents to have a model of the other agents?

What unique problems happen with equivariance in dealing with contact for robotics? Can equivariance help us learn how to learn appropriate contact dynamics more quickly? Does this inevitably require really good hardware?