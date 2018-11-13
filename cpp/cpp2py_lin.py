import os, subprocess, glob

name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

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
/* Include the header in the wrapper code */
{includes1.strip()}
%}}

/* Parse the header to generate wrappers */
{includes2.strip()}"""

with open("module.i", "w") as file_i:
    file_i.write(content)

subprocess.call("swig -python -c++ module.i", shell=True)
subprocess.call(f"g++ -fPIC -shared *.cpp *.cxx -I/usr/include/python3.6m -o _{name}.so", shell=True)

os.remove("module.i")
for f in glob.glob("*.o"):
    os.remove(f)
for f in glob.glob("*wrap.cxx"):
    os.remove(f)
