>>> def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)

>>> fact(1)
1
>>> fact(5)
120
>>> fact(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> fact(1000)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fact(1000)
  File "<pyshell#4>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#4>", line 4, in fact
    return n * fact(n - 1)
  File "<pyshell#4>", line 4, in fact
    return n * fact(n - 1)
  [Previous line repeated 989 more times]
  File "<pyshell#4>", line 2, in fact
    if n==1:
RecursionError: maximum recursion depth exceeded in comparison
>>> def fact(n):
    return fact_iter(n, 1)

>>> def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
