# first we need to import the pandas library for working with csv files. 
# the csv file should be located in the same directory as your main.py file
import pandas as pd

# we are assigning the csv values to a dataframe object
df = pd.read_csv('bestseller.csv')

#printing the top 5 books with headers 
print(df.head())

#printing the dataframe shape (5 rows 7 columns)
print(df.shape)

#printing the column names
print(df.columns)

#dataframe describe
print(df.describe)

#for removing duplicate values
df.drop_duplicates(inplace=True)

#for renaming the header titles 
df.rename(columns={"Name":"Title", "Year": "Publication Year", "User Rating":"Rating"}, inplace=True)

#for converting the price value into a float type to work better
df["Price"] = df["Price"].astype(float)

#counts the number of authors
author_counts = df["Author"].value_counts()

#prints the number of authors
print(author_counts)

#groups by genre and gets the mean of the rating value
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()

#prints the average rating by genre
print(avg_rating_by_genre)

#converts the first 10 values into a csv
author_counts.head(10).to_csv("top_authors.csv")

#converts the average rating to a csv
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
