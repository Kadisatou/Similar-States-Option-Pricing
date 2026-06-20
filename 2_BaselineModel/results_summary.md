# Classical Baseline Results

## Overview

This document summarizes the performance of the classical baseline models used for next-day European call option price forecasting.

Two benchmark models were evaluated:

- **Persistence Forecast** (Naïve Benchmark)
- **ARIMA(1,1,1)** (Classical Statistical Benchmark)

For each option contract, 10 valid forecast dates were randomly selected. Forecasts were generated using only information available up to the forecast date, thereby avoiding look-ahead bias.

Performance was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

Lower values indicate better forecasting performance.

---

## Accuracy Results

| Option Contract | MAE Persistence | MAE ARIMA | RMSE Persistence | RMSE ARIMA |
|----------------|----------------:|----------:|-----------------:|-----------:|
| call_dax_dec26_17400 | 6.240 | 6.252 | 13.960 | 13.986 |
| call_dax_dec26_13800 | 8.930 | 8.936 | 19.993 | 20.011 |
| call_III_dec26_1360 | 19.904 | 20.023 | 29.561 | 29.869 |
| **OVERALL** | **11.691** | **11.737** | **22.124** | **22.273** |

---

## Interpretation of Results

Across all evaluated option contracts, the Persistence benchmark achieved slightly lower forecasting errors than the ARIMA(1,1,1) model.

Overall results:

| Model | MAE | RMSE |
|---------|---------:|---------:|
| Persistence | 11.691 | 22.124 |
| ARIMA(1,1,1) | 11.737 | 22.273 |

The performance difference between the two models is very small. However, ARIMA did not provide a meaningful improvement over the naïve benchmark.

This suggests that the short-term dynamics of the selected option price series are not sufficiently captured by a simple ARIMA(1,1,1) specification.

---

## Dataset Observations

Three option contracts were initially selected for evaluation:

- call_dax_dec26_17400
- call_dax_dec26_13800
- call_III_dec26_1360

During exploratory analysis, the two DAX option contracts exhibited extended periods where the reported **FAIR (MODEL) VALUE** remained constant over time.

This behaviour is atypical for actively changing option prices and may reflect vendor-generated valuation procedures, missing market updates, or characteristics of the selected data field rather than genuine market dynamics.

Results for these contracts are reported for completeness and transparency.

The contract:

```text
call_III_dec26_1360
```

displayed substantially greater temporal variation and is therefore considered the most informative dataset for evaluating forecasting performance.

---

## Forecast Output File

The file:

```text
results.xlsx
```

contains two worksheets.

### Forecasts

Contains:

- forecast date,
- observed option price at time \(t\),
- observed option price at time \(t+1\),
- Persistence forecast,
- ARIMA forecast.

### Accuracy

Contains:

- MAE values,
- RMSE values,
- contract-level results,
- overall benchmark performance.

---

## Conclusion

The Persistence forecast serves as the naïve benchmark and achieved the best overall performance among the tested baseline models.

The ARIMA(1,1,1) model produced very similar results but did not improve forecasting accuracy.

These benchmark results establish a reference point against which the proposed State Similarity Option Pricing model will be evaluated.
