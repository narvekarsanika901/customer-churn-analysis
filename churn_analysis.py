# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:31:15 2026

@author: narve
"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("customer_churn.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())


plt.figure()
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Distribution")
plt.show()


plt.figure()
sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Churn by Contract Type")
plt.show()


plt.figure()
sns.boxplot(x="Churn", y="tenure", data=df)
plt.title("Tenure vs Churn")
plt.show()

print("\nAnalysis Completed")