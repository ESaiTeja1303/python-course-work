#generators
def stream_music(playlist):
  for song in playlist:
    yield song
playlist={
  "telugu": ["Chaleya.mp3", "Sanamtherikasam.mp3", "Devara.mp3", "Saalar.mp3", "vaadire.mp3"],
  "hindi": ["TumHiHo.mp3", "Kesariya.mp3", "ApnaBanaLe.mp3", "Zinda.mp3", "Kalank.mp3"],
  "english": ["BlindingLights.mp3", "ShapeOfYou.mp3", "Senorita.mp3", "Believer.mp3", "Perfect.mp3"],
  "malayalam": ["JimikkiKammal.mp3", "Malare.mp3", "EntammedeJimikki.mp3", "Aaradhike.mp3", "VathikkaluVellaripravu.mp3"],
  "tamil": ["WhyThisKolaveriDi.mp3", "VaathiComing.mp3", "RowdyBaby.mp3", "AnbilAvan.mp3", "ArabicKuthu.mp3"],
  "kanada": ["Karabuu.mp3", "NeeneModalu.mp3", "Belageddu.mp3", "Raajakumara.mp3", "YenammiYenammi.mp3"]
}
p=int(input("Enter 1 to Login and 0 to logout"))
if p==1:
  print("Welcome to Spotify!!!")

  while True:
    i=1
    for key in playlist:
      print(f"{i}.{key}")
      i+=1
    k=input("\nEnter the language or enter 0 to logout: ")
    if k!="0":
      s=stream_music(playlist[k])
      while True:
        m=int(input("Enter number 1 to play and 0 to exit : "))
        if m==1:
          print(next(s))
        else:
          break
    else:
      break
print("Thank you for using Spotify!!!")