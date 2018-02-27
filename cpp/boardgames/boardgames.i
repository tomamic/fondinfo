%module boardgames

%include <std_string.i>

%{
/* Includes the header in the wrapper code */

#include "boardgame.h"
#include "lightsout.h"

%}

/* Parse the header file to generate wrappers */

%include "boardgame.h"
%include "lightsout.h"

