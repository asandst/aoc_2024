import pandas as pd

df = pd.read_csv("input", names=["left", "right"], sep = "[ ]+")

df['left'] = df['left'].sort_values().reset_index(drop=True)
df['right'] = df['right'].sort_values().reset_index(drop=True)
df['part1'] = abs(df['left'] - df['right'])

print("part1: "+ str(df['part1'].sum()))

df2 = pd.merge(df['left'], df['right'], left_on='left', right_on='right')
df2 = df2.groupby('left', as_index=False).count()

df2['part2'] = df2['right'] * df2['left']
print("part2: "+ str(df2['part2'].sum()))