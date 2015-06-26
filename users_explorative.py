#!/usr/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read training and user data
trackFrame = pd.read_csv('train.csv')
userFrame = pd.read_csv('users.csv')
