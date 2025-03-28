# Probability

---

## Notes:
- These formulas are foundational for Monte Carlo simulations, forecasting, and decision trees.
- Use Python's `numpy`, `scipy.stats`, and `pandas` for implementation in practice.

---

## 1. Probability of an Event
```python
# P(A) = Favorable Outcomes / Total Outcomes
```
- Calculates the chance of an event occurring.
- Example: Probability of rolling a 4 on a fair 6-sided die = 1 / 6

---

## 2. Expected Value (E)
```python
# E(X) = sum([P(x) * x for each outcome x])
```
- Average value you’d expect over many trials.
- Used in evaluating the average return or result of random events.

---

## 3. Variance and Standard Deviation
```python
# Variance: Var(X) = sum([P(x) * (x - E(X)) ** 2 for each x])
# Standard Deviation: std_dev = sqrt(Var(X))
```
- Variance measures spread of values around the mean.
- Standard deviation is the square root of variance, representing volatility.

---

## 4. Covariance
```python
# Cov(X, Y) = sum([P(x, y) * (x - E(X)) * (y - E(Y))])
```
- Measures how two variables move together.
- Positive value = they move in the same direction.

---

## 5. Correlation
```python
# Correlation: ρ(X, Y) = Cov(X, Y) / (std_X * std_Y)
```
- Normalized version of covariance between -1 and 1.
- 1 = perfectly correlated; 0 = no correlation; -1 = perfectly inversely correlated

---

## 6. Joint Probability (AND events)
```python
# P(A and B) = P(A) * P(B)  # if A and B are independent
```
- Use when two independent events occur together.

---

## 7. Conditional Probability (IF/THEN events)
```python
# P(A | B) = P(A and B) / P(B)
```
- Probability of A occurring **given** B has occurred.

---

## 8. Bayes’ Theorem
```python
# P(A | B) = [P(B | A) * P(A)] / P(B)
```
- Updates the probability of A based on new information (B).
- Widely used in decision science, risk management, and forecasting.

