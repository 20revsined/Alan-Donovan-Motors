#switcher = {"car": carFunction(), "boat": boatFunction(), "airplane": airFunction()}


class Vehicle():
	def __init__(self, quantity, speed, ModelNumber, AmountGas, KPL, NumPassengers):
		self.quantity = quantity
		self.speed = speed
		self.ModelNumber = ModelNumber
		self.AmountGas = AmountGas #measured in liters
		self.KPL = KPL #kilometers per liter
		self.NumPassengers = NumPassengers


	def speed(x):
		return x * (18 / 5)
		
	def AmountGas(x):
		return (50 - (2 * x))

	def KPL(x):
		return x

	def getQuantity(x):
		return x

	def getModelNumber(x):
		return x

	def NumPassengers(x):
		return x

class Boat(Vehicle):
	def __init__(self, isAfloat):
		self.ModelNumber = ModelNumber
		isAfloat = True

	def NumPassengers(x):
		return x + 4

class Car(Vehicle):
	def __init__(self, ):


	def NumPassengers(x):
		return x - 2

class Main(Vehicle):
		vehicle = str(input("Welcome to Alan Donovan Motors Testing Department! Please enter what type of vehicle you will be testing today."))

		if vehicle == "car":
			car = Vehicle()
			gas = 50
			print(str("You currently have " + str(gas) + " liters left in the tank."))
			passengers = str(input("Please enter the number of passengers traveling in the car with you today. Please note that you may only have a maximum of 4 passengers."))
			CarSpeed = float(input("Please enter the speed of the car in miles per hour (this speed will be converted into km/hr)."))
			Vehicle.speed(CarSpeed)
			print("There are " + str(gas) + " left in the tank of the car, there are " + str(passengers) + " passengers traveling with you in the car, and you are traveling at " + str(speed) + " km/hr.")

		elif vehicle == "boat":
			gas = 50
			print(str("You currently have " + str(gas) + " liters left in the tank."))
			passengers = str(input("Please enter the number of passengers traveling in the boat with you today. Please note that you may only have a maximum of 10 passengers."))
			BoatSpeed = float(input("Please enter the speed of the boat in miles per hour (this speed will be converted into km/hr)."))
			speed(BoatSpeed)
			print("There are " + str(gas) + " left in the tank of the boat, there are " + str(passengers) + " passengers traveling with you in the boat, and you are traveling at " + str(speed) + " km/hr.")

		elif vehicle == "airplane":
			gas = 50
			print(str("You currently have " + str(gas) + " liters left in the tank."))
			passengers = str(input("Please enter the number of passengers traveling in the airplane with you today. Please note that you may only have a maximum of 25 passengers."))
			AirplaneSpeed = float(input("Please enter the speed of the airplane in miles per hour (this speed will be converted into km/hr)."))
			Vehicle.speed(AirplaneSpeed)
			print("There are " + str(gas) + " left in the tank of the airplane, there are " + str(passengers) + " passengers traveling with you in the airplane, and you are traveling at " + str(speed) + " km/hr.")
