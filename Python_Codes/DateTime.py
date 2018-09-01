Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> from datetime import date
>>> today = date.today()
>>> print(today)
2017-08-19
>>> print(today.day + " " + today.month + " " + today.year)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(today.day + " " + today.month + " " + today.year)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(today.day,today.month,today.year)
19 8 2017
>>> today.weekday
<built-in method weekday of datetime.date object at 0x025022A8>
>>> today.weekday()
5
>>> today.year
2017
>>> import datetime
>>> datetime.time
<class 'datetime.time'>
>>> datetime.date
<class 'datetime.date'>
>>> datetime.timezone
<class 'datetime.timezone'>
>>> from datetime import datetime
>>> datetime.now
<built-in method now of type object at 0x1D2EA940>
>>> datetime.now()
datetime.datetime(2017, 8, 19, 19, 19, 12, 63597)
>>> today = datetime.now()
>>> print(today)
2017-08-19 19:19:58.521390
>>> print(today.time)
<built-in method time of datetime.datetime object at 0x02CF4290>
>>> print(today.time())
19:19:58.521390
>>> t = datetime.time(datetime.now())
>>> print(t)
19:21:34.474497
>>> now = datetime.now()
>>> now
datetime.datetime(2017, 8, 19, 22, 20, 29, 568011)
>>> print(now)
2017-08-19 22:20:29.568011
>>> now.strftime("%y")
'17'
>>> now.strftime("%Y")
'2017'
>>> now.strftime("%a %D %b %y")
'Sat 08/19/17 Aug 17'
>>> now.strftime("%a")
'Sat'
>>> now.strftime("%A")
'Saturday'
>>> now.strftime("%d")
'19'
>>> now.strftime("%D")
'08/19/17'
>>> now.strftime("%b")
'Aug'
>>> now.strftime("%B")
'August'
>>> now.strftime("%x")
'08/19/17'
>>> now.strftime("%X")
'22:20:29'
>>> now.strftime("%c")
'Sat Aug 19 22:20:29 2017'
>>> now.strftime("%i")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    now.strftime("%i")
ValueError: Invalid format string
>>> now.strftime("%I")
'10'
>>> now.strftime("%I %M")
'10 20'
>>> now.strftime("%I:%M:%S: %p")
'10:20:29: PM'
>>> now.strftime("%I:%M:%S: %p")
'10:20:29: PM'
>>> now = datetime.now()
>>> now.strftime("%I:%M:%S: %p")
'10:25:24: PM'
>>> now.strftime("%H:%M:%S: %p")
'22:25:24: PM'
>>> 
