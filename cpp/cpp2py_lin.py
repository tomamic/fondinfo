import os, subprocess, glob

name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

includes1 = includes2 = actor_template = ""
for hpp_file in ["g2d/actor.hpp", "../g2d/actor.hpp"] + list(glob.glob("*.hpp")):
    if os.path.exists(hpp_file):
        includes1 += f"#include \"{hpp_file}\"\n"
        includes2 += f"%include \"{hpp_file}\"\n"
        if "actor.hpp" in hpp_file:
            actor_template = "%template() std::vector<Actor*>;\n"

content = f"""%module {name}

%include <std_string.i>
%include <std_vector.i>
%template() std::vector<int>;
{actor_template}

%{{
/* Include the header in the wrapper code */
{includes1.strip()}
%}}

/* Parse the header to generate wrappers */
{includes2.strip()}"""

with open("module.i", "w") as file_i:
    file_i.write(content)

subprocess.call("swig -python -c++ module.i", shell=True)
subprocess.call(f"g++ -fPIC -shared *.cxx -I/usr/include/python3.7m -o _{name}.so", shell=True)

os.remove("module.i")
for f in glob.glob("*.o"):
    os.remove(f)
#for f in glob.glob("*wrap.cxx"):
#    os.remove(f)
