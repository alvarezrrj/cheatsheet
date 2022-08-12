import os

files = os.listdir('.')

for filename in files:
    with open(filename, '+') as file:
        buff = file.read()
        buff
        replace 'src="Images' for 'src="/static/Images':

