import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sys import argv

"""
TODO:
Rework to avoid this warning.
"""
pd.options.mode.chained_assignment = None

#pass the name of the file for analysis
script, filename = argv

#get the sub/key from the fiename
sub = str(filename.split('-')[0])

#read it into a data frame
meta_df = pd.read_csv(filename)

#count the number of unique list_of_keywords found in the file
keyword_count = len(meta_df['Keyword'].unique())

#make a list of the unique values
list_of_keywords = meta_df['Keyword'].unique()

"""
TODO:
Put the below in a try loop, and re-factor.
"""
print(f"\n   (!) Successfully loaded {filename}")
print(f"\n     - Data available for {keyword_count} unique result sets:")
print(f"       {list_of_keywords}\n")

choice_count = int(input(" > How many sets would you like to compare? "))
choice_list = []


#if the user requests the total number of variables:
if choice_count >= len(meta_df['Keyword'].unique()):

    #assign every available value to the choice list
    for item in list_of_keywords:
        choice_list.append(item)

#otherwise, we're going to ask the user choose what to include
else:

    #make a dictionary of all the possible list_of_keywords
    keyword_dict = {key: value for key, value in enumerate(list_of_keywords)}

    #display the options
    print(f"\n   Please select from the below result sets: \n")
    for key in keyword_dict:
        print(f"\t{key} - {keyword_dict[key]}")

    #add selections until the user has reached the chosen amount
    """
    TODO:
    Eventually avoid duplicates...
    """
    print()
    for i in range(choice_count):
        selection = int(input(" > Add a selection: "))
        choice_list.append(keyword_dict[selection])


#assign a df for every keyword to a dictionary
meta_dict = {}
for item in choice_list:
    meta_dict[item] = meta_df[meta_df['Keyword'] == item]



#days since posting
now = pd.to_datetime('today')


"""
TODO:
Refactor this into multiple sections...
"""
#outputting some results...
for key in meta_dict:

    #calculate the date and differential
    meta_dict[key]['Date'] = pd.to_datetime(meta_dict[key]['Date'])
    meta_dict[key]['Date_Difference'] = (now - meta_dict[key]['Date']).dt.days

    knum_of_posts = meta_dict[key]['Post_ID'].count()

    kavg_age = meta_dict[key]['Date_Difference'].mean()
    koldest = meta_dict[key]['Date'].min()

    kmax_score = meta_dict[key]['Score'].max()
    kavg_score = meta_dict[key]['Score'].mean()

    kmax_comments = meta_dict[key]['Comments'].max()
    kavg_comments = meta_dict[key]['Comments'].mean()

    print(f"\n *** SUMMARY OF POST(S) CONTAINING '{key}' ***\n")

    print(f"   - Post count: {knum_of_posts}")
    print(f"   - Oldest post: {str(koldest)[:10]}")
    print(f"   - Avg post age: ~{int(kavg_age)} day(s)\n")

    print(f"   - Max score: {kmax_score}")
    print(f"   - Avg score: {kavg_score}\n")

    print(f"   - Max comments: {kmax_comments}")
    print(f"   - Avg # of comments: {kavg_comments}\n")

    """
    MATPLOTLIB START
    """
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(4, 4))

    fig.canvas.set_window_title(key)

    x_val = ['# of Posts', 'Avg. Score', 'Avg. Comments']
    y_val = [knum_of_posts, kavg_score, kavg_comments]

    plt.tight_layout()
    ax.bar(x_val, y_val)

plt.show()
