import logging
import time
import random


logging.basicConfig(filename='loggings.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: \t%(message)s', datefmt='%d/%m/%Y %H:%M:%S')

#  format='%(message)s:%(levelname)s'
# f'{time.strftime("%m/%d/%Y %H:%M:%S")}: %"(levelname)"s'
for i in range(10):
	number = random.randint(0, 50)

	if number in range(0,9):
		logging.debug("The number is between 0 and 9")
	if number in range(10, 19):
		logging.info('The number is between 10 and 19')
	if number in range(20, 29):
		logging.warning('The number is between 20 and 29')
	if number in range(30, 39):
		logging.error('The number is between 30 and 39')
	if number in range(40, 50):
		logging.critical('The number is between 40 and 50')				

