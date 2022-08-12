from ast import Num


def test_uppercase():
    assert "loud noise".upper() == "LOUD NOISE"


def test_reversed():
    assert list(reversed([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]


def test_some_primes():
    assert 37 in {
        number
        for number in range(2, 50)
        if not any(number % div == 0 for div in range(2, number))
    }