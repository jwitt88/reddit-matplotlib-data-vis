import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sys import argv

#pass the name of the file for analysis
script, filename = argv

#get the sub/key from the fiename
sub = str(filename.split('-')[0])

#read it into a data frame
meta_df = pd.read_csv(filename)

#count the number of unique keywords found in the file
keyword_count = len(meta_df['Keyword'].unique())

#make a list of the unique values
keyword = meta_df['Keyword'].unique()


#display the unique values, and ask the user which ones they want to compare
print(f"""
    (!) Data available for {keyword_count} unique search term(s).
        Please select from the below options: \n""")

for count, item in enumerate(keyword):
    print(f"\tOption {count} - {item}")

sel1 = int(input("\n > Input the option number of your first selection: "))
sel2 = int(input(" > Input the option number of your second selection: "))

#split the results into two distinct data frames
sel1_df = meta_df[meta_df['Keyword'] == keyword[sel1]]
sel2_df = meta_df[meta_df['Keyword'] == keyword[sel2]]




#reworking this tomorrow
"""
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


#plot details, mostl sourced from:
#https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py

plt.style.use('seaborn')
x = np.arange(len(labels))  # the label locations
width = 0.30  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x + .10, score_vals, width, label='Post Score')
rects2 = ax.bar(x + .30, com_vals, width, label='Number of Comments')
rects3 = ax.bar(x + .50, coms_per_day, width, label='Comments Per Day')

ax.set_title(f'Posts retrieved from r/{sub}')

ax.set_xlabel('Post ID')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation='vertical')
ax.set_ylabel('Values')

ax.legend()
fig.tight_layout()
plt.show()"""
