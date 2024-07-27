numbers = [2, 3, 4, 4, 6, 5, 7 , 8, 8, 3]
empty = []
for number in numbers:
    if number not in empty:
        empty.append(number)
print(empty)

# you can also do this, i presonally preffer this method👩🏽‍💻👩🏽‍💻
prices = [2 , 3 , 5 , 6 , 2 , 3 , 5 , 6]
sorted_list = set(prices)
print(sorted_list)