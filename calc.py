
TITLE = 'Smart Calculator'

# separators = '+-*/%**//'
separators = ['+','-', '*', '/', '%', '**', '//']

first_operand = second_operand = 0
operation = ''
result = ''

def hello():
    # print("Hi! It's me, " + TITLE)
    print(f"Hi! It's me, {TITLE}")
    return input("Type a formula or (h|q): ")


def help_calc():
    print(f"""
    {'_'*70}
        Type a formula like:
            x + y for addition
            x - y for substraction
            x / y for division\n          
    {'_'*70}""")

# 2 + 2 3+3 5 +6 8+ 6 h q help quit exit ex qu hel hhh H Q HELP

    
while True:
    formula = hello()

    formula = formula.lower()

    if formula.startswith('q') or formula.startswith('h'):
        formula = formula[0:1]
    match formula:
        case 'h':
            help_calc()
        case 'q' | 'exit':
            print(F'Thank You for using {TITLE}')
            break
        case _:
            for sep in separators:
                # print(f"Separator {sep} => {sep in separators}") 
                if len(formula.split(sep)) == 2:
                    first_operand, second_operand = formula.split(sep)
                    first_operand = first_operand.strip()
                    second_operand = second_operand.strip()
                    
                    if first_operand.isdigit():
                        first_operand = float(first_operand)
                    else:
                        result = f"{first_operand} not a number"
                        break
                    if second_operand.isdigit():
                        second_operand = float(second_operand)
                    else:
                        result = f"{second_operand} not a number"
                        break
                    
                    
                    operation = sep
                    # print(first_operand, second_operand, operation)
                    match operation:
                        case '+':
                            res = first_operand + second_operand
                            # print(res)
                        case '-':
                            res = first_operand - second_operand
                        case '//':
                            res = first_operand // second_operand
                        case '%':
                            res = first_operand % second_operand
                        case _:
                            res = 'Operation not recognized!'
                            
                    result = f'{first_operand} {operation} {second_operand} = {res}'
                    # print(result)
                    # print(first_operand, second_operand)
                    break
                else:
                    result = "Bad command or formula! Try agin, please"
                    
    print(f"Here You are: {result}")
