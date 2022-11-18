#Python CalculatorV3 

#converts strings to numbers 

def convert(sub):  
    c = 0 
    num = 0 
    index = 0 
    for i in range(len(sub)): 
        if sub[i] == '.': 
            c = 1 
        elif sub[i] == '/': 
            c = 2 
            index = i 

    if c == 1: 
        num = float(sub) 
    elif c == 2: 
        num = float(int(sub[0:index]) / int(sub[index+1:len(sub)])) 
    else: 
        num = int(sub) 

    return num 

 
exit = ''  

while exit != 'exit':  

    print("Enter your expression like this \"10 + 7\" or \"18 + -4 / 9\". Enter \"exit\" to exit the program")  
    math = input()  

    calc = None 
    num1 = None 
    num2 = None 
    num3 = None 
    op1 = None 
    op2 = None 
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

    if isTwo: ##Procedure with one operator 

        op1 = math[indexes[0]+1:indexes[1]] 
        part1 = math[0:indexes[0]] 
        part2 = math[indexes[1]+1:len(math)] 
        num1 = convert(part1) 
        num2 = convert(part2) 

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

    if isThree: ##Procedure with two operators  

        op1 = math[indexes[0]+1:indexes[1]]  
        op2 = math[indexes[2]+1:indexes[3]]  
        part1 = math[0:indexes[0]] 
        part2 = math[indexes[1]+1:indexes[2]] 
        part3 = math[indexes[3]+1:len(math)] 
        num1 = convert(part1) 
        num2 = convert(part2) 
        num3 = convert(part3) 

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
        print(math + " = " + str(calc))  

    exit = math  

 
 

 

 