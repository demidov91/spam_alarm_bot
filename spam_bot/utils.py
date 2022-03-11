import re


card_number_regex = re.compile(r'(\d\s*){16}')


def contains_card_number(text: str) -> bool:
    return bool(card_number_regex.search(text))