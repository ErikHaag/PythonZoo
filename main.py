from animals import *
from structures import *
from people import *

import copy
import datetime
import random

built_structures = []

# Get the class names of all the children of the animal class
animal_type_list = animal_base.animal_base.__subclasses__()
animal_type_name_list = [animal_type.__name__.replace("_", " ") for animal_type in animal_type_list]
# similar thing for structures
structure_type_list = [structure_type for structure_type in structure_base.structure_base.__subclasses__() if structure_type.__name__ != "entrance"]
structure_type_name_list = [structure_type.__name__.replace("_", " ") for structure_type in structure_type_list]
# And another for staff
staff_type_list = staff_base.staff_base.__subclasses__()
staff_type_name_list = [staff_type.__name__.replace("_", " ") for staff_type in staff_type_list]

global accumulated_seconds
accumulated_seconds = 0

def step(delta: datetime.timedelta):
    global built_structures
    global accumulated_seconds

    [sim_delta, acc] = divmod(delta.seconds, 30)
    # prevent fast navigation from stopping time 
    accumulated_seconds += acc
    if accumulated_seconds >= 30:
        accumulated_seconds -= 30
        sim_delta += 1
    for _ in range(sim_delta):
        indices = list(range(len(built_structures)))
        random.shuffle(indices)
        for i in indices:
            built_structures[i].step(built_structures, i)

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

def display_columns(l : list, columns : int = 2):
    column = 0
    for line in l:
        if columns <= 1:
            print(line)
        elif column == 0:
            print(line, end="")
        elif column == columns -1:
            print("   ", line)
        else:
            print("   ", line, end="")
        column = (column + 1) % columns
    if column != 0:
        print()

def prompt(prompt : str):
    before = datetime.datetime.now()
    print(prompt)
    answer = input("> ").strip()
    # simulate the period when waiting
    step(datetime.datetime.now() - before)
    if answer == "":
        answer = "back"
    return answer

def prompt_options(prompt : str, options : list = [], additions : list = [], columns : int = 2, include_back : bool = True):
    has_additions = len(additions) != 0
    if has_additions:
        if len(options) != len(additions):
            raise ValueError("additions must be empty or have the same length as options")
    if include_back:
        options.append("back")
        if has_additions:
            additions.append("")
    before = datetime.datetime.now()
    while True:
        print(prompt)
        display = options
        if has_additions:
            display = [o + " " + a for o, a in zip(options, additions)]
        display_columns(display, columns)
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
        if agreement.lower() in ("sure", "y", "yea", "yeah", "yes", "yep"):
            # if they agree, select it.
            answer = closest_option
            break
    # simulate the period when navigating the menus
    step(datetime.datetime.now() - before)
    
    return answer


