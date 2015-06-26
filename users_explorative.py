#!/usr/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read training and user data
trackFrame = pd.read_csv('train.csv')
userFrame = pd.read_csv('users.csv')

# Mark inconsistent data
unique_track_users = np.unique(trackFrame.User)
unique_users = np.unique(userFrame.RESPID)
udiff = np.setdiff1d(unique_track_users, unique_users).size
trackFrame['inconsistent'] = \
    trackFrame.User.apply(lambda uid: uid in udiff)
userFrame['inconsistent'] = \
    userFrame.RESPID.apply(lambda uid: uid in udiff)
