
from scipy.io import wavfile
from matplotlib import pyplot as plt
fs, x = wavfile.read('/home/rguktrkvalley/Pictures/DSP Lab/week2/example_small.wav')


def sampling(x, a):
    if a > 1:
        y=x[::a]
        wavfile.write('ds1.wav',fs,y)


a=int(input("Enter sampling factor:"))
sampling(x, a)

