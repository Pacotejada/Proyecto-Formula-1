import json
import requests
import time
import random

class Race:
    def __init__(self, raceRound, raceName, raceCircuit, raceDate, raceRestaurants, raceMap):
        self.raceRound = raceRound
        self.raceName = raceName
        self.raceCircuit = raceCircuit
        self.raceDate = raceDate
        self.raceRestaurants = raceRestaurants
        self.raceMap = raceMap
    
    def __dict__(self):
        return {
            "Round:" : self.raceRound,
            "Name:" : self.raceName,
            "Circuit:" : self.raceCircuit,
            "Date:" : self.raceDate,
            "Restaurants:" : self.raceRestaurants,
            "Map" : self.raceMap
            }

    def __str__(self):
        return "{\n"f"round: {self.raceRound}\nname: {self.raceName}\ncircuit: {self.raceCircuit}\ndate: {self.raceDate}\nrestaurants: {self.raceRestaurants}\nmap: {self.raceMap}""},\n"

    def __repr__(self):
        return f"round: {self.raceRound}\nname: {self.raceName}\ncircuit: {self.raceCircuit}\ndate: {self.raceDate}\nrestaurants: {self.raceRestaurants}\nmap: {self.raceMap}"

    def add_races (self, races):
        self.races.append(races)

    def show(self):
        print("Round: " + self.raceRound + ", Name: " + self.raceName + ", Circuit: " + self.raceCircuit + ", Date: " + self.raceDate + ", Restaurants: " + self.raceRestaurants + ", Map: " + self.raceMap) 

r = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json")
print(r.status_code)
api_races = r.json()

def main():
    print("Running program")
    online = False

    if(online):
        r = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json")
        api_races = r.json()
    else:
        f = open("API_races.json")
        api_races = json.load(f)
        f.close()
    print(api_races)    
    races = []
    for races in api_races:
        object_race = Race(raceRound=["Round"], raceName=["Name"], raceCircuit=["Circuit"], raceDate=["Date"], raceRestaurants=["Restaurants"], raceMap=["Map"])
        races.append(object_race)

    for races in races:
        races.show()
main()


race_list = []

def assign_racedata():

    newRaceRound = ""
    newRaceName = ""
    newRaceCircuit = ""
    newRaceDate = ""
    newRaceRestaurants = ""
    newRaceMap = ""
    newRace = None
    for r in api_races:
        newRaceRound = r['round']
        newRaceName = r['name']
        newRaceCircuit = r['circuit']
        newRaceDate = r['date']
        newRaceRestaurants = r['restaurants']
        newRaceMap = r['map']
        newRace = race_list(newRaceRound, newRaceName, newRaceCircuit, newRaceDate, newRaceRestaurants, newRaceMap)
        race_list.append(newRace)

def save_racedata():    
    save_races_tofile = open("races.txt", "w")
    save_races_tofile.write("[")
    for r in race_list:
        save_races_tofile.write(r.__str__())
    save_races_tofile.write("]")
    save_races_tofile.close()

def select_race():
    while True:
        selected_race = None
        while selected_race == None:
            for rac in race_list:
                print(rac.raceName)
            selected_race = input("\nElija una carrera:")
        for rac in race_list:
            if selected_race == rac.raceName:
                selected_race = rac.raceName
            else:
                pass
        confirmation = None
        while confirmation == None:
            confirmation = input("La carrera seleccionada es {}", selected_race,"¿Finalizar una carrera?\n[1]Sí [2]No")
            try:
                confirmation = int(confirmation)
                break
            except ValueError:
                print("Inválido: Necesitas introducir un número correspondiente a las opciones mostradas")
        if confirmation == 1:
            print("Finalizando carrera...")
            time.sleep(1)
            return selected_race
        elif confirmation == 2:
            print("Cancelando...")
            time.sleep(1)
            break

def finish_race(selected_race):
    points = 0
    first = points + 25
    second = points + 18
    third = points + 15
    fourth = points + 12
    fifth = points + 10
    sixth = points + 8
    seventh = points + 6
    eighth = points + 4
    ninth = points + 2
    tenth = points + 1
    while True:
        random_drivers = random.sample(race_list)
        print("**PODIUM**")
        for rd in random_drivers:
            if rd in rd[0]:
                print (rd.firstName, rd.lastName, "Puntos:", first)
                firstplace = rd.driverID
            elif rd in rd[1]:
                print (rd.firstName, rd.lastName, "Puntos:", second)
                secondplace = rd.driverID
            elif rd in rd[2]:
                print (rd.firstName, rd.lastName, "Puntos:", third)
                thirdplace = rd.driverID
            elif rd in rd[3]:
                print (rd.firstName, rd.lastName, "Puntos:", fourth)
                fourthplace = rd.driverID
            elif rd in rd[4]:
                print (rd.firstName, rd.lastName, "Puntos:", fifth)
                fifthplace = rd.driverID
            elif rd in rd[5]:
                print (rd.firstName, rd.lastName, "Puntos:", sixth)
                sixthplace = rd.driverID
            elif rd in rd[6]:
                print (rd.firstName, rd.lastName, "Puntos:", seventh)
                seventhplace = rd.driverID
            elif rd in rd[7]:
                print (rd.firstName, rd.lastName, "Puntos:", eighth)
                eighthplace = rd.driverID
            elif rd in rd[8]:
                print (rd.firstName, rd.lastName, "Puntos:", ninth)
                ninthplace = rd.driverID
            elif rd in rd[9]:
                print (rd.firstName, rd.lastName, "Puntos:", tenth)
                tenthplace = rd.driverID
            else:
                print (rd.firstName, rd.lastName, "Puntos:", points)
        winners = [firstplace, secondplace, thirdplace, fourthplace, fifthplace, sixthplace, seventhplace, eighthplace, ninthplace, tenthplace]
        print("Resultados de la carrera", selected_race)
        return winners

assign_racedata()
save_racedata()