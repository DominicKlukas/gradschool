# Basic Idea
Application: The radio spectrum is becoming increasingly congested due to IoT, 5g, self driving vehicle to vehicle communication etc. There are many applications of machine learning for optimizing spectrum usage and avoiding interference. 
For our problem we are interested in spectrum monitoring and classification of signals. The simple "hello world" for ML in this is modulation classification, labeling classes such as BPSK or QPSK. I will send some resources about what this means. We can use this to keep the problem simple while innovating on the model.

What is particularly interesting is the input data type. We have IQ samples from a software defined radio (SDR). Either you represent them as real and imaginary or magnitude-phase. 

In my previous work, we simply threw CNNs at these signals, treating the 2xN signal basically as a weirdly shaped image. This approach sort of works but it's definitely lacking. It is very difficult to make a model that can classify signals with any domain shift from the training set, making practical use difficult. Our strategy was to use preprocessing and augmentation, which again sort of works but is not ideal. I think designing a custom architecture for this data type would be useful and likely novel - I have not heard of anything like this during my time in industry.

> [COMMENT] So the idea is that we want to first identity the symmetry involved here, and then design a neural network which exploits this symmetry.

There are several modifications to a signal we would ideally be invariant to. The first is absolute phase. If all the complex samples are phase shifted by the same amount, this is the same signal as before. However, the image style CNN will see a very different input. If we solve this problem that can honestly be the whole project. 
> [COMMENT] I see... this is the symmetry that we are talking about. Let's do it!

The next thing is frequency shifts. If you have an offset career frequency between the transmitter and receiver, you have a different looking signal, but it should still be identified as the same.
> [COMMENT] Another one... nice.

Also, it should not consider absolute amplitude, although you can usually just normalize in pre processing.  ([COMMENT] Agree.)

To start, read up on IQ sampling.
[IQ Sampling Article](https://pysdr.org/content/sampling.html)

# Preliminary Readings
## IQ Sampling Notes
- You have to sample at twice the frequency of the highest frequency that you expect is in your signal in order for you to be able to accurately reconstruct your signal.
- You can multiply signals by a carrier signal $\sin(2\pi ft)$ and $\cos(2\pi ft)$, and then use a low pass filter, to do "downconversion." (Use the product to sum identities... look them up). The low pass filter kills the high frequency term.
- Often, when you do this down-conversion, you get an unwanted spike at 0. So convert to a signal that is centered slightly off from the signals you care about, kill the signal near zero, and then perform another shift.
- You can use the power theorem (power of the Fourier coefficients is the same as the power of the original signal).
## Digital Modulation
- If we just have square "on and off" signals, the frequency domain looks really nasty: it uses lots of bandwidth.
- The reason we want to be efficient with the amount of bandwidth our signals use is because there are limited wavelengths which are practical to use (low frequencies require too long antennas, high frequencies have other hardware issues) and the signals interfere with each other, so the government has to allocate who can use which ones, and in general it is good to use as little bandwidth for your signals as possible.
- ASK: you multiply a binary square signal by a sinusoidal signal.
- PSK: you modify the phase of your signal to be your symbols.
- QPSK: you have 4 symbols, each 90 degrees apart.
- QAM: You modify both the amplitude and phase of your signal, at the given frequency.
- FSK: kind of like FM radio.
- Differential coding deals with the problem that we might not know which symbol is 1 or 0. The way it works, is you look at the difference between the current symbol and the last, and assign the symbol 1 if there was a change and 0 if there was no change.
	- This will lead to 2 bit errors for every error in symbol... which is not good.
	- To get this to work for PSK you measure difference in phase, not just change in applitude.

## Papers

Here's some stuff on modulation classification. You can see they are talking about CNNs and stuff. The dataset that is mentioned might be useful, however I can code up synthetic dataset generators quickly (I've done it before) and this will give us much more control and flexibility
https://www.arxiv.org/pdf/2502.05315

