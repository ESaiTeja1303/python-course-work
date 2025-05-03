class EvenorOdd:
  def __init__(self,num):
    self.num=num
  def check(self):
    if self.num%2==0:
      print(self.num,"is even")
    else:
      print(self.num,"is odd")
while True:
  num=int(input("Enter the number: "))
  if num!=0:
    obj=EvenorOdd(num)
    obj.check()
  else:
    break