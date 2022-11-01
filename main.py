#functions printing and returning 
#print something in a function, its only for displaying some data, you are doing nothing with the data
#when you return in a function, you are going to use it in another part of your program

from add_fruit import add_fruits
from divide_fruit import divide_fruits
from subtract_fruit import subtract_fruits
from display_fruit import display_fruits

apples = int(input("how many apples?"))
oranges = int(input("how many oranges?"))

#add fruit
#when ever you return items, you must put the returned value inside of a variable
FruitAdded = add_fruits(apples, oranges)
print(FruitAdded)

# subtract fruit 
FruitSubtracted = subtract_fruits(apples, oranges)
print(FruitSubtracted)

# divide fruit 
FruitDivided = divide_fruits(apples, oranges)
print(FruitDivided)

#display the added fruit, subtracted fruit, and divided fruit
display_fruits(FruitAdded, FruitSubtracted, FruitDivided)