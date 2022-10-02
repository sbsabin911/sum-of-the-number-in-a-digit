#this program is used to find the sum of the digit in the given number by using recursion


import math
def calculation(number):
    sum=0
    if number<9:
        return number
    else:
        while number:
            sum+=number%10
            number //=10
        if sum < 9:
            return sum
        else:
            return calculation(sum)


user_input=int(input("enter the number you want="))
print(f"the sum up to the single digit is={calculation(user_input)}")