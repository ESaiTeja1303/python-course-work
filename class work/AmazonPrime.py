# Eraram Sai Teja Goud (PFS:22)

products={"Iphone":10,"Laptop":2,"Butter":4,"Cookies":0,"TV":0,"AC":2,"Washing Machine":0}
user={"Sai Teja":{"PrimeMember":"True","Discount":"True","Password":"SaiTeja123@"},
      "Vishal":{"PrimeMember":"True","Discount":"False","Password":"Vishal@123"},
      "Ram":{"PrimeMember":"False","Discount":"True","Password":"Ram111@"},
      "Manohar":{"PrimeMember":"False","Discount":"False","Password":"Manohar5@"}}
user_name=input("Enter user username: ")
password=input("Enter user password: ")
if user[user_name]["Password"]==password:
  print("Login Successful!!!")
  print("Products available in store")
  for key in products:
    print(key,end=",")
  product=input("\nEnter the product name: ")
  stock=products[product]
  if stock>0:
    print("Stock is available")
    if user[user_name]["PrimeMember"]=="True" and user[user_name]["Discount"]=="True":
      print("You are a PrimeMember and you are eligible for discount too")
    elif user[user_name]["PrimeMember"]=="True" and user[user_name]["Discount"]=="False":
      print("You are a PrimeMember and you are not eligible for discount")
    elif user[user_name]["PrimeMember"]=="False" and user[user_name]["Discount"]=="True":
      print("You are not a PrimeMember and you are eligible for discount")
    else:
      print("You are not a PrimeMember and you are not eligible for discount")
  else:
    print("Stock is not available")
else:
  print("Login Failed!!!")
  print("Please try again")
