import soundfile as sf
import matplotlib.pyplot as plt

#load audio file
file_path="/home/rguktrkvalley/Desktop/WEEK-7/file_example_WAV_1MG.wav"
signal,sample_rate=sf.read(file_path)

#calculate the array
duration=len(signal)/sample_rate
time=[i/sample_rate for i in range(len(signal))]

#plot the signal
plt.figure(figsize=(2,4))
plt.plot(time,signal)
plt.title("Audio signal")
plt.grid(True)
plt.show()
