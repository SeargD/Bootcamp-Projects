'''
Simple calculator app which takes 2 numbers and an operator from the user and outputs the result to screen and text.

'''
Opener = '''This program will take any 2 numbers  and an  operator ( +, -, *, / ) and ouptut the resulting value to console and to a text file.
Floating point numbers and integer values are fine. 
Enter 'quit' as the first number to terminate the program.'''

print(Opener)

RunState = True # Allows for additional function

while RunState == True:
    Number1 = float()
    Number2 = float()
    Result  = float()
    Operator = ""

    ValidInput = False
    while ValidInput == False:
        UserInput = input("Please enter a number: ")
        try:
            float(UserInput)
        except Exception:
            

            print("Input failed to cast as a number")
            continue

        Number1 = float(UserInput)
        ValidInput = True

    ValidInput = False #resets loop condition for user input validation
    while ValidInput == False:
        UserInput = input("Please enter another number: ")
        try:
            float(UserInput)
        except Exception:
            print("Input 2 failed to cast as a number")
            continue

        Number2 = float(UserInput)
        ValidInput = True

    ValidInput = False #resets loop condition for user input validation
    UserInput = input("Please select an operator(+, -, *, or /): ")
    while ValidInput == False:
        Operator = UserInput

        if UserInput == "+":
            Result = Number1 + Number2
            ValidInput = True
        elif UserInput == "-":
            Result = Number1 - Number2
            ValidInput = True
        elif UserInput == "*":
            Result = Number1 * Number2
            ValidInput = True
        elif UserInput == "/":
            if Number2 == 0:
                print("Error: Division by zero.")
                Result = "inf"
                break
            Result = Number1 / Number2
            
            ValidInput = True
        else:
            UserInput = input("Invalid operator. Please try again (+, -, *, /): ")
            continue
            
    with open('output.txt', 'a') as OutputFile:
        OutputString = f"\n{Number1} {Operator} {Number2} = {Result}"
        OutputFile.write(OutputString)