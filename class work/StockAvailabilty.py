#Eraram Sai Teja (PFS-22)
products={"Milk":10,"Bread":0,"Butter":4,"Cookies":3,"Eggs":0,"Chips":2}
for key in products:
  print(key)
product=input("Enter the product name: ")
if products[product]>5:
  print("Available")
elif 0<products[product]<6:
  print("Limited quantity")
else:
  print("Out of stock")
