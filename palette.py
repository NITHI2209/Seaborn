import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
penguin = sns.load_dataset('penguins')
sns.scatterplot(data = penguin, x= "flipper_length_mm" , y="body_mass_g", hue= "island",palette="Set1") #Set2,Set3,deep,muted,bright,pastel,dark,colorblind,qualitative,sequential.diverging
plt.show()
#refer figure 4