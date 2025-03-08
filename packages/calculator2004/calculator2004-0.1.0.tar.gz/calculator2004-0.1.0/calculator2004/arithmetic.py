from dataclasses import dataclass

@dataclass
class Arithmetic:
    _a: float
    _b: float

    def add(self) -> float:
        return self._a + self._b

    def subtract(self) -> float:
        return self._a - self._b

    def multiply(self) -> float:
        return self._a * self._b

    def divide(self) -> float:
        if self._b == 0:
            raise ValueError("Cannot divide by zero")
        return self._a / self._b