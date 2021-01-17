import random

class House_Heating():
	def __init__(self, curr_temp, goal_temp):
		self.curr_temp = curr_temp
		self.goal_temp = goal_temp

	def get_temp(self):
		return self.curr_temp

	def set_temp(self, temp):
		self.curr_temp = temp

	def is_satisfied(self):
		if self.curr_temp == self.goal_temp:
			print("Current tempreture is satisfied.")
			return True
		else:
			print("Current tempreture is not satisfied.")
			return False

	# ____Magic Methods____	

	def __repr__(self):
		return "House-Heating system, checking/setting tempreture."

	def __int__(self):
		return self.curr_temp

	def __eq__(self, other):
		if self.curr_temp == other.curr_temp:
			return True
		else:
			return False	
							


def check_temp(h1, h2, h3, h4):
	if h1.is_satisfied() and h2.is_satisfied() \
	  and h3.is_satisfied() and h4.is_satisfied():
	  	print("All houses have normal tempretures.")
	else:
		print("Tempretures of the houses are not satisfied.")


House1 = House_Heating(random.randrange(10, 30), 22)
House2 = House_Heating(random.randrange(10, 30), 25)
House3 = House_Heating(random.randrange(10, 30), 23)
House4 = House_Heating(random.randrange(10, 30), 26)


# print(House1.curr_temp)
# print(House2.curr_temp)
# print(House3.curr_temp)
# print(House4.curr_temp)
# House1.set_temp(22)
# print(House1.curr_temp)
# House1.is_satisfied()

check_temp(House1, House2, House3, House4)

