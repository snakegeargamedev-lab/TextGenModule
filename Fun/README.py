#This is under a CC Lisense. You may use this as long as you follow the condition(s):
#Credit @Snake_Gear_Gamedev on youtube.

#Welcome! This module is meant to help in the creation of text based games, making them really easy
#to create. Make sure to have fun with this as it is easy and useful.
#Version 1.0.0

#How to Use:

#The main function of this is AskQuestion()

import TextGameGenerator

Question1 = TextGameGenerator.AskQuestion('Would you like to be a warrior or mage?', ['Warrior', "Mage"])
print(Question1)

#There are two parameters for this, Question and Answers
#The question must be in a string form, and answers must be a table.
# The ask question function also returns the value from what the player answerd incase you want to save
#that response. This block of code has the same effect as the one above:

Answers = ['Warrior', 'Mage']
Questions = 'Would you like to be a warrior or mage'

Question2 = TextGameGenerator.AskQuestion(Questions, Answers)
print(Question2)

#This is the Change_Settings() function which changes your settings.
TextGameGenerator.Change_Settings('Pick your class') 

# Either Works 🡡 🡣
NewText = 'Pick your class'
TextGameGenerator.Change_Settings(NewText)


#Currently you can only change the text, however I am working on an update to change whether the function
#returns the Key Value (1,2) or the Text Value ("Mage", "Warrior")
#Also please note that you can set the Value to None if you only want to Minipulate certain values.

#That is all I currently have on the current verion: 1.0.0
#Happy Coding