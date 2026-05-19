# Methodology

# Core Philosophy

## Market-State Recurrence Principle

Financial markets exhibit recurring dynamic structures characterized by repeated:

* volatility patterns,
* liquidity conditions,
* correlation structures,
* and behavioral market regimes.

Although market conditions are never perfectly identical, financial systems frequently revisit similar dynamic states over time.

The proposed framework is based on the principle that:

> Similar market-state trajectories tend to produce statistically similar future option-price behavior.

---

## Historical Analogue Principle

The framework assumes that if the evolution of market factors over a recent interval resembles the evolution observed during some historical interval, then the subsequent option-price dynamics should also exhibit similarity.

The methodology therefore searches for historical analogue intervals whose factor trajectories resemble the current market state.

The next option price observed after those historical intervals is then used to estimate the future option price under current market conditions.

---

## Hybrid Financial Learning Principle

Classical computational finance models and pure machine learning models both exhibit important limitations.

Traditional pricing models:

* impose strong theoretical assumptions,
* often struggle with nonlinear market dynamics,
* and may fail under stressed or rapidly changing market conditions.

Pure machine learning models:

* may overfit,
* often lack financial interpretability,
* and frequently ignore theoretical financial structure.

The proposed framework combines:

* historical analogue learning,
* computational finance theory,
* latent representation learning,
* probabilistic modeling,
* and nonlinear residual correction.

The objective is to construct a hybrid pricing system capable of combining:

* theoretical financial structure,
* nonlinear learning,
* market-state similarity,
* and uncertainty quantification.

---

## Latent Market Structure Principle

Observed market variables alone do not fully describe the internal state of financial markets.

Hidden latent structures exist within:

* volatility dynamics,
* liquidity behavior,
* correlation evolution,
* order-flow structure,
* and regime transitions.

The framework therefore learns hidden latent market factors and latent market regimes directly from historical data.

These latent structures become additional predictive variables used during analogue search and option-price estimation.

---

## Uncertainty and Reliability Principle

Financial predictions should not only produce numerical price estimates.

A reliable pricing framework should also quantify:

* prediction uncertainty,
* confidence levels,
* market instability,
* and model reliability.

The proposed methodology therefore integrates:

* probabilistic confidence estimation,
* Gaussian Process uncertainty modeling,
* and a Dynamic Multi-Layer Reliability Map.

---

# Market-State Construction

## Sequential Market Intervals

Define a historical interval:

$$
I_t = \{t-n+1,\dots,t\}
$$

where:

* \(n\) is the interval length,
* and \(t\) is the final time point of the interval.

Each interval represents the recent evolution of the market state.

---

## Factor Set

We define the factor set:

$$
F = \{k_1,k_2,\dots,k_m\}
$$

where the factors may include:

* stock price $(S_t)$,
* volatility $$\(\sigma_t\)$$,
* interest rate $$\(r_t\)$$,
* dividend yield,
* time-to-maturity $$\(\tau_t\)$$,
* moneyness,
* implied volatility,
* trading volume,
* bid-ask spread,
* liquidity measures,
* option Greeks,
* latent factors,
* and latent regimes.

---

## Market-State Vector

For each time step $\tau$, we define:

$$
X_\tau =
\left[
C_\tau,
S_\tau,
\sigma_\tau,
r_\tau,
\tau_\tau,
\Delta_\tau,
\Gamma_\tau,
\text{Volume}_\tau,
\text{Spread}_\tau,
\dots
\right]
$$

where:

- $C_\tau$: option price,
- $S_\tau$: underlying asset price,
- $\sigma_\tau$: volatility,
- $r_\tau$: interest rate,
- $\tau_\tau$: time-to-maturity,
- $\Delta_\tau$: option price sensitivity to changes in the underlying asset price,
- $\Gamma_\tau$: rate of change of Delta with respect to the underlying asset price.

The interval sequence becomes:

$$
x_{t-n+1:1} =
[X_{t-n+1},...,X_t]
$$

---
# Latent Representation Learning

The framework learns hidden latent market representations from historical intervals.

The objective is to capture nonlinear market dynamics not fully observable through standard financial variables.

The latent learning module includes:

* LSTM autoencoders,
* latent embeddings,
* latent factor extraction,
* and latent regime discovery.

The learned latent variables extend the original factor set into:

$$
F^*
\{S,\sigma,r,\tau,\Delta,\Gamma,\dots,z_1,z_2,\dots,z_p,R_t\}
$$

