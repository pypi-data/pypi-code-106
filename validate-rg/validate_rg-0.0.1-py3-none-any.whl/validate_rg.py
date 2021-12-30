import re
from typing import List


def _clean(rg: str) -> str:
    return re.sub(r'\D', '', rg)


def _is_allowed(rg: str) -> bool:
    first_digit = rg[0]
    return not all(first_digit == digit for digit in rg)


def _generate_factories(rg: str) -> List[int]:
    return list(map(lambda i: i if i <= 9 else i - 8, range(2, len(rg) + 1)))


def _caculate_digit(rg: str) -> str:
    FACTORIES = _generate_factories(rg)
    rg = list(map(lambda x: int(x), rg[:9]))
    result_sum = sum([rg[index] * factory for index, factory in enumerate(FACTORIES)])
    REST = result_sum % 11
    DV = str(11 - REST)
    if DV == '10':
        return 'X'
    if DV == '11':
        return '0'
    return DV


def is_valid(rg: str) -> bool:
    rg: str = _clean(rg)
    if not _is_allowed(rg):
        return False
    return rg[-1] == _caculate_digit(rg)