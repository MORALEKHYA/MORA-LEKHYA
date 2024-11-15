import numpy as np
from scipy.fft import fft, ifft

def overlap_save(x, h, N):
    # Length of the filter
    M = len(h)
    
    # Ensure the FFT length is greater than or equal to the filter length
    if N < M:
        raise ValueError("FFT length N must be greater than or equal to the length of the filter M.")
    
    # Number of points to discard
    L = N - M + 1
    
    # Prepare the input signal by adding initial zeros for overlap
    x_padded = np.concatenate((np.zeros(M - 1), x))
    
    # FFT of the filter
    H = fft(h, N)
    
    # Output array
    y = np.zeros(len(x) + M - 1)
    
    # Process each block
    for i in range(0, len(x), L):
        x_block = x_padded[i:i + N]  # Get a block of input signal
        X = fft(x_block, N)          # FFT of the block
        Y = X * H                    # Multiply in frequency domain
        y_block = ifft(Y).real       # Inverse FFT to get the time domain signal
        
        # Overlap-save: discard the first M-1 points and save the rest
        y[i:i + L] = y_block[M-1:]
    
    return y

# Example usage
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Input signal
h = np.array([1, -1, 1])                   # Filter (impulse response)
N = 5  # FFT length (must be >= len(h))

y = overlap_save(x, h, N)

print("Output signal (convolution result):", y)

