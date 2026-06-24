# Historical Search and Intervals Weight Estimation

This document describes two alternative historical analogue methods used to forecast the next option price.

Both methods operate exclusively on the normalized option-price trajectory.

Market factors such as volatility, interest rates, liquidity variables, and latent factors are intentionally excluded from the similarity search and may later be introduced through a separate correction mechanism.

---

# Notation

Let:

$$
S^{current}
=
(S_1,S_2,\ldots,S_n)
$$

denote the current normalized option-price interval of length \(n\).

For each historical time point \(p\), define the historical interval:

$$
S^{(p)}
=
(S_{p-n+1},S_{p-n+2},\ldots,S_p)
$$

The objective is to predict the next option price:

$$
\hat S_{T+1}
$$

using historical intervals that resemble the current market state.

---

# Method 1: Kernel-Based Historical Analogue Search

## Distance Computation

For each historical interval \(S^{(p)}\), compute the Euclidean distance from the current interval:

$$
d(p)
=
\left\|
S^{current}
-
S^{(p)}
\right\|^2
$$

which can be written as:

$$
d(p)
=
\sum_{i=1}^{n}
\left(
S_i^{current}
-
S_i^{(p)}
\right)^2
$$

Small values indicate strong similarity between the current interval and the historical interval.

---

## Gaussian Kernel Similarity

Distances are transformed into similarity scores using a Gaussian kernel:

$$
k(p)
=
\exp
\left(
-\frac{d(p)}
{2l^2}
\right)
$$

where:

$$
l>0
$$

is a bandwidth parameter controlling how quickly similarity decays with distance.

Properties:

- highly similar intervals produce values close to 1,
- dissimilar intervals produce values close to 0.

---

## Kernel Weights

The similarity scores are normalized into weights:

$$
\alpha_p
=
\frac{k(p)}
{\sum_{q \in \mathcal A} k(q)}
$$

where:

$$
\mathcal A
$$

denotes the set of selected historical analogues.

The weights satisfy:

$$
\sum_{p \in \mathcal A}
\alpha_p
=
1
$$

---

## Prediction

The future option price is predicted as:

$$
\hat S_{T+1}
=
\sum_{p \in \mathcal A}
\alpha_p S_{p+1}
$$

Historical intervals with stronger similarity receive larger weights and therefore contribute more heavily to the forecast.

---

# Method 2: Distance-Ranked Historical Analogues

## Distance Computation

For each historical interval, compute the Euclidean distance:

$$
D(p)
=
\left\|
S^{current}
-
S^{(p)}
\right\|
$$

or equivalently:

$$
D(p)
=
\sqrt{
\sum_{i=1}^{n}
\left(
S_i^{current}
-
S_i^{(p)}
\right)^2
}
$$

Historical intervals are ranked according to increasing distance.

The top \(K\) nearest intervals are selected as analogues.

---

## Inverse-Distance Weights

Each selected analogue receives a weight proportional to the inverse of its distance:

$$
w_p
=
\frac{
1/(D(p)+\delta)
}{
\sum_{q \in \mathcal A}
1/(D(q)+\delta)
}
$$

where:

$$
\delta > 0
$$

is a small stabilization constant preventing division by zero.

The weights satisfy:

$$
\sum_{p \in \mathcal A}
w_p
=
1
$$

---

## Prediction

The next option price is predicted as:

$$
\hat S_{T+1}
=
\sum_{p \in \mathcal A}
w_p S_{p+1}
$$

More similar historical intervals receive larger weights and therefore exert greater influence on the prediction.

---

# Comparison of the Two Methods

| Feature | Method 1 | Method 2 |
|----------|----------|----------|
| Similarity Measure | Gaussian Kernel | Inverse Distance |
| Distance Metric | Euclidean Distance | Euclidean Distance |
| Weighting Function | Kernel Similarity | Reciprocal Distance |
| Weight Normalization | Yes | Yes |
| Forecast Type | Kernel-Weighted Average | Distance-Weighted Average |
| Complexity | Slightly Higher | Simpler |

---
