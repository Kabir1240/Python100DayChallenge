def tip_calculator():
    # print greeting message
    print("Welcome to the tip calculator!")

    # get necessary data
    bill = float(input("What was the total bill?\n$"))
    tip_amount = int(input("How much tip would you like to give? 10, 12 or 15%?\n"))
    n_people = int(input("How many people to split the bill?\n"))

    # calculations
    total_bill = round((bill * (1 + (tip_amount/100))) / n_people, 2)
    bill_as_string = "{:.2f}".format(total_bill)
    print(f"Each person should pay: ${bill_as_string}")


tip_calculator()