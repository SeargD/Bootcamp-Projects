'''
Simple calculator app which takes 2 numbers and an operator from the user and outputs the result to screen and text.

'''

Opener = '''This program will take any 2 numbers  and an  operator ( +, -, *, / ) and ouptut the resulting value to console.
The results will also be addeed to a text file.
Floating point numbers and integer values are fine.
Alternatively, you may input the name of a text file containing equations in the format:
Number 1 operator Number 2
Number 1 operator Number 2

The program will print the results and add them to a file'''

print(Opener)

RunState = True #Setting value to false allows program to terminate after 1 run when file is input

while RunState == True:
    Number1 = float()
    Number2 = float()
    Result  = float()
    Operator = ""
    Filename = ""

    MenuOptions = '''\nWould you like to?
    1. Enter an equation
    2. Parse equations from txt
    3. quit
    '''
    
    UserSelection = input(MenuOptions)

    ValidInput = False
    if UserSelection == "1":
        while ValidInput == False:
            UserInput = input("Please enter a number: ")
            try:    #Testing numeric input
                float(UserInput)
                Number1 = float(UserInput)
                ValidInput = True
            except Exception:
                print("Input failed to cast as a number")
    elif UserSelection == "2":
        while ValidInput == False:
            UserInput = input("Please input your txt file name: ")
            try:    #Testing for valid filename
                f = open(UserInput, 'r')
                f.close()
                Filename = UserInput
                ValidInput = True
                RunState = False
                print(f"{Filename} found. Reading input\n")
            except FileNotFoundError:
                print("File not found please enter a valid filename")
    elif UserSelection == "3":
        quit()
    else:
        print("Invalid option. Try again")
        continue

    
        
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
                
        with open('output.txt', 'a') as OutputFile:#Outputs parsed equations
            OutputString = f"\n{Number1} {Operator} {Number2} = {Result}"
            print(OutputString)
            OutputFile.write(OutputString)

    if Filename == "output.txt":
        print("output.txt reserved for storing solved equations please use another name.")
        continue

    if Filename != "":
        with open(Filename, 'r') as InputFile:
            lisInput = InputFile.readlines()

        for line in lisInput: #Reads each equation line by line 
            line = line.strip() #remove extraneous whitespace from input file

            lisFormula = line.split(' ')

            if len(lisFormula) != 3:
                OutputString = "Invalid operation."
                print(OutputString)
                continue #Prevents invalid operations printing to file
            else:
                try:
                    Number1 = float(lisFormula[0])
                    Number2 = float(lisFormula[2])
                except Exception:
                    print("Invalid operand.")
                    continue #Prevents invalid operations printing to file

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
                print(OutputString)
                continue #Prevents invalid operations printing to file

            with open('output.txt', 'a') as OutputFile:
                
                print(OutputString.strip())
                OutputFile.write(OutputString)
