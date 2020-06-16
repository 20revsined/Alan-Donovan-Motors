class Vehicle():
	def __init__(self, speed, AmountGas, KPL, NumPassengers):
		Vehicle.speed = speed
		self.AmountGas = AmountGas  # measured in liters
		self.KPL = KPL  # kilometers per liter
		self.NumPassengers = NumPassengers

	def getSpeed(self):
		return Vehicle.speed * (18.0 / 5.0)

	def getAmountGas(self):
		return self.AmountGas

	def getKPL(self):
		return self.KPL

	def getNumPassengers(self):
		return self.NumPassengers


class Boat(Vehicle):
	def __init__(self, speed, AmountGas, KPL, NumPassengers, isAfloat):
		Vehicle(speed, AmountGas, KPL, NumPassengers)
		self.isAfloat = isAfloat

	def Floating(self):
		return self.isAfloat


class Car(Vehicle):
	def __init__(self, speed, AmountGas, KPL, NumPassengers):
		Vehicle(speed, AmountGas, KPL, NumPassengers)

	def getSpeed(self):
		return Vehicle.getSpeed(Vehicle)


class Airplane(Vehicle):
	def __init__(self, speed, AmountGas, KPL, NumPassengers, isFlying):
		Vehicle(speed, AmountGas, KPL, NumPassengers)
		self.isFlying = isFlying

	def Flying(self):
		return self.isFlying


car = None
boat = None
airplane = None


def carFunction():
	gas = float(input("How much gas would like in your car (in liters)?: "))
	passengers = int(input(
		"Please enter the number of passengers traveling in the car with you today. Please note that you may only have a maximum of 4 passengers."))
	CarSpeed = float(input(
		"Please enter the speed of the car in miles per hour (this speed will be converted into km/hr)."))
	global car
	car = Car(CarSpeed, gas, 50, passengers)


def boatFunction():
	gas = float(input("How much gas would you like in your boat (in liters)?: "))
	passengers = int(input(
		"Please enter the number of passengers traveling in the boat with you today. Please note that you may only have a maximum of 10 passengers."))
	BoatSpeed = float(input(
		"Please enter the speed of the boat in miles per hour (this speed will be converted into km/hr)."))
	global boat
	boat = Boat(BoatSpeed, gas, 15, passengers, True)


def airplaneFunction():
	gas = float(
		input("How much gas would you like in your airplane (in liters)?: "))
	passengers = int(input(
		"Please enter the number of passengers traveling in the airplane with you today. Please note that you may only have a maximum of 25 passengers."))
	AirplaneSpeed = float(input(
		"Please enter the speed of the boat in miles per hour (this speed will be converted into km/hr)."))
	global airplane
	airplane = Airplane(AirplaneSpeed, gas, 15, passengers, False)


switcher = {"car": carFunction, "boat": boatFunction,
			"airplane": airplaneFunction}

vehicle = str(input(
	"Welcome to Alan Donovan Motors Testing Department! Please enter what type of vehicle you will be testing today."))
if vehicle == "car":
	switcher.get(vehicle)()
	print(car.getSpeed())


elif vehicle == "boat":
	switcher.get(vehicle)()

elif vehicle == "airplane":
	switcher.get(vehicle)()
