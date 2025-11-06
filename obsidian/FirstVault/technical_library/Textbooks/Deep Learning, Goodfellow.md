
Unfortunately, I didn't really take notes (but I did grow in understanding) in reading the first 7 chapters, but I did grow in understanding. A quick review and the content should come back to me pretty quickly. From now on, I will take notes.


## Chapter 9 Convolutional Networks
This chapter discusses:
- Motivation behind CNNs
- Pooling
- Variants of CNNs
- How to apply to different datatypes
- The basis in neuroscience
- Making CNNs efficient

### Convolution and Motivation
Feature map: a hidden layer of an NN.
We don't worry about whether the argument in the convolution is $f(t - a)$ or $f(t + a)$... since then the NN will just learn a flipped function anyways.
Advantages
- Sparse: If your kernel is small, then the multiplications per row in a matrix multiplication is the number of rows times the width of your kernel
- Parameter sharing: since parameters are tied together, this gives us even fewer parameters to learn!
- CNNs are equivariant to translation: if $f$ is the application of our CNN, $g$ is a translation operation and $x$ is our data, then we get $f(g(x)) = g(f(x))$.
Receptive field of an output unit: set of inputs that affect the output.

### Pooling
After going through convolutions, the function goes through a detector stage (which is the name for the non-linear activation function being applied) and then a pooling function. A pooling function is applied to a rectangular region. Max pooling takes the max value in a rectangular region. But you can also take averages, or weighted averages, or the $L^{2}$ norm of a rectangular neighborhood.
- Pooling adds location invariance: if you are doing max pooling, for example, a translation will move the location of the max. But as long as it does not move too much, it will stay inside of the region that you are taking the maximum over.
- The size of the regions we pool over can vary dynamically (for example, the four quarters of an image) so that we can account for different input sizes!

Conceptually, pooling and convolution are infinitely strong priors that encode information about the topology of our data. If we permute the pixels in the image randomly, a permutation invariant network could still come to the same conclusion (like an MLP), but a CNN cannot!

## Variants of the Basic Convolution Function
