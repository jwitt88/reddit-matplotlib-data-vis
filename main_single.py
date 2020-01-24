import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sys import argv

#pass the name of the file for analysis
script, filename = argv

#get the sub/key from the fiename
sub = str(filename.split('-')[0])
keyword = str(filename.split('-')[1]).replace('.csv', '')

#read it into a data frame
df = pd.read_csv(filename)

#convert the desired values into lists
labels = df['Post ID'].tolist()
score_vals = df[' Score'].tolist()
com_vals = df[' Comments'].tolist()


#plot details, mostl sourced from:
#https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py

plt.style.use('seaborn')
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - width/2, score_vals, width, label='Post Score')
rects2 = ax.bar(x + width/2, com_vals, width, label='Number of Comments')


ax.set_title(f'r/{sub} posts containing \'{keyword}\'')

ax.set_xlabel('Post ID')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Values')

ax.legend()
fig.tight_layout()
plt.show()
