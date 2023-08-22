def ass_sum():
   """
   >>> assert sum([1, 2, 3]) == 6
   >>> assert sum([1, 2, 3]) == 6, "Should be 6"
   """
#    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
   """
   >>> assert sum((1, 2, 2)) == 6, "Should be 6"
   Traceback (most recent call last):
       ...
   AssertionError: Should be 6
   
   >>> assert sum((2, 2, 2)) == 6, "Should be 6"
   """
#    assert sum((2, 2, 2)) == 6, "Should be 6"

def test_sum():
   """потрібно перевірити вихід sum() на відомий результат.
   >>> sum([1, 2, 3])
   6
   >>> sum([100, 200, 300])
   600
   перевірити, що sum() чисел (1, 2, 3) дорівнює 6:
   >>> assert sum([1, 2, 3]) == 6
   >>> ass_sum()
   test_sum_tuple()
   """
if __name__ == "__main__":
   import doctest
   doctest.testmod()
