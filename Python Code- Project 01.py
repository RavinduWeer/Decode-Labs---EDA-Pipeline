import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

# ==========================================
# 1. LOAD THE DATA
# ==========================================
file_path = "Dataset for Data Analytics.xlsx"
df = pd.read_excel(r"D:\Decode Labs\Project 01\Dataset for Data Analytics.xlsx")

print("Original Dataset Shape:", df.shape)

# ==========================================
# 2. STATISTICAL IMPUTATION
# ==========================================
# A. Categorical Imputation for 'CouponCode'
df['CouponCode'] = df['CouponCode'].fillna("NO_COUPON")

# B. KNN Imputation for Numerical Columns (to satisfy the project rubric)
# We select the continuous/discrete numerical features
num_cols = ['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']

knn_imputer = KNNImputer(n_neighbors=5)
# Fit and transform the numerical columns
df[num_cols] = knn_imputer.fit_transform(df[num_cols])

print("Missing values after imputation:\n", df.isnull().sum())

# ==========================================
# 3. NEUTRALIZE OUTLIERS (IQR METHOD)
# ==========================================
# We will target 'TotalPrice' as it's the primary financial metric
Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the dataset to keep only the mathematically valid rows
df_clean = df[(df['TotalPrice'] >= lower_bound) & (df['TotalPrice'] <= upper_bound)].copy()

print(f"Rows remaining after Outlier Removal: {df_clean.shape[0]} (Removed {df.shape[0] - df_clean.shape[0]} outliers)")

# ==========================================
# 4. FEATURE ENGINEERING
# ==========================================
# Feature 1: Ratio feature (Average value of items in the cart)
df_clean['Avg_Item_Value'] = df_clean['TotalPrice'] / df_clean['ItemsInCart']

# Feature 2: Temporal feature (Is it a weekend transaction?)
# Ensure 'Date' is a datetime object, then extract the day of week (5 = Sat, 6 = Sun)
df_clean['Date'] = pd.to_datetime(df_clean['Date'])
df_clean['Is_Weekend'] = df_clean['Date'].dt.dayofweek.apply(lambda x: 1 if x >= 5 else 0)

# Feature 3: Binary categorical feature (Did they use a coupon?)
df_clean['Used_Coupon'] = df_clean['CouponCode'].apply(lambda x: 0 if x == "NO_COUPON" else 1)

# ==========================================
# 5. FINAL INSPECTION
# ==========================================
print("\n--- Final Cleaned & Engineered Dataset ---")
print(df_clean[['TotalPrice', 'ItemsInCart', 'Avg_Item_Value', 'Date', 'Is_Weekend', 'Used_Coupon']].head())

# Optional: Save the clean dataset to a new CSV for the next project
# df_clean.to_csv("Cleaned_Dataset_Project1.csv", index=False)  