import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_investment = 10000
years = 30
mean_return = 0.07
volatility = 0.15
simulations = 1000

# Run Simulations
results = []
for _ in range(simulations):
    annual_returns = np.random.normal(mean_return, volatility, years)
    value = initial_investment
    for r in annual_returns:
        value *= (1 + r)
    results.append(value)

# Plot
plt.hist(results, bins=50)
plt.axvline(np.percentile(results, 10), color='r', linestyle='dashed', label="10th Percentile")
plt.title("Monte Carlo Simulation: 30-Year Portfolio Projection")
plt.xlabel("Portfolio Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()
