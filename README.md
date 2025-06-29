# HoSt x Saxion Predictive Model

This repository provides code and data for predicting Dutch electricity prices and operational hours using machine learning models, including XGBoost. The project leverages Dutch TTF gas prices and historical electricity price data.

---

## Repository Layout

```
Data/
    Dutch TTF Natural Gas Futures Historical Data.csv   # Raw gas price data from the internet
    Netherlands_Op_Hours.csv                           # Data for operational hours calculation
    Netherlands.csv                                    # Historical electricity prices (hourly)
    TTF_daily_prediction.csv                           # Predicted daily gas prices
    TTF_hourly_prediction.csv                          # Hourly gas prices after data injection

Code/
    Conversion_Hourly.ipynb                            # Converts daily gas prices to hourly
    Data_Injection_Daily.ipynb                         # Handles missing days, interpolation, and forecasting
    Electricity_Price_Prediction_Model_SARIMAX.ipynb   # SARIMAX model for electricity price prediction
    Electricity_Price_Prediction_Model_XGBOOST.ipynb   # XGBoost model for electricity price prediction
    hours_algo.py                                      # Operational hours calculation logic
    Operational_Hours_Model.ipynb                      # Notebook for operational hours modeling
    Test Models/                                       # Experimental/test notebooks (e.g., Prophet, SARIMAX)
```

---

## Data Files

- **Dutch TTF Natural Gas Futures Historical Data.csv**: Raw gas price data.
- **Netherlands_Op_Hours.csv**: Used for operational hours calculations.
- **Netherlands.csv**: Historical hourly electricity prices for the Netherlands.
- **TTF_daily_prediction.csv**: Daily predicted gas prices.
- **TTF_hourly_prediction.csv**: Hourly gas prices after data injection/interpolation.

---

## Key Notebooks & Scripts

- **Electricity_Price_Prediction_Model_XGBOOST.ipynb**: Main notebook for electricity price prediction using XGBoost.
- **Operational_Hours_Model.ipynb**: Calculates and analyzes operational hours.
- **Conversion_Hourly.ipynb**: Converts daily gas prices to hourly using interpolation.
- **Data_Injection_Daily.ipynb**: Cleans, interpolates, and forecasts gas price data.

---

## Usage

1. Clone the repository:
    ```bash
    https://github.com/amir4466/HoSt_x_Saxion_Predictive_Model.git
    cd HoSt_x_Saxion_Predictive_Model
    ```

2. Open the notebooks in the `Code/` directory to run analyses or predictions.

3. **If you encounter an import error**, run the following in a notebook cell:
    ```python
    %pip install [package_name]
    ```
    Replace `[package_name]` with the name of the missing library (e.g., `xgboost`, `prophet`, `statsmodels`).

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first, and a different branch.

---

## License

[MIT](LICENSE)