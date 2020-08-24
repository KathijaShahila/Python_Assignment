a=input("Enter the String to be reversed")
a=a[::-1]
print(a)

b=input("Enter the string to count upper case and lower case")
count1=0
count2=0
for i in b:
    if (i.islower()):
        count1+=1
    elif(i.isupper()):
        count2+=1
    else:
        pass
print("Number of upper cases= ")
print(count2)
print("Number of lower cases= ")
print(count1)


print("-----FIBONACCI SERIES---")
low=int(input("starting number"))
high=int(input("last number"))

def countfib(low,high):
    f1,f2,f3=0,1,1
    result=0
    while(f1<=high):
        if f1>=low:
            print(f1)
            result+=1
        f1=f2
        f2=f3
        f3=f1+f2
    return result
print("number of fibonacci numbers ",countfib(low,high))

print("Student Marks")
import pandas as pd
df=pd.read_csv(r'C:\Users\Abdulla Safha Ahmed\Desktop\mark.csv')
print(df)
print("Student Name ,Total,Average")
for x in df.values:
    total=x[1]+x[2]+x[3]+x[4]
    avg=total/4
    print(x[0],total,avg)