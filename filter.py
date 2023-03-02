import pandas as pd
import glob
import json
csv_files = glob.glob("./data/*.csv")
dfs = []
cols = ["User name", "Event time", "Event name", "Resources"]
for file in csv_files:
    df = pd.read_csv(file,usecols=cols)
    dfs.append(df)

df = pd.concat(dfs,ignore_index=True)

users = df['User name']
user_list = list(users)
user_list_unique = list(set(user_list))

events = df['Event name']
event_list = list(events)
event_unique = list(set(event_list))
event_unique.sort()
j=0
for i in event_unique:
    print(j,i)
    j= j+1

event_id_to_find=[]
print("select id of event that want to filter and  to exit")
while True:
    event_id = int(input())
    if (event_id == -1):
        break
    else:
        event_id_to_find.append(event_id)

event_name_to_find=[]
for i in event_id_to_find:
    event_name_to_find.append(event_unique[i])

allevent = pd.DataFrame()
for i in user_list_unique:
    allevent = pd.DataFrame()
    for j in event_name_to_find:
        user_name = i
        event_name = j
        filtered_df = df[(df["User name"] == user_name) &
                        (df["Event name"] == event_name)]
        allevent = allevent.append(filtered_df)
    op = "./output/"+i+".csv"
    allevent.to_csv(op)
