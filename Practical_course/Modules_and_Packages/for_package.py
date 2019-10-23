from Geometric_formulas.Circle import Circle_area as CA
from Geometric_formulas.Triangle import area_tr as AT

print('Площадь окружности диаметром 10 м составляет {:.2f} кв.м'.format(CA.circle_ar(10)))
print('Треугольник имеет следующие размеры сторон: 10, 3, 8')
print('По формуле Герона его площадь будет составлять {:.2f}'.format(AT.area_triangle(10, 3, 8)))
