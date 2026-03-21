import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.barplot(data= penguin,x="species",y="body_mass_g",hue="sex",palette=["pink","skyblue"], estimator=np.var)
plt.show()
#Refer figure 12