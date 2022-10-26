#Python CalculatorV2 

exit = '' 

while exit != 'exit': 

    print("Enter your expression like this \"10 + 7\" or \"18 + -4 / 9\". Enter \"exit\" to exit the program") 

    math = input() 

     
    #parts of the expression 

    calc = 0 

    num1 = 0 

    num2 = 0 

    num3 = 0 

    op1 = '' 

    op2 = '' 


    isTwo = False 

    isThree = False 

    ##checks to see what kind of expression it is 

    indexes = [] 

    j = 0 

    for i in range(len(math)): 

        if math[i] == ' ': 

            indexes.append(i) 

            j = j+1 


    if j == 4: 

        isThree = True 

    elif j == 2: 

        isTwo = True 


    if isTwo: ##Procedure one operator 

        op1 = math[indexes[0]+1:indexes[1]] 

        num1 = int(math[0:indexes[0]]) 

        num2 = int(math[indexes[1]+1:len(math)]) 

         

        if op1 == '+': 

            calc = num1 + num2 

        elif op1 == '-': 

            calc = num1 - num2 

        elif op1 == '*': 

            calc = num1 * num2 

        elif op1 == '/': 

            calc = num1 / num2 

        elif op1 == '%': 

            calc = num1 % num2 

     

    if isThree: ##Procedure for two operators 

        op1 = math[indexes[0]+1:indexes[1]] 

        op2 = math[indexes[2]+1:indexes[3]] 

        num1 = int(math[0:indexes[0]]) 

        num2 = int(math[indexes[1]+1:indexes[2]]) 

        num3 = int(math[indexes[3]+1:len(math)]) 

         

        term = 0 

        if op1 == '/' or op1 == '*' or op1 == '%': 

            if op1 == '*': 

                term = num1 * num2 

            elif op1 == '/': 

                term = num1 / num2 

            elif op1 == '%': 

                term = num1 % num2 



            if op2 == '+': 

                calc = term + num3 

            elif op2 == '-': 

                calc = term - num3 

            elif op2 == '*': 

                calc = term * num3 

            elif op2 == '/': 

                calc = term / num3 

            elif op2 == '%': 

                calc = term % num3  

        elif op2 == '/' or op2 == '*' or op2 == '%': 

            if op2 == '*': 

                term = num2 * num3 

            elif op2 == '/': 

                term = num2 / num3 

            elif op2 == '%': 

                term = num2 % num3 

             

            if op1 == '+': 

                calc = num1 + term 

            elif op1 == '-': 

                calc = num1 - term 

            elif op1 == '*': 

                calc = num1 * term 

            elif op1 == '/': 

                calc = num1 / term 

            elif op1 == '%': 

                calc = num1 % term 

        else: 

            if op1 == '+': 

                term = num1 + num2 

            elif op1 == '-': 

                term = num1 - num2 

            if op2 == '+': 

                calc = term + num3 

            elif op2 == '-': 

                calc = term - num3 

     

    if math != 'exit': 

        print(math + " = " + str(int(calc))) 

 
 

    exit = math 

 