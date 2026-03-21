import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.kdeplot(data= penguin,hue="species",x="body_mass_g",fill=True)
plt.show()
#Refer figure 17