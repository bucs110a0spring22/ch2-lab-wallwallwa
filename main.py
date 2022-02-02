
#Part A
weeks = 16
print ("weeks:", weeks , type(weeks))
classes = 5
print ("classes:", classes, type(classes))
tuition = 6000
print ("tuition: $", tuition , type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
cost_per_class = (cost_per_week / classes_per_week)
print ("The University taking $", cost_per_class , "out your wallet for each class this week buddy")
#Part B
import random
lst = ["red" , "blue" , "orange" , "purple" , "green"]
col_ch = (random.choice(lst))
print ( "Your color is:" , col_ch )
