from master import *

from animals import *
from structures import *
from people import *
import datetime

# Get the class names of all the children of the animal class
animal_type_list = [animal_type for animal_type in animal_base.animal_base.__subclasses__()]
animal_type_name_list = [animal_type.__name__.replace("_", " ") for animal_type in animal_type_list]
# similar thing for structures
structure_type_list = [structure_type for structure_type in structure_base.structure_base.__subclasses__() if structure_type.__name__ != "entrance"]
structure_type_name_list = [structure_type.__name__.replace("_", " ") for structure_type in structure_type_list]
# And another for staff
staff_type_list = staff_base.staff_base.__subclasses__()
staff_type_name_list = [staff_type.__name__.replace("_", " ") for staff_type in staff_type_list]

global accumulated_seconds
accumulated_seconds = 0

def step():
    global built_structures

    i = 0
    for structure in built_structures:
        structure.step(i)
        i += 1

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
    answer = input("> ").strip()
    # simulate the period when waiting
    delta = (datetime.datetime.now() - before).seconds
    [sim_delta, acc] = divmod(delta, 30)
    # prevent fast navigation from stopping time 
    global accumulated_seconds
    accumulated_seconds += acc
    if accumulated_seconds >= 30:
        accumulated_seconds -= 30
        sim_delta += 1
    for _ in range(sim_delta):
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
        answer = input("> ").strip()
        if answer in options:
            break
        # if request isn't valid, find the closest one
        closest_option = ""
        closest_distance = -1
        for option in options:
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
    [sim_delta, acc] = divmod(delta, 30)
    # prevent fast navigation from stopping time 
    global accumulated_seconds
    accumulated_seconds += acc
    if accumulated_seconds >= 30:
        accumulated_seconds -= 30
        sim_delta += 1
    for _ in range(sim_delta):
        step()
    return answer


def main():
    global built_structures

    built_structures = [entrance.entrance("entrance")]
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
                    case "staff":
                        menuID = "addStaff"
                    case "structure":
                        menuID = "addStructure"
                    case _:
                        menuID = "main"
            case "addAnimal":
                animal = prompt_options("What kind of animal do you want to add?", animal_type_name_list)
                if animal == "back":
                    menuID = "add"
                    continue
                # 2 loops for the price of one, grandma!
                structure_names = [a.name for s in built_structures for a in s.animals]
                while True:
                    animal_name = prompt("What do you want to name your new " + animal + "?")
                    animal_name = animal_name.strip()
                    animal_name = animal_name[0].upper() + animal_name[1:]
                    if animal_name not in structure_names:
                        break
                    print("An animal already has that name!")
                animal_index = animal_type_name_list.index(animal)
                new_animal = animal_type_list[animal_index](animal_name)
                entrance_index = [s.type for s in built_structures].index("entrance")
                built_structures[entrance_index].animals.append(new_animal)
                print("\"" + animal_name + "\" is in the entrance")
                menuID = "main"
            case "addStaff":
                staff = prompt_options("What type of staff do you want to add?", staff_type_name_list)
                if staff == "back":
                    menuID = "add"
                    continue
                staff_index = staff_type_name_list.index(staff)
                new_staff = staff_type_list[staff_index]()
                entrance_index = [s.type for s in built_structures].index("entrance")
                built_structures[entrance_index].staff.append(new_staff)
                print("your new " + staff + " is in the entrance")
                menuID = "main"
            case "addStructure":
                structure = prompt_options("What type of structure do you want to add?", structure_type_name_list)
                if structure == "back":
                    menuID = "add"
                    continue
                structure_names = [s.name for s in built_structures]
                go_back = False
                while True:
                    structure_name = prompt("What do you want to name you new " + structure + "?")
                    if structure_name == "back":
                        go_back = True
                        break
                    if structure_name not in structure_names:
                        break
                    print("An structure already has that name!")
                if go_back:
                    menuID = "add"
                    continue
                structure_index = structure_type_name_list.index(structure)
                new_structure = structure_type_list[structure_index](structure_name)
                built_structures.append(new_structure)
                menuID = "main"
            case "view":
                match prompt_options("What do you to see", ["animals"]):
                    case "animals":
                        menuID = "viewAnimals"
                    case _:
                        menuID = "main"
            case "viewAnimals":
                animal_list = []
                animal_location_list = []
                str_i = 0
                for structure in built_structures:
                    ani_i = 0
                    for animal in structure.animals:
                        animal_list.append(animal.name)
                        animal_location_list.append([str_i, ani_i])
                        ani_i += 1
                    str_i += 1
                animal = prompt_options("Which animal?", animal_list)
                if animal == "back":
                    menuID = "view"
                    continue
                animal_index = animal_list.index(animal)
                location_index = animal_location_list[animal_index]
                structure_location = built_structures[location_index[0]]
                animal_location = structure_location.animals[location_index[1]]
                print("Location: " + structure_location.name)
                print("Stats:")
                # TODO?: make bar graph
                print("Happiness: " + str(animal_location.happiness))
                print("Hunger:    " + str(animal_location.hunger))
                print("Activity:  " + str(animal_location.activity_timer))
                print("\nDo you want to move this animal?")
                if input("> ") not in ("sure", "y", "yes", "yep"):
                    menuID = "main"
                    continue
                structure_names = [s.name for s in built_structures]
                structure_to_move = prompt_options("Where would you like to move " + animal + "?", structure_names)
                if structure_to_move == "back":
                    menuID = "main"
                    continue
                structure_to_move_index = structure_names.index(structure_to_move)
                if structure_to_move_index == location_index[0]:
                    print(animal + " is already there!")
                    menuID = "main"
                    continue
                # move the animal
                built_structures[structure_to_move_index].animals.append(built_structures[location_index[0]].animals.pop(location_index[1]))
                print(animal + " has been moved")
                menuID = "main"
            case _:
                print("menu id \"" + menuID + "\" not found, returning to home.")
                menuID = "main"
    # TODO?: saving and loading

main()