#!/usr/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

trackFrame = pd.read_csv('train.csv')

rating_count = trackFrame['Rating'].value_counts()
rating_count_sorted = rating_count.sort_index()

# Plot rating distribution as bar plot
plt.figure(figsize=(20,8))
rating_count_sorted.plot(kind='bar')
plt.title("Distribution of overall ratings")
plt.xlabel("Rating"); plt.ylabel("Frequency of rating")
plt.show()

# Calculate and plot mean ratings by artist
artist_ratings = trackFrame[['Artist', 'Rating']].groupby('Artist').mean()
# Sort by rating and highest rating first
artist_ratings_sorted = artist_ratings.sort(columns='Rating', ascending=False)
#plt.figure()
artist_ratings_sorted.plot(kind="bar")
plt.title("Mean rating by artist")
plt.xlabel("Artist"); plt.ylabel("Mean rating")
plt.show()

# Average ratings given by each user in bins of 10
user_ratings = trackFrame[['User', 'Rating']].groupby('User').mean()
user_ratings.hist()
plt.show()
