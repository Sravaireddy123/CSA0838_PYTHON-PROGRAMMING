#program to find grade and average marks of a student
s1=int(input("marks s1="))
s2=int(input("marks s2="))
s3=int(input("marks s3="))
t=s1+s2+s3
print("total=",t)
if(t>=300):
    print(" S grade")
    if(t>=250 and t<300):
        print(" A grade")
        if(t>=200 and t<250):
                print("B grade")
                if(t<200):
                    print(" fail")
average=t/3
print("average=",average)
                      
    
    
