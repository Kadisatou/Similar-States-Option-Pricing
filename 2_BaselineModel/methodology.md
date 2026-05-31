# Baseline Methodology: Classical Next-Day Option Price Forecast

This baseline model forecasts the next-day option price using a classical three-step pipeline:

$$
\hat{C}_{t+1} =
A(\hat{S}_{t+1}, K, r_{t+1}, \hat{\sigma}_{t+1}, \tau_{t+1})
$$

where:

- $$\hat{C}_{t+1}$$ is the forecasted option price,
- $$\hat{S}_{t+1}$$ is the forecasted underlying price,
- $$K$$ is the strike price,
- $$r_{t+1}$$ is the risk-free interest rate,
- $$\hat{\sigma}_{t+1}$$ is the forecasted volatility,
- $$\tau_{t+1}$$ is the remaining time to maturity.

---

## 1. Forecasting the Underlying Price

The underlying asset price is forecasted using a simple random walk or ARIMA-type model.

A basic random walk model is:

$$
S_{t+1} = S_t + \epsilon_{t+1}
$$

or, in return form:

$$
R_{t+1} = \mu + \epsilon_{t+1}
$$

where:

$$
R_t = \ln\left(\frac{S_t}{S_{t-1}}\right)
$$

The forecasted next-day price is then:

$$
\hat{S}_{t+1} =
S_t \exp(\hat{R}_{t+1})
$$

For a simple baseline, one may assume:

$$
\hat{R}_{t+1} = \bar{R}
$$

where $$\bar{R}$$ is the historical average return.

---

## 2. Forecasting Volatility with GARCH(1,1)

Volatility is forecast using a GARCH(1,1) model.

Returns are modeled as:

$$
R_t = \mu + \epsilon_t
$$

with:

$$
\epsilon_t = \sigma_t z_t
$$

where:

$$
z_t \sim N(0,1)
$$

The conditional variance follows:

$$
\sigma_{t+1}^2 =
\omega
+
\alpha \epsilon_t^2
+
\beta \sigma_t^2
$$

where:

- $$\omega$$ is the long-run variance component,
- $$\alpha$$ measures the effect of recent shocks,
- $$\beta$$ measures volatility persistence.

The next-day volatility forecast is:

$$
\hat{\sigma}_{t+1} =
\sqrt{
\omega
+
\alpha \epsilon_t^2
+
\beta \sigma_t^2
}
$$

---

## 3. Pricing the Option with Black-Scholes

Given 
$$ \hat{S}_{t+1}$$

and $$ \hat{\sigma}_{t+1} $$, the option price is computed using the Black-Scholes formula.

For a European call option:

$$
\hat{C}_{t+1} =
\hat{S}_{t+1} N(d_1)-
K e^{-r_{t+1}\tau_{t+1}} N(d_2)
$$

where:

$$
d_1=
\frac{
\ln\left(\frac{\hat{S}_{t+1}}{K}\right)
+
\left(r_{t+1}+\frac{1}{2}\hat{\sigma}_{t+1}^2\right)\tau_{t+1}
}{
\hat{\sigma}_{t+1}\sqrt{\tau_{t+1}}
}
$$

and:

$$
d_2 = d_1 - \hat{\sigma}_{t+1}\sqrt{\tau_{t+1}}
$$

Here, $$N(\cdot)$$ is the cumulative distribution function of the standard normal distribution.

---

## 4. Full Baseline Pipeline

The complete baseline forecasting process is:

### Step 1: Estimate return dynamics

$$
R_t = \ln\left(\frac{S_t}{S_{t-1}}\right)
$$

### Step 2: Forecast the underlying price

$$
\hat{S}_{t+1}=
S_t \exp(\hat{R}_{t+1})
$$

### Step 3: Forecast volatility

$$
\hat{\sigma}_{t+1}=
\sqrt{
\omega
+
\alpha \epsilon_t^2
+
\beta \sigma_t^2
}
$$

### Step 4: Compute time to maturity

$$
\tau_{t+1}=
\frac{T-(t+1)}{252}
$$

assuming 252 trading days per year.

### Step 5: Compute the option price

$$
\hat{C}_{t+1}=
BS(\hat{S}_{t+1},K,r_{t+1},\hat{\sigma}_{t+1},\tau_{t+1})
$$

---

## 5. Purpose of the Baseline Model

This model serves as the classical benchmark for the State Similarity Option Pricing project.

The classical baseline follows the structure:

$$
\text{Forecast drivers}
\rightarrow
\text{Insert into pricing model}
\rightarrow
\text{Obtain option price}
$$

That is:

$$
(\hat{S}_{t+1}, \hat{\sigma}_{t+1}, r_{t+1}, \tau_{t+1})
\rightarrow
\hat{C}_{t+1}
$$

The State Similarity approach will be compared against this baseline by learning directly from historical market states instead of relying only on a parametric pricing model.
