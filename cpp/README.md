## Compile a `g2d` program on Linux

- `sudo apt install build-essential libboost-dev`
- `g++ -pthread -o anim anim.cpp`

## Compile a `g2d` program on Windows

- Install MinGW from <https://nuwen.net/mingw.html>
- Launch `open_distro_window.bat`, in the MinGW folder
- `g++ -O1 -o anim anim.cpp -lws2_32 -lwsock32`
