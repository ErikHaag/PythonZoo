from animals import *
from structures import *
import datetime

# Get the class names of all the children of the animal class
animal_type_list = [animal_type for animal_type in animal_base.animal.__subclasses__()]
animal_type_name_list = [animal_type.__name__.replace("_", " ") for animal_type in animal_type_list]
# similar thing for structures
structure_type_list = [structure_type.__name__.replace("_", " ") for structure_type in structure_base.structure.__subclasses__()]
# TO-DO staff


built_structures = [entrance.entrance()]

def step():
    for structure in built_structures:
        structure.step()

# amount of additions, changes, or deletions required to convert s into t
def levenshtein_distance(s, t):
    row_0 = [i for i in range(len(t) + 1)]
    row_1 = [0 for _ in range(len(t) + 1)]
    for i in range(len(s)):
        row_1[0] = i + 1
        for j in range(len(t)):
            deletion_cost = row_0[j + 1] + 1
            insertion_cost = row_1[j] + 1
            substitution_cost = row_0[j]
            if s[i] != t[j]:
                substitution_cost += 1
            row_1[j + 1] = min([deletion_cost, insertion_cost, substitution_cost])
        
        # swap the lists
        [row_0, row_1] = [row_1, row_0]
    return row_0.pop()

def prompt(prompt : str):
    before = datetime.datetime.now()
    print(prompt)
    answer = input("> ")
    # simulate the period when waiting
    delta = (datetime.datetime.now() - before).seconds
    for _ in range(delta):
        step()
    if answer == "":
        answer = "back"
    return answer

def prompt_options(prompt : str, options : list = []):
    options.append("back")
    before = datetime.datetime.now()
    while True:
        print(prompt)
        on_left = True
        for option in options:
            if on_left:
                print(option, end="")
            else:
                print("   ", option)
            on_left = not on_left
        if not on_left:
            print()
        print()
        # get desired request
        answer = input("> ").lower()
        if answer in options:
            break
        # if request isn't valid, find the closest one
        closest_option = ""
        closest_distance = -1
        for option in options:
            option = option.lower()
            dist = levenshtein_distance(answer, option)
            if dist < closest_distance or closest_distance == -1:
                closest_distance = dist
                closest_option = option
        # ensure the user agrees 
        agreement = input("\"" + answer + "\" is not a valid option, did you mean \"" + closest_option + "\"? ")
        if agreement.lower() in ("sure", "y", "yes", "yep"):
            # if they agree, select it.
            answer = closest_option
            break
    # simulate the period when navigating the menus
    delta = (datetime.datetime.now() - before).seconds
    for _ in range(delta):
        step()
    return answer


def main():
    menuID = "main"
    while True:
        match menuID:
            case "main":
                # add, remove, view, etc.
                match prompt_options("Please select an option:", ["add", "remove", "view", "exit"]):
                    case "add":
                        menuID = "add"
                    case "exit":
                        break
                    case "remove":
                        menuID = "remove"
                    case "view":
                        menuID = "view"
                    case _:
                        pass
            case "add":
                match prompt_options("What do you want to add?", ["animal", "staff", "structure"]):
                    case "animal":
                        menuID = "addAnimal"
                    case "structure":
                        menuID = "addStructure"
                    case "staff":
                        menuID = "addStaff"
                    case _:
                        menuID = "main"
            case "addAnimal":
                if all([s.type != "entrance" for s in built_structures]):
                    print("You need an entrance first!")
                    menuID = "add"
                    continue
                animal = prompt_options("What kind of animal do you want to add?", animal_type_name_list)
                if animal == "back":
                    menuID = "add"
                    continue
                animal_name = prompt("What do you want to name your new " + animal + "?")
                animal_index = animal_type_name_list.index(animal)
                new_animal = animal_type_list[animal_index](animal_name)
                entrance_index = [s.type for s in built_structures].index("entrance") 
                built_structures[entrance_index].animals.append(new_animal)
                print("\"" + animal_name + "\" is in the entrance")
                menuID = "add"
            case _:
                print("menu id \"" + menuID + "\" not found, returning to home.")
                menuID = "main"

main()