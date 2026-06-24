# Resolving the Curse of Dimensionality

Exact matching between high-dimensional market intervals becomes increasingly difficult as the number of factors grows.

The similarity condition:

$$
|k_j-k_j'| \le \epsilon
$$

requires all factors to remain sufficiently close.

Here:

* $\epsilon$ denotes the similarity tolerance threshold,
* controlling how close two market states must be to be considered analogous.

When many factors are included, exact historical matching becomes unlikely because the model must simultaneously match:

* stock price,
* volatility,
* interest rates,
* time-to-maturity,
* moneyness,
* Greeks,
* liquidity variables,
* latent factors,
* and latent regimes.

Therefore, the framework replaces strict exact matching with softer similarity methods.

---

# Problem in Historical Analogue Search

The framework scans historical data and searches for intervals:

$$
I_p = \{p-n+1,\ldots,p\}
$$

such that:

$$
|k_j^{\text{current}}(i)-k_j^{(p)}(i)| \le \epsilon_j
$$

for:

* all factors $j$,
* and all time points inside the interval.

This strict condition may fail when the factor space becomes too large.

The framework therefore uses:

* weighted distance metrics,
* nearest-neighbor selection,
* and kernel similarity functions.

---

# Weighted Distance Metric

We define:

$$
d(I_a,I_b)=
\sum_j w_j \left\|k_j^{(a)}-k_j^{(b)}\right\|^2
$$

where:

* $$I_a$$ and $$I_b$$ are two market intervals,
* $$w_j$$ represents the importance weight of factor $$j$$,
* and the norm measures the difference between the trajectories of the factors.

---

## Interpretation

The metric measures how different two market-state trajectories are.

* Smaller values indicate highly similar intervals.
* Larger values indicate dissimilar market behavior.

The nearest neighbors are therefore the historical intervals producing the smallest values of:

$$
d(I_a,I_b)
$$

These intervals are selected as the historical analogues used for prediction.

---

# Factor Weights

The weights $w_j$ control the importance of each market factor.

For example:

* volatility may receive a high weight because option prices are very sensitive to volatility,
* liquidity may receive a high weight during stressed markets,
* interest rates may receive a higher weight for longer-maturity options,
* and latent factors may receive higher weights if they improve prediction accuracy.

The weights can be chosen using:

* financial intuition,
* cross-validation,
* feature importance,
* sensitivity analysis,
* or learned metric methods.

---

# Nearest-Neighbor Selection

Instead of requiring exact equality or strict tolerance matching, the model selects the closest historical intervals.

Given the current interval:

$$
I_{\text{current}}
$$

the model searches for historical intervals:

$$
I_{p_1},I_{p_2},\ldots,I_{p_M}
$$

that minimize:

$$
d(I_{\text{current}},I_p)
$$

The selected intervals become the historical analogues.

---

# Gaussian Kernel Similarity

A radial basis Gaussian kernel is used to transform distances into similarity scores:

$$
k(X_i,X_j)=
\exp
\left(-\frac{\|X_i-X_j\|^2}{2l^2}\right)
$$

where:

* $$l$$ controls similarity smoothness,
* nearby market states produce stronger similarity scores.

---

## Interpretation

The kernel assigns:

* values close to 1 for highly similar market states,
* values close to 0 for dissimilar states.

This allows the framework to:

* continuously measure similarity between intervals,
* soften strict matching constraints,
* and generalize beyond exact historical repetitions.

The kernel therefore acts as a smooth extension of the analogue-search mechanism.

---

# Kernel-Weighted Analogue Prediction

Instead of treating all selected analogues equally, the model can weight each analogue by its similarity score.

If the model identifies analogue intervals:

$$
I_{p_1},I_{p_2},\ldots,I_{p_M}
$$

with similarity weights:

$$
\alpha_1,\alpha_2,\ldots,\alpha_M
$$

then the prediction can be written as:

$$
\hat C_{T+1}=
\sum_{m=1}^{M}
\alpha_m C_{p_m+1}
$$

where:

$$
\sum_{m=1}^{M}\alpha_m = 1
$$

and:

$$
\alpha_m=
\frac{k(I_{\text{current}},I_{p_m})}
{\sum_{q=1}^{M}k(I_{\text{current}},I_{p_q})}
$$

This gives more influence to the most similar historical analogues.

---

# Final Interpretation

The curse of dimensionality is resolved by replacing rigid exact matching with flexible similarity learning.

The framework uses:

* weighted distance metrics,
* nearest-neighbor search,
* Gaussian kernel similarity,
* and kernel-weighted analogue prediction.

This allows the model to identify useful historical analogues even when the current market state does not exactly match any past interval.
