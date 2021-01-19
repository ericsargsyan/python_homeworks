class Person():
	def __init__(self, name, surename, age):
		self.name = name
		self.surename = surename
		self.age = age

	
	def presentation(self):
		return f"My name is {self.name} {self.surename} and im {self.age} years old."	


class Student(Person):
	def  __init__(self, name, surename, age, university):
		super().__init__(name, surename, age)
		self.university = university

	def present(self):
		return f"{self.presentation()} And i study at {self.university}." 	



# people1 = Person('x' '19')
print(people1.presentation())
people2 = Student('Eric', 'Sargsyan', 19, 'Yerevan State University')
print(people2.present())

