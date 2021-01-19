class Country():
	def __init__(self, country, continent):
		self.country = country
		self.continent = continent

	def presentation_country(self):
		return f"{self.country} located in {self.continent}."


class Brand():
	def __init__(self, brand_name, start_date):
		self.brand_name = brand_name
		self.start_date = start_date

	def presentation_brand(self):
		return f"{self.brand_name} since {self.start_date}"

class Season():
	def __init__(self, season, avg):
		self.season = season
		self.average_tmp = avg

	def presentation_season(self):
		return f"In {self.season} average tempreture is about {self.average_tmp}C."


class Product(Country, Brand, Season):
	def __init__(self, name, type_, price, quantity, country, continent, brand_name, start_date, season, avg):
		Country.__init__(self, country, continent)
		Brand.__init__(self, brand_name, start_date)
		Season.__init__(self, season, avg)
		self.name = name
		self.type_ = type_
		self.price = price
		self.quantity = quantity
	def presentation_product(self):
		return f"{self.name} is a {self.type_}.The price is {self.price} produced in {self.quantity} batch."

	def presentation(self): # 1/2 ?
		# return (f"{self.name} is a {self.type_} produced by {self.brand_name} since {self.start_date} located in {self.country} {self.continent}"
		# f" where in {self.season} average tempreture is {self.average_tmp}C. Product price is {self.price}$ and the quantity is about {self.quantity}.")
		return (f"{self.presentation_product()}Can be found in {self.presentation_country()} " 
			f"where {self.presentation_season()}The product is produced by {self.presentation_brand()}.")

	def discount(self, percent):
		return f"Discounted price will be {self.price - self.price * percent / 100}"	
	
	def produce(self, quantity_):
		self.quantity = self.quantity + quantity_
		return f"increased quantity will be {self.quantity}"

a = Product('X', 'Y', 500, 100, 'Spain', 'Europe', 'Z', '1991', 'Summer', '30.2')
# print(a.quantity)
# print(a.discount(35))
# print(a.produce(152))
# print(a.quantity)
print(a.presentation())