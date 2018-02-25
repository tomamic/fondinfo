%module bounce

%include <std_string.i>
%include <std_vector.i>
%template() std::vector<Actor*>;
%template() std::vector<int>;

%{
/* Includes the header in the wrapper code */

#include "actor.h"
#include "bounce.h"

%}

/* Parse the header file to generate wrappers */

%include "actor.h"
%include "bounce.h"
