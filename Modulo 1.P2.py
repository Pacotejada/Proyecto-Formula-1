import requests
import json

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

    def __dict__(self):
        
        return {
            "ID:" : self.ID,
            "permanentNumber:" : self.permanetNumber,
            "code:" : self.code,
            "team:" : self.team,
            "firstName:" : self.firstname,
            "lastName:" : self.lastname,
            "dateOfbirth:" : self.dateOfbirth,
            "nationality:" : self.nationality
            }

    def __str__(self):
        return "{\n"f"ID: {self.ID}\nPermanent Number: {self.permanentNumber}\nCode: {self.code}\nTeam: {self.team}\nFirst Name: {self.firstName}\nLast Name: {self.lastName}\nDOB: {self.dateOfBirth}\nNationality: {self.nationality}\n""}\n"

    def __repr__(self):

        return "{\n"f"ID: {self.ID}\nPermanent Number: {self.permanentNumber}\nCode: {self.code}\nTeam: {self.team}\nFirst Name: {self.firstName}\nLast Name: {self.lastName}\nDOB: {self.dateOfBirth}\nNationality: {self.nationality},\n""}\n"


driver_list = []

retrieval = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json")
print(retrieval.status_code)
downloaded_list_drivers = retrieval.json()

def show(self):
        print("ID: " + self.ID + "permanetNumber: " + self.permanetNumber + ", code: " + self.code + ", team: " + self.team + "firstName: " + self.firstname + "lastName: " + self.lastname + "dateOfbirth: " + self.dateOfbirth + "nationality: " + self.nationality)    

def main():
    print("Running program")
    online = False

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

    for drivers in drivers:
        drivers.show()
main()  

def assign_and_save_driverdata():

    newDriverID = ""
    newDriverNumber = ""
    newDriverCode = ""
    newDriverTeam = ""
    newDriverfName = ""
    newDriverlName = ""
    newDriverDOB = ""
    newDriverNationality = "" 

    for d in downloaded_list_drivers:
        newDriverID = d['id']
        newDriverNumber = d['permanentNumber'] 
        newDriverCode = d['code']
        newDriverTeam =d ['team']
        newDriverfName = d['firstName'] 
        newDriverlName =d ['lastName']
        newDriverdateOfBirth = d['dateOfBirth']
        newDriverNationality = d['nationality']
        newDriver = driver_list(newDriverID, newDriverNumber, newDriverCode, newDriverTeam, newDriverfName, newDriverlName, newDriverdateOfBirth, newDriverNationality)
        driver_list.append(newDriver)


    save_drivers_tofile = open("drivers.txt", "w")
    save_drivers_tofile.write("[")
    for o in driver_list:
        save_drivers_tofile.write(o.__str__())
    save_drivers_tofile.write("]")
    save_drivers_tofile.close()

assign_and_save_driverdata()