import logging

engine_number = '1_1'
tell_temp = int(input("tell the temp  "))
# the default level for logging is warning
if tell_temp > 50:
	logging.warning('The engine temperature is above the optimal level!')  # will print a message to the console

logging.info('The engine temperature is raising')  # will not print anything
logging.debug(F'The {engine_number} engine temperature is raising')  # will not print anything
logging.error(F"Can't turn off {engine_number} engine")  # will print the message to the console


# logging into a file, and defineing the level

logging.basicConfig(filename='temperatures.log', level=logging.DEBUG)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# clear the rest of logs when writing 

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# you can pass variables as well

logging.warning('%s before you %s', 'Look', 'leap!')

logging.basicConfig(level=logging.DEBUG)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# To change the format which is used to display messages, you need to specify the format you want to use:
# levelname - level=logging.DEBUG
# message  - message which should be logged	

logging.basicConfig(format='%(message)s:%(levelname)s', level=logging.DEBUG)
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# Displaying the date/time in messages

logging.basicConfig(filname="", format='%(asctime)s %(message)s')
logging.warning('is the temperature 100.')
logging.info('is the temperature 100.')

# Exception information can be captured if the exc_info parameter
dict_ = {"key1": 5}

try:
	a = dict_["key2"]
except KeyError:
	logging.error("key2 is not exist", exc_info=True)

print("\n that was error message")

def myFun(*argv, **kwargs):
	a = 0 
    for arg in argv: 
    	a += arg

    return a


