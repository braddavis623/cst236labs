cst 236 lab2 writeup
********************

TDD vs BDD
^^^^^^^^^^

With TDD we take a step back from aiming to write code that satisfies requirements
and first write tests that the code should satisfy. This accomplishes helping ensure 
that more of the code is thoroughly tested, among other things. With BDD, we take yet
another step back, and describe in a more readable format, the behaviors that the
code will need to exhibit. The more plain the language, the more accessible it is 
to those who may not have a full understanding of what it is they are requiring.



About mixins:
^^^^^^^^^^^^^

A moxin is a class that implements methods from multiple other classes. They can 
be difficult to test, as its sometimes more difficult to tell where the problem behavior
originates. Base classes are initialized ased on where the derived class calls the 
super() function. It could be at the begining or the end of the __init__() funciton.


About super()
^^^^^^^^^^^^^

Super() calls the base class' version of the function.


TDD vs BDD difficulty
^^^^^^^^^^^^^^^^^^^^^

I found the BDD model more challenging. It seemed a bit removed, or at least only 
arbitrarily connected to the end-functionality of the code. TDD seemed much more 
useful for driving the production of robust behaviors. BDD did also represent 
another system to get used to, so it would seem to stand that, were someone to 
fully devote themselves to BDD (and their team), then maybe it couldbe useful.
But it seems that it would take a disproportionate amount of time/effort to 
realize only minimal benefits.


Maintainability
^^^^^^^^^^^^^^^

I found that with TDD, I could more quickly jump into a 'groove' that made sense
to me. It seemed easier to conceptualiz and them implement any changes I found 
the need for.


Logging
^^^^^^^

The logging was handled manually.