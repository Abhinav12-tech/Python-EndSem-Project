x=str(input())
y=str(input())
z=str(input())
a=str(input("Enter Keyword: "))
m=x.split(' ')
n=y.split(' ')
o=z.split(' ')

c1,c2,c3=0,0,0
for i in m:
  if i == a:
    c1 += 1
for j in n:
  if j == a:
    c2 += 1
for k in o:
  if k == a:
    c3 += 1
D=[]
D.append(c1)
D.append(c2)
D.append(c3)
D.sort()
print(D)
A=[]
A.append(z)
A.append(y)
A.append(x)
print(A)