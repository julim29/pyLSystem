from typing import List, Tuple
from abc import ABC, abstractmethod
import math


def polar_to_cart(theta: float, r: float, off: Tuple[float, float]) -> Tuple[float, float]:
    off_x, off_y = off
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return x+off_x, y+off_y


def cart_to_polar(pos: Tuple[float, float]) -> Tuple[float, float]:
    x, y = pos
    theta, r = math.degrees(math.atan(y / x)), math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return theta, r


class LSystemInterpreter(ABC):
    """This abstract base class has all the logic behind the interpretation of an LSystem generated string,
    the function _drawline has to be implemented to start working. """
    # Static variables during interpretation
    step_size: float
    start_pos: Tuple[float, float]
    start_angle: float
    angular_step_size: float

    # Dynamic variables during interpretation (updatable)
    angle: float
    stack: List[Tuple[Tuple[float, float], float]]
    current_pos: Tuple[float, float]
    previous_pos: Tuple[float, float]
    current_char: str

    def __init__(self, start_pos: Tuple[float, float] = (0, 0), step_size: float = 1.0, start_angle: float = 0.0,
                 angular_step_size: float = 90.0):
        """This constructor need the following arguments:
        start_pos: The starting postion of the cursor.
        step_size: The distance that the cursor travels during each step.
        start_angle: The initial angle where the cursor is pointing.
        angular_step_size: The angle in degrees that the cursor rotates during each step."""
        self.start_pos = start_pos
        self.start_angle = start_angle
        self.step_size = step_size
        self.angular_step_size = angular_step_size

        self.instruction_map = {
            'F': (self._forward, self._drawline),
            'A': (self._forward, self._drawline),
            '+': (self._clockwise,),
            '-': (self._counterclockwise,),
            'f': (self._forward,),
            'B': (self._backward, self._drawline),
            'b': (self._backward,),
            '[': (self._push,),
            ']': (self._pop,)
        }

    def compile(self, state: str) -> None:
        """This method interprets the state argument as an LSystem generated string with the following instructions:

        F: Move forward, and draw a line.
        A: Move forward, and draw a line (it's useful to be able to do this action with two instructions).
        +: Rotate clockwise.
        -: Rotate counterclockwise.
        f: Move forward, and don't draw a line.
        B: Move backward, and draw a line.
        b: Move backward, and don't draw a line.
        [: Push current state (angle and position) into the stack.
        ]: Pop current state (angle and position) from the stack."""

        # Initialization
        self.angle = self.start_angle
        self.stack = []
        self.current_pos = self.start_pos
        self.previous_pos = self.start_pos

        for c in state:
            self.current_char = c
            if c in self.instruction_map:
                for instruction in self.instruction_map[c]:
                    instruction()

    def _forward(self):
        self.previous_pos = self.current_pos
        self.current_pos = polar_to_cart(self.angle, self.step_size, self.previous_pos)

    def _backward(self):
        self.previous_pos = self.current_pos
        self.current_pos = polar_to_cart(self.angle, -self.step_size, self.previous_pos)

    def _clockwise(self):
        self.angle += self.angular_step_size

    def _counterclockwise(self):
        self.angle -= self.angular_step_size

    def _push(self):
        self.stack.append((self.current_pos, self.angle))

    def _pop(self):
        (self.current_pos, self.angle) = self.stack.pop()

    @abstractmethod
    def _drawline(self):
        """This draws a line between the current position and the previous position.
        This method has to be implemented by a subclass, the necessary parameters to get this to work are:

        self.previous_pos: This has a tuple representing the x, y value of the previous position.
        self.current_pos: This has a tuple representing the x, y value of the current position."""
        pass