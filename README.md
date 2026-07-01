# Decode-Labs---EDA-Pipeline
Advanced exploratory data analysis and feature engineering for e-commerce data
# 🚀 Advanced EDA & Feature Engineering: E-Commerce Dataset
**Decode Labs - Data Analytics Internship | Project 1**

## 📌 Executive Summary
Predictive machine learning models are only as effective as the data feeding them. This project focuses on establishing a mathematically rigorous foundation for an e-commerce dataset by transforming chaotic, raw data into a clean, model-ready architecture. 

## 🧠 Methodology & Mathematical Clarity
Rather than simply dropping missing values, this pipeline relies on statistical logic to preserve data integrity:

*   **Statistical Imputation (KNN):** Handled missing categorical and numerical variables using K-Nearest Neighbors (KNN) and mode substitution, ensuring distribution shapes remained intact.
*   **Outlier Neutralization (IQR Method):** Applied the Interquartile Range (IQR = Q_3 - Q_1) to mathematically isolate and neutralize extreme financial anomalies in `TotalPrice` without distorting the underlying consumer behavior variance.
*   **Feature Engineering:** Extracted three novel predictive signals from existing dimensions:
    1.  `Avg_Item_Value`: A ratio of Total Price to Items in Cart.
    2.  `Is_Weekend`: A binary temporal feature extracted from timestamps.
    3.  `Used_Coupon`: A binary categorical flag mapping promotional engagement.

## 🛠️ Tech Stack
*   **Core:** Python 3.14
*   **Libraries:** Pandas, NumPy, Scikit-Learn, SciPy
*   **Environment:** VS Code

## ⚙️ How to Run the Pipeline
1. Clone this repository: `git clone https://github.com/RavinduWeer/Decode-Labs---EDA-Pipeline`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Place the raw dataset in the `data/` directory.
4. Execute the Python script located in `notebooks/project1.py`.

## 📈 Next Steps
With the dataset mathematically cleaned and engineered, the next phase involves connecting this architecture to an interactive business intelligence dashboard to visualize consumer purchasing behaviors.
