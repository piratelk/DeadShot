y=[]
st=0
x=int(input("Enter binary value : "))
s=str(x)
y2=len(s)
a=0

#input add to list
for n in range(y2):
    y.append(s[a])
    a=a+1
print(y)
y.reverse()
print(y)
 
#line break
print("\n")


#binary converter script
b=0
for q in range(y2):
    l=int(y[b])*2**b
    st=st+int(l)
    b=b+1
print("Decimal value is : ",st)
    
    



