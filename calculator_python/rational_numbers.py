from fractions import Fraction


def irrattional_operation(a: str, b: str, operator):
    f_a = Fraction(a)   # fract_a
    f_b = Fraction(b)   # fract_b
    return f_a+f_b if operator == '+' else f_a-f_b if operator == '-' \
        else f_a*f_b if operator == '*' else f_a/f_b if operator == '/' else False

# print(irrattional_operation('4/5', '10/25', '-'))
