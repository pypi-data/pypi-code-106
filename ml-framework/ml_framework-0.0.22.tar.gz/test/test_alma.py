import pytest


@pytest.mark.parametrize(
    "number_1,number_2,result",
    [
        (1, 1, 2),
        (3, 4, 7),
    ],
)
@pytest.mark.critical
def test_example1(number_1, number_2, result):
    assert number_1 + number_2 == result


@pytest.mark.parametrize(
    "number_1,number_2,result",
    [
        (1, 1, 0),
        (3, 4, 1),
    ],
)
@pytest.mark.long
def test_example2(number_1, number_2, result):
    assert number_2 - number_1 == result
