import pytest

DICT_FOR_TEST = {1: 'a', 2: 'b', 3: 'c'}

class TestDictionary:

    @staticmethod
    def test_dict_1_copy():
        assert DICT_FOR_TEST == DICT_FOR_TEST.copy()

    @staticmethod
    def test_dict_2_get():
        assert DICT_FOR_TEST.get(1) == 'a'

    @staticmethod
    def test_dict_3_update():
        dict_for_test_copy_t3 = DICT_FOR_TEST.copy()
        dict_for_test_copy_t3.update({4: 'd'})
        assert dict_for_test_copy_t3.get(4) == 'd'

    @staticmethod
    def test_dict_4_keys():
        dict_for_test_copy_t4 = DICT_FOR_TEST.copy()
        assert list(dict_for_test_copy_t4.keys()) == [1, 2, 3]

    @staticmethod
    @pytest.mark.parametrize('id_for_pop', [3, 2, 1])
    def test_dict_5_pop_all(id_for_pop):
        dict_for_test_copy_t5 = DICT_FOR_TEST.copy()
        dict_for_test_copy_t5.pop(id_for_pop)
        assert dict_for_test_copy_t5.get(id_for_pop) is None