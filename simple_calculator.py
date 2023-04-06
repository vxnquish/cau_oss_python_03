# %% Homework #2

# 사용자에게 연산방법을 문자열로 입력을 받은 후
# 정수 2개를 입력받아 연산을 수행하는 프로그램

# 연산방법은 "+", "-", "*", "/", "%", "end" 6가지이며,
# "+"일 경우 덧셈(add) "-"일 경우 뺄셈(sub)
# "*"일 경우 곱셈(mul) "/"일 경우 나눗셈(div)
# "%"일 경우 나머지(mod)를 수행하며
# "end"일 경우 반복을 종료하고 "Exit program"을 출력하고 종료한다.
# 그 외 입력의 경우 "Invalid operator"을 출력한다.

# +와 -는 함수로 정의하고 (익명함수X, def)
# *와 /, %는 익명함수(lambda)로 바로 사용한다.

# 연산은 arithmetic_ops 함수를 호출하며 수행한다.
# arithmetic_ops는 연산에 관한 함수로, 내부에서 사용자에게 정수 2개를 입력받은 뒤
# 전달받은 매개함수로 정수를 전달한다

def arithmetic_ops(op):
    num1 = int(input("Input 1st Number:"))
    num2 = int(input("Input 2nd Number:"))
    return num1, num2, op(num1, num2)

# +와 -는 함수로 정의한다
def sum(num1, num2): 
    return num1+num2
def sub(num1, num2): 
    return num1-num2

while True:
    op = input("Input Operation:")
    if op == "end": #종료
        break
    elif op == "+": # 합
        num1, num2, ret = arithmetic_ops(sum)
    elif op == "-": # 차
        num1, num2, ret = arithmetic_ops(sub)
    elif op == "*": # 곱
        num1, num2, ret = arithmetic_ops(lambda x,y: x*y)
    elif op == "/": # 몫
        num1, num2, ret = arithmetic_ops(lambda x,y: x/y)
    elif op == "%": # 나머지
        num1, num2, ret = arithmetic_ops(lambda x,y: x%y)
    else: # 오류
        print("Invalid operation.")
        continue
    print(f"{num1}{op}{num2} = {ret}")  # 연산 결과를 출력
print("Exit Program.")