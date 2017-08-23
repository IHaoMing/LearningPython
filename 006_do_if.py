>>> age = 20
>>> if age >= 18:
    print('your age is', age)
    print('adult')

    
your age is 20
adult
>>> age = 3
>>> if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

    
your age is 3
teenager
>>> if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

    
kid
>>> age = 20
>>> if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

    
teenager
>>> birth = input('birth: ')
birth: 1998
>>> if birth < 2000:
    print('00前')
else:
    print('00后')

    
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    if birth < 2000:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> s = input('birth: ')
birth: 1998
>>> birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
    
