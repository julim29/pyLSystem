from typing import Tuple, Union
import pygame
from LSystemInterpreter import LSystemInterpreter


def float_tuple_to_int_tuple(input_tuple: Tuple[float, float]) -> Union[Tuple[int, int], Tuple[int, ...]]:
    return tuple([int(value) for value in input_tuple])


class PyGameInterpreter(LSystemInterpreter):
    """This class creates interpreters that draw the representation of a LSystem state into a pygame surface."""
    surface: pygame.surface
    line_width: float
    color: Tuple[int, int, int]

    def __init__(self, surface: pygame.surface, line_width: float = 1.0, color: Tuple[int, int, int] = (255, 255, 255),
                 **kwargs):
        self.surface = surface
        self.line_width = line_width
        self.color = color
        super().__init__(**kwargs)

    def _drawline(self):
        pygame.draw.line(self.surface,
                         self.color,
                         float_tuple_to_int_tuple(self.previous_pos),
                         float_tuple_to_int_tuple(self.current_pos),
                         int(self.line_width))
