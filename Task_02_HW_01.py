#importing random module
import random 

def get_numbers_ticket(min:int, max:int, quantity:int):
    #checking if the inputed parametrs meet the requests
    if min < 1 or max > 1000 or min > max:
        return []
    
    if quantity > (max - min + 1):
        return []

    #forming the list of random values within min-max range
    unique_numbers = random.sample(range(min, max+1), quantity)
    #retun the result as list of random values
    return sorted(unique_numbers)


#calling the function with required arguments 
lottery_numbers = get_numbers_ticket(10, 12, 11)
#printing out a result of the function output
print("Ваші лотерейні числа:", lottery_numbers)





