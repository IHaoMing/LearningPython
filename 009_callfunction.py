>>> abs(100)
100
>>> abs(-20)
20
>>> abs(12.34)
12.34
>>> abs(1,2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    abs(1,2)
TypeError: abs() takes exactly one argument (2 given)
>>> abs('a')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    abs('a')
TypeError: bad operand type for abs(): 'str'
>>> max(1, 2)
2
>>> min(1, 2)
1
>>> int('123')
123
>>> int(12.34)
12
>>> str(1.23)
'1.23'
>>> str(100)
'100'
>>> bool(1)
True
>>> bool(' ')
True
>>> bool('')
False
>>> n1 = 255
>>> n2 = 1000
>>> n1 = hex(255)
>>> n1
'0xff'
>>> 
>>> n2 = hex(n2)
>>> n2
'0x3e8'
>>> 
