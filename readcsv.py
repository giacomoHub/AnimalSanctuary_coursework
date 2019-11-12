from animal import Animal,PetAnimal
import csv


#constant names of the files
petCSV = "DADSA 2019-20 CWK A DATA PETS.csv"
treatmentCSV = "DADSA 2019-20 CWK A TREATMENT.csv"
wildCSV = 'DADSA 2019-2O CWK A WILD ANIMALS.csv'


#list of columns in the file
listOfColumns = list()
listOfAnimals = list()
listOfAttr = ["animalID","typeOfAnimal","breed","vaccinated","neutered","microchipNumber","adoptionReason","dateOfArrival","dateOfDeparture","destination","destinationAddress"]



#function to read a csv file and store contents into a list
def readCSV(nameOfFile, listOfObjects, typeOfObject, listOfAttributes):
    #read the csv file
    with open(nameOfFile, 'rt') as csvfile:
        line_count = 0
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if(line_count != 0):
                index=0
                #make new animal in the list "ListOfAnimals"
                listOfObjects.append(typeOfObject())
                lastItem = len(listOfObjects) -1
                #put each element of the row into list[lastItem]
                for element in row:
                    if(index<len(listOfAttributes)):
                        setattr(listOfObjects[lastItem],listOfAttributes[index],element)
                        index=index+1
            else:
                line_count = line_count+1

readCSV(petCSV,listOfAnimals,PetAnimal,listOfAttr)


#debug
print("The number of animals in the list 'list of animals' is: ", len(listOfAnimals))
testIndex = 2
test3 = listOfAnimals[testIndex].adoptionReason
print("the name of the animal in the list at index ",testIndex, " is: ", test3)


print([animal.animalID for animal in listOfAnimals])


