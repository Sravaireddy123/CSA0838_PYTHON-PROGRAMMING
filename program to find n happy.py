#happy number
num=int(input("num:"))
def happy_num(n):
 past=set()
 while n!=1:
        n=sum(int(i)**2for i in str(n))
        if n in past:
           return False
        past.add(n)
 return True
print(happy_num(num))
