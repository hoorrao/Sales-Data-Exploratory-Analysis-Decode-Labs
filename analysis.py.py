import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
# Ensure 'Dataset for Data Analytics.xlsx' is in the same folder as this script
file_path = 'Dataset for Data Analytics.xlsx'
df = pd.read_excel(file_path)

# 2. Data Cleaning
# Fill missing CouponCode with 'No Code' for completeness
df['CouponCode'] = df['CouponCode'].fillna('No Code')

# 3. Anomaly/Outlier Detection (IQR Method)
# Calculate Interquartile Range to identify extreme price values
Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Create a new column to flag outliers
df['IsOutlier'] = df['TotalPrice'].apply(lambda x: 'Yes' if (x < lower_bound) or (x > upper_bound) else 'No')

# Save the cleaned dataset
df.to_excel('Cleaned_Dataset_Project2.xlsx', index=False)

# 4. Data Visualization
# Generate Bar Chart: Order Frequency by Status
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='OrderStatus', palette='viridis')
plt.title('Order Frequency by Status')
plt.savefig('Order_Frequency_Status.png')

# Generate Boxplot: TotalPrice Distribution (to show outliers)
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['TotalPrice'], color='skyblue')
plt.title('Distribution of TotalPrice (Outlier Identification)')
plt.savefig('TotalPrice_Distribution.png')

print("Analysis complete. Cleaned file and charts saved.")