n=int(input("Enter the number: "))
c=0
for i in range(1,n):
  if i%3==0:
    c+=1
print(f"Number of numbers div by 3 is {c}")

# n//3  {use this if no loops are allowed}