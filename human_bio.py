import pandas as pd
import matplotlib.pyplot as plt
import pylab

#making a boxplot with data from Human Biology 2 Course
#importing data from a csv file
data = pd.read_csv('/Users/lidiaerrico/Downloads/exercise.csv')
r_ow = data['R_0_W']

#imputting x and y values and giving a title and axis labels
fig7, ax7 = plt.subplots()
ax7.set_title('Resting respiratory exchange ratio of athletic individuals and Level-2 student.')
ax7.boxplot(r_ow, labels= ['R(0W)']) 
ax7.plot(1,0.92, marker= 'o', color= 'red')
ax7.set_ylabel("Respiratory Exchange Ratio")

plt.figtext(.109, .04,'Figure 1. Boxplot showing the respiratory exchange ratio, at rest, of level-2 student compared to athletic individuals. R value is a ratio of carbon dioxide production (VCO2)\n to oxygen uptake (VO2).The individual is a male, level-2 Human Biology student who volunteered to exercise. The red points represent the values of the student')
plt.show()

