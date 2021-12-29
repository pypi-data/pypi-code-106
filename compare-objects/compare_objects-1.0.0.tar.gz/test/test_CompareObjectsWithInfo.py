from ..compare_objects.CompareObjectsWithInfo import compare_objects_with_info


# ######################### WITH INFORMATION ######################### #

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ NATIVE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


def test_two_strings_val_compare_with_info():
    assert compare_objects_with_info("hello", "hello")[0] is True


def test_two_int_val_compare_with_info():
    assert compare_objects_with_info(1, 1)[0] is True


def test_two_bool_val_compare_with_info():
    assert compare_objects_with_info(True, True)[0] is True


def test_two_float_val_compare_with_info():
    assert compare_objects_with_info(3.33, 3.33)[0] is True


def test_two_strings_val_not_compare_with_info():
    assert compare_objects_with_info("hello", "hell")[0] is False


def test_two_int_val_not_compare_with_info():
    assert compare_objects_with_info(1, 2)[0] is False


def test_two_bool_val_not_compare_with_info():
    assert compare_objects_with_info(True, False)[0] is False


def test_two_float_val_not_compare_with_info():
    assert compare_objects_with_info(3.33, 3.32)[0] is False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONTAINERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HIGH LEVEL ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# *********** list object ************* #


def test_two_empty_lists_with_info():
    assert compare_objects_with_info([], [])[0] is True


def test_two_list_val_compare_with_info():
    assert compare_objects_with_info([1, 2, 3], [1, 2, 3])[0] is True


def test_two_list_val_not_compare_with_info():
    assert compare_objects_with_info([1, 2, 3], [1, 2, 4])[0] is False


def test_two_list_without_same_length_with_info():
    assert compare_objects_with_info([1], [1, 2])[0] is False


# *********** tuple object ************* #


def test_two_empty_tuples_with_info():
    assert compare_objects_with_info((), ())[0] is True


def test_two_tuple_val_compare_with_info():
    assert compare_objects_with_info((1, 2, 3), (1, 2, 3))[0] is True


def test_two_tuple_val_not_compare_with_info():
    assert compare_objects_with_info((1, 2, 3), (1, 2, 4))[0] is False


def test_two_tuple_without_same_length_with_info():
    assert compare_objects_with_info((1,), (1, 2))[0] is False


# *********** set object ************* #

def test_two_empty_sets_with_info():
    assert compare_objects_with_info({}, {})[0] is True


def test_two_set_val_compare_with_info():
    assert compare_objects_with_info({1, 2, 3}, {1, 2, 3})[0] is True


def test_two_set_val_not_compare_with_info():
    assert compare_objects_with_info({1, 2, 3}, {1, 2, 4})[0] is False


def test_two_set_without_same_length_with_info():
    assert compare_objects_with_info({1}, {1, 2})[0] is False


# *********** dict object ************* #

def test_two_empty_dicts_with_info():
    assert compare_objects_with_info({}, {})[0] is True


def test_two_dict_val_compare_with_info():
    assert compare_objects_with_info({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3})[0] is True


def test_two_dict_val_not_compare_val_with_info():
    assert compare_objects_with_info({'a': 1, 'b': 5, 'c': 3}, {'a': 1, 'b': 2, 'c': 3})[0] is False


def test_two_dict_val_not_compare_key_with_info():
    assert compare_objects_with_info({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'r': 2, 'c': 3})[0] is False


def test_two_dict_without_same_length_with_info():
    assert compare_objects_with_info({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2})[0] is False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ NESTED ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~ EQUAL ALL COMBINATIONS~~~~~~~~~~~~~~~ #


def test_equal_list_in_tuple_with_info():
    assert compare_objects_with_info(([1, 2], [3, 4]), ([1, 2], [3, 4]))[0] is True


def test_equal_tuple_in_list_with_info():
    assert compare_objects_with_info([(1, 2), (3, 4)], [(1, 2), (3, 4)])[0] is True


def test_equal_set_in_list_with_info():
    assert compare_objects_with_info([{1, 2}, {3, 4}], [{1, 2}, {3, 4}])[0] is True


