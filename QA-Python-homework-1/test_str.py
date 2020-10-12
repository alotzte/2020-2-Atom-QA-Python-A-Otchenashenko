import pytest

STR_FOR_TEST = " Ququshka "
STR_FOR_TEST_T5 = STR_FOR_TEST


class TestString:

    @staticmethod
    def test_str_3_len():
        assert len(STR_FOR_TEST) == 10

    @staticmethod
    def test_str_2_strip():
        str_for_test_copy_t2 = STR_FOR_TEST
        assert len(str_for_test_copy_t2.strip()) == 8
        assert str_for_test_copy_t2.strip()[0] != " "
        assert str_for_test_copy_t2.strip()[7] != " "
        with pytest.raises(IndexError):
            assert str_for_test_copy_t2.strip()[9] != " "

    @staticmethod
    def test_str_3_lower():
        str_for_test_copy_t3 = STR_FOR_TEST
        assert str_for_test_copy_t3.strip().lower()[0] == 'q'

    @staticmethod
    def test_str_4_sum():
        str_for_test_copy_t4 = STR_FOR_TEST
        assert len(str_for_test_copy_t4 + str_for_test_copy_t4) == len(
            str_for_test_copy_t4) * 2

    @staticmethod
    @pytest.mark.parametrize('i', list(range(len(STR_FOR_TEST_T5.strip()))))
    def test_str_5_upper(i):
        assert STR_FOR_TEST_T5.strip().upper()[i].isupper()