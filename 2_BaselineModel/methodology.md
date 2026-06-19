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

