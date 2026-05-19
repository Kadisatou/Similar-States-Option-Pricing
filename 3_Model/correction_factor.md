# The Correction Factor \(O\)

$O$ is best understood as a residual correction term that adjusts the historical analogue option price to fit current market conditions and regime dynamics.

We define:

$$

C^{\text{true}}_{t+1}

=
C^{\text{analogue}}_{t+1}
+
O_t

$$

where:

* the analogue term captures historical similarity,
* and the correction term adapts the prediction to the present market state.

---

# Why a Correction Factor Is Needed

Historical analogue predictions alone may fail to fully capture:

* regime changes,
* nonlinear dynamics,
* liquidity distortions,
* volatility shifts,
* interest-rate changes,
* and market structural shifts.

Therefore, the framework corrects the analogue-based prediction using both:

* theoretical financial corrections,
* and machine learning residual corrections.

---

# Volatility Correction

Option prices are highly sensitive to volatility.

If the historical analogue had volatility $\sigma_p$, but the current market has volatility \(\sigma_t\), the correction becomes:

$$
O_{\sigma}
\approx
\text{Vega}_t(\sigma_t-\sigma_p)
$$

where:

$$
\text{Vega} = \frac{\partial C}{\partial \sigma}
$$

## Interpretation

* If current volatility is higher than historical volatility, the option value may need to be adjusted upward.
* If current volatility is lower than historical volatility, the option value may need to be adjusted downward.

---

# Time-to-Maturity Correction

Options with different remaining maturities cannot be compared directly without adjustment.

The correction becomes:

$$
O_{\tau}
\approx
\Theta_{\text{Greek}}(\tau_t-\tau_p)
$$

where:

$$
\Theta_{\text{Greek}} = \frac{\partial C}{\partial t}
$$

## Interpretation

Theta measures how option value changes as time passes.

This correction adjusts the analogue price when the current option and the historical analogue have different time-to-maturity values.

---

# Moneyness Correction

Define moneyness:

$$
M_t = \frac{S_t}{K}
$$

or log-moneyness:

$$
m_t = \ln(S_t/K)
$$

The corresponding correction becomes:

$$
O_S \approx \Delta_t(S_t-S_p)
$$

where:

$$
\Delta = \frac{\partial C}{\partial S}
$$

## Interpretation

Delta measures the sensitivity of the option price to changes in the underlying asset price.

This correction adjusts the historical analogue price when the current underlying price differs from the historical analogue underlying price.

---

# Interest Rate Correction

The interest-rate correction becomes:

$$
O_r \approx \rho_t(r_t-r_p)
$$

where:

$$
\rho = \frac{\partial C}{\partial r}
$$

## Interpretation

Rho measures the sensitivity of the option price to interest-rate changes.

This correction is especially relevant when historical analogue periods occurred under different interest-rate environments.

---

# Liquidity Correction

Liquidity conditions may affect observed option prices through bid-ask spreads, trading volume, and open interest.

The liquidity correction can be written as:

$$
O_{\text{liq}} = g(\text{spread},\text{volume},\text{open interest})
$$

where:

* spread measures transaction cost and market friction,
* volume measures trading activity,
* and open interest measures market participation.

## Interpretation

Poor liquidity can reduce pricing reliability and distort observed option prices.

---

# Greek-Based Correction

The theoretical financial correction becomes:

$$

O_{\text{Greek}}

=
\Delta_t(S_t-S_p)
+
\text{Vega}_t(\sigma_t-\sigma_p)
+
\rho_t(r_t-r_p)
+
\Theta_t(\tau_t-\tau_p)
$$

where:

* $$\Delta_t(S_t-S_p)$$ adjusts for underlying price differences,
* $$\text{Vega}_t(\sigma_t-\sigma_p)$$ adjusts for volatility differences,
* $$\rho_t(r_t-r_p)$$ adjusts for interest-rate differences,
* and $$\Theta_t(\tau_t-\tau_p)$$ adjusts for time-to-maturity differences.

---

# ML Residual Correction

Financial markets remain highly nonlinear even after Greek-based corrections.

Therefore, the remaining pricing discrepancy is modeled using machine learning:

$$

O_{\text{residual}}

=
f_{\theta}(X_t)
$$

where:

* $X_t$ is the market-state feature vector,
* and $f_{\theta}$ is a nonlinear learned function.

The final correction becomes:

$$

O_t

=
O_{\text{Greek}}
+
O_{\text{residual}}
$$

---

# Gaussian Process Residual Modeling

The residual correction is modeled using Gaussian Process Regression:

$$
O_{\text{residual}}
\sim
\mathcal{GP}(m(X),k(X,X'))
$$

where:

* \(m(X)\) is the mean function,
* \(k(X,X')\) is the covariance kernel.

The predicted residual becomes:

$$

\hat O_{\text{residual}}

=
\mathbb E
\left[
O_{\text{residual}}
\mid X_t
\right]
$$

with uncertainty:

$$
\text{Var}
\left[
O_{\text{residual}}
\mid X_t
\right]
$$

---

# Final Corrected Pricing Equation

The final corrected price becomes:

$$

\hat C_{t+1}

=
C^{\text{analogue}}_{t+1}
+
O_{\text{Greek}}
+
f_{\theta}(X_t)
$$

where:

* $$C^{\text{analogue}}_{t+1}$$ captures historical analogue pricing,
* $$O_{\text{Greek}}$$ captures theoretical financial corrections,
* and $$f_{\theta}(X_t)$$ captures nonlinear residual market dynamics.

---

# Final Interpretation

The correction factor $O$ allows the framework to preserve the intuition of historical analogue learning while adapting the analogue prediction to current market conditions.

It combines:

* financial theory,
* Greek-based sensitivity adjustment,
* liquidity correction,
* nonlinear machine learning,
* and probabilistic residual modeling.

This makes the final prediction more flexible, more realistic, and more responsive to current market conditions.
