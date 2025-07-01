import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

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

#Displaying the oldest and newest titles years
oldest_title = df["release_year"].min()
newest_title = df["release_year"].max()
print("Oldest title released in year : ", oldest_title)
print("Newest title released in year : ", newest_title)

#Count of content from each country.
country_count = df.groupby("country")["title"].count()
print("The number of content from each country is :")
print(country_count)

#Find all movies released in the year of 2020
year_movies = df[df["release_year"] == 2020]
print("Movies released in the year of 2020 :")
print(year_movies["title"])

#List all content of a Comedy genre.
genre_content = df[df["genre"] == "Comedies"]
print("List of content of a Comedy genre :")
print(genre_content)

#Titles with duration over 100 mins.
movies_df = df[df['type'] == 'Movie']
movies_df['duration_int'] = movies_df['duration'].str.extract('(\d+)').astype(float)
long_movies = movies_df[movies_df['duration_int'] > 100]
print(long_movies[['title', 'duration']])

#Titles with rating "TV-MA" or "R".
title_rating = df[(df["rating"] == "TV-MA") | (df["rating"] == "R")]
print("Titles with rating TV-MA or R :")
print(title_rating["title"])

df.to_csv("cleaned_netflix_data.csv", index=False)

#Visualizing the insights and trends using matplotlib
plt.figure(figsize=(15,10))

#Visualizing total count of movies vs TV shows
plt.subplot(2,2,1)
type_counts = df['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
plt.title('Total count of movies vs TV shows')

#Visualizing the top 5 genres/categories from the dataset
plt.subplot(2,2,2)
plt.bar(top_genres.index, top_genres.values,color = 'skyblue', width = 0.3)
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genres")
plt.ylabel("Number of Titles")

#Visualizing the total number of titles released each year
plt.subplot(2,2,3)
plt.hist(df['release_year'].dropna(), bins=20, color='lightgreen', edgecolor='black')
plt.title("Content Released per Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.show()

