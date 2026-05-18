# Latent Factors and Latent Regimes

## Objective

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

# Step 1 — Build Latent Representations

## Why a Supervised LSTM Autoencoder?

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

## Sequential Market Intervals

Define a historical interval:

\[
I_t = \{t-n+1,\dots,t\}
\]

where:

* \(n\) is the interval length,
* and \(t\) is the final time point of the interval.

The input sequence becomes:

\[
X_{t-n+1:t}
=
[X_{t-n+1},...,X_t]
\]

Each interval represents the recent evolution of the market state.

---

## LSTM Encoder

The sequence is processed through an LSTM encoder:

\[
h_\tau = \text{LSTM}(X_\tau,h_{\tau-1})
\]

The encoder compresses the interval into a latent representation:

\[
z_t = g_\theta(X_{t-n+1:t})
\]

with:

\[
z_t = [z_{1,t},z_{2,t},...,z_{p,t}]
\]

where:

* \(z_t\) represents latent market-state factors,
* \(p\) is the number of latent dimensions,
* and \(g_\theta\) is the learned encoder function.

---

## Decoder Reconstruction

The decoder reconstructs the original interval:

\[
\hat X_{t-n+1:t}
\]

from:

\[
z_t
\]

using the reconstruction loss:

\[
\mathcal L_{\text{recon}}
=
\left|
X_{t-n+1:t}
-
\hat X_{t-n+1:t}
\right|^2
\]

The reconstruction objective forces the latent representation to preserve important information about the historical market interval.

---

# Step 2 — Analyze Latent Dimensions

After learning the latent vector \(z_t\), each latent coordinate is analyzed to understand what type of hidden market information it may encode.

The goal is to determine whether some latent dimensions behave like meaningful financial factors.

---

## Techniques

Possible interpretation techniques include:

* correlation analysis,
* sensitivity analysis,
* PCA-style loading analysis,
* comparison with volatility regimes,
* comparison with liquidity conditions,
* comparison with market stress indicators,
* and comparison with option pricing errors.

---

## Objective

The objective is to determine whether latent variables encode:

* volatility structure,
* liquidity effects,
* market stress,
* nonlinear option behavior,
* and market regime transitions.

---

## Example

If:

\[
\text{Corr}(z_1,\sigma) \gg 0
\]

then:

\[
z_1
\]

may represent a latent volatility factor.

Similarly, if a latent factor increases during crisis periods or high-spread periods, it may represent a latent stress or liquidity factor.

---

# Step 3 — Cluster the Latent Space

The latent representations are clustered in order to identify recurring hidden market regimes.

Each interval \(I_t\) is represented by its latent vector:

\[
z_t
\]

The clustering algorithm groups similar latent vectors together.

---

## Possible Clustering Methods

Possible clustering methods include:

* K-Means,
* Gaussian Mixture Models,
* Spectral Clustering,
* HDBSCAN.

---

## Example Regimes

| Cluster | Interpretation |
| ------- | -------------- |
| A | Calm market |
| B | Trending market |
| C | High volatility |
| D | Crisis regime |

The exact interpretation of each cluster depends on the empirical behavior of the latent vectors and their relationship with observed market variables.

---

# Step 4 — Convert Clusters into Latent Regime Factors

Define:

\[
R_t \in \{1,2,3,4\}
\]

where:

* \(R_t=1\): calm regime,
* \(R_t=2\): trending regime,
* \(R_t=3\): stressed regime,
* \(R_t=4\): crisis regime.

The regime variable \(R_t\) becomes an additional market-state factor.

---

# Final Hybrid Factor Set

The original factor set is extended by adding latent factors and latent regimes:

\[
F^*
=
\{S,\sigma,r,\tau,\Delta,\Gamma,...,z_1,z_2,...,z_p,R_t\}
\]

where:

* \(S\) is the underlying asset price,
* \(\sigma\) is volatility,
* \(r\) is the interest rate,
* \(\tau\) is time-to-maturity,
* \(\Delta\) is Delta,
* \(\Gamma\) is Gamma,
* \(z_1,z_2,...,z_p\) are latent market factors,
* and \(R_t\) is the latent regime indicator.

---

# Final Interpretation

Latent representation learning allows the model to move beyond directly observable market variables.

The latent factors help capture hidden structures inside market dynamics, while the latent regimes help classify recurring market states.

These learned components are then used during:

* historical analogue search,
* option-price prediction,
* correction modeling,
* regime detection,
* and reliability evaluation.
