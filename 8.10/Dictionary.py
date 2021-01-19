class Dictionary():
	# def __init__(self, word):
	# 	self.word = None


	def create_dictionary(self, word):
		d = dict()
		for i in word:
			d[i] = d.get(i, 0) + 1
		return d

	
	# def remove_copies(self, word):
	# 	unique = dict()
	# 	for i in self.create_dictionary(word):
	# 		if self.create_dictionary(word)[i] not in unique.values():
	# 			unique.update({i: self.create_dictionary(word)[i]})
	# 	return unique

	
	def remove_copies(self, dictionary):
		unique = dict()
		for i in dictionary:
			if dictionary[i] not in unique.values():
				unique.update({i: dictionary[i]})
		return unique	
	

	def max_three(self, dictionary):
		ls = list(dictionary.items())
		for i in range(len(ls)):
			for j in range(len(ls)):
				if ls[i][1] > ls[j][1]:
					ls[i], ls[j] = ls[j], ls[i]
		dictionary = dict(ls[:3])				
		return dictionary

