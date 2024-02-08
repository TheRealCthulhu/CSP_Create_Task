import StaticImages
from GeneralFunctions import Clear, NL
from colorist import Color, BrightColor, BgColor
Unlocked = []
def AchievementDisplay():
  print("Back\n")
  if "drivenToMadness" not in Unlocked:
    print(f"{BgColor.RED}???{BgColor.OFF}")
    print("???")
  else:
    print(f"{Color.GREEN}Driven to Madness{Color.OFF}")
    print("That's a lot of driving.")
  NL()
  if "sleepTight" not in Unlocked:
    print(f"{BgColor.RED}???{BgColor.OFF}")
    print("???")
  else:
    print(f"{Color.GREEN}Sleep Tight{Color.OFF}")
    print("What house?")
  
  
  
  
  
  
  leave = input("".rjust(193//2)).lower()
  if leave == "back" or leave == "exit":
    Clear()
    StaticImages.MainMenuImage()