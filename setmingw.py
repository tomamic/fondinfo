import os, subprocess

def add_to_env(key, new_values):
    vals = list(new_values)
    for elem in os.environ.get(key, "").replace("\"", "").split(";"):
        if elem and elem not in vals:
            vals.append(elem)
    os.environ[key] = ";".join(vals)
    subprocess.call(["setx", key, os.environ[key]])

add_to_env("PATH", ["C:\\MinGW\\bin"])
add_to_env("CPATH", ["C:\\MinGW\\include"])
add_to_env("LD_LIBRARY_PATH", ["C:\\MinGW\\lib"])
