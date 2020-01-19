import matplotlib.pyplot as plt
import pandas as pd
from sys import argv

script, filename = argv

sub = filename.split('-')[0]
keyword = filename.split('-')[1]
keyword = keyword.replace('.csv', '')

x_val = []
y_val = []

df = pd.read_csv(filename)

#want to clean these up
scores = df[' Score'].tolist()
comments = df[' Comments'].tolist()
dates = df[' Date'].tolist()

scores.reverse()
comments.reverse()
dates.reverse()

#this isn't exactly dynaming scaling... ^^;
comments = [x*5 for x in comments]

plt.style.use('seaborn')
fig, ax = plt.subplots()

count = len(scores)

for i in range(count):
    ax.scatter(dates[i], scores[i], s=comments[i], c="red")

ax.set_ylabel('Post Score', fontsize='medium')
ax.set_title(f"Posts containing '{keyword}' on r/{sub}", fontsize='x-large')

#want to set this range dynamically
ax.set_ylim([-10, 300])

plt.subplots_adjust(bottom=0.15)
plt.xticks(rotation=45, fontsize='7')
plt.show()
