"""n=int(input("Enter the number  : "))
if str(n)==str(n)[::-1]:
  print("Palindrome Num")
else:
  print("Not a paloindrome num")"""

n=int(input("Enter the number : "))
t=n
rev=0
while n>0:
      d=n%10
      rev=(rev*10)+d
      n=n//10
if rev==t:
      print("Palindrome")
else:
      print("no")