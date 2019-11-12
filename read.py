from animal import Animal,PetAnimal,LinkedList
import csv


#constant names of the files
#petCSV = "data/DADSA 2019-20 CWK A DATA PETS.csv"
#listOfAttr = ["animalID","typeOfAnimal","breed","vaccinated","neutered","microchipNumber","adoptionReason","dateOfArrival","dateOfDeparture","destination","destinationAddress"]



#listOfAnimals = LinkedList()

#function to read a csv file and store contents into a LinkedList
def readCSV(nameOfFile, listOfObjects, typeOfObject, listOfAttributes):
    #read the csv file
    with open(nameOfFile, 'rt') as csvfile:
        line_count = 0
        lastItem = 0
        tempList = list()
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if(line_count != 0):
                index=0
                #make a new Animal 🦒 that will then be added to the list of animal
                tempList.append(typeOfObject())
                
                #populate the attributes of the new animal
                for element in row:
                    if(index<len(listOfAttributes)):
                        setattr(tempList[lastItem],listOfAttributes[index],element)
                        index=index+1
                #Add the new animal in the list "ListOfAnimals"
                print(tempList[0])
                listOfObjects.add(tempList[lastItem])
                lastItem = lastItem+1
            else:
                line_count = line_count+1




#readCSV(petCSV,listOfAnimals,PetAnimal,listOfAttr)
#print("The list of animals is: ")
#print(listOfAnimals.size())
#print(listOfAnimals.head.get_animalID())

#print(listOfAnimals.search("animalID","P23543"))
