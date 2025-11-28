# Equivariant RL Project Notes

## 🧠 Theory

### Discrete vs Continuous RL
- Need a more rigorous treatment.

### Equivariance and Physics Priors
- **Goal:** Equivariance of robot manipulators with physics priors for smooth, gentle movement.  
- **Extrinsic equivariance:** equivariant under *image transform*, not *object transform*.  
- Many policies learn *grasp positions*.

### Relevant Papers

#### World Model / Meta-RL
- *Meta-World: A Benchmark and Evaluation for Multi-Task & Meta-RL*

#### Equivariance
- *E(n)-Equivariant Graph Neural Networks (EGNN)*  
- *SE(3)-Transformers*  
- *Equivariant Goal Conditioned Contrastive Reinforcement Learning*

#### Physics-Structured Priors
- *Regularizing Action Policies for Smooth Control with RL*  
- *Smooth Imitation Learning via Smooth Costs and Smooth Policies*

#### Other Cool Directions
- Equivariant diffusion and flow models.

---

## ⚙️ Design Decisions

- Meta-learning: ❌ (No)  
- Online vs Offline: ✅ Online (use SAC for sample efficiency)  
- Behavior cloning: ❌ (Not RL)  
- Benchmark: PyBullet / RLBench — pick one paper and follow it closely. 
- CleanRL and symmetry breaking?

---

## 💻 Cluster & Environment Setup

### SSH / Login
```bash
ssh -Y klukasd@fir.alliancecan.ca
```
- Use DUO authentication.

### Micromamba Setup
```bash
eval "$(micromamba shell hook -s bash)"
micromamba create -p /project/def-cneary/klukasd/mamba/envs/equirl_310 python=3.10 -c conda-forge
micromamba activate /project/6107222/klukasd/mamba/envs/equirl_310
micromamba install -c conda-forge -y attrdict3 GitPython numpy pybullet scikit-image scipy tqdm dill more-itertools opencv scikit-learn pytorch torchvision matplotlib-base
```
Note: I am no longer using micromamba/
### Notes
- Package install failures on compute nodes likely due to low RAM → request >3 GB next time:
```bash
salloc --time=1:0:0 --mem-per-cpu=3G --ntasks=1 --account=def-cneary
```

For testing code with multiprocessing
```
salloc --account=def-cneary --cpus-per-task=4 --mem=8G --time=0:15:00
```

### File Transfer
Run this on the local computer to copy files to and from the cluster.
```bash
scp -r ~/mv_folder klukasd@fir.alliancecan.ca:~/
scp -r /equi_rl klukasd@fir.alliancecan.ca:~/project/
```


```
events.out.tfevents.1761688043.fc30671.1024394.0
```
---

## 🧩 Equi_RL Code

### Test Commands (CPU)
**CNN baseline**
```bash
python main.py --env=close_loop_block_pulling --planner_episode=100 --dpos=0.02 --drot_n=16 --alg=dqn_com --model=cnn --batch_size=32 --buffer=normal --lr=1e-4 --gamma=0.95 --device_name=cpu
```

**Equivariant model**
```bash
python main.py --env=close_loop_block_pulling --planner_episode=100 --dpos=0.02 --drot_n=16 --alg=dqn_com --model=equi --equi_n=4 --batch_size=32 --buffer=normal --lr=1e-4 --gamma=0.95 --device_name=cpu
```

### Notes
- `lie_learn` deprecated → not needed for SO(3) work.  
- Copied and patched `escnn` locally.  
- Works locally and on cluster.

---

## 🎮 Atari / PPO Code

### Environment Setup
```bash
pip install gymnasium[atari]
module load gcc openc
```
Install ROMs:  
https://github.com/Farama-Foundation/AutoROM

### Request GPU
```bash
salloc --account=def-cneary --gres=gpu:h100:1 --cpus-per-task=8 --mem=24G --time=2:00:00
```

### TensorBoard
```bash
scp klukasd@fir.alliancecan.ca:/home/klukasd/project/atari_experiment/runs/ALE/Breakout-v5__ppo_atari__1__1761688043/events.out.tfevents.1761688043.fc30671.1024394.0 ~/logs/
tensorboard --logdir logs/
# Then open http://localhost:6006/
```

Here is the sh file I use to run the cluster
```
#!/bin/bash
#SBATCH --account=def-cneary
#SBATCH --gres=gpu:h100:1
#SBATCH --cpus-per-task=32
#SBATCH --mem=30G
#SBATCH --time=4:00:00
#SBATCH --output=%x-%j.out  # optional: logs to <jobname>-<jobid>.out
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export BLIS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
module load gcc opencv
source ~/project/atari_experiment/.venv/bin/activate
python atari_experiment/ppo_atari.py
```


