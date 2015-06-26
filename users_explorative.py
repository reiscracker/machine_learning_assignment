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
