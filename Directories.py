import os

print(os.getcwd())
os.chdir('python\pyhton-homeworks')
# C:\Users\Eric Sargsyan\python\pyhton-homeworks\

os.mkdir('Dir1')
os.chdir('Dir1')
os.mkdir('Dir2')
os.makedirs('Dir3/Dir4')

print(os.getcwd())
print(os.listdir())

delete = input("Do you want to delete the folders? y/n ")
if delete == 'y':
	os.chdir('Dir3')
	os.rmdir('Dir4')
	os.chdir('..')
	os.rmdir('Dir3')
	os.rmdir('Dir2')
	os.chdir('..')
	os.rmdir('Dir1')
	print('folders have been deleted.')

