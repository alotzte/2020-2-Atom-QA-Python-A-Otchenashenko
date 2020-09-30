import pytest
import random

def test_dict_update():
    dict_example = {'animal': 'dog'}
    len_before = len(dict_example)
    dict_example.update({'breed': 'husky'})
    assert len(dict_example)-1 == len_before

@pytest.fixture(scope='class')
def random_dict():
    dictionary = {}
    for i in range(random.randint(1, 5)):
        key = ''.join([chr(random.randint(1, 100)) for j in range(i)])
        dictionary[key] = random.randint(-100, 100)
    return dictionary

class TestDictMeth:

    def test_dict_copy(self, random_dict):
        copy_of_dict = random_dict.copy()
        assert copy_of_dict == random_dict

    def test_dict_get(self):
        dict_example = {'a': 1}
        assert dict_example.get('a') == 1

@pytest.mark.parametrize('str_num', ['1', '2', '3'])
def test_dict_key_to_value(str_num):
    dict_example = {'1': 1, '2': 2, '3': 3}
    assert dict_example[str_num] == int(str_num)