def main():
    global built_structures

    built_structures = [entrance.entrance("entrance")]
    menu_id = "main"
    while True:
        match menu_id:
            case "main":
                # add, remove, view, etc.
                match prompt_options("Please select an option:", options=["add", "remove", "view", "exit"], include_back=False):
                    case "add":
                        menu_id = "add"
                    case "exit":
                        break
                    case "remove":
                        menu_id = "remove"
                    case "view":
                        menu_id = "view"
                    case _:
                        pass
            case "add":
                match prompt_options("What do you want to add?", options=["animal", "staff", "structure"]):
                    case "animal":
                        menu_id = "addAnimal"
                    case "staff":
                        menu_id = "addStaff"
                    case "structure":
                        menu_id = "addStructure"
                    case _:
                        menu_id = "main"
            case "addAnimal":
                # ask what animal they want
                new_animal_type = prompt_options("What kind of animal do you want to add?", options=copy.deepcopy(animal_type_name_list), columns = 3)
                if new_animal_type == "back":
                    print("Cancelled.")
                    menu_id = "add"
                    continue
                # 2 loops for the price of one, grandma!
                current_animal_names = [a.name for s in built_structures for a in s.animals]
                # ask for a unique name
                while True:
                    new_animal_name = prompt("What do you want to name your new " + new_animal_type + "?")
                    new_animal_name = new_animal_name[0].upper() + new_animal_name[1:]
                    if new_animal_name not in current_animal_names:
                        break
                    print("An animal already has that name!")
                if new_animal_name == "Back":
                    print("Cancelled.")
                    menu_id = "add"
                    continue
                # Get the constructor...
                animal_index = animal_type_name_list.index(new_animal_type)
                # ...and create a new instance
                new_animal = animal_type_list[animal_index](new_animal_name)
                # find the entrance in the built structures
                entrance_index = [s.type for s in built_structures].index("entrance")
                # and place the new animal there
                built_structures[entrance_index].animals.append(new_animal)
                print("\"" + new_animal_name + "\" is in the entrance")
                menu_id = "main"
            case "addStaff":
                # ask what type of staff they want
                new_staff_type = prompt_options("What type of staff do you want to add?", options=copy.deepcopy(staff_type_name_list))
                if new_staff_type == "back":
                    print("Cancelled.")
                    menu_id = "add"
                    continue
                # find the constructor
                staff_index = staff_type_name_list.index(new_staff_type)
                # create new instance
                new_staff = staff_type_list[staff_index]()
                # find the entrance
                entrance_index = [s.type for s in built_structures].index("entrance")
                # place the staff there
                built_structures[entrance_index].staff.append(new_staff)
                print("your new " + new_staff_type + " is in the entrance")
                menu_id = "main"
            case "addStructure":
                # ask what structure type they'd like
                new_structure_type = prompt_options("What type of structure do you want to add?", options=copy.deepcopy(structure_type_name_list))
                if new_structure_type == "back":
                    print("Cancelled.")
                    menu_id = "add"
                    continue
                # ask for a unique name
                current_structure_names = [s.name for s in built_structures]
                go_back = False
                while True:
                    new_structure_name = prompt("What do you want to name you new " + new_structure_type + "?")
                    if new_structure_name == "back":
                        go_back = True
                        break
                    if new_structure_name not in current_structure_names:
                        break
                    print("A structure already has that name!")
                if go_back:
                    print("Cancelled.")
                    menu_id = "add"
                    continue
                # find the constructor
                structure_index = structure_type_name_list.index(new_structure_type)
                # create a new instance
                new_structure = structure_type_list[structure_index](new_structure_name)
                # place it in the zoo
                built_structures.append(new_structure)
                print(new_structure_name + " has been built.")
                menu_id = "main"
            case "remove":
                match prompt_options("What do you want to remove?", options=["animal", "staff", "structure"]):
                    case "animal":
                        menu_id = "removeAnimal"
                    case "staff":
                        menu_id = "removeStaff"
                    case "structure":
                        menu_id = "removeStructure"
                    case _:
                        menu_id = "main"
            case "removeAnimal":
                # get all animals, their names, and their locations
                current_animals = []
                current_animal_types = []
                current_animal_locations = []
                str_i = 0
                for new_structure_type in built_structures:
                    ani_i = 0
                    for animal_type in new_structure_type.animals:
                        current_animals.append(animal_type.name)
                        current_animal_types.append("(" + type(animal_type).__name__.replace("_", " ") + ")")
                        current_animal_locations.append([str_i, ani_i])
                        ani_i += 1
                    str_i += 1
                # ask for a name
                remove_animal = prompt_options("Which animal?", options=current_animals, additions=current_animal_types)
                if remove_animal == "back":
                    print("Cancelled.")
                    menu_id = "remove"
                    continue
                # confirm deletion
                agree_to_remove = prompt("Are you sure? Please type the animal's name again to confirm.")
                if remove_animal != agree_to_remove:
                    print("Cancelled.")
                    menu_id = "main"
                    continue
                # get the animal's location
                remove_animal_index = current_animals.index(remove_animal)
                location_index = current_animal_locations[remove_animal_index]
                structure_location = built_structures[location_index[0]]
                # and remove it
                animal_location = structure_location.animals.pop(location_index[1])
                print(remove_animal + " has been removed")
                menu_id = "main"
            case "removeStaff":
                # get all the staff and their locations
                current_staff_locations = dict()
                current_staff_count_total = 0
                i = 0
                for structure in built_structures:
                    j = 0
                    for staff in structure.staff:
                        if current_staff_locations.get(staff.role, -1) == -1:
                            current_staff_locations[staff.role] = []
                        current_staff_locations[staff.role].append([i, j])
                        current_staff_count_total += 1
                        j += 1
                    i += 1
                print("There are " + str(current_staff_count_total) + " employees")
                staff_type_keys = sorted(current_staff_locations.keys())
                # ask for the type of staff to remove
                removed_staff_type = prompt_options("What type of staff would you like to remove?", options=staff_type_keys, additions=[" " + str(len(current_staff_locations[staff_type])) + "x" for staff_type in staff_type_keys], columns=3)
                if removed_staff_type == "back":
                    print("Cancelled.")
                    menu_id = "remove"
                    continue
                # pick one staff to remove
                [remove_staff_structure_index, remove_staff_staff_index] = random.choice(current_staff_locations[removed_staff_type])
                # and dismiss them
                built_structures[remove_staff_structure_index].staff.pop(remove_staff_staff_index)
                print("A " + removed_staff_type + " has been fired.")
                menu_id = "main"
            case "removeStructure":
                # get all the structures
                current_structure_names = [s.name for s in built_structures]
                current_structure_types = ["(" + s.type + ")" for s in built_structures]
                # ask which one to demolish
                remove_structure_name = prompt_options("Which structure?", options=current_structure_names, additions=current_structure_types, columns=3)
                if remove_structure_name == "back":
                    print("Cancelled.")
                    menu_id = "remove"
                    continue
                # confirmation
                agree_to_remove = prompt("Are you sure? Please type the structure's name again to confirm.")
                if remove_structure_name != agree_to_remove:
                    print("Cancelled.")
                    menu_id = "main"
                    continue
                # find the structure
                remove_structure_index = current_structure_names.index(remove_structure_name)
                remove_structure = built_structures[remove_structure_index]
                # find the entrance
                entrance_index = [s.type for s in built_structures].index("entrance")
                # copy all the contents to the entrance
                built_structures[entrance_index].animals.extend(remove_structure.animals)
                built_structures[entrance_index].guests.extend(remove_structure.guests)
                built_structures[entrance_index].staff.extend(remove_structure.staff)
                # demolish it
                built_structures.pop(remove_structure_index)
                print("All the animals, staff, and guests in " + remove_structure_name + " have been moved to the entrance,\nand " + remove_structure_name + " has been removed.")
                menu_id = "main"
            case "view":
                match prompt_options("What do you to see", options=["animals", "structures"]):
                    case "animals":
                        menu_id = "viewAnimals"
                    case "structures":
                        menu_id = "viewStructures"
                    case _:
                        menu_id = "main"
            case "viewAnimals":
                # get all the animals and their locations 
                current_animals = []
                current_animal_types = []
                current_animal_locations = []
                str_i = 0
                for structure in built_structures:
                    ani_i = 0
                    for animal_type in structure.animals:
                        current_animals.append(animal_type.name)
                        current_animal_types.append("(" + type(animal_type).__name__.replace("_", " ") + ")")
                        current_animal_locations.append([str_i, ani_i])
                        ani_i += 1
                    str_i += 1
                # ask what animal to view
                view_animal = prompt_options("Which animal?", options=current_animals, additions=current_animal_types)
                if view_animal == "back":
                    menu_id = "view"
                    continue
                # locate it
                view_animal_index = current_animals.index(view_animal)
                location_index = current_animal_locations[view_animal_index]
                structure_location = built_structures[location_index[0]]
                animal_location = structure_location.animals[location_index[1]]
                # print the things (tm)
                print("Location: " + structure_location.name)
                print("Stats:")
                # TODO?: make bar graph
                print("Happiness: " + str(animal_location.happiness))
                print("Hunger:    " + str(animal_location.hunger))
                print("Activity:  " + str(animal_location.activity_timer))
                # confirm move
                print("\nDo you want to move this animal?\n")
                if input("> ") not in ("sure", "y", "yea", "yeah", "yes", "yep"):
                    menu_id = "main"
                    continue
                # get all structures
                current_structure_names = [s.name for s in built_structures]
                current_structure_types = ["(" + s.type + ")" for s in built_structures]
                # ask for destination
                structure_to_move = prompt_options("Where would you like to move " + view_animal + "?", options=current_structure_names, additions=current_structure_types)
                if structure_to_move == "back":
                    menu_id = "main"
                    continue
                # locate structure
                structure_to_move_index = current_structure_names.index(structure_to_move)
                if structure_to_move_index == location_index[0]:
                    print(view_animal + " is already there!")
                    menu_id = "main"
                    continue
                # move the animal
                built_structures[structure_to_move_index].animals.append(built_structures[location_index[0]].animals.pop(location_index[1]))
                print(view_animal + " has been moved")
                menu_id = "main"
            case "viewStructures":
                # get all the structures
                current_structure_names = [s.name for s in built_structures]
                current_structure_types = ["(" + s.type + ")" for s in built_structures]
                # ask for a structure
                view_structure_name = prompt_options("Which structure?", options=current_structure_names, additions=current_structure_types, columns=3)
                if view_structure_name == "back":
                    print("Cancelled.")
                    menu_id = "view"
                    continue
                # find it
                view_structure_index = current_structure_names.index(view_structure_name)
                view_structure = built_structures[view_structure_index]
                # ask for query type
                match prompt_options("What do you want to see inside " + view_structure_name + "?", ["animals", "people"]):
                    case "animals":
                        # print the things (tm)
                        print("There are " + str(len(view_structure.animals)) + " animals here")
                        display_columns([a.name + "  (" + type(a).__name__.replace("_", " ") + ")" for a in view_structure.animals], 3)
                    case "people":
                        # get all the staff
                        staff_count = dict()
                        for s in view_structure.staff:
                            if staff_count.get(s.role, -1) == -1:
                                # this is a new type, so add it to the tally
                                staff_count[s.role] = 0
                            staff_count[s.role] += 1
                        # print the things (tm)
                        print ("There are " + str(len(view_structure.guests)) + " guests")
                        print("and " + str(len(view_structure.staff)) + " staff members here")
                        display_columns([str(c) + "x " + s for s, c in staff_count.items()], 3)
                    case "back":
                        menu_id = "viewStructures"
                        continue
                    case _:
                        pass
                menu_id = "main"
            case _:
                print("menu id \"" + menu_id + "\" not found, returning to home.")
                menu_id = "main"
    # TODO?: saving and loading

main()