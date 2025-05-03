class Institute:
  batchno=22
  @classmethod
  def changebatch(cls,batchno):
    cls.batchno=batchno
    print(cls.batchno,"Inside the cls method")
  
  def setdetails(self,name,course):
    self.name=name
    self.course=course

  def display(self):
    print(f'welcome to {self.course} course {self.name} {Institute.batchno}')
  
  @staticmethod
  def fee():
    print("1 Lakh")

Dinesh=Institute()
Dinesh.setdetails("Dinesh","Python")
Dinesh.display()
Dinesh.fee()

Saiteja=Institute()
Saiteja.setdetails("Saiteja","Java")
Saiteja.display()
Institute.fee()

Institute.changebatch(50)

Saiteja.display()
Dinesh.display()


