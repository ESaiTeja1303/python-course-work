# Eraram Sai Teja Goud (PFS:22)
# Sharing photos from photo Gallery

photo=["beach.png","mountain.png","party1.png","Selfie.png","birthday.png","concert.jpg","sunset.png","trip1.png"]
print("Photo Gallery : ")
for i in range(len(photo)):
  print(f'{i+1}. {photo[i]}')

print("Select Photos to share (enter numbers separated by space) : ")
n=list(map(int,input("Your Selection : ").split(" ")))
s=set()
print("Sharing the following photos: ")
for i in n:
  if i>len(photo):
    print(f"Invalid Selection {i}. {i}th item not in Gallery")
  else:
    s.add(photo[i-1])
for i in s:
  print(f"{i} successfully shared!")

