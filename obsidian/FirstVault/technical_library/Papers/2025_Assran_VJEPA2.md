---
tags:
  - technical_library
title: "V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning"
authors: Mido Assran, Adrien Bardes, David Fan, Quentin Garrido, Russell Howes, Mojtaba, Komeili, Matthew Muckley, Ammar Rizvi, Claire Roberts, Koustuv Sinha, Artem Zholus, Sergio Arnaud, Abha Gejji, Ada Martin, Francois Robert Hogan, Daniel Dugas, Piotr Bojanowski, Vasil Khalidov, Patrick Labatut, Francisco Massa, Marc Szafraniec, Kapil Krishnakumar, Yong Li, Xiaodong Ma, Sarath Chandar, Franziska Meier, Yann LeCun, Michael Rabbat, Nicolas Ballas
bibtex: "@misc{assran2025vjepa2selfsupervisedvideo,      title={V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning},       author={Mido Assran and Adrien Bardes and David Fan and Quentin Garrido and Russell Howes and Mojtaba and Komeili and Matthew Muckley and Ammar Rizvi and Claire Roberts and Koustuv Sinha and Artem Zholus and Sergio Arnaud and Abha Gejji and Ada Martin and Francois Robert Hogan and Daniel Dugas and Piotr Bojanowski and Vasil Khalidov and Patrick Labatut and Francisco Massa and Marc Szafraniec and Kapil Krishnakumar and Yong Li and Xiaodong Ma and Sarath Chandar and Franziska Meier and Yann LeCun and Michael Rabbat and Nicolas Ballas},      year={2025},      eprint={2506.09985},      archivePrefix={arXiv},      primaryClass={cs.AI},      url={https://arxiv.org/abs/2506.09985}, }"
pretty_cite:
link: https://doi.org/10.48550/arXiv.2506.09985
topics: Video Models, Robotics, Prediction
reading_lists: Cyrus
projects:
type:
to_read: true
stars:
---
## Introduction
A lot of similar ideas to the JEPA philosophy paper. [[2022_LeCun_JEPAMotivationAPathTowardsAutoMI]]

Goal: train a JEPA model beforehand (I am assuming, to learn the embedding and prediction models effectively). After that, train an actor on these representations, on a small amount of interaction data.

Question: how do we ensure that it doesn't learn a bunch of irrelevant information in the representation, and only the information relevant to the task? It learns the information relevant in order to predict that the future video is a continuation...

JEPA is trained, first, with videos. (I am guessing... will see later, that it is training some sort of encoder/predictor strategy). After that, it can recieve further training to:
- Answer questions about videos with language (Language Alignment)
- Classify objects and actions in the videos (Attentive Probe Training)
- Action-Conditioned Post-Training (Planning and Robot Manipulation)

- V-JEPA 2 is the energy model discussed in the paper, which can tell how likely it is that a video y is the completion of a video x. (Self-supervised model). Recall that it does so by training an embedding space for x and y, and training a function that compares the two that takes in some latent variable (which encodes higher level decisions). The way it makes that comparison is by making a prediction of the embedded variable $s_{y}$ given the embedded variable $s_{x}$.
## 2. Pretraining Phase
V-JEPA 2 is trained as follows:
$$
\text{minimize}_{\theta, \phi, \Delta_{y}} \lvert P_{\phi}(\Delta_{y}, E_{\theta}(x)) - \text{sg}(E_{\bar{\theta}}(y)) \rvert 
$$
- The encoder used for $y$ is the same as the one used for $x$, so we don't train both at the same time (hence the stop-grad operator). We also use the exponential moving average of the parameters on the encoder for $y$, so it doesn't update as quickly/right away, to help with exploration I suppose.
- $\Delta_{y}$ is a learnable token that tells the predictor which parts of the video are masked.
- Refer the the JEPA architecture for more details! Except here, we don't have a latent variable $z$ anymore.
- This is more than just an image encoder... the entire (masked) video is the data from which we are making our prediction.
After this, they have all sorts of notes on their data and training procedures.

_The main point is that we have learned an effective video encoder! We may swap out other predictors in the previous sections but we will use the trained encoder representation._

## 3. Action-Conditioned World Model
Autoregressive: finds next state based on all previous states.
Proprioceptive: internal measurements.
We freeze the video encoder, and then train a predictor which is conditioned on robot actions/sensor data.

Question: since it is all unlabelled, how can we derive MPC objectives?

The loss function.
- We use the video encoder as an image encoder (recall that a video is just a still image). From each video frame $x_{k}$ we get some embedded state $z_{k}$. (We freeze the encoder from the previous state).
- We have four frames per second. We measure $a_{k}$, $s_{k}$, and the images $z_{k}$ at each point in time. ($a_{k}$ can be derived from the progression of the states).
- Teacher forcing is when the model is fed the correct sequence of actions up until time $k$ and then has to make a good prediction for $k+1$.
- Rollout is when you have a starting state at $t=1$ and have to make your own predictions up until time $T$ based on your previous predictions for $1 < k \leq T$, and then you compute the loss at the final state (or potentially at every guessed state). In particular, you are given a sequence of actions, and you want to see how the actions will result in your states/videos changing.
We can write these two different types of loss functions as
$$
\mathcal{L}_{\text{teacher-forcing}}(\phi) = \frac{1}{T} \sum_{k=1}^{T} \lvert \hat{z}_{k+1} - z_{k+1} \rvert  = \frac{1}{T} \sum_{k=1}^{T} \lvert P_{\phi} \left( (a_{t}, s_{t}, E(x_{t}))_{t \leq k}\right) - E(x_{k+1}) \rvert_{1}
$$
And, our rollout loss is,
$$
\mathcal{L}_{\text{rollout}}(\phi) = \lvert P_{\phi}(a_{1:T}, s_{1}, z_{1}) - z_{T+1} \rvert_{1}
$$
Here, $P_{\phi}$ only ever predicts the next state: we are overloading notation a little bit, in having $a_{1:T}$ being the result of autoregressivly running the model.
The total loss is the sum of these losses. For rollout we only train 2 timesteps forward.

### Inferring actions by planning
Now that we have trained a predictor that can tell us what latent state we will end up in given a sequence of actions, we can now compute the difference between the state we want to end up in $z_{g}$, and the state we will end up in if we follow a sequence of actions: $(a_{i})_{i \in [T]}$.
That is:
$$
\mathcal{E}(\hat{a}_{1:T}; z_{k}, s_{k}, z_{g}) = \lvert P(\hat{a}_{1:T}; s_{k}, z_{k}) - z_{g} \rvert_{1}
$$
Then, we have $(a_{i}^{\star})_{i \in [T]} = \text{argmin}_{\hat{a}_{1:T}} \mathcal{E}$.

Rest of paper
- Section 4 then shows experimental results which use this action conditioned model!
- Section 5 evaluates the encoder, seeing how good the representations are. Do so by training a classifier on top of it, on the representations which we ran through our encoder.
- Section 6 runs on another benchmark.
- Section 7: use the encoder representations on a VLM.