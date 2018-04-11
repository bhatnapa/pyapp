from numpy import loadtxt
import matplotlib.pyplot as plt
import numpy as np
import os, time, glob

def compute1():
    x1 = []
    x2 = []

    # scan the rows of the file stored in lines, and put the values into some variables:
    #for line in lines:
    with open('/Users/Purva/PycharmProjects/vib1/Tempdata1.txt', 'r') as file:
        for row in file:
            a, b = row.split()
            x1.append(int(a))
            x2.append(int(b))

    plt.plot(x1)
    plt.plot(x2)
    plt.show()

    s1 = np.array(x1)
    s2 = np.array(x2)

    x3 = []
    x4 = []

    #for row in x1:
    subsamples1 = np.split(s1, 2)
    for i in range(len(subsamples1)):
        peakVal1 = max(subsamples1[i]) - min(subsamples1[i])
        #print peakVal1
        x3.append(int(peakVal1))

    subsamples2 = np.split(s2, 2)
    for j in range(len(subsamples2)):
        peakVal2 = max(subsamples2[j]) - min(subsamples2[j])
        #print peakVal2
        x4.append(int(peakVal2))

    print x3
    print x4

    p1 = np.array(x3)
    p2 = np.array(x4)

    peaks = p1-p2

    print peaks

    t = [10,20]

    #plt.figure()  # needed to avoid adding curves in plot
    #plt.plot(t, peaks)
    #plt.title('Resistance')
    #if not os.path.isdir('static'):
        #os.mkdir('static')
    #else:
        ## Remove old plot files
        #for filename in glob.glob(os.path.join('static', '*.png')):
            #os.remove(filename)
        # # Use time since Jan 1, 1970 in filename in order make
        # # a unique filename that the browser has not chached
        # plotfile = os.path.join('static', str(time.time()) + '.png')
        # plt.savefig(plotfile)
        # return plotfile




































# import matplotlib.pyplot as plt
# from numpy import loadtxt
# import numpy as np
#
# # Make sure txt file is in the right folder and use that location below
# data = loadtxt("/Users/Purva/PyCharmProjects/vib1/TempData.txt",float)
# plot(data)
# show()
#
# # split on number of total data values / 1000 to come up with total number of splits
# subsamples = np.split(data,6)
# for i in range(len(subsamples)):
#     peakVal = max(subsamples[i]) - min(subsamples[i])
#     print peakVal
#
# # to-do: add plot iframe to html page after form submission