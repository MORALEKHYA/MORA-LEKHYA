import numpy as np
from scipy.io import wavfile

# Load the audio file
input_filename = '/home/rguktrkvalley/Pictures/DSP Lab/week2/example_small.wav'
output_filename = 'upsampled_audio.wav'
fs, x = wavfile.read(input_filename)

# Check if the audio data is mono or stereo
if x.ndim == 1:
    # Mono audio
    channels = 1
else:
    # Stereo audio
    channels = x.shape[1]

# Define the upsampling factor
a = 2  # Upsampling factor to double the sample rate
fs1 = int(fs * a)  # New sample rate

# Calculate the new length for upsampling
new_length = int(len(x) * a)

# Initialize the upsampled audio array
if channels == 1:
    # Mono
    upsampled_audio = np.zeros(new_length, dtype=x.dtype)
else:
    # Stereo
    upsampled_audio = np.zeros((new_length, channels), dtype=x.dtype)

# Insert original samples and perform linear interpolation for upsampling
for i in range(len(x) - 1):
    upsampled_audio[i * a] = x[i]  # Place the original sample at intervals of 'a'
    for j in range(1, a):  # Interpolate between samples
        t = j / a
        if channels == 1:
            # Linear interpolation for mono
            upsampled_audio[i * a + j] = (1 - t) * x[i] + t * x[i + 1]
        else:
            # Linear interpolation for stereo
            upsampled_audio[i * a + j] = (1 - t) * x[i] + t * x[i + 1]

# Handle the last sample(s)
upsampled_audio[-1] = x[-1]

# Save the upsampled audio to a new file
wavfile.write(output_filename, fs1, upsampled_audio.astype(np.int16))

print(f"Original Sample Rate: {fs} Hz")
print(f"New Sample Rate (upsampled): {fs1} Hz")
print("Duration of upsampled audio should be approximately halved.")

