# Sarah Grobe
# POCS HW 17
# Due 2/10/23


# imports
import pandas as pd
import matplotlib.pyplot as plt
import statistics


# read in data
d1 = pd.read_csv('data/k.csv')
d2 = pd.read_csv('data/trichoptera.csv')

cutoff = 100

master = d1[d1.d0 > cutoff]
subset = d2[d2.d0 > cutoff]

master = master.append(subset)

all_nocutoff = d1.append(d2)



# preliminary plot
plt.scatter(d1['d0'], d1['k'], color='black')
plt.scatter(d2['d0'], d2['k'], color='black')
plt.title('K value by vein diameter d_0')
plt.xlabel('d_0')
plt.ylabel('k')
plt.show()


plt.scatter(master['d0'], master['k'], color = 'black')
plt.title('K value by vein diameter d_0 for d_0 > 100')
plt.xlabel('d_0')
plt.ylabel('k')
plt.show()


print('Mean k value after cutoff:', str(statistics.mean(master['k'])))
print('Mean k value no cutoff:', str(statistics.mean(all_nocutoff['k'])))
