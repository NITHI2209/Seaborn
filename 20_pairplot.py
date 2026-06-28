import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.pairplot(data= penguin,hue="sex",palette="Set2",diag_kind="kde")
plt.show()
#Refer figure 20
