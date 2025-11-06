Somehow I bumped into this paper on [control barrier functions](https://arxiv.org/pdf/1903.11199), and it looked interested.

I read the first chapter of Principles of Model Checking.
As far as I understood, the basic concept is
- Writing down the qualitative requirements that you want your program to do in a way that is formally verifiable.
- You create a simplified version of your program (or the parts of your program you NEED to work) in a language that is compatible with your model checker
- Next, you partition the input space into relevant chunks for testing.
- If passes then good! If not, then either your requirements are wrong or your program is wrong.

How DeepSeek rewrote the transformer
Reactive Synthesis
Safe reinforcement learning via Shielding