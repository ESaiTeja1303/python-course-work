
#Eraram Sai Teja Goud (PFS - 22) 

products={"Iphone":40000,"Laptop":85000,"Headphones":2500,"Smartwatch":7000,"Backpack":1500,"AC":30000,"Washing Machine":25000,"Mouse":800}
pro={1:"Iphone",2:"Laptop",3:"Headphones",4:"Smartwatch",5:"Backpack",6:"AC",7:"Washing Machine",8:"Mouse"}
print("Available Products: ")
i=0
for key,value in products.items():
  i+=1
  print(f'{i}. {key} - ₹{value}')
print("\nAdd items to your cart (Enter product numbers separated by spaces) : ")

n=list(map(int,input("Your Selection : ").split()))

d=dict()
for i in n:
  if i in d:
    d[i]+=1
  else:
    d[i]=1

print("Your Shopping Cart: ")

for key,value in d.items():
  print(f'{pro[key]} x {value} = ₹{products[pro[key]]*value}')

print(f'Total items in your cart: {len(n)}')
print(f'Total Amount : ₹{sum(products[pro[key]]*value for key,value in d.items())}')
