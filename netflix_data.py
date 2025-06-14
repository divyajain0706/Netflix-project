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

#Renaming the date_added column to datetime
df.rename(columns={'date_added' : 'datetime'}, inplace=True)
print(df.columns)

#Performing Analysis
#Total count of movies vs TV shows
total_movies = (df['type'] == 'Movie').sum()
total_tvshows = (df['type'] == 'TV Show').sum()
print("Total number of movies :", total_movies)
print("Total number of TV shows :", total_tvshows)

#Renaming the listed_in column to genre
df.rename(columns={"listed_in" : "genre"}, inplace=True)
print(df.columns)

#Displaying the top 5 genres/categories from the dataset
top_genres = df["genre"].value_counts().head(5)
print(top_genres)

#Total number of titles released each year
total_titles = df.groupby("release_year")["title"].count()
print("Total number of titles released each year :")
print(total_titles)