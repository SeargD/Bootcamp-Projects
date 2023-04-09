'''
Simple calculator app which takes 2 numbers and an operator from the user and outputs the result to screen and text.

'''
Opener = '''This program will take any 2 numbers  and an  operator ( +, -, *, / ) and ouptut the resulting value to console.
The results will also be addeed to a text file.
Floating point numbers and integer values are fine.
Alternatively, you may input the name of a text file in the form of:
{Number 1} {operator} {Number 2}
{Number 1} {operator} {Number 2}

The program will print the results and add them to a file
Enter 'quit' as the first number to terminate the program.'''

print(Opener)

RunState = True #Setting value to false allows program to terminate after 1 run when file is input

while RunState == True:
    Number1 = float()
    Number2 = float()
    Result  = float()
    Operator = ""
    Filename = ""

    ValidInput = False
    while ValidInput == False:
        UserInput = input("Please enter a number or a text file (example.txt): ")
        try:    #Testing numeric input
            float(UserInput)
            Number1 = float(UserInput)
            ValidInput = True
        except Exception:
            print("Input failed to cast as a number")
            
            if UserInput.lower() == "quit": #Testing for user quit request
                quit()

            try:    #Testing for valid filename
                f = open(UserInput, 'r')
                f.close()
                Filename = UserInput
                ValidInput = True
                RunState = False
                print(f"{Filename} found. Reading input")
            except FileNotFoundError:
                print("File not found please enter a valid filename")
        
    if Filename == "":
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
            print(OutputString)
            OutputFile.write(OutputString)

    if Filename != "":
        with open(Filename, 'r') as InputFile:
            lisInput = InputFile.readlines()

        lisOutput = list()
        for line in lisInput: 
            line = line.strip('\n') #remove extraneous whitespace from input file

            lisFormula = line.split(' ')

            if len(lisFormula) != 3:
                OutputString = "Invalid operation."
                lisOutput.append(OutputString)
                print(OutputString)
            else:
                try:
                    Number1 = float(lisFormula[0])
                    Number2 = float(lisFormula[2])
                except Exception:
                    print("Invalid operand.")
                    continue

                Operator = lisFormula[1]
            
            if Operator == "+":
                Result = Number1 + Number2
                OutputString = f"\n{Number1} {Operator} {Number2} = {Result}"

            elif Operator == "-":
                Result = Number1 - Number2
                OutputString = f"\n{Number1} {Operator} {Number2} = {Result}"

            elif Operator == "*":
                Result = Number1 * Number2
                OutputString = f"\n{Number1} {Operator} {Number2} = {Result}"
            elif Operator == "/":
                if Number2 == 0:
                    print("Error: Division by zero.")
                    Result = "inf"
                    OutputString = f"\n{Number1} {Operator} {Number2} = {Result}"
                else:
                    Result = Number1 / Number2
                    OutputString = f"\n{Number1} {Operator} {Number2} = {Result}"
            else:
                OutputString = "Invalid operator."
                lisOutput.append(OutputString)
                print(OutputString)

            with open('output.txt', 'a') as OutputFile:
                
                print(OutputString.strip())
                OutputFile.write(OutputString)
