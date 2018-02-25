%module fifteen

%include <std_string.i>
%include <std_vector.i>

%{
/* Includes the header in the wrapper code */

#include "fifteen.h"

%}

/* Parse the header file to generate wrappers */

%include "fifteen.h"
