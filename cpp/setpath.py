import os
folders = ["C:\\MinGW\\bin", "C:\\MinGW\\mingw64\\bin"]
for elem in os.environ["PATH"].split(";"):
	if elem and elem not in folders:
		folders.append(elem)
newpath = ";".join(folders)
os.environ["PATH"] = newpath
os.system(f'setx PATH "{newpath}"')
os.system(f'setx CPATH "C:\\MinGW\\include"')
os.system(f'setx LD_LIBRARY_PATH "C:\\MinGW\\lib"')
