
# ************************ compare_object_with_info.py ****************************** #
#                                                                                     #
#   compare_object_with_info.py -                                                     #
#                                                                                     #
#       Description:                                                                  #
#                                                                                     #
#           This component, is able to compare any two object, nested and             #
#           not nested, and gives a simple result == True or False and information.   #
#                                                                                     #
#                                                                                     #
# *********************************************************************************** #


success_message = "Objects are equal!"


def compare_objects_with_info(a, b, indention=''):
    if not isinstance(a, type(b)):
        return False
    elif isinstance(a, dict):
        return compare_dict_with_info(dict(sorted(a.items())), dict(sorted(b.items())), indention)
    elif isinstance(a, list) or isinstance(a, tuple):
        return compare_list_with_info(a, b, indention)
    else:
        comparison = (a == b)
        if not comparison:
            comparison = (False, f"{indention}mismatch between {a} != {b}")
        else:
            comparison = True, f"{a} and {b} are equal!"
        return comparison


# *************** NESTED COMPLEX OBJECTS ******************** #

def is_complex_with_info(item):
    return isinstance(item, dict) or isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set)


# dict nested in other objects
def dict_in_dict_of_dicts_with_info(parent_key, elem, dict_of_elem, indention):
    for k, v in dict_of_elem.items():
        if isinstance(elem, type(v)) and sorted(elem.keys()) == sorted(v.keys()) and parent_key == k:
            result = compare_objects_with_info(elem, v, f"{indention}  ")
            if not result[0]:
                return result
            else:
                return True, success_message
    return False, f"Element {elem}, is not appear correctly in dict {dict_of_elem}"


def dict_in_list_with_info(elem, list_of_elem, indention):
    collect_info = ""
    counter = 1
    for j in range(len(list_of_elem)):
        if isinstance(elem, type(list_of_elem[j])):
            if sorted(elem.keys()) == sorted(list_of_elem[j].keys()):
                result, info = compare_objects_with_info(elem, list_of_elem[j], f"{indention}  ")
                if result:
                    return True, success_message
                else:
                    collect_info += f"{indention}{counter} : {info}\n"
                    counter += 1
            else:
                info = f'Origin Element keys {sorted(elem.keys())} and current object keys {sorted(list_of_elem[j].keys())}'
                collect_info += f"{indention}{counter} : {info}\n"
                counter += 1
    return False, f"Element {elem}, is not exist in list in the exact way.\n\n{indention}Reasons are : \n{collect_info}"


# indices objects nested in other objects
def list_in_dict_with_info(parent_key, elem, dict_of_elem, indention):
    for k, v in dict_of_elem.items():
        if parent_key == k:
            if type(elem) != type(v):
                return False, f"{indention}Elements {elem} and {v}, refer to the same key ``{parent_key}``, with diff types"
            elif not compare_objects_with_info(elem, v)[0]:
                return compare_objects_with_info(elem, v, f"{indention}  ")
            else:
                return True, success_message
    return False, f"Element {elem}, is not appear correctly in dict {dict_of_elem}."


def list_and_tuple_within_list_with_info(elem, list_of_elem, indention):
    collect_info = ""
    counter = 1
    for j in range(len(list_of_elem)):
        if isinstance(elem, type(list_of_elem[j])):
            result, info = compare_objects_with_info(elem, list_of_elem[j], f"{indention}  ")
            if result:
                return True, success_message
            else:
                collect_info += f"{indention}{counter} : {info}\n"
                counter += 1
    return False, f"Element {elem} is not exist in list in the exact way.\n\n{indention}Reasons are : \n{collect_info}"


def properties_do_not_fit_with_info(a, b, indention):
    if len(a) != len(b):
        return False, f"{indention}{a} length is {len(a)} and {b} length is {len(b)}"
    if a.keys() != b.keys():
        return False, f"{indention}{a} keys are {list(a.keys())} and {b} keys is {list(b.keys())}"
    return True, success_message


def compare_dict_with_info(a, b, indention):
    result = properties_do_not_fit_with_info(a, b, indention)
    if not result[0]:
        return result
    for key, value in a.items():
        if isinstance(value, dict):
            result = dict_in_dict_of_dicts_with_info(key, value, b, indention)
            if not result[0]:
                return result
        elif is_complex_with_info(value):
            result = list_in_dict_with_info(key, value, b, indention)
            if not result[0]:
                return result
        else:
            if value != b[key]:
                return False, f"Mismatch between values for key ``{key}``, {value} != {b[key]}."
    return True, success_message


def compare_list_with_info(a, b, indention):
    if len(a) != len(b):
        return False, f"Mismatch - length of list {a} is {len(a)} and {b} is {len(b)}"
    for i in range(len(a)):
        if isinstance(a[i], dict):
            result = dict_in_list_with_info(a[i], b, f"{indention}")
            if not result[0]:
                return result
        elif is_complex_with_info(a[i]):
            result = list_and_tuple_within_list_with_info(a[i], b, f"{indention}")
            if not result[0]:
                return result
        else:
            if not a[i] in b:
                return False, f"Element {a[i]} is in {a} and not in {b}"
    return True, success_message
