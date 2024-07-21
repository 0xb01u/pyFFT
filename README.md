# pyFFT - Cooley-Tukey's algorithm
This is a Python implementation of Cooley-Tukey's fast Fourier transform (FFT) algorithm, which computes the discrete Fourier transform (DFT) of a given wave in `O(n * log(n))` time.

This program was developed as part of a college task for a course focused on algorithms. **It is for educational purposes only, and is not suitable for any production environments.**

## Programs included
`Cooley-Tukey.py` is a Python program which takes a file's path as argument and computes the discrete Fourier transform for the wave stored on that file using Cooley-Tukey's algorithm. As a reference, it also computes the DFT using a definition-based algorithm (which is `O(n²)` in time). Then, it computes the inverse discrete Fourier transform (IDFT) for the resulting DFT, which should output a wave similar to the original (input). The DFT and IDFT are written to a file called _out.txt_. The program also outputs to stdout the performance comparison between Cooley-Tukey's and the definition-based algorithms, in the form of "operations performed" and "seconds taken".

`waveGenerator.py` creates a valid file representing a wave to use with `Cooley-Tukey.py`, taking 2 to 4 arguments: the path of the output file, a frequency in Hertzs, a number of samples and a duration in seconds (being the last two arguments optional). Default values for the optional arguments are, respectively, 256 and 1.

# TODO
- Add a graphic output.
- Add more control over the output options.
- Improve the programs' invocation by using the `argparse` module.

These TODO tasks may or may not be completed somewhen in the future.
