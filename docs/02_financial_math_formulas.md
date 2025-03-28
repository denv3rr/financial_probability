# Time Value of Money & Investment Metrics

---

## Notes:
- All these equations are commonly implemented in Python using `numpy`, `pandas`, or financial libraries like `numpy_financial`, `QuantLib`, or `PyPortfolioOpt`.
- You can easily wrap each formula in functions for reusable analysis.

---

## 1. Future Value (FV)
```python
# FV = PV * (1 + r) ** n
```
- **PV** = Present Value  
- **r** = Interest rate per period  
- **n** = Number of periods  

---

## 2. Present Value (PV)
```python
# PV = FV / (1 + r) ** n
```
- Calculates today's value of a future amount.

---

## 3. Net Present Value (NPV)
```python
# NPV = sum([C_t / (1 + r) ** t for t in range(1, n+1)]) - C_0
```
- **C_t** = Cash inflow at time t  
- **r** = Discount rate  
- **n** = Number of time periods  
- **C_0** = Initial investment (negative value)

---

## 4. Internal Rate of Return (IRR)
```python
# NPV = 0  # Solve for r that sets NPV to zero
```
- IRR is found using iterative numerical methods (e.g. Newton-Raphson)

---

## 5. Capital Asset Pricing Model (CAPM)
```python
# E_Ri = Rf + beta_i * (E_Rm - Rf)
```
- **E_Ri** = Expected return of investment i  
- **Rf** = Risk-free rate  
- **beta_i** = Volatility of asset i relative to market  
- **E_Rm** = Expected market return

---

## 6. Sharpe Ratio
```python
# Sharpe = (E_Rp - Rf) / std_p
```
- **E_Rp** = Expected return of the portfolio  
- **Rf** = Risk-free rate  
- **std_p** = Standard deviation of the portfolio (volatility)


