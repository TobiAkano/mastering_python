weight = int(input("weight:"))
unit = str(input("K(g) or L(bs)")).upper
while unit == "K":
    converter = weight * 2.204
    print("your weight in pounds is:" , converter,"lbs")
else:
    converter = weight * 0.453592
    print("your weight in kilograms is",converter,"kg")