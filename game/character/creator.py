import random
import time
import game.character.character as character
import game.tools as tools
import game.engine.wait as wait


def new():
    properties = {}
    properties["name"] = input("Please input your adventurer's name:")

    print('Select your race')
    properties['race'] = tools.show_picker(['Human', 'Elf', 'Dwarf'])

    print('Select your gender')
    properties['gender'] = tools.show_picker(['Male', 'Female', 'Other'])

    print()
    print("Rolling ability scores")
    # "\r" takes the cursor to the beginning of the line

    wait.quick_spin()
    print()
    properties["strength"] = random.randint(3, 18)
    properties["dexterity"] = random.randint(3, 18)
    properties["constitution"] = random.randint(3, 18)
    properties["hitpoints"] = 10

    return character.Character(properties)
