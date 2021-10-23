# pyLSystem
Python library designed to build fractals from L-systems.

# What are L-systems?
L-systems consist of a string of symbols that have a determined rule to calculate a new string of symbols, which will be the new state of this system, and each symbol can be interpreted as an instruction to draw an image.<br>
Let's look at an example to understand it better.<br>
Suppose that we start with the following string:<br>

AABB

And that we have this set of rules:<br>

A -> A

B -> AB

So, this means that each one of the "A" symbols in our initial string will be replaced with an "A", with the same logic, each one of the "B" symbols will be replaced with an "AB". Therefore if we apply this rule to our initial string we get:

AAABAB

But nothing is stopping us here, we can do this as many times as we want:

AAAABAAB<br>
AAAAABAAAB<br>

This is exactly what each object from the class "LSystem" in this library do, and although watching a string evolve is all fun and games, we can push this forward and assign each symbol an instruction to draw images.<br>

What kind of instructions can we assign to a string of symbols?, well, Lindenmayer already thought about this, and he imagined a pointer, like a pen on a paper, each symbol tells the hand holding the pen if it should move forward, backward, or rotate. I know that a pen has cylindrical symmetry and that it doesn't really matter if we rotate it, what I mean by a "rotation" in this case, is the direction that "forward" mean, for example, if by "forward" we mean moving north, if I apply a rotation, in the next symbol, by forward I will be refering to west (obviously that we can define rotations different than just 90 degrees).<br>
<br>
So now that we understand what kind of instructions we should define, let's define them, here we have the set of instructions that the LSystemInterpreter class from this library uses:<br>
<br>
F: Move forward, and draw a line.<br>
A: Move forward, and draw a line (it's useful to be able to do this action with two instructions).<br>
+: Rotate clockwise.<br>
-: Rotate counterclockwise.<br>
f: Move forward, and don't draw a line.<br>
B: Move backward, and draw a line.<br>
b: Move backward, and don't draw a line.<br>
[: Push current state (angle and position) into the stack.<br>
]: Pop current state (angle and position) from the stack.<br>

Wait why are we talking about stacks all of the sudden?, this is because if we want our instructions to make branches in our drawing, the stack is going to make it much easier, besides, we can define whatever we want.<br>
Let's look at a more graphical example of these L-Sytems.

# Example images
# Sierpinski triangle
![alt text](https://github.com/julim29/pyLSystem/blob/main/Images/Sierpinski_0.jpg)
![alt text](https://github.com/julim29/pyLSystem/blob/main/Images/Sierpinski_1.jpg)
![alt text](https://github.com/julim29/pyLSystem/blob/main/Images/Sierpinski_2.jpg)
![alt text](https://github.com/julim29/pyLSystem/blob/main/Images/Sierpinski_3.jpg)
