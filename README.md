# Financial Probability

Probability and financial formulas with practical applications related to finance, wealth advisory, risk management, or quantitative roles.

[Jump to Formulas Section](#formulas)

<br>
<br>
<br>

---

## 📘 Contents

- `docs/` - Explanations of major topics
- `cheatsheets/` - Printable guides and PDFs
- `notebooks/` - Interactive Python notebooks
- `scripts/` - Utility scripts for simulations
- `resources/` - Recommended books, links, and a glossary

---

## 🔍 Key Topics

- Basic Probability
- Expected Value, Variance, Correlation
- Time Value of Money (FV, PV, NPV, IRR)
- Portfolio Theory (Sharpe Ratio, CAPM, Optimization)
- Monte Carlo Simulations
- Role-based Applications in Finance

---

## Getting Started

Clone the repo:
```bash
git clone https://github.com/denv3rr/financial_probability.git
cd financial_probability
```


If using Jupyter Notebooks:
```bash
jupyter notebook notebooks/interactive_formula_explorer.ipynb
```

---

## Use Cases

| Role | Application |
|--------|-------------|
| Financial Advisory |	Explain risk vs. return, use FV/PV to model client portfolios |
| Investment Analysis | Calculate Sharpe, beta, and expected return scenarios |
| Risk Management | Use Monte Carlo to estimate downside probabilities |
| Quantitative Analysis |	Run correlation matrices and regression on financial assets |

---

## Formulas

**View full math-rendered version in notebook:**  
[View the Notebook →](notebooks/full_financial_formulas.ipynb)

Rendered using LaTeX with SVG images via [Codecogs](https://latex.codecogs.com/)

---

### 🎲 Probability

![P(A)](https://latex.codecogs.com/svg.image?\dpi{150}&space;P(A)&space;=&space;\frac{\text{Favorable&space;Outcomes}}{\text{Total&space;Outcomes}})

![E(X)](https://latex.codecogs.com/svg.image?\dpi{150}&space;E(X)&space;=&space;\sum&space;P(x)&space;\cdot&space;x)

![Var and Std Dev](https://latex.codecogs.com/svg.image?\dpi{150}&space;Var(X)&space;=&space;\sum&space;P(x)&space;(x&space;-&space;E(X))^2,&space;\quad&space;\sigma&space;=&space;\sqrt{Var(X)})

![Covariance](https://latex.codecogs.com/svg.image?\dpi{150}&space;Cov(X,Y)&space;=&space;\sum&space;P(x,y)(x&space;-&space;E(X))(y&space;-&space;E(Y)))

![Correlation](https://latex.codecogs.com/svg.image?\dpi{150}&space;\rho_{X,Y}&space;=&space;\frac{Cov(X,&space;Y)}{\sigma_X&space;\cdot&space;\sigma_Y})

---

### 💸 Time Value of Money

![FV](https://latex.codecogs.com/svg.image?\dpi{150}&space;FV&space;=&space;PV&space;\cdot&space;(1&space;+&space;r)^n)

![PV](https://latex.codecogs.com/svg.image?\dpi{150}&space;PV&space;=&space;\frac{FV}{(1&space;+&space;r)^n})

![NPV](https://latex.codecogs.com/svg.image?\dpi{150}&space;NPV&space;=&space;\sum_{t=1}^{n}&space;\frac{C_t}{(1&space;+&space;r)^t}&space;-&space;C_0)

![IRR](https://latex.codecogs.com/svg.image?\dpi{150}&space;NPV&space;=&space;0&space;\quad&space;\text{(solve&space;for&space;}r\text{)})

---

### 📊 Portfolio Theory

![E(Rp)](https://latex.codecogs.com/svg.image?\dpi{150}&space;E(R_p)&space;=&space;\sum&space;w_i&space;\cdot&space;E(R_i))

![Portfolio Variance](https://latex.codecogs.com/svg.image?\dpi{150}&space;\sigma_p^2&space;=&space;\sum&space;w_i^2&space;\cdot&space;\sigma_i^2&space;+&space;\sum_{i&space;\neq&space;j}&space;w_i&space;w_j&space;\cdot&space;Cov(i,&space;j))

![Sharpe Ratio](https://latex.codecogs.com/svg.image?\dpi{150}&space;Sharpe&space;=&space;\frac{E(R_p)&space;-&space;R_f}{\sigma_p})

![CAPM](https://latex.codecogs.com/svg.image?\dpi{150}&space;E(R_i)&space;=&space;R_f&space;+&space;\beta_i(E(R_m)&space;-&space;R_f))

![Beta](https://latex.codecogs.com/svg.image?\dpi{150}&space;\beta_i&space;=&space;\frac{Cov(R_i,&space;R_m)}{Var(R_m)})

---

### 🎲 Monte Carlo Simulation

![Monte Carlo](https://latex.codecogs.com/svg.image?\dpi{150}&space;\text{Final&space;Value}&space;=&space;PV&space;\cdot&space;\prod_{t=1}^{n}(1&space;+&space;r_t))

![Dist](https://latex.codecogs.com/svg.image?\dpi{150}&space;r_t&space;\sim&space;\mathcal{N}(\mu,&space;\sigma^2))

---

## Contributions Welcome

If you have an equation, scenario, or script to add, create a pull request or open a discussion.
