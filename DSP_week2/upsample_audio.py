'''import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
x=wavfile.read('/home/rguktrkvalley/Pictures/DSP Lab/week2/example_small.wav')
a=int(input("enter the sampling factor:")
'''
import numpy as np
from scipy.io import wavfile

# Load the audio file
#input_filename = 'input_audio.wav'
'''output_filename = 'upsampled_audio.wav'
sample_rate, audio_data = wavfile.read('/home/rguktrkvalley/Pictures/DSP Lab/week2/example_small.wav')

# Check if the audio data is stereo (2D array) or mono (1D array)
if audio_data.ndim == 1:
    # Mono audio
    channels = 1
else:
    # Stereo audio
    channels = audio_data.shape[1]

# Define the upsampling factor
upsample_factor=float(input("Enter a number:"))
new_sample_rate = sample_rate * upsample_factor

# Prepare the upsampled audio array
new_length = len(audio_data) * upsample_factor
if channels == 1:
    # Mono
    upsampled_audio = np.zeros(new_length, dtype=audio_data.dtype)
else:
    # Stereo
    upsampled_audio = np.zeros((new_length, channels), dtype=audio_data.dtype)

# Perform manual linear interpolation for upsampling
for i in range(len(audio_data) - 1):
    if channels == 1:
        # Mono channel
        upsampled_audio[i * upsample_factor] = audio_data[i]
        for j in range(1, upsample_factor):
            t = j / upsample_factor
            upsampled_audio[i * upsample_factor + j] = (1 - t) * audio_data[i] + t * audio_data[i + 1]
    else:
        # Stereo channel
        upsampled_audio[i * upsample_factor] = audio_data[i]
        for j in range(1, upsample_factor):
            t = j / upsample_factor
            upsampled_audio[i * upsample_factor + j] = (1 - t) * audio_data[i] + t * audio_data[i + 1]

# Handle the last sample(s)
upsampled_audio[-1] = audio_data[-1]

# Save the upsampled audio to a new file
wavfile.write(output_filename, new_sample_rate, upsampled_audio.astype(np.int16))

print(f"Original Sample Rate: {sample_rate} Hz")
print(f"Upsampled Sample Rate: {new_sample_rate} Hz")'''
import numpy as np
from scipy.io import wavfile

# Load the audio file
#input_filename = 'input_audio.wav'
output_filename = 'stretched_audio.wav'
sample_rate, audio_data = wavfile.read('home/rguktrkvalley/Pictures/DSP Lab/week2/example_small.wav')

# Check if the audio data is stereo (2D array) or mono (1D array)
if audio_data.ndim == 1:
    # Mono audio
    channels = 1
else:
    # Stereo audio
    channels = audio_data.shape[1]

# Define the downsampling factor (for stretching the duration)
scaling_factor = 0.5  # To double the duration
new_sample_rate = int(sample_rate * scaling_factor)

# Calculate the new length, ensuring it's an integer
new_length = int(len(audio_data) / scaling_factor)

# Initialize the stretched audio array
if channels == 1:
    # Mono
    stretched_audio = np.zeros(new_length, dtype=audio_data.dtype)
else:
    # Stereo
    stretched_audio = np.zeros((new_length, channels), dtype=audio_data.dtype)

# Perform manual linear interpolation for downscaling
for i in range(len(audio_data) - 1):
    if channels == 1:
        # Mono channel
        stretched_audio[int(i / scaling_factor)] = audio_data[i]
        for j in range(1, int(1 / scaling_factor)):
            t = j * scaling_factor
            if int(i / scaling_factor) + j < new_length:
                stretched_audio[int(i / scaling_factor) + j] = (1 - t) * audio_data[i] + t * audio_data[i + 1]
    else:
        # Stereo channel
        stretched_audio[int(i / scaling_factor)] = audio_data[i]
        for j in range(1, int(1 / scaling_factor)):
            t = j * scaling_factor
            if int(i / scaling_factor) + j < new_length:
                stretched_audio[int(i / scaling_factor) + j] = (1 - t) * audio_data[i] + t * audio_data[i + 1]

# Handle the last sample(s)
stretched_audio[-1] = audio_data[-1]

# Save the stretched audio to a new file
wavfile.write(output_filename, new_sample_rate, stretched_audio.astype(np.int16))

print(f"Original Sample Rate: {sample_rate} Hz")
print(f"New Sample Rate (stretched): {new_sample_rate} Hz")
print("Duration of stretched audio should be approximately doubled.")



