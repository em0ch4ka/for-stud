def sum(a,b):return a + b

def multi(a,b): return a * b

def division(a,b):return a / b

def subtraction(a,b):return a - b

def calculate(a,b,op):
    if op == "sum":
        return sum(a,b)
    elif op == "multi":
        return multi(a,b)
    elif op == "division":
        return division(a,b)
    elif op == "subtraction":
        return subtraction(a,b)
    else:
        return "Ошибка"
    


a = int(input("Веберите 1 число"))
b = int(input("Веберите 2 число"))
op = input(f"Веберите операцию (sum,multi,division,subtraction): ")

result = calculate(a,b,op)
print(result) 


    