n=int(input("Enter the range : "))
s=0
for i in range(2,n+1):
  p=0
  for j in range(1,i+1):
    if i%j==0:
      p+=1
  if p<3:
    print(i)
    s+=i
print(f"Sum of prime nos in given range : {s}")