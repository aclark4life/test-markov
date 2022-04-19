# Via https://towardsdatascience.com/introduction-to-linear-regression-in-python-c12a072bedf0
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Generate 'random' data
np.random.seed(0)
X = (
    2.5 * np.random.randn(100) + 1.5
)  # Array of 100 values with mean = 1.5, stddev = 2.5
res = 0.5 * np.random.randn(100)  # Generate 100 residual terms
y = 2 + 0.3 * X + res  # Actual values of Y

# Create pandas dataframe to store our X and y values
df = pd.DataFrame({"X": X, "y": y})

# Show the first five rows of our dataframe
print(df.head())

# Calculate the mean of X and y
xmean = np.mean(X)
ymean = np.mean(y)

# Calculate the terms needed for the numator and denominator of beta
df['xycov'] = (df['X'] - xmean) * (df['y'] - ymean)
df['xvar'] = (df['X'] - xmean)**2

# Calculate beta and alpha
beta = df['xycov'].sum() / df['xvar'].sum()
alpha = ymean - (beta * xmean)
print(f'alpha = {alpha}')
print(f'beta = {beta}')
