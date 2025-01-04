def add(a,b):
    print(a+b)
    return a+b
def sub(a,b):
    print(a-b)
    return a-b
def mul(a,b):
    print(a*b)
    return a*b
def div(a,b):
    if b == 0:
        print("除数不能为零")
    else:
        print(a/b)
        return a/b
def quit():
    print("输入错误")
print("*"*50)
print("\t\t选择运算：\n"
        "\t\t\t1. 加\n"
        "\t\t\t2. 减\n"
        "\t\t\t3. 乘\n"
        "\t\t\t4. 除")
print("*"*50)
while True:
    choice = input("输入你的选择(1/2/3/4): ")
    num1 = float(input("输入第一个数字: "))
    num2 = float(input("输入第二个数字: "))
    if choice == '1':
        add(num1,num2)
    elif choice == '2':
        sub(num1,num2)
    elif choice == '3':
        mul(num1,num2)
    elif choice == '4':
        div(num1,num2)
    else:
        quit()
        break