from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace('-', '+-')
        fractions = expression.split('+')
        
        result = Fraction(0, 1)
        
        for fraction in fractions:
            if fraction:
                result += Fraction(fraction)
        
        return f"{result.numerator}/{result.denominator}"