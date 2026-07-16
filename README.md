# Sales-Data-Exploratory-Analysis-Decode-Labs
# Customer Transaction Analysis - Project 2

## Project Overview
This project involves exploratory data analysis (EDA) and data cleaning on a customer order dataset to identify trends and anomalies in purchasing behavior.

## Data Cleaning Methodology
- **Handling Missing Values**: The `CouponCode` column contained 309 missing entries, which were replaced with "No Code" to ensure data completeness[cite: 4].
- **Anomaly Detection**: Used the Interquartile Range (IQR) method to identify 8 high-value outliers in the `TotalPrice` column[cite: 4].
- **Data Enrichment**: Added an `IsOutlier` flag column (Yes/No) to the dataset to distinguish these anomalies for further business review[cite: 4].

## Key Insights
- **Order Overview**: The dataset consists of 1,200 transactions with an average transaction value of approximately $1,053.97[cite: 4].
- **Status Distribution**: Most orders are processed successfully (Delivered/Shipped), while a smaller subset is Cancelled or Returned[cite: 4].
- **Anomaly Note**: The 8 identified outliers represent transactions significantly outside the normal price range, requiring further manual investigation[cite: 4].

## Visualizations
![Order Frequency by Status](Order_Frequency_Status.png)
*Figure 1: Comparison of order volume across different statuses.*

![TotalPrice Distribution](TotalPrice_Distribution.png)
*Figure 2: Distribution of total price highlighting identified outliers.*
