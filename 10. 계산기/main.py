#로고
from art import logo
from replit import clear

#덧셈
def add(a, b):
  return a+b
#뺄셈
def subtract(a, b):
  return a-b

#곱셈
def multiply(a, b):
  return a*b

#나누기
def divide(a, b):
  return a/b

operation = {
  "+": add, 
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  continue_operation = True
  num1 = float(input("첫번째 숫자를 입력하세요: "))
  
  while continue_operation:
    for symbol in operation:
      print(symbol)
    operation_symbol = input("어떤 연산을 하시겠습니까?\n연산자:")
    num2 = float(input("연산할 숫자를 입력하세요: "))
    answer = operation[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_operation = input("연산을 계속 하시겠습니까? y or n").lower()
    if continue_operation == "n":
      continue_operation = False
      clear()
      calculator()
    else:
      num1 = answer
      

calculator() 
  