## Compile a `g2d` program on Linux

- `sudo apt install build-essential libboost-dev`
- `g++ anim.cpp -o anim -pthread`

## Compile a `g2d` program on Windows

- Install MinGW from <https://nuwen.net/mingw.html>
- Launch `open_distro_window.bat`, in the MinGW folder
- `g++ -O1 anim.cpp -o anim.exe -lws2_32 -lwsock32`
