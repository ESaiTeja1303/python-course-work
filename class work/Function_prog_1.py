

#1. Add Two Numbers
def add(a,b):
  return a+b
print(add(int(input("Enter first number: ")),int(input("Enter second number: "))))

#2. Square a Number
def square(a):
  return a*a
print(square(int(input("Enter a number: "))))

#3.area of circle
def area_of_circle(r):
  return (3.14*r*r)
print(area_of_circle(int(input("Enter radius of circle: "))))

#4.Greeting
def greet(a):
  return a
print("Hello,",greet(input("Enter your name: ")))

#5.c --> f
def c_to_f(t):
  k=(t*9/5)+32
  return k
print(c_to_f(int(input("Enter temperature in celsius: "))))

#6.multiplication of 3 numbers
def mul(a,b,c):
  return a*b*c
a,b,c=map(int,input("Enter three numbers: ").split())
print(mul(a,b,c))

#7.simple interest
def interest(p,r,t):
  return (p*r*t)/100
p,r,t=map(int,input("Enter principle,rate,time: ").split())
print(interest(p,r,t))

#8.length of string
def lenth_of_string(s):
  c=0
  for i in s:
    c+=1
  return c

print(lenth_of_string(input("Enter a string: ")))

#9.appending element
def append(l,d):
  l.append(d)
  print(l)
l=list(map(int,input("enter the numbers: ").split()))
d=int(input("enter the number to append: "))
append(l,d)

#10. Double Each Element in a List
def double(l):
  return list(map(lambda x:x*2,l))
l=list(map(int,input("enter numbers space separated : ").split()))
print(double(l))

#11. Sort a List
def sor(l):
  l.sort()
  return l
l=list(map(int,input("enter numbers space separated : ").split()))
print(sor(l))

#12. Clear a List Inside Function
def clear(l):
  l.clear()
  return l
l=list(map(int,input("Enter the numbers space sperated: ").split()))
print("cleared list : ",clear(l))

#13. Update Dictionary Value
def update(d,k,v):
  d[k]=v
  return d
t=input("Enter dictionary: ")
d=dict(eval(t))
k=input("Enter key: ")
v=input("Enter value: ")
if v.isdigit():
  v=int(v)
print(update(d,k,v))

#14. Remove Element from List by Value
def remove_element(l,r):
  l.remove(r)
  return l
l=list(map(int,input("Enter the numbers space sperated: ").split()))
r=int(input("Enter the number to remove: "))
print("Updated list : ",remove_element(l,r))

#15. Add Key to Dictionary
def Add_key(d,k,v):
  d[k]=v
  return d

g=input("Enter dictionary: ")
d=eval(g)
k=input("Enter new key: ")
v=input("Enter new value:")
if v.isdigit():
  v=int(v)
print(Add_key(d,k,v))

#16. Increment All Values in Dictionary
def inc_value(d):
  for key,value in d.items():
    d[key]=value+1

  return d
g=input("Enter dictionary: ")
d=eval(g)
print(inc_value(d))

#17. Factorial of a Number
def factorial(n):
  a=1
  for i in range(1,n+1):
    a*=i
  return a
n=int(input("Enter a number: "))
print(factorial(n))

#18. Fibonacci Number (Nth Term)
def fibnocci_of_nth_term(n):
  l=[0,1]
  for i in range(2,n+1):
    l.append(l[i-1]+l[i-2])
  print(l)
  return l[-1]


n=int(input("Enter the number: "))
print(fibnocci_of_nth_term(n))

#19. Sum of First N Natural Numbers
def sum_of_n_natural_numbers(n):
  sum=0
  for i in range(1,n+1):
    sum+=i
  return sum

n=int(input("Enter a number: "))
print(sum_of_n_natural_numbers(n))

#20. Reverse a String Using Recursion
def reverse_str(s):
  if len(s)==0:
    return s
  else:
    return reverse_str(s[1:])+s[0]

s=input()
print(reverse_str(s))

#21. Power of a Number (a^b using recursion)

def power_of_num(a,b):
  k=a**b
  return k
n=int(input("Enter the base number: "))
p=int(input("Enter the power: "))
print(power_of_num(n,p))

#22. Sum of Digits Using Recursion
def sum_of_digits(n):
  sum=0
  while n>0:
    r=n%10
    sum+=r
    n=n//10
  return sum

n=int(input("Enter the number: "))
print(sum_of_digits(n))

#23. Check Palindrome String Using Recursion
def is_Palindrome(s):
  if s==s[::-1]:
    return True
  else:
    return False

s=input("Enter the string: ")
print(is_Palindrome(s))

#24. GCD of Two Numbers Using Recursion
def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)


a,b=map(int,input("Enter two numbers: ").split())
print("GCD is",gcd(a,b))

#25. Maximum of Three Numbers Using max()
def max_of_three(a,b,c):
  return max(a,b,c)

a,b,c=map(int,input("Enter three numbers: ").split())
print(max_of_three(a,b,c))

#26. Sort a List Using sorted()
def sort_list(l):
  return sorted(l)
l=list(map(int,input("Enter the numbers space sperated: ").split()))
print(sort_list(l))

#27. Sum of Elements Using sum()
def sum_of_elements(l):
  return sum(l)
l=list(map(int,input("Enter the numbers space sperated: ").split()))
print(sum_of_elements(l))

#28. Find Data Type Using type()
def find_type(d):
  try:
    i=eval(d)
  except:
    i=d
  return type(i)
n=input("Enter the data: ")
print(find_type(n))

#29. Print Even Numbers up to N
def even_num(n):
  for i in range(n+1):
    if i%2==0:
      print(i,end=" ")

n=int(input("Enter the range: "))
even_num(n)

#30. Return List of Squares
def list_of_squares(l):
  return list(map(lambda x:x*x,l))

l=list(map(int,input("Enter the numbers space sperated: ").split()))
print(list_of_squares(l))

#31. Check if Number is Prime
def is_prime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True


n=int(input("Enter the num: "))
print(is_prime(n))

#32. Count Vowels in a String
def vowels_count(s):
  c=0
  e="aeiou"
  for i in s:
    if i in e:
      c+=1
  return c

s=input("Enter the word : ")
print(vowels_count(s))

#33. Multiply by 2 Using Lambda
def mul_by_2(n):
  y=lambda x:x*2
  return y(n)
n=int(input("Enter the num: "))
print(mul_by_2(n))

#34. Square List Using map() and Lambda
def sq_li(l):
  return list(map(lambda x:x*x,l))

l=list(map(int,input("enter the numbers space separated : ").split()))
print(sq_li(l))

#35. Filter Even Numbers Using filter() and Lambda
def eve(l):
  return list(filter(lambda x:x%2==0,l))

l=list(map(int,input("enter the numbers space separated : ").split()))
print(eve(l))

#36. Sort Tuples by Second Value Using Lambda
def sort_tuples_second_value(tuple_list):
  return sorted(tuple_list, key=lambda x: x[1])



input_str = input("Enter list of tuples: ")

tuple_list = [eval(t) for t in input_str.replace('),', ') ').split()]

print("Sorted list:", sort_tuples_second_value(tuple_list))