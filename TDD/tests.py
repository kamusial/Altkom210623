from functions import *
#import functions

# def tests_add():
#     assert add(3, 7) == 10
#
#
# def tests_multiplication_basic():
#     assert multiplication(3, 5) == 15
#     assert multiplication(3, 10) == 30
#
#
# def tests_multiplication_advanced():
#     assert multiplication(100, 1.1) == 110
#     assert multiplication(3, 'Anna') == 'AnnaAnnaAnna'
#     assert multiplication(3, 3.5) == 10
#     assert multiplication(5, -3) == 0


def test_fissbuzz_basic():
    assert fissbuzz(1) == 1
    assert fissbuzz(2) == 2
    assert fissbuzz(3) == 'fiss'
    assert fissbuzz(4) == 4
    assert fissbuzz(5) == 'buzz'
    assert fissbuzz(6) == 'fiss'
    assert fissbuzz(10) == 'buzz'
    assert fissbuzz(15) == 'fissbuzz'

def test_fissbuzz_advanced():
    assert fissbuzz(0) == 0
    assert fissbuzz(-1) == 0
    assert fissbuzz('Mama') == 0
    assert fissbuzz(4.7) == 'buzz'





