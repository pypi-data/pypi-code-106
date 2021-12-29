# ******************************* compare_object.py ********************************* #
#                                                                                     #
#   compare_object.py -                                                               #
#                                                                                     #
#       Description:                                                                  #
#                                                                                     #
#           This component, is able to compare any two object, nested and             #
#           not nested, and gives a simple result == True or False.                   #
#                                                                                     #
#                                                                                     #
# *********************************************************************************** #


def compare_objects(a, b):
    if not isinstance(a, type(b)):
        return False
    elif isinstance(a, dict):
        return compare_dict(dict(sorted(a.items())), dict(sorted(b.items())))
    elif isinstance(a, list) or isinstance(a, tuple):
        return compare_list(a, b)
    else:
        return a == b


# *************** NESTED COMPLEX OBJECTS ******************** #

def is_complex(item):
    return isinstance(item, dict) or isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set)


# dict nested in other objects
def dict_in_dict_of_dicts(elem, dict_of_elem):
    for k, v in dict_of_elem.items():
        if isinstance(elem, type(v)) and sorted(elem.keys()) == sorted(v.keys()) and compare_objects(elem, v):
            return True
    return False


def dict_in_list(elem, list_of_elem):
    for j in range(len(list_of_elem)):
        if isinstance(elem, type(list_of_elem[j])) and \
                sorted(elem.keys()) == sorted(list_of_elem[j].keys()) and compare_objects(elem, list_of_elem[j]):
            return True
    return False


# indices objects nested in other objects
def list_in_dict(elem, dict_of_elem):
    for k, v in dict_of_elem.items():
        if type(elem) == type(v) and compare_objects(elem, v):
            return True

    return False


def list_and_tuple_within_list(elem, list_of_elem):
    for j in range(len(list_of_elem)):
        if isinstance(elem, type(list_of_elem[j])) and compare_objects(elem, list_of_elem[j]):
            return True
    return False


def properties_do_not_fit(a, b):
    return (len(a) != len(b)) or (a.keys() != b.keys())


def compare_dict(a, b):
    if properties_do_not_fit(a, b):
        return False
    for key, value in a.items():
        if isinstance(value, dict):
            if not dict_in_dict_of_dicts(value, b):
                return False
        elif is_complex(value):
            if not list_in_dict(value, b):
                return False
        else:
            if value != b[key]:
                return False
    return True


def compare_list(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if isinstance(a[i], dict):
            if not dict_in_list(a[i], b):
                return False
        elif is_complex(a[i]):
            if not list_and_tuple_within_list(a[i], b):
                return False
        else:
            if not a[i] in b:
                return False
    return True
