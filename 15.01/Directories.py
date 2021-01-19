import os

print(os.getcwd())

os.mkdir('Dir1')
path = os.path.join(os.getcwd(), 'Dir1')
os.chdir('Dir1')
os.mkdir('Dir2')
os.makedirs('Dir3/Dir4')

print(os.getcwd())
print(os.listdir())

delete = input("Do you want to delete the folders? y/n ")
if delete == 'y':
	for i in os.listdir():
		if os.path.isdir():
			os.chdir('Dir3')		
			os.rmdir('Dir4')
	os.chdir('..')
		if os.path.isdir():
			os.rmdir('Dir3')
	        os.rmdir('Dir2')
	os.chdir('..')
		if os.path.isdir():
			os.rmdir('Dir1')
	print('folders have been deleted.')

