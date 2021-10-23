from typing import Dict


class LSystem:
    """
    This class is used to represent LSystems, this keeps track of the axiom, the state, and the rules of the LSystem
    in addition to providing useful methods to evaluate its evolution.

    Attributes:
        state: String that represents the current state of the system.
        rules: Dictionary that represents the update rule of the system. E.g.: system.rule['A'] = 'F'
        axiom: String that represents the initial state of the system. E.g.: system.axiom = 'F[F]A'
    """

    state: str
    rules: Dict[str, str]
    _axiom: str

    def __init__(self):
        self.rules = {}
        self._axiom = ''

    def reset(self) -> None:
        """Resets the LSystem to its initial state (the axiom)."""
        self.state = self._axiom

    @property
    def axiom(self) -> str:
        """Initial state of the LSystem."""
        return self._axiom

    @axiom.setter
    def axiom(self, axiom: str) -> None:
        self._axiom = axiom
        self.state = axiom

    def _apply_rule(self):
        new_seq = ""

        for c in self.state:
            new_seq = new_seq + self.rules.get(c, c)

        self.state = new_seq

    def next(self, iterations: int = 1) -> None:
        """Updates the state of the system by the amount of iterations passed into this function, by default this is
        1. """
        for _ in range(iterations):
            self._apply_rule()

    def __str__(self):
        return f"""LSystem:
    Axiom: {self.axiom}
    Rules: {self.rules}
    State: {self.state}"""
