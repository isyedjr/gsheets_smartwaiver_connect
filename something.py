import pandas as pd
import numpy as np
from google.oauth2.service_account import Credentials
import smartwaiver

scope = []

# store responses
box = []
storage = [][]

# smart waiver stuff
key = ''
waiver = smartwaiver.Smartwaiver(key)

data = waiver.get_waiver_summaries()

# store title in array, will write to form
for i in data
    box.append(i.title)

# write to 2D array - names
for i in len(box)
    storage[i][1] = box[i]

# write to 2D array - form status
for i in len(box)
    if () # need to search sheet here
        storage[i][2] = 1
    else
        storage[i][2] = 0

# copy array into new sheet
