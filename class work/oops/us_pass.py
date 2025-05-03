class Institute:
  def __init__(self,username,password):
    self.username=username
    self.password=password
  def login(self):
    if self.username and self.password:
      print("Login Successful",self.username)
    else:
      print("Login Failed",self.username)
Teja=Institute("Teja","1234")
Teja.login()

Dinesh=Institute("Dinesh","0")
Dinesh.login()