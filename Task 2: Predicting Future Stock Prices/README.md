# Stock Price Prediction using Linear Regression

## Overview

This project uses Machine Learning to predict the next day's stock closing price using historical stock market data obtained from Yahoo Finance. The model is trained on past stock information such as opening price, highest price, lowest price, and trading volume to estimate future closing prices.

---

## Task Objective

The objective of this project is to:

* Collect historical stock market data using the `yfinance` API.
* Perform data preprocessing and feature selection.
* Predict the next day's closing stock price.
* Train and evaluate a Machine Learning regression model.
* Visualize and compare actual versus predicted stock prices.

---

## Dataset Used

**Source:** Yahoo Finance

**Library:** `yfinance`

**Stock Used:** Apple Inc. (AAPL)

### Features (Input Variables)

* Open Price
* High Price
* Low Price
* Volume

### Target Variable

* Next Day Closing Price

The target variable is created by shifting the `Close` column by one day using:

```python
data['Target'] = data['Close'].shift(-1)
```

This allows the model to learn how today's market information relates to tomorrow's closing price.

---

## Technologies and Libraries

* Python
* Google Colab
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* yfinance

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Downloaded historical stock data from Yahoo Finance.
2. Created a target column for next-day closing prices.
3. Removed missing values generated during shifting.
4. Selected relevant features.
5. Split data into training and testing sets while preserving chronological order (`shuffle=False`).

---

## Model Applied

### Linear Regression

A Linear Regression model was used to learn the relationship between:

```text
Open Price
High Price
Low Price
Volume
```

and

```text
Next Day Closing Price
```

The model was trained using historical stock market data and then tested on unseen data.

---

## Model Evaluation

The model was evaluated using:

### Mean Absolute Error (MAE)

Measures the average prediction error.

### Root Mean Squared Error (RMSE)

Measures prediction error while penalizing larger mistakes.

### R² Score

Measures how well the model explains the variation in stock prices.

---

## Results

| Metric   | Value  |
| -------- | ------ |
| MAE      | 3.08   |
| RMSE     | 4.23   |
| R² Score | 0.9749 |

---

## Visualization

The project includes a graph comparing:

* Actual Closing Prices
* Predicted Closing Prices

This visualization helps assess how closely the model's predictions match real stock market behavior.

---

## Key Findings

* Historical stock market data can be used to build predictive models.
* Linear Regression successfully learned relationships between stock indicators and future closing prices.
* The model's reliability was assessed using MAE, RMSE, and R² Score.
* Visualization showed the difference between actual and predicted values, helping evaluate model performance.
* Preserving the chronological order of stock data is important when working with time-series datasets.

---

## Future Improvements

Possible enhancements include:

* Using Random Forest Regressor for comparison.
* Adding technical indicators such as Moving Averages and RSI.
* Using multiple stocks for comparative analysis.
* Exploring advanced time-series models such as LSTM networks.
* Deploying the model as a web application using Streamlit.

---

## Author

AI/ML Internship Task – Stock Price Prediction using Machine Learning
