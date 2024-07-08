import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-228989",
    "38050 111 22 11   ",
]
full_num_length = 13
num_length = 10


def normalize_phone(phone_number: str) -> str:
    format_pattern = r"\+38|\d"
    entrance_pattern = r"\+38"
    digits_list = re.findall(format_pattern, phone_number)
    formatted_num = "".join(digits_list)

    if len(formatted_num) > full_num_length:  # Check for the valid number length
        return "Please, enter valid phone number"

    if not re.search(entrance_pattern, formatted_num):  # Check if number starts with international Ukraine code
        formatted_num = f"+38{formatted_num[len(formatted_num) - num_length:]}"

    return formatted_num


for number in raw_numbers:
    print(normalize_phone(number))
