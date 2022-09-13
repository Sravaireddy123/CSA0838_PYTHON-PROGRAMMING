num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
choice=int(input("choice : "))
def subraction(n,m):
    sub=n-m
    return sub
if choice== 1:
    print(num1,"+",num2,"=",num1+num2)
elif choice== 2:
    print(num1,"-",num2,"=",substract(num1,num2))
elif choice== 3:
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice== 4:
    print(num1,"/",num2,"=",divide(num1,num2))
