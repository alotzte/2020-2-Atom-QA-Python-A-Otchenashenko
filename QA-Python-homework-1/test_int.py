import pytest

def test_int_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        assert 1/0

class Test_add_and_multiplicate:
    def test_int_addition(self):
        assert 1 + 1 == 2 and -1 + -1 == -2

    def test_int_multiplication(self):
        assert 2 * 3 == 6 and 0 * 1 == 0

@pytest.mark.parametrize('equation, result', [('1/1', 1),
                                              ('-10/5', -2),
                                              ('-10/-2', 5)
                                              ])
def test_int_division(equation, result):
    assert eval(equation) == result

def test_int_sign_change():
    assert (-1)*(-1) == 1