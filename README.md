# Historical State Similarity Option Pricing

## Overview

Similar States Option Pricing is a hybrid computational finance and machine learning framework for European option pricing based on:

* historical market-state similarity,
* latent factor learning,
* regime detection,
* probabilistic uncertainty estimation,
* and nonlinear residual correction.

The central idea of the project is the following:

> If market factors evolve today similarly to how they evolved during some past interval, then future option-price behavior should also evolve similarly to what followed those historical intervals.

The framework searches for historical market intervals whose dynamics resemble the current market state, then uses the future option behavior observed after those intervals to estimate future option prices under current market conditions.

The project combines:

* computational finance theory,
* historical analogue learning,
* latent representation learning,
* Gaussian Process residual modeling,
* and multidimensional reliability visualization.

---

# Objectives

The objective of the project is to create a hybrid option-pricing framework capable of:

* learning hidden latent market structures,
* detecting recurring historical market states,
* identifying market regime transitions,
* improving pricing accuracy through historical analogue learning,
* integrating computational finance theory with machine learning,
* modeling nonlinear residual pricing dynamics,
* quantifying prediction uncertainty,
* and constructing interpretable multidimensional market-state diagnostics.

The framework aims to move beyond purely theoretical pricing models and purely black-box machine learning systems by combining:

* financial interpretability,
* market-state similarity,
* nonlinear learning,
* and probabilistic confidence estimation

into a unified pricing architecture.

---

# Repository Structure

```text
project-root/
│
├── 0_LiteratureReview/
│   └── README.md
│
├── 1_DatasetCharacteristics/
│   └── README.md
│
├── 2_BaselineModel/
│   └── README.md
│
├── 3_Model/
│   ├── README.md
│   ├── methodology.md
│   ├── latent_factors.md
│   ├── correction_factor.md
│   ├── curse_of_dimensionality.md
│   └── reliability_map.md
│
├── 4_Presentation/
│   └── README.md
│
├── CoverImage/
│
├── .gitignore
├── LICENSE
└── README.md
```

---

# Models Used

## Computational Finance Models

The project currently considers several classical computational finance pricing frameworks for benchmarking and comparison:

* Black-Scholes Model
* Heston Stochastic Volatility Model
* Monte Carlo Simulation
* FFT-Based Pricing Methods

These models serve as theoretical and empirical benchmark pricing systems.

---

## Machine Learning and Hybrid Modeling

The proposed framework combines several machine learning and statistical learning techniques:

* Historical Analogue Learning
* Nearest-Neighbor Market-State Search
* Weighted Distance Similarity
* Gaussian Kernel Similarity
* LSTM Autoencoders
* Latent Representation Learning
* Latent Regime Detection
* Gaussian Process Regression
* Residual Nonlinear Correction
* Dynamic Reliability Visualization

Possible supporting models include:

* XGBoost
* LightGBM
* K-Means Clustering
* Gaussian Mixture Models
* Spectral Clustering
* HDBSCAN

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

The dataset is used to:

* construct sequential market-state intervals,
* learn latent market representations,
* identify historical analogues,
* estimate future option prices,
* and evaluate model reliability across different market conditions.

---

# Results

The project aims to evaluate:

* pricing accuracy,
* robustness across market regimes,
* analogue-state prediction quality,
* latent regime interpretability,
* uncertainty estimation,
* and reliability diagnostics.

The project considers this Evaluation metrics:

* Mean Absolute Error (MAE),
* Root Mean Squared Error (RMSE),
* confidence intervals,
* predictive uncertainty,
* and benchmark comparisons against classical pricing models.

The project also introduces a Dynamic Multi-Layer Reliability Map designed to visualize:

* pricing reliability,
* volatility conditions,
* market distress,
* prediction quality,
* and statistical confidence.

---

# Authors

Kadisatou Fane