### AI/ML-Based Automatic Modulation Recognition
- AI models are better for automated modulation recognition because they can recognize intricate complex features that cannot be mathematically formulated in a straightforward way.
- More complex models are feasible because of better computing power.
- Learning must be supervised... so a labelled dataset is required.
- Purpose of this paper is to compare current models, show their constraints, which should tell us how to make better models.
- Results
	- Biggest model isn't necessarily best... certain architectures perform better
	- All models struggle with SNR... work must be done here
	- Not one model is best with all modulation types. GFSK is difficult for all of them.
- Methods to improve the performance
	- Train first on low noise signals and then increase your training set to more noise.
	- They show that, when your training data includes noise, but not the full amount of noise in the extremist samples, you may get slightly better performance (a bit questionable though, since the result isn't super significant).
	- Architecture variations:
		- They add LSTM and GRU (a type of RNN) layers to each of the architectures.
			- Helps on architectures which don't already have a long term memory component in them.
- Future Approaches to improve performance
	- Do more pre-processing
	- Sim-2-real kind of approach, where you train on relevant synthetic data first, especially augmenting difficult cases, before training on real data.
	- New Architectures
		- Transformers
		- LSTMs for long term correlations
		- GRUs for short term dependencies
	- Ensemble Training Strategies
		- Train different models, each good at a different thing.

Questions
- Did they train on the same base frequency throughout all of these? (Or is that the point... that the same frequency will always be used for these applications?)

https://ieeexplore.ieee.org/document/10017640 here is another example where they throw a standard resnet architecture at it. I've seen mobilenet used as well. None of them are really made for this and although they work I think a custom architecture for the data type would be better. I need to do a more detailed lit review to find out whether there has been any work on this, however even if there is I am confident we will be able to make our own unique and novel innovations in this space.
All of my papers here https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=alec%20digby used IQ sample datasets, although they came from a multi antenna array which changes things slightly.
^ These are all ML research on top of datasets I created in the lab.
There are some cool innovations in the ML stuff there but again nothing that looks in detail at the unique properties of the input data format

# February 24, 2026
## Software design
Alec walked me through the way we generate signals. We go through the following process:
- First, we define the signal, with a pseudo random number generator.
- Then, we choose the symbols.. PBSK, all the other SKs, QAM, etc. Define them manually. This is the modulation map function.
- Pad with zeros between the signals you have defined, so that you have a pulse shaping filter
- Convolve with pulse shaping filter
- Add noise (Gaussian White)
- Apply Transformations
	- Add phase shift (uniformly) to the complex numbers
	- Multiply by cos of some frequency ($e^{j\omega t}$)
	- Do resampling with sinc interpolation (or some other kind of interpolation)
- We want the signal to be 1024 long.
## Coding Time
Packages:
- SciPy signal
	- Has filters, convolutions, fft, etc.
- Numpy
	- Use this for arrays of complex numbers

Create a dataclass for the configs
Should have the following specifications:
- Modulation type
- Length of signal
- Phase shift
- Noise
- Symbol rate
- Transmission Sample Rate
- Output sample rate
- Frequency offset

Then, I will have a class, called "SignalGenerator", with the following methods
- Init: doesn't really do anything
- Method to generate a batch of signals with
	- Required parameters
		- Signal length
		- Number of signals to generate
	- Optional Parameters
		- Modulation types
		- Range of frequency offsets
		- Range of phase shift
		- SNR
		- Output sample rate
- Method to generate a signal
	- Takes in a SignalConfig object
		- Modulation type (string)
		- Symbol rate
		- Output signal length
		- Phase shift
		- Frequency offset
		- SNR
	- Computes conservative estimate of number of bits required (will concatenate signal later)
	- Runs modulation map
- Modulation map
	- For every modulation type, computes the conversion between a bit string and a sequence of symbols
- Method to map a bit to a modulation type