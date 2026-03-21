import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.violinplot(data= penguin,x="species",y="body_mass_g",hue="sex",split=True)
plt.show()
#Refer figure 15