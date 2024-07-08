import random
"""Function generates random list of sorted unique numbers with a given length"""


def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list:
    random_sequence = []
    while 1 <= min_number < max_number <= 1000 and 1 <= quantity <= 1000:
        """Generates random list of unique numbers with a given length"""
        random_sequence = random.sample(range(min_number, max_number), quantity)
        """Sorts the list"""
        list.sort(random_sequence)
        return random_sequence
    else:
        print("Please enter correct data: 1 <= min < max <= 1000, 1 <= quantity <= 1000")
        return random_sequence


print("Your lottery numbers:", get_numbers_ticket(100, 200, 10))
