from PyGameInterpreter import PyGameInterpreter
from LSystem import LSystem
import pygame
import pygame.locals

def main():
    my_system = LSystem()
    my_system.axiom = 'F'
    my_system.rules['A'] = 'F+A+F'
    my_system.rules['F'] = 'A-F-A'

    my_system.next(5)

    pygame.display.set_mode(size=(1000, 1000))
    surface = pygame.display.get_surface()

    interpreter = PyGameInterpreter(surface=surface,
                                    line_width=2.0,
                                    step_size=5.0,
                                    angular_step_size=60.0,
                                    start_pos=(500, 500))

    interpreter.compile(my_system.state)

    pygame.image.save(surface, "fractal.jpg")

if __name__ == '__main__':
    main()