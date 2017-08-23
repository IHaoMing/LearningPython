>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']
>>> len(classmates)
3
>>> classmates[0]
'Michael'
>>> classmates[1]
'Bob'
>>> classmates[2]
'Tracy'
>>> classmates[3]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    classmates[3]
IndexError: list index out of range
>>> classmates[-]
SyntaxError: invalid syntax
>>> classmates[-1]
'Tracy'
>>> calssmates[-2]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    calssmates[-2]
NameError: name 'calssmates' is not defined
>>> classmates[-2]
'Bob'
>>> classmates[3]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    classmates[3]
IndexError: list index out of range
>>> classmates.append('Adam')
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Bob', 'Tracy']
>>> classmates.pop(1)
'Bob'
>>> classmates[1] = 'Sarah'
>>> classmates
['Michael', 'Sarah']
>>> ca
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ca
NameError: name 'ca' is not defined
>>> 
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
>>> L = []
>>> len(L)
0
>>> classmates = ('Michael', 'Bob', 'Tracy')
>>> classmates
('Michael', 'Bob', 'Tracy')
>>> t = (1,2)
>>> t
(1, 2)
>>> t = ()
>>> t
()
>>> t = ('a', 'b', ['A', 'B'])
>>> t
('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
>>> L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
>>> print(L[0][0])
Apple
>>> print(L[1][1])
Python
>>> print(L[2][2])
Lisa
