l=list(map(int,input("Enter the numbers space separated: ").split()))
ma=l[0]
mi=l[0]
for i in range(len(l)):
  if ma<l[i]:
    ma=l[i]
  elif mi>l[i]:
    mi=l[i]
print(f"max : {ma} , min : {mi}")