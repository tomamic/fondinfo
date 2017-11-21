TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt
CONFIG += c++11

SOURCES += main.cpp \
    box.cpp \
    boxlayout.cpp \
    vboxlayout.cpp \
    hboxlayout.cpp

HEADERS += \
    box.h \
    boxlayout.h \
    vboxlayout.h \
    hboxlayout.h

