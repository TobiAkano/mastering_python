try:
    number = int(input("what is your phone number: "))
    print(number)
    income = 100000
    income_number = income/number
except ZeroDivisionError :
    print("you can not put 0 as your number ")
except ValueError:
    print("Enter a number not a word ")
