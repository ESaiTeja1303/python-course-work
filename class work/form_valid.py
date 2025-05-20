import re
from datetime import  datetime

#1.Validate Full Name
def validate_name(name):
  pattern=r'^[A-Za-z]{2,25} ([A-Za-z]{2,25})+$'
  return bool(re.fullmatch(pattern,name))
#2.Validate Email
def validate_email(email):
  pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  return bool(re.fullmatch(pattern,email))
#3. Validate Phone Number
def validate_phone(phone):
  pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
  print(bool(re.fullmatch(pattern,phone)))
  return bool(re.fullmatch(pattern,phone))
  print(phone)

#
#4.Validate Password
def validate_password(password):
  pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
  return bool(re.fullmatch(pattern,password))
#5.Validate username
def validate_username(username):
  pattern=r'^[a-zA-z0-9]{5,15}$'
  return bool(re.fullmatch(pattern,username))
#6.Validate DOB
def validate_dob(dob):
  try:
    datetime.strptime(dob,"%Y-%m-%d")
    return True
  except ValueError:
    return False
def get_valid_input(prompt,validation_func):
  while True:
    user_input=input(prompt)
    if validation_func(user_input):
      return user_input
    else:
      print("Invalid input, please try again!!")
def main():
  print("\nFORM VALIDATION PROGRAM USING REGULAR EXPRESSION\n")
  name=get_valid_input("Enter full name (e.g., John Doe)",validate_name)
  email=get_valid_input("Enter your email : ",validate_email)
  phone=get_valid_input("Enter your phone number: ",validate_phone)
  username=get_valid_input("Create a username (5-15 alphanumeric characters): ",validate_username )
  password=get_valid_input("Create a password (min 8 chars, 1 uppercase,1 num,1 special char)",validate_password)
  dob=get_valid_input("Enter your date of birth(YYYY-MM-DD): ",validate_dob)
  print("\n All fields validated successfully.")
  print("Form submitted successfully")

if __name__=="__main__":
  main()