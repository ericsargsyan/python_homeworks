import datetime
import time
from functools import wraps

# This decorator fucntions working time in a given file

def my_decorator(file_name) -> callable:
	def decorator(func: callable) -> callable:
		@wraps(func)
		def decor(*args, **kwargs):
			print(datetime.datetime.now())
			execution_time = datetime.datetime.now()
			result = func(*args, **kwargs)
			print(f"Time taken: {(datetime.datetime.now() - execution_time).seconds} seconds")
			with open(file_name, 'a') as file:
				file.write(f"Execution time: {(execution_time.strftime('%m/%d/%Y, %H:%M:%S'))}\n")
				if result is not None:
					file.write(f"{str(result)}\n")
				else:
					file.write('None\n')
				file.write(f"Time taken: {(datetime.datetime.now() - execution_time).seconds} seconds\n")
			print("Inside decor fucntion")
			return result
		return decor
	return decorator	

file_name = 'test10.txt'

@my_decorator(file_name)

# some functions

def some_function(some_arguments):
	# some code
	for i in range(222222):
		print(i)		
	return some_arguments

a = some_function(222)
print(some_function.__name__)
print(a)

