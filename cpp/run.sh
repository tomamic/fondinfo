g++ main.cpp -Wno-deprecated -Wno-deprecated-declarations -DWEBVIEW_GTK=1 `pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0` -o _main
./_main
