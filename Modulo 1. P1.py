import requests
import json

class Constructor():
    def __init__(self, id, name, nationality):
        self.id = id
        self.name = name
        self.nationality = nationality
        self.drivers = []

    def add_driver (self, driver):
        self.drivers.append(driver)

    def show(self):
        print("ID: " + self.id + ", Name: " + self.name + ", Nationality: " + self.nationality) 

class Drivers():
    def __init__(self, ID, permanetNumber, code, team, firstname, lastname, dateOfbirth, nationality):
        self.ID = ID
        self.permanetNumber = permanetNumber
        self.code = code
        self.team = team
        self.firstname = firstname
        self.lastname = lastname
        self.dateOfbirth = dateOfbirth
        self.nationality = nationality
    def show(self):
        print("ID: " + self.ID + "permanetNumber: " + self.permanetNumber + ", code: " + self.code + ", team: " + self.team + "firstName: " + self.firstname + "lastName: " + self.lastname + "dateOfbirth: " + self.dateOfbirth + "nationality: " + self.nationality)    

def main():
    print("Running program")
    online = False

    if(online):
        r = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json")
        api_constructors = r.json()
    else:
        f = open("API_constructores.json")
        api_constructors = json.load(f)
        f.close()
    constructors = []
    for constructor in api_constructors:
        object_constructor = Constructor(constructor["id"], constructor["name"], constructor["nationality"])
        constructors.append(object_constructor)
    for constructores in constructors:
        constructores.show()

    if(online):
        r = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json")
        api_drivers = r.json()
    else:
        f = open("API_drivers.json")
        api_drivers = json.load(f)
        f.close()
    print(api_drivers)    
    drivers = []
    for driver in api_drivers:
        object_drivers = Drivers(driver["id"], driver["permanentNumber"], driver["code"], driver["team"], driver["firstName"], driver["lastName"], driver["dateOfBirth"], driver["nationality"])
        drivers.append(object_drivers)
        #Buscar en la lista de constructores el team
        #Añadir a la lista del team el driver
    for drivers in drivers:
        drivers.show()  

    
    def constructor(id):
        temp = None
        for id in constructor:
            if id[id] == id:
                temp = id
            break
        return temp
       
main()
