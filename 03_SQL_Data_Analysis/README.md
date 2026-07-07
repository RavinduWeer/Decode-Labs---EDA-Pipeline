# 🗄️ Project 3: SQL Data Analysis & Relational Extraction

![Python](https://img.shields.io/badge/Python-3.14-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite3-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Problem Statement
Raw data tables are rarely suitable for direct business intelligence. The objective of this project was to bridge the gap between massive datasets and specific business answers through pure relational logic. This required translating procedural questions into declarative SQL queries to filter, group, and aggregate data efficiently.

## ⚙️ Methodology & Execution Architecture
To execute the queries within a Python pipeline, an in-memory `sqlite3` database engine was initialized. The queries were structured strictly adhering to the SQL Execution Order (`FROM` $\rightarrow$ `WHERE` $\rightarrow$ `GROUP BY` $\rightarrow$ `HAVING` $\rightarrow$ `SELECT` $\rightarrow$ `ORDER BY`) to optimize computational cost before visualization.

---

### 📊 Visual Evidence: SQL Insights Dashboard
![SQL Extraction Insights](SQL_Insights_Project3.jpg)

---

## 🔍 SQL Execution & Result Sets

### Query 1: The WHERE Funnel (High-Volume Orders)
**Objective:** Isolate revenue and transaction volume exclusively for large-cart purchases ($\geq 5$ items) by utilizing row-level filtering prior to aggregation.

| Product   |   Total_Transactions |   Total_Revenue |   Avg_Order_Value |
|:----------|---------------------:|----------------:|------------------:|
| Printer   |                  120 |          $157,861 |           $1,315.51 |
| Chair     |                  129 |          $156,678 |           $1,214.56 |
| Laptop    |                  108 |          $146,280 |           $1,354.44 |
| Tablet    |                  121 |          $145,968 |           $1,206.35 |
| Monitor   |                  106 |          $134,418 |           $1,268.09 |

* **Insight:** Printers and Chairs drive the highest aggregate revenue when examining bulk purchases, indicating a strong B2B or office-setup purchasing pattern.

### Query 2: Aggregated Bucketing (The HAVING Clause)
**Objective:** Identify VIP customers by aggregating total lifetime value and utilizing the `HAVING` clause to filter the grouped buckets for spend exceeding $3,000.

| CustomerID   |   Purchase_Count |   Lifetime_Value |
|:-------------|-----------------:|-----------------:|
| C38840       |                2 |          $5,723.23 |
| C57276       |                1 |          $3,456.40 |
| C67260       |                1 |          $3,390.80 |

* **Insight:** A highly concentrated segment of VIP customers exists. Notably, `C38840` achieved the highest lifetime value across multiple purchases whereas others crossed the threshold in a single transaction.

### Query 3: Status Filtering & Performance
**Objective:** Extract successful revenue streams by filtering for specific categorical string matching (`Shipped` OR `Delivered`) and grouping by `PaymentMethod`.

| PaymentMethod   |   Total_Revenue |   Transaction_Volume |
|:----------------|----------------:|---------------------:|
| Online          |        $123,571   |                  120 |
| Gift Card       |         $96,041 |                   93 |
| Debit Card      |         $91,101 |                   82 |
| Cash            |         $90,475 |                   88 |
| Credit Card     |         $87,571 |                   83 |

* **Insight:** Generic "Online" payments are the dominant revenue driver for successful fulfillment, followed closely by Gift Card redemptions, outpacing traditional Credit Card usage.
