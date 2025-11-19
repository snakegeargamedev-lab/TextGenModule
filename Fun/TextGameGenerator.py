# This module is under a CC liscence. This means that you can use this module as long as you give
#credits to me the creator, @Snake_Gear_Gamedev on youtube.
#Side note: If there are settings you do not want to change, set them to None.

#Here are the module(s) I am using:
import enum

#Class for one of the Settings.
class AnswerType(enum.Enum):
    Corrosponding_Value = True; #Examples: 1,2,3,4
    Actual_Value = False; #Examples: "Hello", "Use Potion", "Go Left", "Eat Mushroom"

#Here are some variables that you can change that effect the way this module works:
Player_Input_Dialogue = 'Action (Use Corrosponding Number Key): '
Returning_Type = AnswerType


#This is the function to change the Dialogue Settings

def Change_Settings(Input_Dialogue: str, ReturnType: AnswerType):
    if Input_Dialogue != None:
        global Player_Input_Dialogue
        Player_Input_Dialogue = Input_Dialogue
    
    if ReturnType != None:
        pass #Will be updated soon.



#This is the function to ask questions and save the results.

def AskQuestion(Question: str, Answers: list):
    print(Question)
    Question_Answerd = False

    Answer_Keybinds = []
    for i,v in enumerate(Answers):
        Answer_Keybinds.append(i+1)
    
    while Question_Answerd == False:
        for i,v in enumerate(Answers):
            print(v,'(', i+1, ')', end='        ')

        print('\n')    
        PlayerChoice = input(Player_Input_Dialogue)            
        for i, v in enumerate(Answer_Keybinds):
            if PlayerChoice == str(v):
                Question_Answerd = True
                PlayerChoice = v
                break

    return PlayerChoice


