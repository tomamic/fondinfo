import os
folders = ["C:\\MinGw\mingw64\\bin"]
for elem in os.environ["PATH"].split(";"):
	if elem and elem not in folders:
		folders.append(elem)
newpath = ";".join(folders)
os.environ["PATH"] = newpath
os.system(f'setx PATH "{newpath}"')
