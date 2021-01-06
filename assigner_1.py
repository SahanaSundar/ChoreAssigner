"""
Updated version
Allows the user to enter names and chores and assigns all chores at once
Runs in the terminal of an IDE
"""
import random
names = list()
chores = list()
names_to_chores = dict()
chores_taken = set()
names_taken = set()


def input_names():
    """
    This function allows the users to input the names of people that need
    chores assigned to them
    """
    name_count = int(input("How many people need chores assigned to them? "))
    for i in range(0, name_count):
        new_name = input("Enter the name of person " + str(i + 1) + " :")
        names.append(new_name)
    return name_count


def input_chores():
    """
    This function allows the users to input the chores to be assigned
    """
    chore_count = int(input("How many chores need to be assigned? "))
    for i in range(0, chore_count):
        new_chore = input("Enter chore " + str(i + 1) + " :")
        chores.append(new_chore)
    return chore_count


def randomize(): 
    """
    This method shuffles the order of the names and chores
    """
    random.shuffle(chores)
    random.shuffle(names) 


def assign_chores(name_count, chore_count):
    min_chores_per_person = int(chore_count/name_count)
    for i in range(0, len(names)):
        curr_name = names[i] 
        names_to_chores[curr_name] = set() 
        for j in range(0, min_chores_per_person): 
            curr_chore = chores.pop()
            names_to_chores[curr_name].add(curr_chore) 
    k = 0
    while len(chores) > 0: 
        name = names[k]
        curr_chore = chores.pop()
        names_to_chores[name].add(curr_chore)
        k = k + 1
    print(names_to_chores)


def main():
    """
    Main method
    """
    name_count = input_names()
    chore_count = input_chores()
    randomize()
    assign_chores(name_count, chore_count)


if __name__ == '__main__':
    main()
