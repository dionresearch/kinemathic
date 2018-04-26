from kinemathic.animation import animate
import statsmodels.api as sm


data = sm.datasets.co2.load_pandas()
co2 = data.data

animate(co2, '../output/co2.mp4', axis=1, step=25, autoscale=False)
animate(co2, '../output/co2_autoscale.mp4', axis=1, step=25, autoscale=True)
animate(co2, '../output/co2_bar_auto.mp4', axis=1, step=25, kind='hist')
