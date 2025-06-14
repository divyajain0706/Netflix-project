import pandas as pd
import numpy as np 

#Loading the CSV file
df = pd.read_csv(r"D:\Python Programs\pandas programs\Netflix-project\nextflix_data.csv", encoding="latin1")

#Displaying concise information about the dataset
print("Displaying the information of the dataset :")
print(df.info())

#Displaying column names and missing values.
print("Column names :")
print(df.columns)

print("Missing values if any :")
print(df.isnull().sum())

#Filling the missing values in the director,cast and country columns.
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Cast not listed")
df['country'] = df['country'].fillna("Unknown Country")

print(df.isnull().sum())

#Checking whether there are duplicate values or not
print("Duplicate values if any :")
print(df.duplicated().sum())