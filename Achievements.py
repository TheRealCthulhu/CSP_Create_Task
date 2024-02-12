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
  NL()
  if "itBegins" not in Unlocked:
    print(f"{BgColor.RED}???{BgColor.OFF}")
    print("???")
  else:
    print(f"{Color.GREEN}And so it Begins{Color.OFF}")
    print("Welcome to The House")
  NL()
  if "theEnd?" not in Unlocked:
    print(f"{BgColor.RED}???{BgColor.OFF}")
    print("???")
  else:
    print(f"{Color.GREEN}The End?{Color.OFF}")
    print("That's it? For now...")
    
  '''NL()
  if "welcomeHome" not in Unlocked:
    print(f"{BgColor.RED}???{BgColor.OFF}")
    print("???")
  else:
    print(f"{Color.GREEN}Welcome Home{Color.OFF}")
    print("No wonder it felt familiar")
  '''
  
  
  
  
  leave = input("".rjust(193//2)).lower()
  if leave == "back" or leave == "exit":
    Clear()
    StaticImages.MainMenuImage()