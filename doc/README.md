# Documentation

# Basic use of LSystem
To create a new L-system object, we need to call the `LSystem` empty constructor:

```
from LSystem import LSystem

my_system = LSystem()
```

Then, once we have this object, we can define its rules and its axiom:

```
my_system.axiom = 'F'
my_system.rules['F'] = 'F+F-F-F+F'
```

As we can see in this syntax, `my_system.rules` is a dictionary, to add a new rule we just have to define a new key-value pair.<br>
In this case, we have defined this rule:

<p align="center">F -> F+F-F-F+F<p>

To get the current state of the system we can access the "state" attribute:

```
print(my_system.state) #Prints the current state of the system
```

Finally, we can step forward the state of the system with the use of the "next" method, and we can reset the system to its initial state with the use of the "reset" method:

```
my_system.next() #Advances the state of the system once
my_system.next(5) #Advances the state of the system 5 times
my_system.reset() #Resets the state of the system to its initial state
```
  
# Basic use of PyGameInterpreter
