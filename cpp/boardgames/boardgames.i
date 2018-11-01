%module boardgames

%include <std_string.i>

%{
/* Includes the header in the wrapper code */

#include "boardgame.h"
#include "lightsout.h"
#include "fifteen.h"

%}

/* Parse the header file to generate wrappers */

%include "boardgame.h"
%include "lightsout.h"
%include "fifteen.h"

