# Baseline Methodology: Classical Next-Day Option Price Forecast

This baseline model forecasts the next-day option price using a classical three-step pipeline:

$$
\hat{C}_{t+1} =
f(\hat{S}_{t+1}, K, r_{t+1}, \hat{\sigma}_{t+1}, \tau_{t+1})
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
$$\hat{S}_{t+1}$$

and $$\hat{\sigma}_{t+1}$$, the option price is computed using the Black-Scholes formula.

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




# Baseline Methodology: Direct Next-Day Option Price Forecasting

## Overview

The objective of this baseline model is to forecast the next-day European call option price:

$$
C_{t+1}
$$

using only historical observations of the option price series:

$$
\{C_1, C_2, \ldots, C_t\}
$$

Unlike traditional option pricing models such as Black-Scholes, this baseline does not attempt to forecast underlying asset prices, volatility, interest rates, or time to maturity. Instead, the option price itself is treated as a time series and forecasted directly.

Two classical forecasting approaches are used:

1. **Persistence Forecast**
2. **ARIMA Forecast**

These methods are appropriate because the target variable is a sequential time series where the next value may depend on previous observations. The persistence model provides a simple benchmark, while ARIMA captures temporal patterns and trends that may exist in historical option prices.

---

# 1. Persistence Forecast

## Motivation

The persistence model assumes that the best estimate of tomorrow's option price is today's observed option price.

This approach is commonly used as a benchmark in financial forecasting because many financial time series exhibit strong short-term continuity.

Any forecasting model should ideally outperform this simple baseline.

---

## Data Used

For a forecast date \(t\), the model uses only:

$$
C_t
$$

where:

- \(C_t\) = observed option price at date \(t\)

No additional historical observations are required.

---

## Forecast Formula

The persistence forecast is:

$$
\hat{C}_{t+1}^{(P)} =
C_t
$$

where:

- \(\hat{C}_{t+1}^{(P)}\) = predicted next-day option price
- \(C_t\) = current observed option price

---

## Computation Steps

### Step 1

Observe the current option price:

$$
C_t
$$

### Step 2

Assign tomorrow's forecast equal to today's value:

$$
\hat{C}_{t+1}^{(P)} =
C_t
$$

### Step 3

Compare the prediction against the true next-day price:

$$
C_{t+1}
$$

---

# 2. ARIMA Forecast

## Motivation

The ARIMA model extends the persistence approach by learning temporal dependencies from historical option prices.

It attempts to model:

- trends,
- autocorrelation,
- short-term dynamics,

contained in the historical option price series.

Because option prices evolve over time and may exhibit serial dependence, ARIMA provides a natural statistical benchmark for next-day forecasting.

---

## Data Used

For a forecast date \(t\), the model uses all historical option prices available up to that date:

$$
\{C_1, C_2, \ldots, C_t\}
$$

In the implementation, at least 30 historical observations are required before a forecast is produced.

---

## ARIMA(1,1,1) Model

The baseline uses:

$$
ARIMA(1,1,1)
$$

where:
## Please put the vairbales inside $$ otherwise github will not translate it well.

- \(p=1\): one autoregressive term,
- \(d=1\): first differencing,
- \(q=1\): one moving-average term.

The general ARIMA model is:

$$
\phi(B)(1-B)^d C_t =
\theta(B)\epsilon_t
$$

where: ## PUT these in $ sign##

- \(B\) = backshift operator,
- \(\phi(B)\) = autoregressive polynomial,
- \(\theta(B)\) = moving-average polynomial,
- \(\epsilon_t\) = white-noise error term.

For the ARIMA(1,1,1) specification:

$$
\Delta C_t=
\alpha
+
\phi \Delta C_{t-1}
+
\epsilon_t
+
\theta \epsilon_{t-1}
$$

where:

$$
\Delta C_t=
C_t - C_{t-1}
$$

is the first-differenced option price;

## Add: 
and C_t+1 = DElta + C_{t} is the forecasted option price (correct me if I am wrong.)

---

## Remove the section below, i.e., on the computation Steps. It is not relevant.
## Computation Steps 

### Step 1

Collect all historical option prices:

$$
\{C_1,\ldots,C_t\}
$$

### Step 2

Fit an ARIMA(1,1,1) model using the historical series.

### Step 3

Generate a one-step-ahead forecast:

$$
\hat{C}_{t+1}^{(ARIMA)}
$$

### Step 4

If

$$
\hat{C}_{t+1}^{(ARIMA)} < 0
$$

the forecast is discarded because option prices cannot be negative.

### Step 5

Compare the prediction against the true next-day value:

$$
C_{t+1}
$$

---

# 3. Forecast Evaluation
##Add the sentence: Here,  we compare the prediction against the true next-day value.

The forecasting performance of both approaches is assessed using:

1. Mean Absolute Error (MAE)
2. Root Mean Squared Error (RMSE)

These metrics compare predicted prices against the observed next-day option prices.

