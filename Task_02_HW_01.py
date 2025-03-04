#importing random module
import random 

def get_numbers_ticket(min:int, max:int, quantity:int):
    #checking if the inputed parametrs meet the requests
    if min >= 1 and max <= 1000 and min < quantity < max:
        #forming the list of random values within min-max range
        unique_numbers = random.sample(range(min, max), quantity)
        #retun the result as list of random values
        return sorted(unique_numbers)
    else:
        #return an empty list if the condition in "if" is wrong
        return []


#calling the function with required arguments 
lottery_numbers = get_numbers_ticket(1, 49, 6)
#printing out a result of the function output
print("Ваші лотерейні числа:", lottery_numbers)





