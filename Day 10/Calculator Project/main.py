from django.db.models.expressions import result
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2


def multiply(n1,n2):
    return n1 * n2


def divide(n1, n2):
    return n1 * n2


cal_dict = {
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator_fun():
    print(art.logo)
    calculator = True
    num_1 = float(input("Enter thr first number: "))

    while calculator :
        for symbol in cal_dict:
            print(symbol)
        operation_symbol = input("pick an operation: ")
        num_2 = float(input("Enter the next number: "))

        answer = cal_dict[operation_symbol](num_1,num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {answer}")
        choice = input("Want to continue calculation with  previous result, type 'y':  ").lower()



        if choice == "y":
            num_1 = answer
            print("\n" * 20)
        else:
            calculator = False
            calculator_fun()

calculator_fun()