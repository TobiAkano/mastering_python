from num2words import num2words
phone_number = str(input("Phone:"))
for number in phone_number:
    print(num2words(number))