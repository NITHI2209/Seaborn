import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.rugplot(data= penguin,x="body_mass_g",hue="species",palette="Set2",height=0.2)
plt.show()
#Refer figure 19