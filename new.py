def calculate():
    while True:
        previous = input("Enter previous API: ")
        current = input("Enter current API: ")

        if not (previous.replace('.', '', 1).isdigit() and current.replace('.', '', 1).isdigit()):
            print("Please only input numbers.")
            continue

        previous = float(previous)
        current = float(current)

        if previous > 100 or current > 100:
            print("Invalid Number (Should be less than or equal to 100)")
            continue

        if previous == current:
            print("Your API remained the same")
        else:
            change = (current - previous) / abs(previous) * 100
            if change > 0:
                print(f"You have increased by {round(change)}%")
            else:
                print(f"You have decreased by {round(abs(change))}%")

        rerun = input("Do you want to calculate again? (yes/no): ")
        if rerun.lower() != 'yes':
            break

calculate()