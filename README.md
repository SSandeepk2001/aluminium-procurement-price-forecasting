# 🚀 Aluminium Procurement Price Forecasting

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Backend-Flask-green)
![Machine Learning](https://img.shields.io/badge/ML-TimeSeries-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A **Machine Learning Time Series Forecasting System** that predicts aluminium prices to help organizations **optimize procurement decisions and reduce supply chain costs.**

This project applies **SARIMA and Facebook Prophet models** to analyze historical aluminium price trends and deploys the prediction system using a **Flask REST API**.

---

# 📌 Problem Statement

Aluminium prices fluctuate due to **market demand, raw material costs, and economic conditions**.
Incorrect procurement timing can lead to **significant financial losses**.

This project solves that problem by **predicting future aluminium prices using machine learning models.**

---

# 🧠 Tech Stack

| Category         | Technology          |
| ---------------- | ------------------- |
| Programming      | Python              |
| Data Processing  | Pandas, NumPy       |
| Visualization    | Matplotlib, Seaborn |
| Machine Learning | SARIMA, Prophet     |
| Backend          | Flask               |
| Model Storage    | Pickle              |
| Version Control  | Git, GitHub         |

---

# 📂 Project Architecture

```
Data Source
    │
    ▼
Data Cleaning & Preprocessing
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Time Series Modeling
(SARIMA & Prophet)
    │
    ▼
Model Evaluation
    │
    ▼
Flask API Deployment
    │
    ▼
Price Prediction Output
```

---

# 📁 Project Structure

```
aluminium-procurement-price-forecasting
│
├── Aluminium_Data.csv
├── Python_code.ipynb
├── model_building.py
├── prophet_model.pkl
├── sarima_model.pkl
├── app.py
├── sql_code.sql
├── README.md
└── LICENSE
```

---

# 📊 Project Workflow

1️⃣ Data Collection
2️⃣ Data Cleaning & Preprocessing
3️⃣ Exploratory Data Analysis (EDA)
4️⃣ Time Series Forecasting
5️⃣ Model Training (SARIMA & Prophet)
6️⃣ Model Evaluation
7️⃣ Flask API Deployment

---

# 🤖 Machine Learning Models

### 📉 SARIMA

Seasonal AutoRegressive Integrated Moving Average model used to capture **trend and seasonal patterns** in aluminium prices.

### 📈 Facebook Prophet

A robust forecasting model designed to handle:

* Trend changes
* Seasonality
* Missing values
* Time series forecasting

---

# 🔌 Flask API Deployment

The trained models are deployed using a **Flask REST API** that provides aluminium price predictions.

### Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

# 📡 API Endpoint

### Predict Aluminium Price

```
POST /predict
```

### Example Request

```json
{
 "date": "2025-01-01"
}
```

### Example Response

```json
{
 "predicted_price": 2450.32
}
```

---

# 📊 Key Features

✔ Aluminium price forecasting
✔ Time series analysis
✔ Outlier detection
✔ Data visualization
✔ Flask REST API deployment
✔ Model comparison (SARIMA vs Prophet)

---

# 💼 Business Impact

Using predictive analytics, organizations can:

* Reduce procurement costs
* Forecast aluminium price trends
* Optimize purchasing strategies
* Improve supply chain planning

---

# 📸 Future Improvements

* Deploy API on **AWS / Railway / Render**
* Build **interactive dashboard**
* Add **real-time price data integration**
* Implement **LSTM deep learning model**

---

# 👨‍💻 Author

**Sandeep Kumar**

🎓 B.Tech – Computer Science Engineering
📊 Data Scientist | Machine Learning | Generative AI

GitHub
https://github.com/SSandeepk2001

---

⭐ If you like this project, give it a **star** on GitHub.
