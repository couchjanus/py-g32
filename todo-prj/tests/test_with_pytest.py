# test_with_pytest.py
import pytest

def test_always_passes():
   assert True

@pytest.mark.skip()
def test_always_fails():
   assert False

