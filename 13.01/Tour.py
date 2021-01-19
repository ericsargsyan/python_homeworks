class Hotel():
	def __init__(self, hotel_name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price, **kwds):
		self.hotel_name = hotel_name
		self.place = place
		self.rooms_mid = rooms_mid
		self.mid_room_price = mid_room_price
		self.rooms_lux = rooms_lux
		self.lux_room_price = lux_room_price

	def presentation(self):
		return (f"Hotel {self.hotel_name} located in {self.place}.We have {self.rooms_mid} ordinary rooms"
			f" and {self.rooms_lux} luxury rooms.Price for ordinary room is {self.mid_room_price}$ per night and for"
			f" luxury room {self.lux_room_price}$ per night.")

	def booking(self, room, type_): 
		if type_ == "mid":
			self.rooms_mid[room] = 'busy'
		if type_ == "lux":
			self.rooms_lux[room] = 'busy'	

	def available_room_check(self, room_check):
		if room_check == 'mid':
			if 'free' in self.rooms_mid.values():
				return "We have available room"
			else:
				return "Sorry all rooms are busy"
		if room_check == 'lux':
			if 'free' in self.rooms_lux.values():
				return "We have available room"
			else:
				return "Sorry all rooms are busy"				

	def discount(self):
		pass


class Taxi():
	def __init__(self, taxi_name, car_types, price_for_tour, **kwds):
		self.taxi_name = taxi_name
		self.car_types = car_types
		self.price_for_tour = price_for_tour

	def presentation(self):
		return f"{self.taxi_name} company provides {self.car_types} and price for it {self.price_for_tour}"	

	def discount(self):
		pass


class Tour(Hotel, Taxi):
	
	def __init__(self, tour_name, **kwds):
		self.tour_name = tour_name
		Hotel.__init__(self, **kwds)
		Taxi.__init__(self, **kwds)
		# super().__init__(**kwds)
		self.price_mid = self.mid_room_price + self.price_for_tour
		self.prcie_lux = self.lux_room_price + self.price_for_tour



	
	def presentation(self):
		return (f"Hello we offer {self.tour_name} tour.We have to options {self.price_mid} and {self.prcie_lux}."
			f"which includes transport with {Taxi.presentation(self)}.We will stay at {Hotel.presentation(self)}")





rooms_mid = {'room1': 'free', 'room2': 'free', 'room3': 'free', 'room4': 'free', 'room5': 'free'}
rooms_lux = {'room1': 'free', 'room2': 'free', 'room3': 'free', 'room4': 'free', 'room5': 'free'}


print(Tour(tour_name='Dilijan',hotel_name='Armando', place='California', rooms_mid='empty', 
	mid_room_price=20, rooms_lux="busy", lux_room_price=50, taxi_name="Ohanyan", car_types='bmw',price_for_tour= 25000).presentation())




# class House():
# 	def __init__(self, room1_tmp, room2_tmp, room3_tmp, room4_tmp):
# 		self.room1 = room1_tmp
# 		self.room2 = room2_tmp
# 		self.room3 = room3_tmp
# 		self.room4 = romm4_tmp

# 	def get_tempreture(self, room):
# 		return self.room	

# 	def set_tempreture(self, room):
		

# a = House(32,33,40,20)
# print(a.get_tempreture())
