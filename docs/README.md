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
This class is a subclass of LSystemInterpreter, in the next section I will explain how you can build your own interpeter from this base class, but for now, to use PyGameInterpreter we need to create an object from this class, here we have the arguments for the constructor:
  
```
PyGameInterpreter(surface: pygame.surface, line_width: float = 1.0, color: Tuple[int, int, int] = (255, 255, 255), start_pos: Tuple[float, float] = (0, 0), step_size: float = 1.0, start_angle: float = 0.0, angular_step_size: float = 90.0)
```

Required arguments:<br>
*`surface: pygame.surface`: This is the pygame surface over which this object will draw.<br>
<br>
Optional arguments:<br>
* `line_width: float`: Width of the line in pygame, defaults to `1.0`.<br>
* `color: Tuple[int, int, int]`: Tuple with the color of the line in format 24-bit rgb, defaults to `(255, 255, 255)` <br>
* `start_pos: Tuple[float, float]`: Tuple with the 2D cartesian coordinates of the starting position of the pointer, defaults to `(0, 0)`.<br>
* `step_size: float`: Step size of the translation of the pointer, defaults to `1.0`.<br>
* `start_angle: float`: Initial angle in degrees of the pointer, defaults to `0.0`.<br>
* `angular_step_size: float`: Step size of the rotation of the pointer in degrees, defaults to `90.0`.<br>
<br>
To draw something, we need to call the following method:<br>
  
```
myPyGameInterpreter.compile(state: str)
```
  
Required arguments:<br>
* `state: str`: String representing the state of an L-system.<br>
  
# How to build your own interpreter
If you want to be able to draw images in any other place different than pygame, you can do that by subclassing LSystemInterpreter, and overriding the method called `_drawline`, here you can access the current position with `self.current_pos`, and you can access the previous position with `self.previous_pos`. Using these two points, you have to do the neccessary to draw a line between them in your application.<br>
