from math import pi


class Circle():
	def __init__(self, radius):
		# if radius > 0:
		# 	self.radius = radius
		# else:
		# 	radius = 1
		self.radius = radius

	def area(self):
		return pi * self.radius * self.radius


	def perimeter(self):
		return 2 * pi * self.radius


r = int(input('Input radius: '))
c = Circle(r)
print(c.area())
print(c.perimeter())
