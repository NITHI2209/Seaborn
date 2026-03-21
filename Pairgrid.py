import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
graph = sns.PairGrid(data= penguin,hue="sex",palette="Set2")
graph.map_upper(sns.scatterplot)
graph.map_lower(sns.kdeplot)
graph.map_diag(sns.histplot)
graph.add_legend()
plt.show()
#Refer figure 21