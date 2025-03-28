import numpy as np
import matplotlib.pyplot as plt

# Configuration
initial_investment = 10000
years = 30
mean_return = 0.07
volatility = 0.15
simulations = 1000

def simulate_growth():
    """Simulates portfolio growth over time using Monte Carlo."""
    results = []
    for _ in range(simulations):
        value = initial_investment
        for _ in range(years):
            yearly_return = np.random.normal(mean_return, volatility)
            value *= (1 + yearly_return)
        results.append(value)
    return results

# Run simulation
simulated_end_values = simulate_growth()

# Plot results
plt.hist(simulated_end_values, bins=50, color='skyblue', edgecolor='black')
plt.axvline(np.percentile(simulated_end_values, 10), color='red', linestyle='dashed', label='10th Percentile')
plt.title("Monte Carlo Simulation - 30 Year Portfolio Growth")
plt.xlabel("Final Portfolio Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
