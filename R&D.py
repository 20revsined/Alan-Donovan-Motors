class Vehicle():
	def __init__(self, quantity, speed, ModelNumber, AmountGas, KPL, NumPassengers):
		self.quantity = quantity
		self.speed = speed
		self.ModelNumber = ModelNumber
		self.AmountGas = AmountGas #measured in liters
		self.KPL = KPL #kilometers per liter
		self.NumPassengers = NumPassengers


	def getspeed(self):
		return self.speed * (18.0 / 5.0)
		
	def getAmountGas(self):
		return self.AmountGas

	def getKPL(self):
		return self.KPL

	def getQuantity(self):
		return self.quantity

	def getModelNumber(self):
		return self.ModelNumber

	def getNumPassengers(self):
		return self.NumPassengers

class Boat(Vehicle):
	def __init__(self, quantity, speed, ModelNumber, AmountGas, KPL, NumPassengers, isAfloat):
		Vehicle(quantity, speed, ModelNumber, AmountGas, KPL, NumPassengers)
		self.isAfloat = isAfloat

	def getNumPassengers(self):
		return Vehicle.getNumPassengers(self) + 4

class Car(Vehicle):
	def __init__(self, quantity, speed, ModelNumber, AmountGas, KPL, NumPassengers):
		Vehicle(quantity, speed, ModelNumber, AmountGas, KPL, NumPassengers)
	
	def getNumPassengers(self):
		return Vehicle.getNumPassengers(self) - 2

def carFunction():
	gas = float(input("How much gas would like in your car (in liters)?: "))
	passengers = int(input("Please enter the number of passengers traveling in the car with you today. Please note that you may only have a maximum of 4 passengers."))
	CarSpeed = float(input("Please enter the speed of the car in miles per hour (this speed will be converted into km/hr)."))
	car = Car(1, CarSpeed, 1001, gas, 50, passengers)

def boatFunction():
	gas = float(input("How much gas would you like in your boat (in liters)?: "))
	passengers = int(input("Please enter the number of passengers traveling in the boat with you today. Please note that you may only have a maximum of 10 passengers."))
	BoatSpeed = float(input("Please enter the speed of the boat in miles per hour (this speed will be converted into km/hr)."))
	boat = Boat(1, BoatSpeed, 1001, gas, 15, passengers, True)

switcher = {"car": carFunction, "boat": boatFunction}

vehicle = str(input("Welcome to Alan Donovan Motors Testing Department! Please enter what type of vehicle you will be testing today."))
if vehicle == "car":
	switcher.get(vehicle)()

elif vehicle == "boat":
	switcher.get(vehicle)()

# elif vehicle == "airplane":
	# gas = 50
	# print(str("You currently have " + str(gas) + " liters left in the tank."))
	# passengers = str(input("Please enter the number of passengers traveling in the airplane with you today. Please note that you may only have a maximum of 25 passengers."))
	# AirplaneSpeed = float(input("Please enter the speed of the airplane in miles per hour (this speed will be converted into km/hr)."))
	# print("There are " + str(gas) + " left in the tank of the airplane, there are " + str(passengers) + " passengers traveling with you in the airplane, and you are traveling at " + str(speed) + " km/hr.")
