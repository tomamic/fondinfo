import os, sys, subprocess, glob, urllib.request, zipfile

swig_ver = "swigwin-3.0.12"
swig_zip = swig_ver + ".zip"
if not os.path.exists(swig_ver):
    url = "https://kent.dl.sourceforge.net/project/swig/swigwin/"
    url += swig_ver + "/" + swig_zip
    with urllib.request.urlopen(url) as response:
        content = response.read()
        with open(swig_zip, "wb") as local_file:
            local_file.write(content)
    with zipfile.ZipFile(swig_zip, "r") as zip_ref:
        zip_ref.extractall(".")
    os.remove(swig_zip)

name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
#py_home = f"{os.environ['LOCALAPPDATA']}\\Programs\\Python\\Python37-32"
py_home = os.path.dirname(sys.executable)
cb_home = f"{os.environ['PROGRAMFILES(X86)']}\\CodeBlocks"
os.environ["PATH"] = f"C:\\MinGW\\bin;{cb_home}\\MinGW\\bin;{swig_ver};{os.environ['PATH']}"

includes1 = includes2 = ""
for fn in glob.glob("*.h"):
    includes1 += f"#include \"{fn}\"\n"
    includes2 += f"%include \"{fn}\"\n"

content = f"""%module {name}

%include <std_string.i>
%include <std_vector.i>
%template() std::vector<int>;
/*%template() std::vector<Actor*>;*/

%{{
/* Includes the header in the wrapper code */
{includes1.strip()}
%}}

/* Parse the header file to generate wrappers */
{includes2.strip()}"""

with open("module.i", "w") as file_i:
    file_i.write(content)

subprocess.call(f"swig -python -c++ module.i")
subprocess.call(f"g++ -std=c++14 -D_hypot=hypot -c *.cpp *.cxx -I\"{py_home}\\include\"")
subprocess.call(f"g++ -shared *.o \"{py_home}\\libs\\*.a\" -o _{name}.pyd")

os.remove("module.i")
for f in glob.glob("*.o"):
    os.remove(f)
for f in glob.glob("*wrap.cxx"):
    os.remove(f)
