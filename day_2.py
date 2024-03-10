def tip_calculator():
    # print greeting message
    print("Welcome to the tip calculator!")

    # get necessary data
    total_bill = float(input("What was the total bill?\n$"))
    tip_amount = int(input("How much tip would you like to give? 10, 12 or 15%?\n"))
    n_people = int(input("How many people to split the bill?\n"))

    # calculations
    total_bill = round((total_bill * (1 + (tip_amount/100))) / n_people, 2)
    print(f"Each person should pay: ${total_bill}")


tip_calculator()