
#Python Calculator

exit = ''
while exit != 'exit':
    print("Enter your expression like this \"10 + 7\" or \"18 / 9\". Enter \"exit\" to exit the program")
    math = input()
    
    num1 = 0
    num2 = 0
    op = ''

    i = 0
    c = 0
    while i < len(math):

        if math[i] == ' ' and c == 0:
            num1 = int(math[0:i])
            op = math[i+1:i+2]
            c = 1

        elif math[i] == ' ' and c == 1:
            num2 = int(math[i+1:len(math)])
        
        i = i+1
    
    calc = 0
    if op == '+':
        calc = num1 + num2
    elif op == '-':
        calc = num1 - num2
    elif op == '*':
        calc = num1 * num2
    elif op == '/':
        calc = num1 / num2
    elif op == '%':
        calc = num1 % num2
    
    if math != 'exit':
        print(math + " = " + str(int(calc)))
    
    exit = math 
