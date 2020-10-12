import random
import math
import pytest


class TestInt:

    @staticmethod
    def test_int_1_sum():
        assert 1 + 1 == 2

    @staticmethod
    def test_int_2_pow():
        assert pow(random.randint(2, 5), 0) == 1

    @staticmethod
    def test_int_3_sqrt():
        with pytest.raises(ValueError):
            assert math.sqrt(-1)

    @staticmethod
    def test_int_4_abs():
        assert abs(-1) == 1

    @staticmethod
    @pytest.mark.parametrize('i', [random.randint(3, 5),
                                   random.randint(6, 10)])
    def test_int_5_more(i):
        assert i > 2