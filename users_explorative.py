#!/usr/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read training and user data
#trackFrame = pd.read_csv('train.csv')
userFrame = pd.read_csv('users.csv')

# Print overall statistics about users
userCount = userFrame.RESPID.count()
maleUserCount = userFrame[userFrame.GENDER == 'Male']['RESPID'].count()
femaleUserCount = userFrame[userFrame.GENDER == 'Female']['RESPID'].count()
print("Count of distinct users: %s" % userCount)
print("Count of male users: %s" % maleUserCount)
print("Count of female users: %s" % femaleUserCount)
print("(%f percent male, %f percent female)" % ( float(maleUserCount) / userCount * 100, float(femaleUserCount) / userCount * 100 ))
print("Youngest user: %s, oldest user %s" % (userFrame['AGE'].min(), userFrame['AGE'].max()))

# Distribution of age
plt.figure(figsize=(20,8))
plt.subplot(1, 2, 1)
userFrame['AGE'].hist(bins=20)
plt.title("Distribution of age")
plt.xlabel("Age"); plt.ylabel("Amount of users with that age")

plt.subplot(1, 2, 2)
userFrame.boxplot(column="AGE")
plt.show()

