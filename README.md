# pyLSystem
Python library designed to build fractals from L-systems.

# Usage
The simplest way to use pyLSystem is to copy this git, and start editing the "main.py" file which generates images from an L-System like the ones shown in the examples below.

# What are L-systems?
L-systems consist of a string of symbols that have a determined rule to calculate a new string of symbols that replaces the previous one. By doing this process over and over, we get new states of the system. <br>
On the other hand, each symbol can be interpreted as an instruction to draw an image.<br>

Let's look at an example to understand it better.<br>
Suppose that we start with the following string:<br>

<p align="center">
  AABB
</p>

And that we have this set of rules:<br>

<p align="center">
  A -> A<br>
  B -> AB
</p>


This means that each one of the "A" symbols in our initial string will be replaced with an "A", with the same logic, each one of the "B" symbols will be replaced with an "AB". Therefore if we apply this rule to our initial string we get:

<p align="center">
  AAABAB
</p>

But nothing is stopping us here, we can do this as many times as we want:

<p align="center">AAAABAAB<br>
AAAAABAAAB<br>
</p>
  
This is exactly what each object from the class "LSystem" in this library do, and although watching a string evolve is all fun and games, we can push this forward and assign each symbol an instruction to draw images.<br>

What kind of instructions can we assign to a string of symbols?, well, Lindenmayer already thought about this, and he imagined a pointer, like a pen on a paper, each symbol tells the hand holding the pen if it should move forward, backward, or rotate. I know that a pen has cylindrical symmetry and that it doesn't really matter if we rotate it, what I mean by a "rotation" in this case, is the direction that "forward" mean, for example, if by "forward" we mean moving north, if I apply a rotation, in the next symbol, by forward I will be referring to west (obviously, we can define different angles of rotations, not just 90 degrees).<br>
<br>
So now that we understand what kind of instructions we should define, let's define them, here we have the set of instructions that the LSystemInterpreter class from this library uses (this is usually the standard way):<br>
<br>
* `F`: Move forward, and draw a line.<br>
* `A`: Move forward, and draw a line (it's useful to be able to do this action with two instructions).<br>
* `+`: Rotate clockwise.<br>
* `-`: Rotate counterclockwise.<br>
* `f`: Move forward, and don't draw a line.<br>
* `B`: Move backward, and draw a line.<br>
* `b`: Move backward, and don't draw a line.<br>
* `[`: Push current state (angle and position) into the stack.<br>
* `]`: Pop current state (angle and position) from the stack.<br>
* Any other symbol: Do nothing. <br>
<br>
Wait why are we talking about stacks all of the sudden?, this is because if we want our instructions to make branches in our drawing, the stack is going to make it much easier, besides, we can define whatever we want.<br>
Let's look at a more graphical example of these L-Sytems, for this we are going to define a L-System that generates a Koch curve, graphically, this is how a Koch curve must be built:

![alt text](https://upload.wikimedia.org/wikipedia/commons/a/a6/Quadratic_Koch_curve_type1_iterations.png)

To do this, here we have our initial string, which is called "axiom", and the rules:<br>
Axiom:<br>
<p align="center">F<p><br>
Rules:<br>
<p align="center">F -> F-F+F+F-F<p><br>


So, what this rule is telling us, is that each line segment `F` gets transformed into a curve of the form `F+F−F−F+F`, we can think about this as if each segment of the Koch curve is transformed into a Koch curve level 2.

# Example images
Here we have some images that can be easly generated using this library.
## Sierpinski triangle
Growing stages of an L-system Sierpinski triangle.
![alt text](https://github.com/julim29/pyLSystem/blob/main/Images/Sierpinski_0.jpg)
![alt text](https://github.com/julim29/pyLSystem/blob/main/Images/Sierpinski_1.jpg)
![alt text](https://github.com/julim29/pyLSystem/blob/main/Images/Sierpinski_2.jpg)
![alt text](https://github.com/julim29/pyLSystem/blob/main/Images/Sierpinski_3.jpg)
