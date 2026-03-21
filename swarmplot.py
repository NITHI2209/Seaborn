import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.swarmplot(data = penguin, x= "species" , y="body_mass_g", hue= "island")
plt.show()
#Refer figure 6
