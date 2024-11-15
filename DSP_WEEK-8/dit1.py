
import numpy as np

# Function to compute the Discrete Fourier Transform (DFT) directly
'''def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X'''

# Main recursive function using DIT (Decimation-In-Time)
def fft_dit_dft(x):
    N = len(x)
    
    # Base case: if the length of the input is 1, return the input
    if N <= 1:
        return x
    
    # Decimation: split into even and odd indices
    even = fft_dit_dft(x[0::2])
    odd = fft_dit_dft(x[1::2])
    
    # Combine using DFT on smaller parts
    return combine(even, odd, N)

# Function to combine even and odd parts using twiddle factors
def combine(even, odd, N):
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Example usage
x = np.random.random(8)  # Input signal, length must be a power of 2
fft_result = fft_dit_dft(x)
print("FFT result using DIT and DFT:", fft_result)

# Validate result using numpy's FFT for comparison
'''np_fft_result = np.fft.fft(x)
print("NumPy FFT result:", np_fft_result)'''




