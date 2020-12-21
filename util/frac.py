from fractions import Fraction


def pretty_fractions():
    """Monkey patch fractions to look nicer when printed out"""
    def fraction__repr__(self):
        if self.numerator == 0:
            return '0'
        elif self.denominator == 1:
            return f'{self.numerator}'
        else:
            return f'{self.numerator}/{self.denominator}'
    setattr(Fraction, '__repr__', fraction__repr__)
