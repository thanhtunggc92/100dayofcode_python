
from logo import Logo

print(Logo)

def add(n1,n2):
    return n1+n2
def minus(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2 
operator_dict={
    "+":add,
    "-":minus,
    "*":multiply,
    "/":divide,
    
}
# if operator == "+":
#     print(add(first_number,second_number))
# elif operator == "-":
#    print( minus(first_number,second_number))
# elif operator == "*":
#    print( multiply(first_number,second_number))
# elif operator == "/":
#    print( divide(first_number,second_number)   )
first_number= float(input("what is the first numer?"))
for key in operator_dict:
    print(key)
cal=True
answer=0
while cal:
    operator=input("Pick an operator: ")
    second_number=float(input("what is the next number?"))

    calculation= operator_dict[operator]
    answer=(calculation(first_number,second_number))

    print(f"{first_number}{operator}{second_number}={answer}")
    asking=input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to exit")
    
    if asking =='y':
        first_number=answer
    elif asking =='n':
        cal= False
