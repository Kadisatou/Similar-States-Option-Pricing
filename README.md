# Dynamic-State-Similarity-Pricing

## Overview

This project proposes a hybrid computational finance and machine learning framework for European option pricing based on historical market-state similarity, latent factor learning, and nonlinear residual correction.

The central idea is the following:

> If market factors evolve today similarly to how they evolved during some past interval, then the future option price should behave similarly to what happened after that historical interval.

The framework combines:

* historical analogue learning,
* latent market-state modeling,
* regime detection,
* Gaussian Process residual correction,
* and computational finance theory.

The model searches for historical intervals that resemble the current market state, then uses the observed future option behavior from those intervals to estimate future prices under current conditions.

---

# Detailed Description

## Formal Mathematical Interpretation

We define the factor set:

[
F = {k_1,k_2,\dots,k_m}
]

where the factors may include:

* stock price (S_t),
* volatility (\sigma_t),
* interest rate (r_t),
* dividend yield,
* time-to-maturity (\tau_t),
* moneyness,
* implied volatility,
* trading volume,
* bid-ask spread,
* liquidity measures,
* Greeks,
* latent market factors,
* and latent market regimes.

The observed sequential market vector at time (\tau) becomes:

[
X_\tau =
[
C_\tau,
S_\tau,
\sigma_\tau,
r_\tau,
\tau_\tau,
\Delta_\tau,
\Gamma_\tau,
\text{Volume}*\tau,
\text{Spread}*\tau,
\dots
]
]

where:

* (C_\tau): option price,
* (S_\tau): underlying asset price,
* (\sigma_\tau): volatility,
* (r_\tau): interest rate,
* (\tau_\tau): time-to-maturity,
* (\Delta_\tau): option price sensitivity to changes in the underlying asset price,
* (\Gamma_\tau): rate of change of Delta with respect to the underlying asset price.

---

## Deriving the Latent Factors and Latent Regimes

### Objective

Learn hidden latent market factors and latent market regimes from historical intervals of European option prices and observed market variables.

The objective is to capture hidden nonlinear market dynamics not fully represented by visible factors such as:

* stock price,
* volatility,
* interest rates,
* Greeks,
* liquidity variables,
* and option surface characteristics.

The learned latent representations are later transformed into additional predictive market-state factors and market regimes.

---

## Step 1 — Build Latent Representations

### Why a Supervised LSTM Autoencoder?

A supervised sequence autoencoder is chosen because the project is fundamentally based on:

* temporal interval dynamics,
* historical trajectory similarity,
* repeated market states,
* and sequential option-price behavior.

An LSTM architecture is particularly suitable because:

* option prices evolve sequentially through time,
* volatility exhibits persistence and clustering,
* market regimes evolve dynamically,
* and recent trajectories influence future option prices.

---

### Sequential Market Intervals

Define a historical interval:

[
I_t = {t-n+1,\dots,t}
]

The input sequence becomes:

[
X_{t-n+1:t}
===========

[X_{t-n+1},...,X_t]
]

---

### LSTM Encoder

The sequence is processed through an LSTM encoder:

[
h_\tau = \text{LSTM}(X_\tau,h_{\tau-1})
]

The encoder compresses the interval into a latent representation:

[
z_t = g_\theta(X_{t-n+1:t})
]

with:

[
z_t = [z_{1,t},z_{2,t},...,z_{p,t}]
]

where:

* (z_t) represents latent market-state factors.

---

### Decoder Reconstruction

The decoder reconstructs the original interval:

[
\hat X_{t-n+1:t}
]

from:

[
z_t
]

using the reconstruction loss:

[
\mathcal L_{\text{recon}}
=========================

\left|
X_{t-n+1:t}
-----------

\hat X_{t-n+1:t}
\right|^2
]

---

## Step 2 — Analyze Latent Dimensions

Study relationships between latent coordinates and known financial variables.

### Techniques

* correlation analysis,
* sensitivity analysis,
* PCA-style loading analysis.

### Objective

Determine whether latent variables encode:

* volatility structure,
* liquidity effects,
* market stress,
* nonlinear option behavior,
* and market regime transitions.

### Example

If:

[
\text{Corr}(z_1,\sigma) \gg 0
]

then:

[
z_1
]

may represent a latent volatility factor.

---

## Step 3 — Cluster the Latent Space

Cluster latent representations to identify recurring hidden market regimes.

### Possible Clustering Methods

* K-Means,
* Gaussian Mixture Models (GMM),
* Spectral Clustering,
* HDBSCAN.

### Example Regimes

| Cluster | Interpretation  |
| ------- | --------------- |
| A       | Calm market     |
| B       | Trending market |
| C       | High volatility |
| D       | Crisis regime   |

---

## Step 4 — Convert Clusters into Latent Regime Factors

Define:

[
R_t \in {1,2,3,4}
]

