# pyFFT - Cooley-Tukey's algorithm
This is a Python implementation for Cooley-Tukey's fast Fourier transform (FFT) algorithm, which computes the discrete Fourier transform (DFT) of a given wave in O(n * log(n)) time.
This program was written as part of a college task for a subject focused on algorithms.

## Programs included
**Cooley-Tukey.py** is a Python program which takes a file's path as argument and computes the discrete Fourier transform for the wave stored on that file using Cooley-Tukey's algorithm and a definition-based algorithm (which is O(n^2) in time). It also computes the inverse discrete Fourier transform (IDFT) for the resulting DFT, which should look alike the original wave. The DFT and IDFT are written to a file called _out.txt_. The program also outputs to the standard exit a comparison of the performance of Cooley-Tukey's algorithm against the definition-based algorithm, in the form of operations performed and seconds taken by each algorithm to compute the DFT.

**waveGenerator.py** creates a valid file representing a wave to use with _Cooley-Tukey.py_, taking 2 to 4 arguments: the path of the output file, a frequency in Hertzs, a number of samples and a duration in seconds (being the last two arguments optional). Default values for the optional arguments are, respectively, 256 and 1.

# TODO
- Add a graphic output.
- Add more control over the output options.