---

## Prediction Error

For each forecast:

$$
e_i = C_{t+1,i} -
\hat{C}_{t+1,i}
$$

where: 
##Add $$ to the formulas otherwise it won't work

- \(C_{t+1,i}\) = true option price,
- \(\hat{C}_{t+1,i}\) = forecasted option price,
- \(e_i\) = forecast error.

---

## Mean Absolute Error (MAE)

### Formula

$$
MAE =
\frac{1}{N}
\sum_{i=1}^{N}
|e_i|
$$

or equivalently:

$$
MAE =
\frac{1}{N}
\sum_{i=1}^{N}
\left|
C_{t+1,i} -
\hat{C}_{t+1,i}
\right|
$$

---

### Variables 
## Put the formulas inside $$ otherwise it won't work.

- \(N\) = number of forecasts
- \(C_{t+1,i}\) = true option price
- \(\hat{C}_{t+1,i}\) = predicted option price

---

### Interpretation

MAE measures the average absolute forecasting error.

For example:

$$
MAE = 2
$$

means that forecasts are, on average, two price units away from the true option price.

Lower MAE indicates better forecasting accuracy.

---

## Root Mean Squared Error (RMSE)

### Formula

$$
RMSE =
\sqrt{
\frac{1}{N}
\sum_{i=1}^{N}
e_i^2
}
$$

or:

$$
RMSE =
\sqrt{
\frac{1}{N}
\sum_{i=1}^{N}
\left(
C_{t+1,i} -
\hat{C}_{t+1,i}
\right)^2
}
$$

---

### Variables
## Put the formulas inside $$ othertwise the won't work.

- \(N\) = number of forecasts
- \(C_{t+1,i}\) = true option price
- \(\hat{C}_{t+1,i}\) = predicted option price

---

### Interpretation

RMSE penalizes large forecasting errors more heavily than MAE because errors are squared before averaging.

A model with occasional large mistakes will therefore obtain a higher RMSE.

Lower RMSE indicates better predictive performance.

---

# 4. Baseline Objective

The purpose of this baseline is to establish a classical benchmark for the State Similarity Option Pricing project.

The baseline forecasting framework is:

$$
\{C_1,\ldots,C_t\}
\rightarrow
\hat{C}_{t+1}
$$

using either:

$$
\hat{C}_{t+1}^{(P)} =
C_t
$$

or

$$
\hat{C}_{t+1}^{(ARIMA)} =
ARIMA(C_1,\ldots,C_t)
$$

The State Similarity model will be evaluated against these benchmarks to determine whether historical market-state matching can improve next-day option price forecasting accuracy.







-----



# Baseline Methodology: Direct Next-Day Option Price Forecasting

## Overview

The objective of this baseline model is to forecast the next-day European call option price:

$$
C_{t+1}
$$

using only historical observations of the option price series:

$$
\{C_1, C_2, \ldots, C_t\}
$$

Unlike traditional option pricing models such as Black-Scholes, this baseline does not attempt to forecast underlying asset prices, volatility, interest rates, or time to maturity. Instead, the option price itself is treated as a time series and forecasted directly.

Two benchmark forecasting approaches are used:

1. **Persistence Forecast (Naïve Benchmark)**
2. **ARIMA Forecast (Classical Statistical Benchmark)**

These methods are appropriate because the target variable is a sequential time series where future values may depend on previous observations.

The persistence model provides a simple benchmark that assumes no change in the option price from one day to the next. It establishes the minimum level of predictive performance that any more sophisticated model should exceed.

The ARIMA model provides a classical statistical benchmark by explicitly modelling temporal dependencies, trends, and autocorrelation present in historical option prices.

For each option series, 10 valid forecast dates are randomly selected. For each selected date, only information available up to that date is used to generate a one-step-ahead forecast, thereby avoiding look-ahead bias.

---

# 1. Persistence Forecast (Naïve Benchmark)

## Motivation

The persistence model assumes that the best estimate of tomorrow's option price is today's observed option price.

This approach is commonly used as a naïve benchmark in financial forecasting because many financial time series exhibit strong short-term continuity.

Any forecasting model should ideally outperform this simple baseline.

---

## Data Used

For a forecast date $$t$$, the model uses only:

$$
C_t
$$

where:

- $$C_t$$ = observed option price at date $$t$$

No additional historical observations are required.

---

## Forecast Formula

The persistence forecast is:

$$
\hat{C}_{t+1}^{(P)}=
C_t
$$

where:

- $$\hat{C}_{t+1}^{(P)}$$ = predicted next-day option price
- $$C_t$$ = current observed option price

---

## Computation Steps

### Step 1

Observe the current option price:

$$
C_t
$$

### Step 2

Assign tomorrow's forecast equal to today's value:

$$
\hat{C}_{t+1}^{(P)}=
C_t
$$

### Step 3

Compare the prediction against the true next-day price:

$$
C_{t+1}
$$

---

