>>> names = ['Michael', 'Bob', 'Tracy']
>>> scores = [95, 75, 85]
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
>>> d['Adam'] = 67
>>> d['Adam']
67
>>> d['Jack'] = 90
>>> d['Jack']
90
>>> d['Jack'] = 88
>>> d['Jack']
88
>>> d['dad']
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d['dad']
KeyError: 'dad'
>>> 'daf' in d
False
>>> d.get('daf')
>>> d.get('dad', -1)
-1
>>> d.pop('Bob')
75
>>> d
{'Michael': 95, 'Tracy': 85, 'Adam': 67, 'Jack': 88}
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}
>>> s.remove(4)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.remove(4)
KeyError: 4
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.remove(4)
>>> s
{1, 2, 3}
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> s
{1, 2, 3}
>>> a
['a', 'b', 'c']
>>> a = 'abc'
>>> a.replace('a', 'A')
'Abc'
>>> a
'abc'
>>> b = replace('a', 'A')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b = replace('a', 'A')
NameError: name 'replace' is not defined
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'