where:

* (R_t=1): calm regime,
* (R_t=2): trending regime,
* (R_t=3): stressed regime,
* (R_t=4): crisis regime.

The final hybrid factor set becomes:

[
F^*
===

{S,\sigma,r,\tau,\Delta,\Gamma,...,z_1,z_2,...,z_p,R_t}
]

---

## Current State

We take the most recent interval:

[
I_{\text{current}} = {T-n+1,...,T}
]

where:

* (T) denotes the current time,
* (n) denotes the interval length.

For each factor:

[
k_j^{\text{current}}(i)
]

we obtain a trajectory over the last (n) observations.

---

## Historical Search

We scan historical data and search for intervals:

[
I_p = {p-n+1,...,p}
]

such that:

[
|k_j^{\text{current}}(i)-k_j^{(p)}(i)| \le \epsilon_j
]

for:

* all factors (j),
* and all time points inside the interval.

This means:

> Find historical periods where the market-state evolution resembles the current market-state evolution.

The approach is closely related to:

* nearest-neighbor forecasting,
* dynamic time warping,
* kernel similarity learning,
* and state-space reconstruction.

---

## Prediction Rule

Suppose the search identifies one or several matching historical intervals:

[
I_{p_1},I_{p_2},...,I_{p_M}
]

The corresponding future option prices immediately after those intervals are:

[
C_{p_1+1},C_{p_2+1},...,C_{p_M+1}
]

### Case 1 — Single Matching Interval

If only one matching interval exists:

[
\hat C_{T+1} = C_{p_1+1}
]

The predicted future price is directly obtained from the historical analogue.

---

### Case 2 — Multiple Matching Intervals

If several matching intervals are found, the future option price is estimated using the average of all matching future observations:

[
\hat C_{T+1}
============

\frac1M
\sum_{m=1}^{M} C_{p_m+1}
]

This averaging stabilizes the prediction and reduces sensitivity to isolated market anomalies.

---

# The Correction Factor (O)

(O) is best understood as a residual correction term that adjusts the historical analogue option price to fit current market conditions and regime dynamics.

We define:

[
C^{\text{true}}_{t+1}
=====================

C^{\text{analogue}}_{t+1}
+
O_t
]

where:

* the analogue term captures historical similarity,
* and the correction term adapts the prediction to the present market state.

---

## Volatility Correction

[
O_{\sigma}
\approx
\text{Vega}_t(\sigma_t-\sigma_p)
]

where:

[
\text{Vega} = \frac{\partial C}{\partial \sigma}
]

---

## Time-to-Maturity Correction

[
O_{\tau}
\approx
\Theta_{\text{Greek}}(\tau_t-\tau_p)
]

where:

[
\Theta_{\text{Greek}} = \frac{\partial C}{\partial t}
]

---

## Moneyness Correction

Define moneyness:

[
M_t = \frac{S_t}{K}
]

or log-moneyness:

[
m_t = \ln(S_t/K)
]

The corresponding correction becomes:

[
O_S \approx \Delta_t(S_t-S_p)
]

where:

[
\Delta = \frac{\partial C}{\partial S}
]

---

## Interest Rate Correction

[
O_r \approx \rho_t(r_t-r_p)
]

where:

[
\rho = \frac{\partial C}{\partial r}
]

---

## Liquidity Correction

[
O_{\text{liq}} = g(\text{spread},\text{volume},\text{open interest})
]

---

## Greek-Based Correction

The theoretical financial correction becomes:

[
O_{\text{Greek}}
================

\Delta_t(S_t-S_p)
+
\text{Vega}_t(\sigma_t-\sigma_p)
+
\rho_t(r_t-r_p)
+
\Theta_t(\tau_t-\tau_p)
]

---

## ML Residual Correction

Financial markets remain highly nonlinear even after Greek-based corrections.

Therefore, the remaining pricing discrepancy is modeled using machine learning:

[
O_{\text{residual}}
===================

f_{\theta}(X_t)
]

where:

* (X_t) is the market-state feature vector,
* and (f_{\theta}) is a nonlinear learned function.

The final correction becomes:

[
O_t
===

O_{\text{Greek}}
+
O_{\text{residual}}
]

---

## Gaussian Process Residual Modeling

The residual correction is modeled using Gaussian Process Regression:

