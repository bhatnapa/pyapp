import matplotlib.pyplot as plt
from numpy import loadtxt
import numpy as np

# Make sure txt file is in the right folder and use that location below
data = loadtxt("/Users/Purva/Flaskapp/static/data.txt",float)
plot(data)
show()

# split on number of total data values / 1000 to come up with total number of splits
subsamples = np.split(data,6)
for i in range(len(subsamples)):
    peakVal = max(subsamples[i]) - min(subsamples[i])
    print peakVal

# to-do: add plot iframe to html page after form submission
