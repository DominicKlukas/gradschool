Kalman filtering is when you take the weighted average of a position update of your system derived from physics and a measurement that you take, weighted by how certain you are about both of them.

A bayesian network is a directed graph which depicts the probabilistic relationships 
between random variables.

Bayesian filtering is when we use Baye's law to make a prediction we have about some event A better.
Recall that: P(A|B) = P(B|A)P(A)/P(B)
This shows up, for example, when we are solving MDPs as LP problems.

PID tuning, is when you have a closed loop system whose input into the controller is e = r - y, (desired position vs position you are at), and the controller responds with an input which is the sum of three terms: K_p * e, K_p/T_i* int e, K_pT_d * $\frac{d}{dt}$e. This was inspired by watching how helmsmen steer their ships: 
- if you are drifting off course constantly, they more and more aggressively steer on course to correct if they can see that they aren't making any progress (integrate)
- they obviously steer if they are far from where they want to be (proportional) and 
- if they can see that the rate of change of their value is too quick, they may reduce it in anticipation. Indeed: if this derivative is negative (too negative because changing too quickly) then you will have a decrease in the rate at which it is trying to change. If the derivative is positive, then you are increasing your distance from your desired point and you want the derivative to increase the input to help you get back on track.