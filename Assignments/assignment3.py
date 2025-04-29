#Eraram Sai Teja Goud
# **Assignment - 3***#
n=int(input("Enter the number of messages : "))
chats={}
for i in range(n):
    name, chat = input().split(":", 1)
    name = name.strip()
    chat = chat.strip()
    if name in chats:
        chats[name].append(chat)
    else:
        chats[name] = [chat]

print(chats)
print(chats.keys())


def options():
  l=["Exit","Count total number of messages","Identify unique users in the chat","Count total words in the chat","Calculate average words per message","Find the longest message sent",
  "Find the most active user","Get message count for a specific user","Find the most frequently used word by a specific user","Retrieve the first and last message sent by a user",
  "Check if a user is present in the chat","Find commonly repeated words","Identify the user with the longest average message length","Count how many messages mention a specific user",
    "Remove duplicate messages","Sort messages alphabetically","Extract all questions asked in the chat","Calculate the reply ratio between two users","Check for deleted messages",
  ]
  for i in range(len(l)):
    print(f"{i}.{l[i]}")

def count_tn_of_messages(chats):
  c=0
  for key in chats.keys():
    c+=len(chats[key])
  return c

def unique_users(chats):
  l=set()
  for key in chats.keys():
    l.add(key)
  return f"{len(l)} \n{l}"

def total_words_chat(chats):
  c=0
  m=""
  for key in chats.keys():
    m+=" ".join(chats[key])+" "
  return len(m.split())

def average_words_per_message(chats):
  c=0
  m=""
  for key in chats.keys():
    m+=" ".join(chats[key])+" "
    k=len(m.split())
    c+=len(chats[key])
  return k/c

def longest_message(chats):
  m=""
  for key in chats.keys():
    for i in chats[key]:
      if len(i)>len(m):
        m=i
  return m

def most_active_user(chats):
  act_user=""
  m=0
  for key in chats.keys():
    if len(chats[key])>m:
      m=len(chats[key])
      act_user=key
  return act_user

def msgcount_specificuser(chats):
  user=input("Enter the user name : ")
  for key in chats.keys():
    if key==user:
      return len(chats[key])
  return "User not found"

def freq_word_specificuser(chats):
  user=input("Enter the user name : ")
  m=""
  for key in chats.keys():
    if key==user:
      m+=" ".join(chats[key])
      k=m.split()
  d={}
  for i in k:
    if i in d:
      d[i]+=1
    else:
      d[i]=1
  l=[]
  for value in d.values():
    l.append(value)
  m=max(l)
  for key,value in d.items():
    if value==m:
      return key

def first_last_message(chats):
  user=input("Enter the user name : ")
  for key in chats.keys():
    if key==user:
      return f"1st {user} : {chats[key][0]},\nlast {user} : {chats[key][-1]}"
  return "User not found"

def check_user(chats):
  user=input("Enter the user name : ")
  for key in chats.keys():
    if key==user:
      return "User found"
  return "User not found"

def common_words(chats):
  m=""
  for key in chats.keys():
    m+=" ".join(chats[key])+" "
    k=m.split()
  d={}
  for i in k:
    if k in d:
      d[k]+=1
    else:
      d[k]=1
  for key,value in d.items():
    if value>1:
      print(key,end=" ")

def longest_avg_msg_len(chats):
  m=""
  for key in chats.keys():
    for i in chats[key]:
      if len(i)>len(m):
        m=i
  k=len(m.split())
  return k


def count_specific_user(chats):
  user=input("Enter the user name : ")
  c=0
  for key in chats.keys():
    if key==user:
      for i in chats[key]:
        if user in i:
          c+=1
  return f"Messages mentioning {user} : {c}"

def remove_duplicates(chats):
  for key in chats.keys():
    chats[key]=list(set(chats[key]))
  return len(chats)

def sort_alphabetically(chats):
  nw=[]
  for key in chats.keys():
    for i in chats[key]:
      nw.append(i)
  return sorted(nw)

def extract_questions(chats):
  nw=[]
  for msgs in chats.values():
    for i in msgs:
      if "?" in i:
        nw.append(i)
  return nw

def calculate_reply_ratio(chats):
  a,b=input().split(" and ")
  a = a.strip()
  b = b.strip()
  count = 0
  if b in chats:
    for msg in chats[b]:
      if a in msg:
        count += 1
  return f"Reply ratio between {b} to {a} is {count}"

def check_for_deleted_msg(chats):
  nw=[]
  for key in chats.keys():
    for i in chats[key]:
      if "deleted" in i:
        nw.append(i)
  return len(nw)



while True:
  print("==="*15)
  print("Options : ")
  options()
  print("==="*15)
  choice=int(input("Enter your choice : "))
  if choice==1:
    print(f"Total Messages in chat : {count_tn_of_messages(chats)}")
  elif choice==2:
    print(f"Total unique users : {unique_users(chats)}")
  elif choice==3:
    print(f"Total words in chat : {total_words_chat(chats)}")
  elif choice==4:
    print(f"Average words per message : {average_words_per_message(chats)}")
  elif choice==5:
    print(f"Longest message : {longest_message(chats)}")
  elif choice==6:
    print(f"most active user : {most_active_user(chats)}")
  elif choice==7:
    print(f"Message count for a specific user : {msgcount_specificuser(chats)}")
  elif choice==8:
    print(f"Most frequently used word by a specific user : {freq_word_specificuser(chats)}")
  elif choice==9:
    print(f"Retrieve the first and last message sent by a user : {first_last_message(chats)}")
  elif choice==10:
    print(f"Check if a user is present in the chat : {check_user(chats)}")
  elif choice==11:
    print(f"commonly repeated words : {common_words(chats)}")
  elif choice==12:
    print(f"longest avg msg len : {longest_avg_msg_len(chats)}")
  elif choice==13:
    print(f"Count how many messages mention a specific user : {count_specific_user(chats)}")
  elif choice==14:
    print(f"Remove duplicate messages : {remove_duplicates(chats)}")
  elif choice==15:
    print(f"Sort messages alphabetically:{sort_alphabetically(chats)}")
  elif choice==16:
    print(f"Extract all questions asked in the chat : {extract_questions(chats)}")
  elif choice==17:
    print(f"Calculate the reply ratio between two users : {calculate_reply_ratio(chats)}")
  elif choice==18:
    print(f"Check for deleted messages : {check_for_deleted_msg(chats)}")
  elif choice==0:
    break
  else:
    print("Invalid choice")
