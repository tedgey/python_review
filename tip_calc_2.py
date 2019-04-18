# bill_amount = float(input("What is the total bill amount? "))

# service_level = input("How was your level of service? (Good, fair, or bad) ")

# people_count = float(input("Split how many ways? "))

# if service_level == "good": 
#     tip_amount =bill_amount * .20
#     total = bill_amount + tip_amount
#     print("Tip amount: $%.2f" % (tip_amount,))
#     print("Total amount: $%.2f" % (total,))
#     print("Amount per person: $%.2f" % ((total/people_count)))

# elif service_level == "fair":
#     tip_amount =bill_amount * .15
#     print("Tip amount: $%.2f" % (tip_amount,))
#     print("Total amount: $%.2f" % (total,))
#     print("Amount per person: $%.2f" % ((total/people_count)))

# elif service_level == "bad":
#     tip_amount =bill_amount * .10
#     print("Tip amount: $%.2f" % (tip_amount,))
#     print("Total amount: $%.2f" % (total,))
#     print("Amount per person: $%.2f" % ((total/people_count)))

# else:
#     print("Please try again")


bill_amount = float(input("What is the total bill amount? "))
service_level = input("How was your level of service? (Good, fair, or bad) ")
people_count = float(input("Split how many ways? "))

def group_tip_calc(bill_amount, service_level, people_count):
    if service_level == "good": 
        tip_amount = bill_amount * .20
        total = bill_amount + tip_amount
        print("Tip amount: $%.2f" % (tip_amount,))
        print("Total amount: $%.2f" % (total,))
        print("Amount per person: $%.2f" % ((total/people_count)))

    elif service_level == "fair":
        tip_amount = bill_amount * .15
        total = bill_amount + tip_amount
        print("Tip amount: $%.2f" % (tip_amount,))
        print("Total amount: $%.2f" % (total,))
        print("Amount per person: $%.2f" % ((total/people_count)))

    elif service_level == "bad":
        tip_amount = bill_amount * .10
        total = bill_amount + tip_amount
        print("Tip amount: $%.2f" % (tip_amount,))
        print("Total amount: $%.2f" % (total,))
        print("Amount per person: $%.2f" % ((total/people_count)))

    else:
        print("Please try again")

group_tip_calc(bill_amount, service_level, people_count)