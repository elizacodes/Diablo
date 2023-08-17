# The baseline of this program is to acknowledge the basics of Python programming
# along with importing multiple libraries to showcase module import, such as
# pandas and numpy. Also, I just really enjoyed Diablo IV. So there's that.

# ------ BLUEPRINT -------
# The idea of this program is to import an Excel file with existing Diablo characters
# These characters include their gender, level, class, and what world tier they are in
# The user will also be asked if they would like to enter in their own characters as well
# and be added to the list of data that has been provided
# After creating their character, maybe a machine learning model can be developed in order
# to predict the user's next character? (may differ base on the amount of characters that
# the user inputs)

import pyinputplus as pyip
import pandas as pd

# import Excel file with other characters
def read_file():
    diablo_data = pd.read_excel('file.xlxs')
    for row in range(0, diablo_data.max_row):
        for col in diablo_data.iter_cols(1, diablo_data.max_column):
            print(col[row].value)

# -------------------------
# ---- "FINISHED WORK" ----
# -------------------------

# --- USER INPUT FOR CHARACTER ---
def classes():
    classes = ["Rogue",
               "Sorcerer",
               "Barbarian",
               "Druid",
               "Necromancer"]
    
    return classes

def character_class(classes):
    print("What is the name of your character?")
    name = pyip.inputStr().capitalize().strip()
    while True:
            #if class_choice != classes:
            # if not class_choice is classes:
            #     raise TypeError("That class isn't part of the game. Try again.")
            # else:
            #     break
        print("What is your class?")
        class_choice = pyip.inputStr().capitalize().strip()
        if class_choice not in classes():
            raise TypeError("That class isn't part of the game. Try again.")
        else:
            break
    print("What is your level?")
    character_lvl = pyip.inputInt()
    while True:
        if character_lvl < 0:
            print("You must enter a level higher than 0.")
        else:
            break
            
    return class_choice, character_lvl, name

# --- DETECTING WORLD TIER BASED ON CHARACTER LEVEL ---
    
def world_tiers(character_lvl):
    char_levels = {(0, 20): 1,
                   (20, 50): 2,
                   (50, 70): 3,
                   (70, 100): 4}
    for i in char_levels.keys():
        if (character_lvl >= i[0]):
            if (len(i) > 1):
                if (character_lvl < i[1]):
                    world_tier = char_levels[i]
                    break
            else:
                world_tier = char_levels[i]
    
    return world_tier

# --- DISPLAY DIABLO CHARACTERS FOR USER ---

def diablo_characters(class_choice, character_lvl, world_tier, name):
    characters = []
    diablo_dict = {
        'Name': name,
        'Class': class_choice,
        'Level': character_lvl,
        'World Tier': world_tier
    }
    
    characters.append(diablo_dict)
    print(f"Diablo Characters: {characters}")
    
    return characters
    
# --- ASK THE USER TO ENTER ANOTHER CHARACTER ---

def ask_again(characters): # figure out how to append to the original dictionary of characters
    print("Would you like to enter another character?")
    user_prompt = pyip.inputStr().capitalize().strip()
    if user_prompt == "YES" or "Y":
        update = character_class(classes)
        # return update
    elif user_prompt == "NO" or "N":
        print("Have fun gaming.")
    else:
        update = characters.append(user_prompt)
        
    print(f"Diablo Characters: {update}")

# --- RUNNING MAIN ---

def main():
    # error = False
    # try/except for reading data file
    class_choice, character_lvl, name = character_class(classes)
    world_tier = world_tiers(character_lvl)
    characters = diablo_characters(class_choice, character_lvl, world_tier, name)
    ask_again(characters)
    
main()
