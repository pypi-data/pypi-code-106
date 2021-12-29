from ..compare_objects.CompareObjects import compare_objects


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ NATIVE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def test_two_strings_val_compare():
    assert compare_objects("hello", "hello") is True


def test_two_int_val_compare():
    assert compare_objects(1, 1) is True


def test_two_bool_val_compare():
    assert compare_objects(True, True) is True


def test_two_float_val_compare():
    assert compare_objects(3.33, 3.33) is True


def test_two_strings_val_not_compare():
    assert compare_objects("hello", "hell") is False


def test_two_int_val_not_compare():
    assert compare_objects(1, 2) is False


def test_two_bool_val_not_compare():
    assert compare_objects(True, False) is False


def test_two_float_val_not_compare():
    assert compare_objects(3.33, 3.32) is False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONTAINERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HIGH LEVEL ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# *********** list object ************* #


def test_two_empty_lists():
    assert compare_objects([], []) is True


def test_two_list_val_compare():
    assert compare_objects([1, 2, 3], [1, 2, 3]) is True


def test_two_list_val_not_compare():
    assert compare_objects([1, 2, 3], [1, 2, 4]) is False


def test_two_list_without_same_length():
    assert compare_objects([1], [1, 2]) is False


# *********** tuple object ************* #


def test_two_empty_tuples():
    assert compare_objects((), ()) is True


def test_two_tuple_val_compare():
    assert compare_objects((1, 2, 3), (1, 2, 3)) is True


def test_two_tuple_val_not_compare():
    assert compare_objects((1, 2, 3), (1, 2, 4)) is False


def test_two_tuple_without_same_length():
    assert compare_objects((1,), (1, 2)) is False


# *********** set object ************* #

def test_two_empty_sets():
    assert compare_objects({}, {}) is True


def test_two_set_val_compare():
    assert compare_objects({1, 2, 3}, {1, 2, 3}) is True


def test_two_set_val_not_compare():
    assert compare_objects({1, 2, 3}, {1, 2, 4}) is False


def test_two_set_without_same_length():
    assert compare_objects({1}, {1, 2}) is False


# *********** dict object ************* #

def test_two_empty_dicts():
    assert compare_objects({}, {}) is True


def test_two_dict_val_compare():
    assert compare_objects({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3}) is True


def test_two_dict_val_not_compare_val():
    assert compare_objects({'a': 1, 'b': 5, 'c': 3}, {'a': 1, 'b': 2, 'c': 3}) is False


def test_two_dict_val_not_compare_key():
    assert compare_objects({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'r': 2, 'c': 3}) is False


def test_two_dict_without_same_length():
    assert compare_objects({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2}) is False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ NESTED ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~ EQUAL ALL COMBINATIONS~~~~~~~~~~~~~~~ #


def test_equal_list_in_tuple():
    assert compare_objects(([1, 2], [3, 4]), ([1, 2], [3, 4])) is True


def test_equal_tuple_in_list():
    assert compare_objects([(1, 2), (3, 4)], [(1, 2), (3, 4)]) is True


def test_equal_set_in_list():
    assert compare_objects([{1, 2}, {3, 4}], [{1, 2}, {3, 4}]) is True


def test_equal_list_in_dict():
    assert compare_objects({"a": [1, 2], "b": [3, 4]}, {'a': [1, 2], "b": [3, 4]}) is True


def test_equal_dict_in_list():
    assert compare_objects([{"a": [1, 2], "b": [3, 4]}, 5], [{'a': [1, 2], "b": [3, 4]}, 5]) is True


def test_equal_set_in_tuple():
    assert compare_objects(({1, 2}, {3, 4}), ({1, 2}, {3, 4})) is True


def test_equal_dict_in_tuple():
    assert compare_objects(({'a': 1, 'b': 2}, {'a': 3, 'b': 4}), ({'a': 1, 'b': 2}, {'a': 3, 'b': 4})) is True


def test_equal_tuple_in_dict():
    assert compare_objects({'a': (5, 6), 'b': 2}, {'a': (5, 6), 'b': 2}) is True


def test_equal_list_in_list():
    assert compare_objects([[1, 2], [3, 4]], [[1, 2], [3, 4]]) is True


def test_equal_tuple_in_tuple():
    assert compare_objects(((1, 2), (3, 4)), ((1, 2), (3, 4))) is True


def test_equal_dict_in_dict():
    assert compare_objects({'a': {"in": 4}, 'b': 2}, {'a': {"in": 4}, 'b': 2}) is True


# ~~~~~~~~~~~~~ NOT EQUAL ALL COMBINATIONS~~~~~~~~~~~~~~~ #


def test_not_equal_list_in_tuple():
    assert compare_objects(([1, 2], [3, 4]), ([1, 2], [3, 5])) is False


def test_not_equal_tuple_in_list():
    assert compare_objects([(1, 2), (3, 4)], [(1, 2), (3, 5)]) is False


def test_not_equal_set_in_list():
    assert compare_objects([{1, 2}, {3, 4}], [{1, 2}, {3, 5}]) is False


def test_not_equal_list_in_dict():
    assert compare_objects({"a": [1, 2], "b": [3, 4]}, {'a': [1, 2], "b": [3, 5]}) is False


def test_not_equal_dict_in_list():
    assert compare_objects([{"a": [1, 2], "b": [3, 4]}, 5], [{'a': [1, 2], "b": [3, 4]}, 6]) is False


def test_not_equal_set_in_tuple():
    assert compare_objects(({1, 2}, {3, 4}), ({1, 2}, {3, 5})) is False


def test_not_equal_dict_in_tuple():
    assert compare_objects(({'a': 1, 'b': 2}, {'a': 3, 'b': 4}), ({'a': 1, 'b': 2}, {'a': 3, 'b': 5})) is False


def test_not_equal_tuple_in_dict():
    assert compare_objects({'a': (5, 6), 'b': 2}, {'a': (5, 6), 'b': 5}) is False


def test_not_equal_list_in_list():
    assert compare_objects([[1, 2], [3, 4]], [[1, 2], [3, 5]]) is False


def test_not_equal_tuple_in_tuple():
    assert compare_objects(((1, 2), (3, 4)), ((1, 2), (3, 5))) is False


def test_not_equal_dict_in_dict():
    assert compare_objects({'a': {"in": 4}, 'b': 2}, {'a': {"in": 5}, 'b': 2}) is False


def test_not_equal_dict_in_dict_out():
    assert compare_objects({'a': {"in": 4}, 'b': 2}, {'a': {"in": 4}, 'b': 5}) is False
