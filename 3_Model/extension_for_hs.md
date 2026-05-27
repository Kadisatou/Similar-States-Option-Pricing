# Future Extension for Historical Search and Sliding: Ranked Analogues and Weighted Prediction

## Ranked Historical Analogues

Instead of using only a strict similarity threshold, historical intervals can be ranked according to their total similarity distance from the current market state.

Let:

- $$S^{current}$$ denote the current normalized option-price interval
- $$S^{(p)}$$ denote a historical normalized interval
- $$k_j^{current}$$ and $$k_j^{(p)}$$ denote the normalized factor trajectories

Define the option-price distance:

$$

d_S(p)

=
\left\|
S^{current} - S^{(p)}
\right\|
$$

and factor distances:

$$

d_{k_j}(p)

=

\left\|
k_j^{current} - k_j^{(p)}
\right\|
$$

A total analogue distance can then be defined as:


$$

D(p)

=

\alpha d_S(p)
+
\sum_{j=1}^{m}
\beta_j d_{k_j}(p)
$$

where:

- $$\alpha$$ controls the importance of option-price similarity
- $$\beta_j$$ controls the importance of factor $$j$$

Historical intervals are then ranked by increasing $$D(p)$$.

The top $$K$$ most similar historical intervals are selected as analogues.

---


# Weighted Prediction from Historical Analogues


For each selected historical analogue interval $$p$$, the observed future option price after that interval is:

$$
S_{p+n}
$$

where:

- $$n$$ is the interval length.

Instead of averaging future prices equally, more similar analogues can receive larger weights.

Define analogue weights:

$$

w_p

=
\frac{
1/(D(p)+\delta)
}{
\sum_{q \in \mathcal{A}}
1/(D(q)+\delta)
}
$$

where:

- $$D(p)$$ is the total analogue distance
- $$\delta > 0$$ is a small numerical stabilization constant
- $$\mathcal{A}$$ is the set of selected analogues

The predicted next option price becomes:

$$

\hat S_T

=
\sum_{p \in \mathcal{A}}
w_p S_{p+n}
$$

Thus, historical intervals that more closely resemble the current market state contribute more strongly to the prediction.

---

# Possible Future Improvements

## Alternative Weight Functions

Exponential weighting:

$$

w_p

=
\frac{
e^{-D(p)}
}{
\sum_q e^{-D(q)}
}
$$

This penalizes distant analogues more aggressively.

---

# Dynamic Factor Weighting

Factor weights could adapt dynamically according to market regimes:

- volatility-dominant regimes
- trend-dominant regimes
- macroeconomic regimes

---

# Regime Clustering Before Analogue Search

Historical intervals could first be clustered into market regimes before performing analogue search, reducing computational complexity and improving relevance.

---

# Multi-Horizon Prediction

The framework could later predict:

- short-term option price evolution
- volatility trajectories
- probability distributions of future prices
