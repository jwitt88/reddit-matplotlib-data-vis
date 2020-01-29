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

#days since posting
now = pd.to_datetime('today')
df['Date'] = pd.to_datetime(df['Date'])
df['Date_Difference'] = (now - df['Date']).dt.days

#convert the desired values into lists (only show 10)
labels = df['Post ID'][:10].tolist()
score_vals = df['Score'][:10].tolist()
com_vals = df['Comments'][:10].tolist()

#calculate the number of comments per day
df['Comments_Per_Day'] = df['Comments'] / df['Date_Difference']
coms_per_day = df['Comments_Per_Day'][:10].tolist()

print(df['Comments_Per_Day'])

#plot details, mostl sourced from:
#https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py

plt.style.use('seaborn')
x = np.arange(len(labels))  # the label locations
width = 0.30  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x + .10, score_vals, width, label='Post Score')
rects2 = ax.bar(x + .30, com_vals, width, label='Number of Comments')
rects3 = ax.bar(x + .50, coms_per_day, width, label='Comments Per Day')


ax.set_title(f'r/{sub} posts containing \'{keyword}\'')

ax.set_xlabel('Post ID')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation='vertical')
ax.set_ylabel('Values')

ax.legend()
fig.tight_layout()
plt.show()
