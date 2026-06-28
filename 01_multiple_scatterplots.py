import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
fig , axs = plt.subplots(1,4,figsize=(30,5))
sns.scatterplot(data = penguin, x= "flipper_length_mm" , y="body_mass_g", hue= "island",ax=axs[0])
sns.scatterplot(data = penguin, x= "flipper_length_mm" , y="body_mass_g", hue= "sex",ax=axs[1])
sns.scatterplot(data = penguin, x= "flipper_length_mm" , y="body_mass_g", hue= "species",ax=axs[2])
sns.scatterplot(data = penguin, x= "species" , y="sex", hue= "bill_depth_mm",ax=axs[3])
plt.show()
#Refer figure 1