def test_equal_list_in_dict_with_info():
    assert compare_objects_with_info({"a": [1, 2], "b": [3, 4]}, {'a': [1, 2], "b": [3, 4]})[0] is True


def test_equal_dict_in_list_with_info():
    assert compare_objects_with_info([{"a": [1, 2], "b": [3, 4]}, 5], [{'a': [1, 2], "b": [3, 4]}, 5])[0] is True


def test_equal_set_in_tuple_with_info():
    assert compare_objects_with_info(({1, 2}, {3, 4}), ({1, 2}, {3, 4}))[0] is True


def test_equal_dict_in_tuple_with_info():
    assert compare_objects_with_info(({'a': 1, 'b': 2}, {'a': 3, 'b': 4}), ({'a': 1, 'b': 2}, {'a': 3, 'b': 4}))[
               0] is True


def test_equal_tuple_in_dict_with_info():
    assert compare_objects_with_info({'a': (5, 6), 'b': 2}, {'a': (5, 6), 'b': 2})[0] is True


def test_equal_list_in_list_with_info():
    assert compare_objects_with_info([[1, 2], [3, 4]], [[1, 2], [3, 4]])[0] is True


def test_equal_tuple_in_tuple_with_info():
    assert compare_objects_with_info(((1, 2), (3, 4)), ((1, 2), (3, 4)))[0] is True


def test_equal_dict_in_dict_with_info():
    assert compare_objects_with_info({'a': {"in": 4}, 'b': 2}, {'a': {"in": 4}, 'b': 2})[0] is True


# ~~~~~~~~~~~~~ NOT EQUAL ALL COMBINATIONS~~~~~~~~~~~~~~~ #


def test_not_equal_list_in_tuple_with_info():
    assert compare_objects_with_info(([1, 2], [3, 4]), ([1, 2], [3, 5]))[0] is False


def test_not_equal_tuple_in_list_with_info():
    assert compare_objects_with_info([(1, 2), (3, 4)], [(1, 2), (3, 5)])[0] is False


def test_not_equal_set_in_list_with_info():
    assert compare_objects_with_info([{1, 2}, {3, 4}], [{1, 2}, {3, 5}])[0] is False


def test_not_equal_list_in_dict_with_info():
    assert compare_objects_with_info({"a": [1, 2], "b": [3, 4]}, {'a': [1, 2], "b": [3, 5]})[0] is False


def test_not_equal_dict_in_list_with_info():
    assert compare_objects_with_info([{"a": [1, 2], "b": [3, 4]}, 5], [{'a': [1, 2], "b": [3, 4]}, 6])[0] is False


def test_not_equal_set_in_tuple_with_info():
    assert compare_objects_with_info(({1, 2}, {3, 4}), ({1, 2}, {3, 5}))[0] is False


def test_not_equal_dict_in_tuple_with_info():
    assert compare_objects_with_info(({'a': 1, 'b': 2}, {'a': 3, 'b': 4}), ({'a': 1, 'b': 2}, {'a': 3, 'b': 5}))[
               0] is False


def test_not_equal_tuple_in_dict_with_info():
    assert compare_objects_with_info({'a': (5, 6), 'b': 2}, {'a': (5, 6), 'b': 5})[0] is False


def test_not_equal_list_in_list_with_info():
    assert compare_objects_with_info([[1, 2], [3, 4]], [[1, 2], [3, 5]])[0] is False


def test_not_equal_tuple_in_tuple_with_info():
    assert compare_objects_with_info(((1, 2), (3, 4)), ((1, 2), (3, 5)))[0] is False


def test_not_equal_dict_in_dict_with_info():
    assert compare_objects_with_info({'a': {"in": 4}, 'b': 2}, {'a': {"in": 5}, 'b': 2})[0] is False


def test_not_equal_dict_in_dict_out_with_info():
    assert compare_objects_with_info({'a': {"in": 4}, 'b': 2}, {'a': {"in": 4}, 'b': 5})[0] is False
