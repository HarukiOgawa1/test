a=1
b=2
c=3
print(a,b,c)
x=0
for i in range(3):
    if b<c:
        x=b
        b=c
        c=x
    if a<b:
        x=a
        a=b
        b=x

print(a,b,c)
