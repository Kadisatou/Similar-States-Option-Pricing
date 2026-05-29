# State Similarity Option Pricing Model

## Overview

This folder contains the core modeling framework of our proposed ML approach.

The proposed methodology combines:

* computational finance,
* historical analogue learning,
* latent representation learning,
* probabilistic modeling,
* and nonlinear machine learning correction

into a unified hybrid pricing architecture for European option pricing.

The model is based on the following principle:

> Similar market-state trajectories tend to produce statistically similar future option-price behavior.

The framework therefore searches for historical market intervals whose dynamics resemble the current market state, then uses the observed future option behavior from those intervals to estimate future option prices under current market conditions.

---

# Core Components

The model architecture combines several interconnected components:

* market-state construction,
* latent factor learning,
* latent regime detection,
* historical analogue search,
* similarity learning,
* Greek-based correction,
* machine learning residual correction,
* probabilistic uncertainty estimation,
* and dynamic reliability visualization.

---

# Methodological Structure

The detailed methodology is separated into the following documents.

---

## Main Methodology

```text
methodology.md
```

Contains:

* the global philosophy of the framework,
* the complete machine learning pipeline,
* market-state construction,
* analogue pricing methodology,
* uncertainty estimation,
* and the final hybrid pricing equation.

---

## Latent Factors and Regime Learning

```text
latent_factors.md
```

Contains:

* latent representation learning,
* LSTM autoencoder architecture,
* latent factor extraction,
* latent-space interpretation,
* clustering methods,
* and latent market regime construction.

---

## Correction Framework

```text
correction_factor.md
```

Contains:

* Greek-based correction,
* volatility correction,
* moneyness correction,
* liquidity correction,
* residual machine learning correction,
* and Gaussian Process residual modeling.

---

## Resolving the Curse of Dimensionality

```text
curse_of_dimensionality.md
```

Contains:

* weighted distance metrics,
* nearest-neighbor analogue selection,
* Gaussian kernel similarity,
* kernel-weighted prediction,
* and high-dimensional similarity learning.

---

## Dynamic Multi-Layer Reliability Map

```text
reliability_map.md
```

Contains:

* reliability visualization,
* volatility diagnostics,
* distress indicators,
* prediction-quality monitoring,
* confidence estimation,
* and multidimensional market-state interpretation.

---

# Global Machine Learning Pipeline

```text
Market Data
     ↓
Feature Construction
     ↓
Latent State Learning
     ↓
Regime Detection
     ↓
Historical Analogue Search
     ↓
Greek-Based Correction
     ↓
ML Residual Correction
     ↓ 
Analogue Pricing
     ↓
Confidence Estimation
     ↓
Reliability Visualization
     ↓
Final Option Price
```

---

# Final Objective

The objective of the proposed framework is to construct a pricing system capable of integrating:

* theoretical financial structure,
* nonlinear machine learning,
* latent market-state dynamics,
* historical market similarity,
* and probabilistic uncertainty estimation

into a unified interpretable option-pricing framework.

---

# Related Project Sections

Additional repository sections include:

* `0_LiteratureReview/`
* `1_DatasetCharacteristics/`
* `2_BaselineModel/`
* `4_Presentation/`

These complementary sections provide:

* academic background,
* dataset analysis,
* benchmark pricing models,
* and project presentation material.

---

# Author

Kadisatou Fane
