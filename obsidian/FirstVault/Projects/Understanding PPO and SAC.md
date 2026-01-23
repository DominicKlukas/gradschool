Phase 1:
- One clean PPO from scratch (no framework to help)
	- Gymnasium Cartpole
	- Single File
	- Minimal Logging
	- Focus: Rollout buffer, GAE, PPO loss, reproducibility
Phase 2:
- SAC via CleanRL
	- Delete and rewrite
		- replay buffer
		- target update logic
	- Keep: Training Loop, Logging
	- Verify curves match
- Integrate:
	- Optuna Ask/Tell
	- Add pruning
	- Handle crashes/retries
	- Structured outputs per trial