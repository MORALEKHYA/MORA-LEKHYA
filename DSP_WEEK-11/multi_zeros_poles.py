
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Ask user for input
num_poles = int(input("Enter the number of poles: "))
num_zeros = int(input("Enter the number of zeros: "))

poles = []
zeros = []

print("Enter the poles:")
for i in range(num_poles):
    real_part = float(input(f"Real part of pole {i+1}: "))
    imag_part = float(input(f"Imaginary part of pole {i+1}: "))
    poles.append(complex(real_part, imag_part))

print("Enter the zeros:")
for i in range(num_zeros):
    real_part = float(input(f"Real part of zero {i+1}: "))
    imag_part = float(input(f"Imaginary part of zero {i+1}: "))
    zeros.append(complex(real_part, imag_part))

# Create transfer function from poles and zeros
z, p = np.array(zeros), np.array(poles)
b, a = signal.zpk2tf(z, p, 1)

# Frequency response
w, h = signal.freqz(b, a)

# Plot magnitude response
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h))
plt.title('Magnitude Response')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Magnitude')

# Plot phase response
plt.subplot(2, 1, 2)
plt.plot(w, np.angle(h))
plt.title('Phase Response')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Phase [radians]')

plt.tight_layout()
plt.show()
