import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
column= ["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]
sns.heatmap(data= penguin[column].corr(),annot= True,cmap="Blues",linewidths=2,linecolor="black")
plt.show()
#Refer figure 18