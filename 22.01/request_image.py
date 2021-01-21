import requests


class Image_Request():
	def __init__(self, URL):
		self.image_list = []
		response = requests.get(URL)

		with open('script.txt', 'w') as script_file:
			script_file.write(response.text)

		with open('script.txt', 'r') as script_file:
			for line in script_file:
				if line.startswith('<img'):
					line = line.split("\"")
					self.image_list.append(line[1])

class Image_jpeg(Image_Request):
	
	def download(self):
		for i in range(len(self.image_list)):
			dw_photo = requests.get('https:' + self.image_list[i])
			with open(f"photo{i + 1}.jpeg", 'wb') as photo:
				photo.write(dw_photo.content)			

class Image_png(Image_Request):

	def download(self):
		for i in range(len(self.image_list)):
			dw_photo = requests.get('https:' + self.image_list[i])		
			with open(f"photo{i + 1}.png", 'wb') as photo:
				photo.write(dw_photo.content)


	
# test = Image_png("https://xkcd.com/")
# test.download()


