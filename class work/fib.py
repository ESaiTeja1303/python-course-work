n=int(input("Enter input : "))
a=0
b=1
if n==0:
  print("none")
elif n==1:
  print(a)
elif n==2:
  print(a,b)
elif n>2:
  print(a,b,end=" ")
  for i in range(n-2):
    t=a+b
    a=b
    b=t
    print(t,end=" ")