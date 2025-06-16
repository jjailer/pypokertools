import pytest

from examples.isomorph import get_all_canonicals, get_canonical, get_translation_dict
from pokertools import cards_from_str as cards


def test_get_all_canonicals():
    assert len(get_all_canonicals()) == 1755

@pytest.mark.parametrize(
    "flop, expected_result",
    [
        (('6s 8d 7c'), ('6c 7d 8h')),
        (('Qs Qd 4d'), ('4c Qc Qd')),
        (('Qs Ts Tc'), ('Tc Td Qc')), # ABB -> ABA
    ]
)
def test_get_canonical(flop, expected_result):
    assert get_canonical(cards(flop)) == cards(expected_result)


@pytest.mark.parametrize(
    "flop, expected_result",
    [
        (('6s 8d 7c'), {'c': 'd', 'd': 'h', 'h': 's', 's': 'c'}),
        (('Qs Qd 4d'), {'c': 'h', 'd': 'c', 'h': 's', 's': 'd'}),
        (('Qs Ts Tc'), {'c': 'd', 'd': 'h', 'h': 's', 's': 'c'}),
    ]
)
def test_get_translation_dict(flop, expected_result):
    assert get_translation_dict(cards(flop)) == expected_result