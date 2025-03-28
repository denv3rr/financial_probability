# Portfolio Theory & Optimization

---

## Notes:
- Python libraries like `numpy`, `matplotlib`, and `PyPortfolioOpt` can be used to build, optimize, and visualize portfolios.
- You can also use `cvxpy` for custom constraint-based optimization problems.
  
> These formulas are essential for portfolio construction, diversification analysis, and risk-return optimization. They are foundational to tools like Modern Portfolio Theory and the Efficient Frontier. Libraries like `PyPortfolioOpt`, `numpy`, and `pandas` are helpful for implementing them in Python.


---

## 1. Expected Portfolio Return
```python
# E_Rp = sum([w_i * E_Ri for each asset i])
```
- **w_i** = weight of asset i in the portfolio  
- **E_Ri** = expected return of asset i  
- Gives the weighted average return of all assets in the portfolio.

---

## 2. Portfolio Variance (2+ assets)
```python
# Var_p = sum([w_i**2 * Var_i for all i]) + sum([w_i * w_j * Cov_ij for i ≠ j])
```
- Measures overall portfolio risk considering weights and co-movement of assets.

---

## 3. Portfolio Standard Deviation
```python
# std_p = sqrt(Var_p)
```
- Also known as portfolio volatility — reflects how much returns vary.

---

## 4. Covariance Between Assets
```python
# Cov(X, Y) = sum([P(x, y) * (x - E_X) * (y - E_Y)])
```
- Key input when calculating portfolio variance and risk of multiple assets.

---

## 5. Correlation Between Assets
```python
# Corr(X, Y) = Cov(X, Y) / (std_X * std_Y)
```
- Tells you how similarly two assets behave.
- Useful for diversification: lower correlation = better diversification.

---

## 6. Beta (β)
```python
# Beta_i = Cov(R_i, R_m) / Var(R_m)
```
- Measures an asset’s sensitivity to market movements.
- Used in CAPM and risk-adjusted performance.

---

## 7. Risk-Return Tradeoff

- Higher expected return typically comes with higher risk `(std_dev)`
- Use metrics like Sharpe Ratio to evaluate return vs. volatility.

---

## 8. Diversification Benefit

- Risk can be reduced without lowering expected return by combining uncorrelated assets.
- Optimal portfolios balance asset weights to reduce total portfolio risk.

---

## 9. Efficient Frontier (Conceptual)
- A set of optimal portfolios offering the highest expected return for a given risk.
- Plotted using return (Y-axis) vs. risk (X-axis).
