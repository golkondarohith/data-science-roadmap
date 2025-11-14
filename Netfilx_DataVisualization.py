#import the libraries
import pandas as pd
import matplotlib.pyplot as plt


#Load the csv file
df = pd.read_csv("netflix_titles.csv")

#clean data
df = df.dropna(subset = ['type', 'release_year', 'rating', 'country', 'duration'])

type_counts = df['type'].value_counts()

#Bar chart
plt.figure(figsize=(6, 4))
plt.bar(type_counts.index, type_counts.values, color = ['skyblue', 'orange'] )
plt.title("Number of TV Shows Vs Movies on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
# plt.show()


#Pie Chart
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct="%1.1f", startangle=90)
plt.title("Content Rating")
plt.tight_layout()
plt.savefig("content_rating.png")
plt.show()



