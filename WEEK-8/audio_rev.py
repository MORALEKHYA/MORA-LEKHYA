from scipy.io import wavfile
(fs,x)=wavfile.read("npy.wav")
x_reverse=x[::-1]
wavfile.write('np.wav',fs,x_reverse)
