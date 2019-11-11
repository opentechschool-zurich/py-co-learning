import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from cycler import cycler 

iris = pd.read_csv('iris_data.csv')

x = iris['sepal_length']
y = iris['sepal_width']

# label = iris['species'].unique()

plt.scatter(x, y, alpha=.5)
plt.savefig('iris-01.png')

# with scatter one cannot set custom colors
# https://stackoverflow.com/questions/21654635/scatter-plots-in-pandas-pyplot-how-to-plot-by-category
# https://matplotlib.org/3.1.1/tutorials/intermediate/color_cycle.html
# https://matplotlib.org/3.1.0/gallery/color/named_colors.html

groups = iris.groupby('species')

fig, ax = plt.subplots()
ax.set_prop_cycle(color=['xkcd:crimson', 'xkcd:green', 'xkcd:indigo'])
ax.margins(0.05) # add 5% padding to the autoscaling
for name, group in groups:
    ax.plot(group['sepal_length'], group['sepal_width'], marker='+', linestyle='', ms=12, label=name)
ax.legend()

plt.savefig('iris-02.png')
