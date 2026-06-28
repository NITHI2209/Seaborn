import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.set_theme(style="darkgrid") #whitegrid ,white,dark,ticks
sns.scatterplot(data = penguin, x= "flipper_length_mm" , y="body_mass_g", hue= "island")
plt.show()
#Refer figure 2 
