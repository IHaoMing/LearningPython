>>> def power(x):
	return x*x

>>> power(5)
25
>>> power(15)
225
>>> def power(x, n)
SyntaxError: invalid syntax
>>> def power(x, n):
	s = 1
	while n>0:
		n =  n-1
		s = s*x
	return s

>>> power(5, 2)
25
>>> power(5, 3)
125
>>> def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

>>> power(5)
25
>>> power(5, 2)
25
>>> power(5, 3)
125
>>> def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

    
>>> def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

    
>>> enroll('Sarah', 'F')
name: Sarah
gender: F
age: 6
city: Beijing
>>> def add_end(L=[]):
    L.append('END')
    return L

>>> 
>>> add_end([1, 2, 3])
[1, 2, 3, 'END']
>>> add_end(['x', 'y', 'z'])
['x', 'y', 'z', 'END']
>>> add_end()
['END']
>>> 
