import os, re

files = os.listdir('templates')

for filename in files:
    print()
    if ".html" in filename:
        print(f"opening {filename}")
        buff = ""
        with open(f"templates/{filename}", 'r') as file:
            buff = file.read()
            buff = re.sub('src="Images', 'src="/static/Images', buff)
            print("substitution done")
        with open(f"templates/{filename}", 'w') as file:
            print("rewriting file")
            file.write(buff)

