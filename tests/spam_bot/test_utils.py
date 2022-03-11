import pytest

from spam_bot.utils import contains_card_number


@pytest.mark.parametrize(
    'text',
    [
        'Karta-šmarta 0345 6789  34582378',
        '0345678934582378 Karta-šmarta ',
        '0345678934582378',
        '0345 6789 3458 2378',
    ],
)
def test_contains_card_number__positive(text):
    assert contains_card_number(text)


@pytest.mark.parametrize(
    'text',
    [
        'Karta-šmarta 0345 789  34582378',
        '034567893-4582378 Karta-šmarta ',
        '034567a934582378',
        '+375292020327',
    ],
)
def test_contains_card_number__negative(text):
    assert not contains_card_number(text)
