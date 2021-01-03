
"""
cleaning
Description: program to randomly choose what each person does when cleaning 
our house. 
"""
import random 


def main(): 
    print("enter done once you've finished")
    name = ""
    name_count = 0
    chores = set()
    while name != "done":
        name = input('enter a name ')
        num = random.randint(1, 11)
        chores.add(0)
        while num in chores:
            num = random.randint(1, 11)
        chores.add(num)
        name_count += 1
        
        if num == 1:
            print("You get vacuuming upstairs")
        elif num == 2:
            print("You get vacuuming downstairs")
        elif num == 3:
            print("You get dusting")
        elif num == 4:
            print("You get mopping") 
        elif num == 5:
            print("You get cleaning toilets")
        elif num == 5:
            print("You get cleaning mirrors")
        elif num == 6:
            print("You get sinks and countertops in the bathroom")
        elif num == 7:
            print("You get sink and appliances in the kitchen")
        elif num == 8:
            print("You get countertops in the kitchen")
        elif num == 9:
            print("You get wiping furniture")
        elif num == 10:
            print("you get cleaning the showers.")
        elif num == 11:
            print("you get vauuming the stairs") 
        
        
        if(name_count == 11): 
            print("all chores have been assigned")
            name = "done" 


if __name__ == '__main__': 
    main() 
