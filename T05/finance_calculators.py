import math

OpeningStatement = '''Welcome to the finance calculator. Please select your investment type: 
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on your home loan'''

print(OpeningStatement)

isValidInput = False

while not isValidInput:
    UserSelection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

    UserSelection = UserSelection.lower()

    if UserSelection == "investment" or UserSelection == "bond":
        isValidInput = True
    else:
        UserSelection = input("Invalid input. Please enter either 'investment' or 'bond': ")
        
        UserSelection = UserSelection.lower()
        if UserSelection == "investment" or UserSelection == "bond":
            isValidInput = True

if UserSelection == "investment":
    print("Investment selected.")
    Deposit = float(input("Please input deposit amount: $"))
    Rate = float(input("Please input the interest rate: ")) / 100 #Annual interest rate 
    Term = int(input("Please input the number of years you plan to invest this amount: "))
    

    

    isValidInput = False
    while not isValidInput:
        InterestType = input("Simple or compound interest? ")

        InterestType = InterestType.lower()

        if InterestType == "simple" or InterestType == "compound":
            isValidInput = True
        else:
            InterestType = input("Invalid input. Please enter either 'simple' or 'compound': ")

            if InterestType == "simple" or InterestType == "compound":
                isValidInput = True

    RoI = float()
    if InterestType == "simple":
        RoI = Deposit*(1 + Rate * Term)
        print()

        print(f"After {Term} year(s) you can expect a return of ${round(RoI, 2)} from your initial investment of ${Deposit}")

    if InterestType == "compound":
        RoI = Deposit * math.pow((1 + Rate), Term)
        print()

        print(f"After {Term} year(s) you can expect a return of ${round(RoI, 2)} from your initial investment of ${Deposit}")

if UserSelection == "bond":
    print("Bond selected.")
    Value = float(input("Please input the value of the house: $"))
    Rate = float(input("Please input the interest rate: ")) / 100 /12 #Monthly interest rate 
    Term = int(input("Please input the number of years you need to repay the bond: "))

    Repayment = (Rate * Value) / (1 - (1 + Rate)**(-Term*12))

    print(f"The monthly repayment for the bond will be: ${Repayment}")