#main program for the sanctuary programm
#Giacomo Pellizzari
#03/11/2019

#menu
def mainMenu():
    #List all of the possible selections
    print("------------------------------------------------------")
    print("-1: Create an entry for a new arrival")
    print("-2: Find data of an animal by using the sanctuarys ID")
    print("-3: Produce a list of people that have abused their animals in the pas")
    print("-4: Produce a list of cats that are ready for adoption")
    print("-5: Produce a list of dogs that are ready for adoption")
    print("-6: Produce a list of animals that are ready to be returned to their owners")
    print("-7: edit or insert new data")
    print("-0: exit")

    #Get user input
    selection = int(input("select your option:"))

    #Switch between what the user has selected
    if(selection == 1):
        print("---You have selected 'Create an entry for a new arrival'")
        return True

    if(selection == 2):
        print("---You have selected 'Find data of an animal by using the santuarys ID'")
        return True

    if(selection == 7):
        stayInMenu = True
        while(stayInMenu == True):
            stayInMenu = subMenu()
        return True

    if(selection == 0):
        check = input("Are you sure that you want to exit? Y/N ")
        if(check == "y" or check == "Y"):
            return False
        else:
            return True

def subMenu():
    print("------------------------------------------------------")
    print("-1: Enter details of surgery")
    print("-2: Enter microchip number")
    print("-3: edit status of an animal")
    print("-4: Edit date of departure")
    print("-5: Edit destination of the animal")
    print("-0: Back")

    selection = int(input("select your option:"))

    if(selection == 1):
        print("---You have selected 'Enter details of surgery'")
        return True

    if(selection == 0):
        check = input("Are you sure that you want to go back? Y/N ")
        if(check == "y" or check == "Y"):
            return False
        else:
            return True



#start of the program
print("WELCOME TO THE SANCTUARY")


#variable declaration
stayInMenu = True

#read the CSV file


#sort the lists by Sanctuary ID


#show menu options until the user doen't select the exit button
while(stayInMenu == True):
    stayInMenu = mainMenu()


#program closure
print("goodbye!")
