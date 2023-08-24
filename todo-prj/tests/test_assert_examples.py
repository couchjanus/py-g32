# test_assert_examples.py

# Якщо умова assert вірна, то нічого не відбувається, 
# і програма продовжує своє нормальне виконання. 

def test_passing():
	assert (1, 2, 3) == (1, 2, 3)

number = 42
# У цьому випадку програма продовжує своє нормальне виконання. 
assert number > 0, f"number greater than 0 expected, got: {number}"

# Хибний вираз number > 0 робить assert невдалим, викликаючи помилку 
# AssertionError і перериваючи виконання програми.
# assert number < 0

# Щоб зробити ваші твердження зрозумілими для інших розробників, 
# рекомендовано додати описове повідомлення про твердження: 

# assert number < 0, f"number greater than 0 expected, got: {number}"

def test_uppercase():
	assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
	assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
	assert 37 in {
       num
       for num in range(2, 50)
       if not any(num % div == 0 for div in range(2, num))
   }
