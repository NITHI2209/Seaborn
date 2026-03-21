import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.violinplot(data= penguin,x="species",y="body_mass_g")
sns.swarmplot(data=penguin,x="species",y="body_mass_g",color="black",size=3)
plt.show()
#Refer figure 16