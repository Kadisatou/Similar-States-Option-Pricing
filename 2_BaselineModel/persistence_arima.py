"""
Classical baseline for next-day option price forecasting.

Models:
- Persistence (naïve benchmark)
- ARIMA(1,1,1) (classical statistical benchmark)

Evaluation:
- MAE
- RMSE
"""

import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

warnings.filterwarnings("ignore")


def forecast_one_sheet(
    file_path,
    sheet_name,
    n_random_dates=10,
    date_col="DATE",
    price_col="FAIR (MODEL) VALUE",
    random_state=42,
    arima_order=(1, 1, 1),
    min_history=30,
):
    # Load and clean the option price series
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df.columns = df.columns.str.strip()
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce", dayfirst=True)
    df[price_col] = pd.to_numeric(df[price_col], errors="coerce")
    df = df.dropna(subset=[date_col, price_col]).sort_values(date_col).reset_index(drop=True)

    # Define today's price and the true next-day price
    df["forecast_date_t_plus_1"] = df[date_col].shift(-1)
    df["C_t"] = df[price_col]
    df["C_true_t_plus_1"] = df[price_col].shift(-1)

    # Valid forecast dates must have a next-day value and enough past data for ARIMA
    valid_indices = df.dropna(subset=["forecast_date_t_plus_1", "C_t", "C_true_t_plus_1"]).index
    valid_indices = [idx for idx in valid_indices if idx >= min_history]

    if len(valid_indices) < n_random_dates:
        raise ValueError(f"Not enough valid rows in {sheet_name}")

    sampled_indices = (
        pd.Series(valid_indices)
        .sample(n=n_random_dates, random_state=random_state)
        .sort_values()
        .tolist()
    )

    forecasts = []

    for idx in sampled_indices:
        history = df.loc[:idx, "C_t"].dropna()
        C_t = df.loc[idx, "C_t"]
        C_true = df.loc[idx, "C_true_t_plus_1"]

        # Naive benchmark: tomorrow's price equals today's price
        C_hat_persistence = C_t

        # Classical statistical benchmark: ARIMA forecast using prices up to date t only
        try:
            C_hat_arima = float(ARIMA(history, order=arima_order).fit().forecast(steps=1).iloc[0])
            C_hat_arima = np.nan if C_hat_arima < 0 else C_hat_arima
        except Exception:
            C_hat_arima = np.nan

        forecasts.append({
            "sheet_name": sheet_name,
            "DATE_t": df.loc[idx, date_col],
            "forecast_date_t_plus_1": df.loc[idx, "forecast_date_t_plus_1"],
            "C_t": C_t,
            "C_true_t_plus_1": C_true,
            "C_hat_persistence": C_hat_persistence,
            "C_hat_ARIMA": C_hat_arima,
        })

    forecast_table = pd.DataFrame(forecasts)

    # Forecast errors: true next-day price minus predicted next-day price
    error_persistence = forecast_table["C_true_t_plus_1"] - forecast_table["C_hat_persistence"]
    error_arima = forecast_table["C_true_t_plus_1"] - forecast_table["C_hat_ARIMA"]

    summary_table = pd.DataFrame({
        "sheet_name": [sheet_name],
        "MAE_persistence": [error_persistence.abs().mean()],
        "RMSE_persistence": [np.sqrt((error_persistence ** 2).mean())],
        "MAE_ARIMA": [error_arima.abs().mean()],
        "RMSE_ARIMA": [np.sqrt((error_arima ** 2).mean())],
    })

    return forecast_table, summary_table


folder = Path("data")
file_path = folder / "data01.xlsx"

sheets = [
    "call_dax_dec26_17400",
    "call_dax_dec26_13800",
    "call_III_dec26_1360",
]

results = [
    forecast_one_sheet(file_path, sheet, n_random_dates=10, random_state=42)
    for sheet in sheets
]

forecast_results = pd.concat([r[0] for r in results], ignore_index=True)
accuracy_summary = pd.concat([r[1] for r in results], ignore_index=True)

# Overall performance across the selected option sheets
overall_row = pd.DataFrame({
    "sheet_name": ["OVERALL"],
    "MAE_persistence": [accuracy_summary["MAE_persistence"].mean()],
    "RMSE_persistence": [np.sqrt(np.mean(accuracy_summary["RMSE_persistence"] ** 2))],
    "MAE_ARIMA": [accuracy_summary["MAE_ARIMA"].mean()],
    "RMSE_ARIMA": [np.sqrt(np.mean(accuracy_summary["RMSE_ARIMA"] ** 2))],
})

accuracy_summary = pd.concat([accuracy_summary, overall_row], ignore_index=True)

output_path = folder / "results.xlsx"

with pd.ExcelWriter(output_path) as writer:
    forecast_results.to_excel(writer, sheet_name="Forecasts", index=False)
    accuracy_summary.to_excel(writer, sheet_name="Accuracy", index=False)

print("\nForecast Results:")
print(forecast_results)

print("\nAccuracy Summary:")
print(accuracy_summary)

print(f"\nSaved results to:\n{output_path}")
