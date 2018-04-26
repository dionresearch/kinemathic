import pandas as pd
from kinemathic.animation import tweening
from kinemathic.resample import between_rows


df = pd.DataFrame(
    [
        ['a',12,15,9,17,19],
        ['b',11,16,16,10,0],
        ['c',10,10,10,10,10],
    ],
    columns=['code','Jan', 'Feb', 'Mar', 'Apr', 'May']
)

tweening(df, '../output/multi_interpolate.mp4', axis=0, fps=2)
