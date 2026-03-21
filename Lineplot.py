import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.set_style("whitegrid")
sns.set_context("talk")
sns.lineplot(data= penguin,x="body_mass_g",y="flipper_length_mm",hue="sex",color= "orange")
plt.show()
#Refer figure 10