# 2. ARIMA Forecast (Classical Statistical Benchmark)

## Motivation

The ARIMA model extends the persistence approach by learning temporal dependencies from historical option prices.

It attempts to model:

- trends,
- autocorrelation,
- short-term dynamics,

contained in the historical option price series.

Because option prices evolve over time and may exhibit serial dependence, ARIMA provides a natural statistical benchmark for next-day forecasting.

---

## Data Used

For a forecast date $$t$$, the model uses all historical option prices available up to that date:

$$
\{C_1, C_2, \ldots, C_t\}
$$

In the implementation, at least 30 historical observations are required before a forecast is produced.

---

## ARIMA(1,1,1) Model

The baseline uses:

$$
ARIMA(1,1,1)
$$

where:

- $$p=1$$: one autoregressive term,
- $$d=1$$: first differencing,
- $$q=1$$: one moving-average term.

The general ARIMA model is:

$$
\phi(B)(1-B)^d C_t=
\theta(B)\epsilon_t
$$

where:

- $$B$$ = backshift operator,
- $$\phi(B)$$ = autoregressive polynomial,
- $$\theta(B)$$ = moving-average polynomial,
- $$\epsilon_t$$ = white-noise error term.

For the ARIMA(1,1,1) specification:

$$
\Delta C_t=
\alpha
+
\phi \Delta C_{t-1}
+
\epsilon_t
+
\theta \epsilon_{t-1}
$$

where:

$$
\Delta C_t=
C_t - C_{t-1}
$$

is the first-differenced option price.

The ARIMA model forecasts the next differenced value:

$$
\widehat{\Delta C}_{t+1}
$$

which is transformed back into an option price forecast using:

$$
\hat{C}_{t+1}=
C_t
+
\widehat{\Delta C}_{t+1}
$$

where:

- $$\widehat{\Delta C}_{t+1}$$ = forecasted next-day price change,
- $$\hat{C}_{t+1}$$ = forecasted next-day option price.

The resulting forecast is therefore:

$$
\hat{C}_{t+1}^{(ARIMA)}
$$

---

# 3. Forecast Evaluation

Here, we compare the prediction against the true next-day value.

The forecasting performance of both approaches is assessed using:

1. Mean Absolute Error (MAE)
2. Root Mean Squared Error (RMSE)

These metrics compare predicted prices against the observed next-day option prices.

---

## Prediction Error

For each forecast:

$$
e_i=
C_{t+1,i}-
\hat{C}_{t+1,i}
$$

where:

- $$C_{t+1,i}$$ = true option price,
- $$\hat{C}_{t+1,i}$$ = forecasted option price,
- $$e_i$$ = forecast error.

---

## Mean Absolute Error (MAE)

### Formula

$$
MAE=
\frac{1}{N}
\sum_{i=1}^{N}
|e_i|
$$

or equivalently:

$$
MAE=
\frac{1}{N}
\sum_{i=1}^{N}
\left|
C_{t+1,i}-
\hat{C}_{t+1,i}
\right|
$$

### Variables

- $$N$$ = number of forecasts
- $$C_{t+1,i}$$ = true option price
- $$\hat{C}_{t+1,i}$$ = predicted option price

### Interpretation

MAE measures the average absolute forecasting error.

For example:

$$
MAE = 2
$$

means that forecasts are, on average, two price units away from the true option price.

Lower MAE indicates better forecasting accuracy.

---

## Root Mean Squared Error (RMSE)

### Formula

$$
RMSE=
\sqrt{
\frac{1}{N}
\sum_{i=1}^{N}
e_i^2
}
$$

or equivalently:

$$
RMSE=
\sqrt{
\frac{1}{N}
\sum_{i=1}^{N}
\left(
C_{t+1,i}-
\hat{C}_{t+1,i}
\right)^2
}
$$

### Variables

- $$N$$ = number of forecasts
- $$C_{t+1,i}$$ = true option price
- $$\hat{C}_{t+1,i}$$ = predicted option price

### Interpretation

RMSE penalizes large forecasting errors more heavily than MAE because errors are squared before averaging.

A model with occasional large mistakes will therefore obtain a higher RMSE.

Lower RMSE indicates better predictive performance.

---

# 4. Baseline Objective

The purpose of this baseline is to establish benchmark models for the State Similarity Option Pricing project.

The forecasting framework is:

$$
\{C_1,\ldots,C_t\}
\rightarrow
\hat{C}_{t+1}
$$

using either the naïve benchmark:

$$
\hat{C}_{t+1}^{(P)}=
C_t
$$

or the classical statistical benchmark:

$$
\hat{C}_{t+1}^{(ARIMA)}=
ARIMA(C_1,\ldots,C_t)
$$

The State Similarity model will be evaluated against these benchmarks to determine whether historical market-state matching can improve next-day option price forecasting accuracy.

A successful State Similarity model should achieve lower MAE and RMSE values than both the persistence and ARIMA benchmarks.

