import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

# Training data
X = np.array([[1], [3], [5], [6], [7]])
y = np.sin(X).ravel()

# Define kernel
kernel = RBF(length_scale=1.0) + WhiteKernel(noise_level=0.1)
gpr = GaussianProcessRegressor(kernel=kernel)

# Fit
gpr.fit(X, y)

# Predict
X_ = np.linspace(0, 10, 100).reshape(-1, 1)
y_mean, y_std = gpr.predict(X_, return_std=True)

# Plot
plt.figure(figsize=(8,5))
plt.plot(X_, y_mean, 'b-', label='Mean Prediction')
plt.fill_between(X_.ravel(), y_mean - 2*y_std, y_mean + 2*y_std, 
                 alpha=0.2, color='blue', label='Confidence Interval')
plt.plot(X, y, 'ro', label='Observed Data')
plt.title('Gaussian Process Regression')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
