from typing import Literal


def climate_controled_tagging(description_text: str) -> bool:
    """
        Checks the list of words in a check_list and adds a column (indicator) with boolean values.
        :param pricing: dataframe containing pricing data for one week
        :param indicator: name of the column
        :param check_list: list of possible cases where indicator column should be 1
        :return: dataframe containing pricing data for one week and added column (indicator)
        """

    terms = ['climate', 'air condition', 'air cool', 'humid', 'heat', 'central air', 'dehumidified']
    negation_terms = [f'{a} {b}' for a in ['no', 'not'] for b in terms]

    for neg_term in negation_terms:
        if neg_term in description_text.lower():
            return False

    for term in terms:
        if term in description_text.lower():
            return True

    return False


def size_category_tagging(size_text: str) -> Literal["Small", "Medium", "Large"]:
    """
    Categorizes size into small, medium or large based on the area
    :param pricing: dataframe consisting of pricing data for one week
    :return: size category (small, medium or large)
    """

    tmp_char = ''
    dig_enc = False
    tmp_dimensions = []

    for char in size_text:
        if char.isdigit():
            tmp_char = tmp_char + char
        else:
            tmp_dimensions.append(tmp_char)
            tmp_char = ''
    else:
        tmp_dimensions.append(tmp_char)

    tmp_dimensions = [dim for dim in tmp_dimensions if dim != '']

    size_sq_ft = int(tmp_dimensions[0]) * int(tmp_dimensions[1])

    if size_sq_ft < 100:
        return "Small"
    elif size_sq_ft >= 100 and size_sq_ft < 200:
        return "Medium"
    elif size_sq_ft >= 200 and size_sq_ft < 100000:
        return "Large"
    else:
        raise ValueError(
            f"Seomething is wrong with the sqare footage, it's either to big or some other invalid value: {size_sq_ft}")


def elevator_access_tagging(description_text: str) -> str:
    terms = ['elevator', 'lift']
    negation_terms = [f'{a} {b}' for a in ['no', 'not'] for b in terms]

    for neg_term in negation_terms:
        if neg_term in description_text.lower():
            return False

    for term in terms:
        if term in description_text.lower():
            return True

    return False


def ground_floor_tagging(description_text: str) -> str:
    terms = ['1st floor', 'ground level']
    negation_terms = [f'{a} {b}' for a in ['no', 'not'] for b in terms]

    for neg_term in negation_terms:
        if neg_term in description_text.lower():
            return False

    for term in terms:
        if term in description_text.lower():
            return True

    return False


def drive_up_tagging(description_text: str) -> bool:
    terms = ['drive-up', 'drive up', 'covered loading area/indoor access', 'loading bay access']
    negation_terms = [f'{a} {b}' for a in ['no', 'not'] for b in terms]

    for neg_term in negation_terms:
        if neg_term in description_text.lower():
            return False

    for term in terms:
        if term in description_text.lower():
            return True

    return False


def check_special_case_tagging(description_text: str) -> str:
    """
    Flags every storage unit considered a special case (e.g. storage has no dimensions, wine/vehicle storage, etc.)
    :param pricing: dataframe consisting of pricing data for one week
    :return: special case type or nan for regular storage units
    """
    vehicles = ['boat', 'motorcycle', 'car', 'vehicle', 'parking']

    if isinstance(description_text, float):
        raise TypeError('Input must be text description.')
    elif "wine" in description_text.lower():
        return "Wine Storage"
    elif "parking" in description_text.lower() or "RV" in description_text or any(
            v in description_text.lower() for v in vehicles):
        return "Vehicle Storage"
    elif "locker" in description_text.lower():
        return "Locker"
    elif "mailbox" in description_text.lower():
        return "Mailbox"

    return ''
