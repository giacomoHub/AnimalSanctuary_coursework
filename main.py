#main program for the sanctuary programm
#Giacomo Pellizzari
#03/11/2019

#imports
from read import readCSV
from animal import Animal,PetAnimal,WildAnimal,LinkedList,TreatmentObj
def wait():
    input("-----Press enter to procede-----")

#function that prints a list to screen (it doesn't return anything)
def printList(listToPrint):
    i=0
    for x in range (len(listToPrint)):
            print(listToPrint[i].animalID)
            i = i+1


#1 4 4 2 2 9 9 0
#Function that removes doubles from a list
def removeDoubles(listToProcess):
    result = list()
    for element in listToProcess:
        if element not in result:
            result.append(element)
    return result

#function to sort a list in ascending order
#using quicksort algorithm
def sortList(listToProcess):
    result = list()

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
    selection = int(input("select your option: "))

    #Switch between what the user has selected
    if(selection == 1):
        print("---You have selected 'Create an entry for a new arrival'")

        wait()
        return True

    if(selection == 2):
        print("---You have selected 'Find data of an animal by using the santuarys ID'")
        animalID = input("Insert a valid anial ID: ")
        
        #get first letter of animal id to decide if its pet or wild
        if(animalID[:1].lower() == "p"):
            #search if the entry exists otherwise 
            if(listOfPets.searchIfExists("animalID",animalID)==True):
                animal = listOfPets.find("animalID",animalID)
                print(animal.toString())
            else:
                print("The ID that you inserted is not present on the list")
        elif(animalID[:1].lower() == "w"):  
            if(listOfWildAnimals.searchIfExists("animalID",animalID)==True):
                animal = listOfWildAnimals.find("animalID",animalID)
                print(animal.toString())
            else:
                print("The id that you inserted is not present on the list")
        else:
            print("ERROR --- INVALID ID ENTERED")
        wait()
        return True

    #List of abusive owners
    if(selection == 3):
        abusiveOwners = listOfTreatments.returnOccurence("abuseOwner")
        #remove doubles
        abusiveOwners = removeDoubles(abusiveOwners)
        #sort
        print(abusiveOwners)
        wait()
        return True

    if(selection == 4):
        catsReadyForAdoption = listOfPets.extract("Cat")
        #print the idis of all of the cats ready for adoption
        printList(catsReadyForAdoption)
        wait()
        return True

    if(selection == 5):
        dogsReadyForAdoption = listOfPets.extract("Dog")
        #print the IDs of the dogs ready for adoption
        printList(dogsReadyForAdoption)
        wait()
        return True

    if(selection == 6):
        print("you have selected six")

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
TREATMENT = "data/DADSA 2019-20 CWK A TREATMENT.csv"
LISTOFPETATTR = ["animalID","typeOfAnimal","breed","vaccinated","neutered","microchipNumber","adoptionReason","dateOfArrival","dateOfDeparture","destination","destinationAddress"]
LISTOFWILDATTR = ["animalID","typeOfAnimal","vaccinated","admissionReason","dateOfArrival","dateOfDeaparture","destination","destinationAddress"]
LISTOFTREATMENT = ["sanctuaryID","surgery","surgeryDate","medication","start","finish","abuseOwner","abandoningOwner"]
listOfPets = LinkedList()
listOfWildAnimals = LinkedList()
listOfTreatments = LinkedList()
catsReadyForAdoption = list()
dogsReadyForAdoption = list()
abusiveOwners = list()


#read the CSV file
readCSV(PETCSV,listOfPets,PetAnimal,LISTOFPETATTR)
print(listOfPets.size())

readCSV(WILDCVS,listOfWildAnimals,WildAnimal,LISTOFWILDATTR)
print(listOfWildAnimals.size())

readCSV(TREATMENT,listOfTreatments,TreatmentObj,LISTOFTREATMENT)
print(listOfTreatments.size())
print("---------DATA LOADED IN CORRECTLY----------")
#sort the lists by Sanctuary ID

#test things


#show menu options until the user doen't select the exit button
while(stayInMenu == True):
    stayInMenu = mainMenu()


#program closure
print("goodbye!")