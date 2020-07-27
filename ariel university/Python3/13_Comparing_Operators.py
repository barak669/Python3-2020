a = 1
a == 1
True
a = 2
a == 1
False

a == 1 is the same as (a == 1) == True, but a == 1 is more readable, so most of the time we shouldn't write == True anywhere.

a = 1
a == 1
True
(a == 1) == True
True
a = 2
a == 1
False
(a == 1) == True
False

Usage	Description	True examples
a == b	a is equal to b	1 == 1
a != b	a is not equal to b	1 != 2
a > b	a is greater than b	2 > 1
a >= b	a is greater than or equal to b	2 >= 1, 1 >= 1
a < b	a is less than b	1 < 2
a <= b	a is less than or equal to b	1 <= 2, 1 <= 1
We can also combine multiple comparisons. This table assumes that a and b are Booleans.

Usage	Description	True example
a and b	a is True and b is True	1 == 1 and 2 == 2
a or b	a is True, b is True or they're both True	False or 1 == 1, True or True
a=True
b=False
a or b
True
a and b
False