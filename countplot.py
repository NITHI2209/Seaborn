import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.countplot(data= penguin,x="species",hue="island",palette="Set3")
plt.show()
#Refer figure 13