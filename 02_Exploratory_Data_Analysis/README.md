# 📊 Project 2: Exploratory Data Analysis (EDA) & Diagnostic Framework

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Libraries](https://img.shields.io/badge/Libraries-Pandas_|_Seaborn-lightgrey)
![Status](https://img.shields.io/badge/Status-Verified_Insight-success)

## 📌 1. Problem Statement
Before building predictive models, raw data must be interrogated to uncover hidden patterns, trends, and distributions. The objective of this phase was to construct a diagnostic framework to understand the center of gravity, measure variability, and map the linear relationships within our e-commerce dataset.

## ⚙️ 2. Methodology: The Diagnostic Framework
Utilized Python (`pandas`, `seaborn`) to conduct a rigorous univariate and bivariate analysis of 1,200 valid transactional records.
* **The Five-Number Summary:** Established baseline structural parameters (Min, Q1, Median, Q3, Max) for core financial metrics.
* **Locating Center of Gravity:** Compared mean vs. median sensitivity to diagnose distributional skewness.
* **Mapping Relationships:** Calculated the Pearson Correlation Coefficient ($r$) to identify the strongest predictors of `TotalPrice`.

---

### 📈 Visual Evidence: The EDA Dashboard
![Diagnostic Framework: EDA](EDA_Dashboard_Project2.jpg)

---

## 🔍 3. Key Findings (The Verdict)

### A. Distribution Shape & Skewness
The data exhibits a definitive **right-skewed** distribution, heavily pulled by premium outlier transactions.
* **Mean Total Price:** $1053.97 (Sensitive to anomalies)
* **Median Total Price:** $823.62 (The robust "true" center)
* *Diagnosis:* Relying solely on the average for business forecasting will artificially inflate expected revenue. The median must be used as the baseline.

### B. Correlation Signals
Pearson $r$ analysis revealed the core drivers of total cart value:
* **Unit Price ($r = 0.72$):** Strongest positive correlation. Premium items drive revenue significantly faster than bulk purchasing.
* **Quantity ($r = 0.62$):** Moderate-to-strong correlation.
* **Items In Cart ($r = 0.39$):** Weak correlation. Cart size alone is a poor predictor of final checkout value.

### C. Categorical Revenue
The categorical analysis indicates that `Chair` and `Printer` segments are the primary volume drivers, vastly outperforming the `Phone` category in total aggregated revenue.

## 💡 4. Strategic Recommendations
1. **Pricing Strategy:** Since premium items ($r = 0.72$) drive total value more effectively than cart size ($r = 0.39$), marketing efforts should focus on upselling high-tier products rather than simply encouraging users to add more cheap items to their cart.
2. **Forecasting:** All future predictive models and financial forecasts must use median-based baseline metrics rather than mean-based metrics to account for the right-skewed transaction behavior.
