# bill_amount = float(input("What is the total bill amount? "))

# service_level = input("How was your level of service? (Good, fair, or bad) ")


# if service_level == "good": 
#     tip_amount =bill_amount * .20
#     total = bill_amount + tip_amount
#     print("Tip amount: $%.2f" % (tip_amount,))
#     print("Total amount: $%.2f" % (total,))

# elif service_level == "fair":
#     tip_amount =bill_amount * .15
#     total = bill_amount + tip_amount
#     print("Tip amount: $%.2f" % (tip_amount,)) 
#     print("Total amount: $%.2f" % (total,))

# elif service_level == "bad":
#     tip_amount =bill_amount * .10
#     total = bill_amount + tip_amount
#     print("Tip amount: $%.2f" % (tip_amount,))
#     print("Total amount: $%.2f" % (total,)) 

# else:
#     print("Please try again")


bill_amount = float(input("What is the total bill amount? "))
service_level = input("How was your level of service? (Good, fair, or bad) ")

def tip_calc(bill_amount, service_level):
    if service_level == "good": 
        tip_amount =bill_amount * .20
        total = bill_amount + tip_amount
        print("Tip amount: $%.2f" % (tip_amount,))
        print("Total amount: $%.2f" % (total,))

    elif service_level == "fair":
        tip_amount =bill_amount * .15
        total = bill_amount + tip_amount
        print("Tip amount: $%.2f" % (tip_amount,)) 
        print("Total amount: $%.2f" % (total,))

    elif service_level == "bad":
        tip_amount =bill_amount * .10
        total = bill_amount + tip_amount
        print("Tip amount: $%.2f" % (tip_amount,))
        print("Total amount: $%.2f" % (total,)) 

    else:
        print("Please try again")

tip_calc(bill_amount, service_level)




