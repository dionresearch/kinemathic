import pandas as pd
from kinemathic.animation import animate
from kinemathic.resample import between_rows


df = pd.DataFrame([['a',12,15,9,17,19],['b',11,16,16,10,0]], columns=['code','Jan', 'Feb', 'Mar', 'Apr', 'May'])

df_expanded = between_rows(df)

print(df_expanded.describe())
print(df_expanded.head())

animate(df_expanded, '../output/interpolate.mp4', fps=2)
