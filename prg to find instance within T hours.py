E=[]
L=[]
T=int(input("Range T :"))
for i in range(T):
    e=int(input("E : "))
    E.append(e)
for i in range(T):
    l=int(input("L : "))
    L.append(l)
sum=0
max=0
for i in range(T):
    sum+=E[i]-L[i]
    max=max(Sum,Max)
print ("output", Max)
