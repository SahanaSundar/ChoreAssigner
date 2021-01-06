"""
Updated version
Things to fix --> entering getting the person number
"""
names = dict()


def input_names(): 
    name_count = input("How many people need chores assigned to them?") 
    for i in range(1, name_count + 1):
        new_name = input("Enter the name a person:") 
        names[i] = new_name


def main(): 
    input_names()


if __name__ == '__main__': 
    main() 


