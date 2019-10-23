def area_triangle(a, b, c):
    '''Расчет площади треугольника по фформуле Герона'''
    p = perimeter(a, b, c)
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    return 0.5 * (a + b + c)