---

## 📚 RL Theory Notes

### Policy Optimization Overview

#### Vanilla Policy Gradient
\[
\hat{g}_{k} = \frac{1}{\mathcal{D}_{k}} \sum_{\tau \in \mathcal{D}_{k}} \sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}(a_t|s_t)|_{\theta_k} \hat{A}_k
\]

#### TRPO
\[
\theta_{k+1} = \arg\max_\theta \mathcal{L}(\theta_k, \theta) \text{ s.t. } \bar{D}_{KL}(\theta|\theta_k) \le \delta
\]

#### PPO
- First-order variant of TRPO.
- Two forms: *Penalty* and *Clip* (clips overly large updates).

---

## 🧭 E(2) CNN Notes
- **Point group:** fixes a point (rotations, reflections).  
- **Field type:** datatype containing group + representation info; defines channel dimension.  
- **Gspaces:** specify how the group acts.  
- **ReLU:** works with regular reps (permutation-equivariant).  
  Non-regular → custom nonlinearity needed.

---

## 📅 Timeline Highlights

### 2025-10-02
- Goal: get code running on Anaconda.
- Learned cluster basics.
- Hit package version issues → ask Cyrus about cluster installation workflow.

### 2025-10-03
- Fixed install using micromamba.
- Equi_RL baseline runs locally.
- Runs successfully on Compute Canada.
- Next step: reproduce paper experiments → reimplement full stack.
- Plan to test PPO with CleanRL.

---

## 🧾 Misc Notes
- “Cool stuff”: equivariant diffusion / flow models.
- “Sick Days”: read code (`main.py`, other files).
- Will set up a spreadsheet for trials to match the paper.
- Eventually reimplement full stack from scratch.



### Atari Training Logs
---
001
- Going to try messing with the learning rate, by keeping it constant, to see if that will result in better late game learning.
002
- Changed learning rate from 2.5e-4 to 1e-4, and turned anneal_lr off, to see if that helps with late game. Didn't work. Both plateaued and was very noisy.
003
- `num_envs=32, num_steps=256, num_minibatches=8`
- `update_epochs=3`
- `clip_coef=0.2`
- `ent_coef=0.02`
- `learning_rate=2.5e-4, anneal_lr=True`
- `target_kl=0.02`
- Rationale: larger batch + fewer epochs = stabler critic; wider clip keeps useful updates.
004
- `num_envs=32, num_steps=256, num_minibatches=8`
- `update_epochs=3`
- `clip_coef=0.2`
- `ent_coef=0.02`
- `target_kl=0.02`
- `learning_rate=1e-4, anneal_lr=True`
005
- `num_envs=32, num_steps=256, num_minibatches=8`
- `learning_rate=5e-5, anneal_lr=False`
- `update_epochs=4`, `clip_coef=0.2`, `ent_coef=0.02`, `target_kl=0.02`
006
`num_envs=32, num_steps=256, num_minibatches=8`
- `update_epochs=3`
- `clip_coef=0.2`
- `ent_coef=0.02`
- `learning_rate=2.5e-4, anneal_lr=True`
- `target_kl=0.02`
- `gamma=0.995`, `gae_lambda=0.97`
007
**E — Longer rollouts, same batch (variance cut)**
- `num_envs=16, num_steps=512, num_minibatches=8`, `update_epochs=3`
- `clip_coef=0.2`
- `ent_coef=0.02`
- `learning_rate=2.5e-4, anneal_lr=True`
- `target_kl=0.02`
- Rationale: fewer resets per update, better bootstrapping for critic.
008
- `num_envs=32, num_steps=256, num_minibatches=8`
- `update_epochs=3`
- `clip_coef=0.2`
- `ent_coef=0.02`
- `learning_rate=2.5e-4, anneal_lr=True`
- `target_kl=0.02`3
- `total_steps=80,000,000`
010
https://www.kaggle.com/code/auxeno/ppo-on-atari-rl
Matched the settings on this website as good as I could


## Novermber 12 Meeting
1. PPO satisfies this equivariance property
	1. The value function has to be group equivariant
	2. Our construction of a PPO policy and value function, given a shared backbone, satisfies the conditions for group equivariance
	3. Why wouldn't they use equivariant PPO

## Mujoco Code
- On CleanRL RPO is what is being used... so will try and use this algorithm instead. Apparently it is strictly better.
- module load mujoco