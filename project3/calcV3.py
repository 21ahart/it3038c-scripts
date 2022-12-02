#Python CalculatorV3

#converts strings to numbers
def convert(sub): 
    c = 0
    num = 0
    index = 0
    for i in range(len(sub)):
        if sub[i] == '.':
            c = 1
        if sub[i] == '/':
            c = 2
            index = i

    if c == 1:
        num = float(sub)
    elif c == 2:
        num = float(int(sub[0:index]) / int(sub[index+1:len(sub)]))
    else:
        num = int(sub)
    
    return num

#takes in string to find format errors returns true or false 
def finderr(str):
    dcnt = 0
    fcnt = 0

    for i in range(len(str)):
        if str[i] == ' ':
            return False
        elif str[i] == '/':
            dcnt = dcnt + 1
        elif str[i] == '.':
            fcnt = fcnt + 1
    
    if fcnt >= 2 or dcnt >= 2:
        return False
    elif (fcnt + dcnt) >= 2:
        return False
    
    return True
        
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
    flerr = 0 #error determination variable

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
    else:
        flerr = 1

    if isTwo: ##Procedure with one operator
        
        op1 = math[indexes[0]+1:indexes[1]]
        part1 = math[0:indexes[0]]
        part2 = math[indexes[1]+1:len(math)]
        err1 = finderr(part1)
        err2 = finderr(part2)

        if err1 and err2:
            num1 = convert(part1)
            num2 = convert(part2)
        else:
            flerr = 1
            num1 = 0
            num2 = 0

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
        term = 0
        op1 = math[indexes[0]+1:indexes[1]] 
        op2 = math[indexes[2]+1:indexes[3]] 
        part1 = math[0:indexes[0]]
        part2 = math[indexes[1]+1:indexes[2]]
        part3 = math[indexes[3]+1:len(math)]
        
        err1 = finderr(part1)
        err2 = finderr(part2)
        err3 = finderr(part3)

        if err1 and err2 and err3:
            num1 = convert(part1)
            num2 = convert(part2)
            num3 = convert(part3)
        else:
            flerr = 1
            num1 = 0
            num2 = 0
            num3 = 0

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

    if math != 'exit' and flerr == 0: 
        print(math + " = " + str(calc))
    elif flerr == 1 and math != 'exit':
        print('Incorrect Format Used')
    exit = math 

 