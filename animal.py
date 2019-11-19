#Class Animal wich is also a node of the list
class Animal:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = newdata
        
    def set_next(self, new_next):
        self.next = new_next

    def get_animalID(self):
        return self.animalID

    def get(self, attributeName):
        return self.__getattribute__(attributeName)


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_animalID() > item.get_animalID():
                stop = True
            else:
                previous = current
                current = current.get_next()
        
        temp = item
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    #function to search a particular object(node) in the list 
    #takes in attributeToSearch (ie. animalID or Vaccinated)
    def searchIfExists(self, attributeToSearch, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get(attributeToSearch) == item:
                found = True
            else:
                if current.get_animalID() > item:
                    stop = True
                else:
                    current = current.get_next()
        
        return found

    def find(self,attributeToSearch,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get(attributeToSearch) == item:
                found = True
                return current
            else:
                current = current.get_next()

    #function to get all of the occurences of a list where the attribute is not null
    #the function returns a list (es: list of all of the abusive owners)
    def returnOccurence(self, attributeToSearch):
        current = self.head
        result = list()
        while current != None:
            if current.get(attributeToSearch) != "":
                result.append(current.get(attributeToSearch))
            current = current.get_next()

        return result


    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def getLastItem(self):
        return self.head

    #function that traverses the list and searches for elements that satisfy a condition
    #returns a list
    def extract(self,animalType):
        current = self.head
        #list to store the animals ready for adoption
        result = list() 

        while current != None:
            if(current.readyForAdoption(animalType)==True):
                result.append(current)
            current = current.get_next()
        
        return result

    

        




class PetAnimal(Animal): 
    #constructor of class pet
    def __init__(self, animalID = "", typeOfAnimal = "", vaccinated = "", dateOfArrival = "", dateOfDeparture = "", destination = "", destinationAddress = "", breed = "", neutered = "", microchipNumber = "9"):
        self.animalID = animalID
        self.typeOfAnimal = typeOfAnimal
        self.vaccinated = vaccinated
        self.dateOfArrival = dateOfArrival
        self.dateOfDeparture = dateOfDeparture
        self.destination = destination
        self.destinationAddress = destinationAddress
        self.breed = breed
        self.neutered = neutered
        self.microchipNumber = microchipNumber

    def toString(self):
        print("AnimalID:            ", self.animalID)
        print("Type of Animal:      ", self.typeOfAnimal)
        print("Breed:               ", self.breed)
        print("Vaccinated:          ", self.vaccinated)
        print("Neutered:            ", self.neutered)
        print("MicrochipNumber:     ", self.microchipNumber)
        print("Adoption Reason:     ", self.adoptionReason)
        print("Date of Arrival:     ", self.dateOfArrival)
        print("Date of Departure:   ", self.dateOfDeparture)
        print("Destination:         ", self.destination)
        print("Destination Address: ", self.destinationAddress)

    def readyForAdoption(self, animalType):
        ready = False
        if(self.typeOfAnimal == animalType):
            if(self.vaccinated == "Yes"):
                if(self.neutered == "Yes"):
                    if(len(self.microchipNumber)>2):
                        ready = True
        return ready


class WildAnimal(Animal):
    #constructor of class pet
    def __init__(self, animalID = "", typeOfAnimal = "", admissionReason = "", vaccinated = "", dateOfArrival = "", dateOfDeparture = "", destination = "", destinationAddress = ""):
        self.animalID = animalID
        self.typeOfAnimal = typeOfAnimal
        self.admissionReason = admissionReason
        self.vaccinated = vaccinated
        self.dateOfArrival = dateOfArrival
        self.dateOfDeparture = dateOfDeparture
        self.destination = destination
        self.destinationAddress = destinationAddress

    def toString(self):
        print("AnimalID:            ", self.animalID)
        print("Type of Animal:      ", self.typeOfAnimal)
        print("Vaccinated:          ", self.vaccinated)
        print("Admission Reason:    ", self.admissionReason)
        print("Date of Arrival:     ", self.dateOfArrival)
        print("Date of Departure:   ", self.dateOfDeparture)
        print("Destination:         ", self.destination)
        print("Destination Address: ", self.destinationAddress)

class TreatmentObj(Animal):

    #constructor of class pet
    def __init__(self, animalID = ""):
        self.animalID = animalID
            

    def toString(self):
        print("sanctuaryID:         ", self.sanctuaryID)
        print("Surgery:             ", self.surgery)
        print("Vaccinated:          ", self.vaccinated)
        print("Admission reason:    ", self.admissionReason)
        print("Date of arrival:     ", self.dateOfArrival)
        print("dateOfDeparture:     ", self.dateOfDeparture)
        print("destination:         ", self.destination)
        print("destinationAddress:  ", self.destinationAddress)