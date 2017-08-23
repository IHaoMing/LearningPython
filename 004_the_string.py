>>> print('包含中文的str')
包含中文的str
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
>>> '\u4e2d\u6587'
'中文'
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    '中文'.encode('ascii')
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
SyntaxError: multiple statements found while compiling a single statement
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

'中文'
>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
>>> 'Hello,%s'%'world'
'Hello,world'
>>> 'Hi %s,you have %d.'%('Michael',1000000)
'Hi Michael,you have 1000000.'
>>> '%2d-%02d'%(3, 1)
' 3-01'
>>> '%.2f'%3.1415926
'3.14'
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
>>> s1 = 72
>>> s2 = 85
>>> r = s1 * s2
>>> r = (s2-s1)/s1
>>> print('%.1f'%r)
0.2
>>> 
