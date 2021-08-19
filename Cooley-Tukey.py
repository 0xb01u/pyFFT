# -*- coding: utf-8 -*-
#
# Basic implementation of the Cooley-Tukey radix-2 DIT algorithm.
#
# This code is free and can be used or modified in any desired way.
#
import math, functools, sys, matplotlib
from time import time

__author__ = "0xb01u"
__email__ = "boluelbot@gmail.com"

SECONDS = 0	# Wave duration.
OP = 0		# Operations performed.
TIME = 0	# Execution time.

# DFT for x
def fft(x):
	global OP

	N = len(x)

	if N == 1:
		return [x[0]]

	X = [0] * N

	even = fft(x[:N:2])
	odd = fft(x[1:N:2])

	for k in range(N//2):
		w = math.e**(-2j*math.pi * k/N)
		X[k] = even[k] + w * odd[k]
		X[k + N//2] = even[k] - w * odd[k]
		OP += 2

	return X

# Inverse DFT for X
def ifft(X):
	N = len(X)

	if N == 1:
		return [X[0]]

	x = [0] * N

	even = ifft(X[:N:2])
	odd = ifft(X[1:N:2])

	for k in range(N//2):
		w = math.e**(2j*math.pi * k/N)
		x[k] = (even[k] + w * odd[k])/N
		x[k + N//2] = (even[k] - w * odd[k])/N

	return x

# Definition-based DFT
def naive(x):
	global OP
	OP = 0

	N = len(x)
	X = [0] * N

	for k in range(N):
		for n in range(k):
			X[k] += x[n] * math.e**(2j*math.pi * k*n/N )
			OP += 1

	return X

# Interprets the DFT results into a group of frequency-domain samples
def interpret(X, t):
	l = [0] * (len(X) // t)
	for i in range(len(l)):
		for j in range(t):
			l[i] += X[t*i + j]

	return l

# Reads a wave from a file
def readWave(name):
	# File format:
	# 1st line: an integer stating the difference in seconds between the first
	# and the last samples.
	# Next lines: a real, the value of each sample.
	# (One sample per line.)
	global SECONDS

	f = open(name, "r").readlines()
	SECONDS = int(f.pop(0)[:-1])

	return map(lambda x : float(x[:-1]), f)

# Output text format for the DFT
def fformat(X):
	s = "Fourier's transform: (" + str(X)[1:-1] + ")" + "\n\n"
	for i in range(len(X)):
		if X[i] > 0.01:
			s += "Frequency " + str(i) + "Hz: " + str(100*X[i]) + "%\n"

	return s

# Output text format for the inverse DFT
def tformat(x):
	return "Inverse Fourier's transform: (" + str(x)[1:-1] + ")" + "\n"

# This program reads a file given as argument and interprets it as a group
# of wave samples. It computes its DFT, and the inverse DFT of the obtained result
# (it should look the same as the original group of samples). It outputs both of
# them into "out.txt"-
# It also compares the execution time and number of operations of the Cooley-Tukey
# algorithm to a naive, definition-based algorithm.
def main():
	global TIME
	global OP
	global SECONDS

	x = readWave(sys.argv[1])
	N = len(x)	# Number of samples

	X = fft(x)
	
	X_ = interpret(X[:N//2], SECONDS)
	inv = list(map(lambda x : abs(x), ifft(X)))
	
	s = functools.reduce(lambda a, b: abs(a) + abs(b), X_)	# Sum of all the values of the transform
	X_ = list(map(lambda x : abs(x) / s, X_))

	f = open("out.txt", "w+")
	TIME = time()
	f.write(fformat(X_))
	TIME = time() - TIME
	f.write("_" * 50 + "\n\n")
	f.write(tformat(inv))
	f.close()

	print("Cooley-Tukey algorithm:\n" + str(OP) + " operations.\n" + str(TIME) + " seconds.\n\n")
	TIME = time()
	naive(x)	
	TIME = time() - TIME
	print("Definition-based algorithm:\n" + str(OP) + " operations.\n" + str(TIME) + " seconds.\n\n")


if __name__ == "__main__":
	main()
