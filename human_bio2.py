import pandas as pd
import matplotlib.pyplot as pyplot
import pylab

#making a scatterplot with data from Human Biology 2 Course
#importing data from a csv file
data = pd.read_csv('/Users/lidiaerrico/Downloads/exercise2.csv')
workrate_x = data['W']
oxygenintake_y = data['VO2_(ml/kg/min)']

#imputting x and y values and giving a title and axis labels
pyplot.scatter(workrate_x, oxygenintake_y)
pyplot.title("Relationship between oxygen intake and work rate of athletic individuals and Level-2 student") #gives the whole graph a title
pyplot.xlabel("Work Rate (W)")
pyplot.ylabel("VO2 (ml/kg/min)")

#adding the individual data points of the "athlete" so they can be compared to the values of the individual 

#Initially tried to code it as shown below- but it connected the points into a single line, so I then separated each point so that it acted as an individual point 
#pyplot.plot([0,30,60,90,120],[4.86,7.6,10.1,11.4,16.2], marker= 'o', color= 'red')
pyplot.plot(0,4.86, marker= 'o', color= 'red')
pyplot.plot(30,7.6, marker= 'o', color= 'red')
pyplot.plot(60,10.1, marker= 'o', color= 'red')
pyplot.plot(90,11.4, marker= 'o', color= 'red')
pyplot.plot(120,16.2, marker= 'o', color= 'red')

#allows the addition of a description of the graph
pyplot.figtext(.109, .04,'Figure 2. Scatter plot showing the relationship between VO2 and work rate of athletic individuals and level-2 student.VO2 (ml.kg.min) is the value of oxygen inspired, in\nrelation to weight of the individual.The individual is a male, level-2 Human Biology student who volunteered to exerciseThe red points represent the values of the student.')

pyplot.show()