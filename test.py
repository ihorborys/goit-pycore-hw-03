import random
"""Function generates random list of sorted unique numbers with a given length"""
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """Generates random list of unique numbers with a given length"""
    random_sequence = random.sample(range(min, max), quantity)
    """Sort list"""
    list.sort(random_sequence)
    return random_sequence


print(get_numbers_ticket(1, 50, 6))
