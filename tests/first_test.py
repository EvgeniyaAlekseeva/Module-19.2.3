import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculation_correctly(self):
        assert self.calc.multiply(self, 5, 3) == 15

    def test_adding_calculation_correctly(self):
        assert self.calc.adding(self, 81, 4) == 85

    def test_division_correctly(self):
        assert self.calc.division(self, 49, 7) == 7

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 16, 0) == 16
