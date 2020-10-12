import random
import pytest

SET_FOR_TEST1 = {1, 2, 3}
SET_FOR_TEST2 = {4, 5}


class TestSet:

    @staticmethod
    def test_set_1_len():
        assert len(SET_FOR_TEST1) == 3

    @staticmethod
    def test_set_2_repeat_an_element():
        assert SET_FOR_TEST1.isdisjoint(SET_FOR_TEST2)

    @staticmethod
    def test_set_3_copy():
        set_for_test1_copy_t_4 = SET_FOR_TEST1.copy()
        assert set_for_test1_copy_t_4 == SET_FOR_TEST1

    @staticmethod
    def test_set_4_add():
        set_for_test1_copy_t4 = SET_FOR_TEST1.copy()
        set_for_test1_copy_t4.add(random.randint(10, 11))
        assert (len(set_for_test1_copy_t4)) == (len(SET_FOR_TEST1) + 1)

    @staticmethod
    @pytest.mark.parametrize('set_for_test_5', [{1, 2, 3, 4, 5},
                                                {1, 2, 3, 4, 5, 6}])
    def test_set_5_subset(set_for_test_5):
        assert set_for_test_5 >= SET_FOR_TEST1