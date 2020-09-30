import pytest
import random

def test_list_sort():
    list_example = [random.randint(1, 100) for i in range(2)]
    assert all(list_example[i] == list_example[i] for i in range(2))

class TestEqualMultiple:

    def test_multiple_int(self):
        list_example = [1, 'i']
        assert type(list_example*random.randint(-1, 1)).__name__ == 'list'

    def test_multiple_not_int(self):
        list_example = [1, 'i']
        with pytest.raises(TypeError):
            assert list_example*0.1

def test_list_concatenation():
    list_1 = [1]
    list_2 = ['i']
    assert list_1 + list_2 == [1, 'i']

@pytest.mark.parametrize('i', [0, 1, 2, 3])
def test_list_index(i):
    list_example = [0, 1, 2, 3]
    assert list_example[i] == i


