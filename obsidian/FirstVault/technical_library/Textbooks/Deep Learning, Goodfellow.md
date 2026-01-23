
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
We observe the following properties used in normal implementations:
- There are typically multiple channels in hidden features, with one kernel for each feature.
- Stride, and padding, affect the dimensions of the output vectors. If we don't pad at all, the convolution is called "valid"; if we pad such that the input and output dimensions match, we get a "same" convolution; if we pad such that each pixel is used in the same number of output pixels, the layers grow, and we get a "full" convolution. We typically want something between same and valid.
### Locally Connected Layers
- Same subset of edges are non-zero as for a convolution, but they are not "tied together"
- Intuition: you know that the features may exist in different regions but we do not require them to be the same in different regions because we don't expect them to show up in different regions.
- Tiled convolution is a mix between the two, where we switch between different kernels for different output pixels.
### Backpropagation
- Given the partial gradient w.r.t. the output of a layer, we use the chain rule to determine the derivative w.r.t. the kernal parameters and also the inputs.
### Structured Outputs
- We need not only use classifications vectors... we can use more complicated outputs, like full on pixel maps that segregate regions of the image into different classes

Convolution can be helpful when you don't know the size of your input, but you do know that, however long it is, it is made up of the same "stuff" the can all be searched for the same types of features.

There are also techniques we can use to make convolution faster: applying Fourier transforms + scalar multiplication + inverse transform, or simplifying kernels that are the outer product of vectors (so instead of having the kernel be a matrix of a dimension d (with some scalar to the power d parameters) it is the product of d vectors.

Also, training the first kernel layers (that identify the features) can be the most expensive part. Instead, we can fix them, by either initializing them to be random, or to look for edges of certain coarseness.
Finally, we can also do "k-means cluster", which looks for the features which best match the patterns found in the images.
However, these approaches are becoming obsolete, as computing power and data are no longer as scarce.

Finally, CNNs were the first networks that were efficient enough to be effective when we had less computing power... other networks took too long to train so researchers saw no promise and gave up earlier than they should have (MLPs and Backprop were considered to have failed), but now that we have more computing power funnily enough their experiments have been deemed successful though they thought they failed.

## Chapter 10 Recurrent Neural Networks
Main point: they process sequential data.
The way they do it: you have a function $f$ parameterized by $\theta$.
Then, you feed previous outputs back into $f$ with a time delay: $f_{t+1}(f_t, x_{t+1})$, where $x$ is the input.
