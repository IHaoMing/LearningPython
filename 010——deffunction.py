>>> def my_abs(x):
	if x>= 0:
		return x
	else:
		return -x

	
>>> my_abs(6)
6
>>> my_abs(-9)
9
>>> def nop():
	pass

>>> if age >= 18:
	pass

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    if age >= 18:
NameError: name 'age' is not defined
>>> def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

>>> my_abs('A')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    my_abs('A')
  File "<pyshell#15>", line 3, in my_abs
    raise TypeError('bad operand type')
TypeError: bad operand type
>>> import math
>>> def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

>>> x, y = move(100, 100, 60, math.pi / 6)
>>> print(x, y)
151.96152422706632 70.0
>>> r = move(100, 100, 60, math.pi/6)
>>> r
(151.96152422706632, 70.0)
>>> 
