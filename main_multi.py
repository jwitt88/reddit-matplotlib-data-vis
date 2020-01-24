import matplotlib.pyplot as plt
import pandas as pd

list_of_files = [
'sanantonio-homeless.csv',
'houston-homeless.csv',
'dallas-homeless.csv',
'austin-homeless.csv']

meta_df = []
num_of_posts = []
avg_score = []
avg_num_of_comments = []

meta_df = [pd.read_csv(file) for file in list_of_files]

for i in range(len(meta_df)):
    num_of_posts.append(len(meta_df[i]))
    avg_score.append(meta_df[i][' Score'].mean())
    avg_num_of_comments.append(meta_df[i][' Comments'].mean())

names = ['SA', 'H', 'D', 'A']
my_colors = ['black', '#0400ff', '#00b2ff', '#ff7c00']

fig, ax = plt.subplots(1, 3, figsize=(9, 3), dpi=100, sharey=False)
fig.canvas.set_window_title("'homeless' posts within 14 days on Reddit")

ax[0].set_title("number of posts")
ax[0].bar(names, num_of_posts, color=my_colors)

ax[1].set_title("avg post score")
ax[1].bar(names, avg_score, color=my_colors)

ax[2].set_title("avg number of comments")
ax[2].bar(names, avg_num_of_comments, color=my_colors)

plt.show()