[
O_{\text{residual}}
\sim
\mathcal{GP}(m(X),k(X,X'))
]

where:

* (m(X)) is the mean function,
* (k(X,X')) is the covariance kernel.

The predicted residual becomes:

[
\hat O_{\text{residual}}
========================

\mathbb E
\left[
O_{\text{residual}}
\mid X_t
\right]
]

with uncertainty:

[
\text{Var}
\left[
O_{\text{residual}}
\mid X_t
\right]
]

---

# Resolving the Curse of Dimensionality

Exact matching between high-dimensional market intervals becomes increasingly difficult as the number of factors grows.

The similarity condition:

[
|k_j-k_j'| \le \epsilon
]

requires all factors to remain sufficiently close.

Here:

* (\epsilon) denotes the similarity tolerance threshold,
* controlling how close two market states must be to be considered analogous.

When no exact analogue exists, the framework instead uses:

* weighted distance metrics,
* nearest-neighbor selection,
* and kernel similarity functions.

---

## Weighted Distance Metric

We define:

[
d(I_a,I_b)
==========

\sum_j w_j ||k_j^{(a)}-k_j^{(b)}||^2
]

where:

* (I_a) and (I_b) are two market intervals,
* (w_j) represents the importance weight of factor (j),
* and the norm measures the difference between the trajectories of the factors.

### Interpretation

The metric measures how different two market-state trajectories are.

* Smaller values indicate highly similar intervals,
* larger values indicate dissimilar market behavior.

The nearest neighbors are therefore the historical intervals producing the smallest values of:

[
d(I_a,I_b)
]

These intervals are selected as the historical analogues used for prediction.

---

## Gaussian Kernel Similarity

A radial basis Gaussian kernel is used to transform distances into similarity scores:

[
k(X_i,X_j)
==========

\exp
\left(
-\frac{||X_i-X_j||^2}{2l^2}
\right)
]

where:

* (l) controls similarity smoothness,
* nearby market states produce stronger similarity scores.

### Interpretation

The kernel assigns:

* values close to 1 for highly similar market states,
* values close to 0 for dissimilar states.

This allows the framework to:

* continuously measure similarity between intervals,
* soften strict matching constraints,
* and generalize beyond exact historical repetitions.

The kernel therefore acts as a smooth extension of the analogue-search mechanism.

---

## Final Hybrid Pricing Model

The final pricing framework becomes:

[
\boxed{
\hat C_{t+1}
============

C^{\text{analogue}}*{t+1}
+
O*{\text{Greek}}
+
f_{\theta}(X_t)
}
]

where:

* (C^{\text{analogue}}_{t+1}) captures historical analogue pricing,
* (O_{\text{Greek}}) captures theoretical financial corrections,
* and (f_{\theta}(X_t)) captures nonlinear residual market dynamics.

---

# Dynamic Multi-Layer Reliability Map

The project also proposes a dynamic visualization framework where each option node contains diagnostic information about:

* volatility,
* market distress,
* prediction quality,
* and confidence levels.

The visualization combines:

* computational finance,
* numerical pricing,
* machine learning,
* volatility analysis,
* and market diagnostics.

Each option node is dynamically surrounded by rings whenever a diagnostic metric exceeds a predefined threshold.

The visualization therefore captures:

* numerical stability,
* prediction reliability,
* market stress,
* volatility,
* and confidence in the pricing process.

---

# Objectives

* Construct a hybrid machine learning framework for European option pricing.
* Learn hidden latent market factors and market regimes.
* Detect recurring historical market states.
* Improve pricing accuracy through analogue learning.
* Integrate computational finance theory with machine learning.
* Model nonlinear residual dynamics using Gaussian Processes.
* Build interpretable multidimensional market-state representations.
* Develop a dynamic reliability and diagnostic visualization framework.

---

# Repository Structure

```text
project-root/
│
├── data/
├── notebooks/
├── src/
│   ├── preprocessing/
│   ├── feature_engineering/
│   ├── latent_models/
│   ├── analogue_search/
│   ├── residual_models/
│   ├── visualization/
│   └── evaluation/
│
├── results/
├── figures/
├── README.md
└── requirements.txt
```

---

# Models Used

## Computational Finance Models

* Black-Scholes
* Heston Model
* Monte Carlo Simulation
* FFT-based Pricing Methods

---

## Machine Learning Models

* LSTM Autoencoder
* Gaussian Process Regression (GPR)
* XGBoost
* LightGBM
* K-Means Clustering
* Gaussian Mixture Models
* Spectral Clustering
* HDBSCAN

---

## Similarity and Distance Models

* Weighted Euclidean Distance
* Gaussian Radial Basis Kernel
* Nearest-Neighbor State Matching
* Dynamic Trajectory Similarity

---

# Dataset

The dataset is obtained from Refinitiv Eikon.

The project uses:

* historical European option prices,
* underlying asset prices,
* implied volatility data,
* interest rates,
* option Greeks,
* trading volume,
* liquidity variables,
* and market regime indicators.

---

# Results

The project aims to evaluate:

* pricing accuracy,
* robustness across market regimes,
* analogue-state prediction quality,
* latent regime interpretability,
* and uncertainty estimation.

Evaluation metrics may include:

* MAE,
* RMSE,
* confidence intervals,
* and benchmark comparisons against classical pricing models.

---

# Authors

Kadisatou Fane