where:

- $z_i$ are latent market factors,
- and $R_t$ denotes latent market regimes.


The latent learning framework is detailed in:

```text
latent_factors.md
```

---

# Historical Analogue Search

## Current Market State

We define the current interval:

$$
I_{\text{current}} = \{T-n+1,\dots,T\}
$$

where:

- $T$ denotes the current time point.

For each factor:

$$
k_j^{\text{current}}(i)
$$

we observe the recent trajectory over the last $n$ observations.

---

## Historical Search

The framework scans historical data and searches for intervals:

$$
I_p = \{p-n+1,\dots,p\}
$$

such that:

$$
|k_j^{\text{current}}(i)-k_j^{(p)}(i)| \le \epsilon_j
$$

for:

- all factors $j$,
- and all time points inside the interval.
- 
where:

* $\epsilon_j$ is the similarity tolerance threshold for factor $j$.

The objective is to identify historical periods whose market-state evolution resembles the current market state.

---

# Resolving the Curse of Dimensionality

Exact matching between high-dimensional market states becomes increasingly difficult as the number of factors increases.

The framework therefore replaces strict matching with:

* weighted distance metrics,
* nearest-neighbor selection,
* and Gaussian kernel similarity.

The technic used to solve this curse is detailed in:

```text
curse_of_dimensionality.md
```
---
# Prediction Engine

Suppose the framework identifies one or several matching historical intervals:

$$ I_{p_1},I_{p_2},\dots,I_{p_M}$$

The corresponding future option prices are:
$$C_{p_1+1},C_{p_2+1},\dots,C_{p_M+1}$$

---

## Single Analogue Prediction

If only one analogue interval exists:

$$
\hat C_{T+1} = C_{p_1+1}
$$

The future price estimate is directly obtained from the historical analogue.

---

## Multiple Analogue Prediction

If several analogue intervals are found:

$$
\hat c_{T+1} =
\frac1M
\sum_{m=1}^{M} C_{p_m+1}
$$

The averaging process stabilizes the prediction and reduces sensitivity to isolated market anomalies.

---

# Correction Framework

Historical analogue predictions alone may fail to fully capture:

* regime changes,
* nonlinear dynamics,
* liquidity distortions,
* and market structural shifts.

The framework therefore introduces a correction factor:

$$
C^{\text{true}}_{t+1}

=
C^{\text{analogue}}_{t+1}
+
O_t
$$

where:

- $$C^{\text{analogue}}_{t+1}$$ is the historical analogue estimate,
- and $O_t$ is the market-state correction term.

The correction framework combines:

* Greek-based theoretical corrections,
* and machine learning residual corrections.

The complete correction methodology is detailed in:

```text
correction_factor.md
```

---

# Uncertainty Estimation

The framework integrates probabilistic uncertainty estimation through Gaussian Process Regression.

The predictive distribution becomes:

$$
V_t^{pred}
\sim
\mathcal N(\mu_t,\sigma_t^2)
$$

where:

* $$\mu_t$$ is the predicted option value,
* $$\sigma_t^2$$ is the predictive variance.

The predictive variance provides:

* confidence intervals,
* uncertainty estimation,
* and reliability measurements.

---

# Reliability Visualization

The framework includes a Dynamic Multi-Layer Reliability Map designed to visualize:

* pricing reliability,
* volatility conditions,
* market stress,
* prediction quality,
* and confidence levels.

The visualization transforms each option price into a multidimensional diagnostic object.

The reliability visualization framework is detailed in:

```text
reliability_map.md
```

---

# Final Hybrid Pricing Equation

The final hybrid pricing system becomes:

$$
\boxed{
\hat C_{t+1}

=

C^{\text{analogue}}_{t+1}
+
O_{\text{Greek}}
+
f_\theta(X_t)
}
$$

where:

* $C^{\text{analogue}}_{t+1}$ captures historical market analogues,
* $O_{\text{Greek}}$ captures theoretical financial corrections,
* and $f_\theta(X_t)$ captures nonlinear residual market dynamics.

---

# Final Interpretation

The proposed framework models European option dynamics as a hybrid interaction between:

* observable market variables,
* latent market structures,
* recurring historical analogues,
* probabilistic uncertainty,
* and nonlinear financial corrections.

The system therefore combines:

* computational finance,
* machine learning,
* latent representation learning,
* and market-state diagnostics

into a unified dynamic pricing architecture.
