import re

#declare the function
def normalize_phone(phone_number):
    #describing the pattern to be deleted/replaced
    phone_number_pattern = r"[^\+0-9]"
    #replacing the pattern with space symbol using sub functon from re
    phone = re.sub(phone_number_pattern, "", phone_number)
    #check if the number starts with +
    if phone.startswith("+"):
        return phone
    #check if number does not start with + and adding necessary sign/signs at the start of the number
    else:
        if phone.startswith("380"):
            return f'+{phone}'
        else:
            return f'+38{phone}'


#creation of a function to output "a convenient-to-read" string of numbers 
def print_numbers_in_rows(numbers:list):
    num_count = len(numbers)
    if num_count % 2 == 0:
        print("Нормалізовані номери телефонів для SMS-розсилки:")
        for i in range(0, num_count,2):
            print(f"{numbers[i]} {numbers[i+1]}")
    else:
        print("Нормалізовані номери телефонів для SMS-розсилки:")
        for i in range(0, num_count, 3):
            if i + 2 < num_count:
                print(f"{numbers[i]} {numbers[i+1]} {numbers[i+2]}")
            else:
                remaining_numbers = numbers[i:num_count]
                print(" ".join(remaining_numbers))


raw_numbers = [
    "067\\t123 4567",
    "067\\t123 4567",
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "38050 111 22 00   "
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print_numbers_in_rows(sanitized_numbers)


