#main program for the sanctuary programm
#Giacomo Pellizzari
#03/11/2019

#imports
from read import readCSV
from animal import Animal,PetAnimal,WildAnimal,LinkedList

#menu
def mainMenu():
    #List all of the possible selections
    print("------------------------------------------------------")
    print("-1: Create an entry for a new arrival")
    print("-2: Find data of an animal by using the sanctuarys ID")
    print("-3: Produce a list of people that have abused their animals in the past")
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
        animalID = input("Insert a valid anial ID: ")
        #get first letter of animal id to decide if its pet or wild

        animal = listOfPets.search("animalID",animalID)
        #search if the entry exists otherwise 
        if(listOfPets.search("animalID",animalID)==True):
            animal.toString()
        else:
            print("The ID that you inserted is not present on the list")
        
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
    print("-3: Edit status of an animal")
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
PETCSV = "data/DADSA 2019-20 CWK A DATA PETS.csv"
WILDCVS = "data/DADSA 2019-20 CWK A WILD ANIMALS.csv"
LISTOFPETATTR = ["animalID","typeOfAnimal","breed","vaccinated","neutered","microchipNumber","adoptionReason","dateOfArrival","dateOfDeparture","destination","destinationAddress"]
LISTOFWILDATTR = ["animalID","typeOfAnimal","vaccinated","admissionReason","dateOfArrival","dateOfDeaparture","destination","destinationAddress"]
listOfPets = LinkedList()
listOfWildAnimals = LinkedList()


#read the CSV file
readCSV(PETCSV,listOfPets,PetAnimal,LISTOFPETATTR)
print(listOfPets.size())

readCSV(WILDCVS,listOfWildAnimals,WildAnimal,LISTOFWILDATTR)
print(listOfWildAnimals.size())

#sort the lists by Sanctuary ID

#test things
listOfPets.head.pingpong()


#show menu options until the user doen't select the exit button
while(stayInMenu == True):
    stayInMenu = mainMenu()


#program closure
print("goodbye!")
