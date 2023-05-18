# %% 

def arithmetic_ops(op):
    num1 = int(input("Input 1st Number:" + " "))
    num2 = int(input("Input 2nd Number:" + " "))
    return num1, num2, op(num1, num2)

# +와 -는 함수로 정의한다
def sum(num1, num2): 
    return num1+num2
def sub(num1, num2): 
    return num1-num2

while True:
    op = input("Input Operation:" + " ")
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
    else:           # 오류
        print("Invalid operation.")
        continue
    print(f"{num1} {op} {num2} = {ret}")  # 연산 결과를 출력
print("Exit Program.")


# %%
