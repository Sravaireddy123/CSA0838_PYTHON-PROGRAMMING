def daigonal(matrix,c):
    print("diagonal: ",end="")

    for i in range(c):
        print(matrix[i][i], end=",")
        print()

        
r=int(input("enter the number of rows:"))
c=int(input("enter the number of colums:"))
matrix=[]
print(" enter the entries row wise:")

for i in range(r):
    a=[]
for j in range(c):
    a.append(input())
    
daigonal(matrix,c)
