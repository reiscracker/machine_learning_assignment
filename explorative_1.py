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

