from ft_package import unique_elements, flatten_list, reverse_string


def test_unique_elements():
    """test for function unique_elements"""
    assert unique_elements([1, 2, 2, 3]) == [1, 2, 3]
    assert unique_elements([]) == []
    assert unique_elements(["a", "b", "a"]) == ["a", "b"]


def test_flatten_list():
    """test for function flatten_list"""
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([]) == []
    assert flatten_list([[1], [2, 3], [4]]) == [1, 2, 3, 4]


def test_reverse_string():
    """test for function reverse_string"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("Python") == "nohtyP"


test_unique_elements()
test_flatten_list()
test_reverse_string()
print("All utility function tests passed!")
