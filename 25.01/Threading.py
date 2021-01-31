import requests
import threading
import json
import time
import datetime
import concurrent.futures

def download_images(json_file):
	with open(json_file, 'r') as photo_file:
		photos = json.load(photo_file)

	for i in photos['images']:
		images = requests.get(i['URL'])
		with open(f"{i['name']}.jpeg", 'wb') as uploads:
			uploads.write(images.content)

starting_time = datetime.datetime.now()# .strftime('%m/%d/%Y, %H:%M:%S')

print(f"Starting Time: {starting_time.strftime('%m/%d/%Y, %H:%M:%S')}")

threading_list = []

x = threading.Thread(target=download_images, args=("images.json",))
x.start()



# with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#    executor.map(download_images, ["images.json"])
    
# print(f"Code Execution Time: {(datetime.datetime.today() - starting_time).seconds}")
download_images('images.json')

print(f"Code Execution Time: {(datetime.datetime.today() - starting_time).seconds}")


