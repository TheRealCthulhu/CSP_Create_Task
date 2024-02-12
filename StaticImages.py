from colorist import Color, BrightColor, BgColor
from GeneralFunctions import Clear, Wait, NL
import Vars, Animations, Achievements








def MainMenuImage():
  Clear()
  print("█████████████████     ███           ███     █████████████████".center(200, " "))
  print("▀▀▀▀▀▀█████▀▀▀▀▀▀     ███           ███     █████████████████".center(200, " "))
  print("      █████           ███           ███     ███              ".center(200, " "))
  print("      █████           ███▙▄▄▄▄▄▄▄▄▄▟███     ███              ".center(200, " "))
  print("      █████           █████████████████     ███████████████  ".center(200, " "))
  print("      █████           ███▛▀▀▀▀▀▀▀▀▀▜███     ███              ".center(200, " "))
  print("      █████           ███           ███     ███              ".center(200, " "))
  print("      █████           ███           ███     █████████████████".center(200, " "))
  print("      █████           ███           ███     █████████████████".center(200, " "))
  print("▄▄▄           ▄▄▄           ▄▄▄▄▄            ▄▄           ▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     ".center(204, " "))
  print("███           ███         ▟██▀▀▀██▙         ▟██           ██▙     █████████████████     █████████████████    ".center(204, " "))
  print("███           ███       ▟██▛     ▜██▙       ███           ███     ███▛                  █████████████████    ".center(204, " "))
  print("███           ███      ██▛         ▜██      ███           ███     ███                   ███                  ".center(204, " "))
  print("███▙▄▄▄▄▄▄▄▄▄▟███     ▟██           ██▙     ███           ███     ███▙                  ███                  ".center(204, " "))
  print("█████████████████     ██             ██     ███           ███     ▜███████████████▙     ███████████████      ".center(204, " "))
  print("███▛▀▀▀▀▀▀▀▀▀▜███     ▜██           ██▛     ███           ███                  ▜███     ███                  ".center(204, " "))
  print("███           ███      ██▙         ▟██      ███           ███                   ███     ███                  ".center(204, " "))
  print("███           ███       ▜██▙     ▟██▛       ▐██▙         ▟██▌                  ▟███     █████████████████    ".center(204, " "))
  print("███           ███         ▜██▄▄▄██▛          ▜█████████████▛      █████████████████     █████████████████    ".center(204, " "))
  print("▀▀▀           ▀▀▀           ▀▀▀▀▀              ▀▀▀▀▀▀▀▀▀▀▀         ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀     ".center(204, " "))
  print("\n\n")
  if Vars.HasSave == False:
    print(f"{BrightColor.GREEN}New Game{BrightColor.OFF}".center(210," "))
    print(f"{BrightColor.BLACK}Achievements{BrightColor.OFF}".center(210," "))
    print(f"{Color.RED}Exit{Color.OFF}".center(210," "))
  elif Vars.HasSave == True:
    print(f"{BrightColor.GREEN}New Game{BrightColor.OFF}".center(210," "))
    print(f"{BrightColor.GREEN}Achievements{BrightColor.OFF}".center(210," "))
    print(f"{Color.RED}Exit{Color.OFF}".center(210," "))
  Option = input("".rjust(193//2)).lower()
  if Option == "exit" or Option == "3":
    Clear()
    print("Are you sure? Yes/No".center(210, " "))
    Exit = input("".rjust(193//2)).lower()
    if Exit == "no" or Exit == "2":
      MainMenuImage()
    elif Exit == "yes" or Exit == "1":
      quit
  elif Option == "new game" or Option == "new" or Option == "1":
    Animations.Driving()
  elif Option == "achievements" or Option == "2":
    Clear()
    Achievements.AchievementDisplay()
  elif Option == "skip":
    Animations.Driving("skip")
  elif Option == "door":
    Door()

def HomeImage():
  Clear()
  print("                 ████                 ".center(200, " "))
  print("              ██████████              ".center(200, " "))
  print("           ████████████████           ".center(200, " "))
  print("        ██████████████████████        ".center(200, " "))
  print("      ██████████████████████████      ".center(200, " "))
  print("    ██████████████████████████████    ".center(200, " "))
  print("  ██████████████████████████████████  ".center(200, " "))
  print(" ████████████████|▔▔|████████████████ ".center(200, " "))
  print("█████████████████|▁▁|█████████████████".center(200, " "))
  print("██████████████████████████████████████".center(200, " "))
  print("██████████████████████████████████████".center(200, " "))
  print("██████████████████████████████████████".center(200, " "))
  print("██████████████████████████████████████".center(200, " "))
  print("██████████████████████████████████████".center(200, " "))
  print("████████████████      ████████████████".center(200, " "))
  print("████████████████    * ████████████████".center(200, " "))
  print("████████████████      ████████████████".center(200, " "))
  print("████████████████▁▁▁▁▁▁████████████████")
  print("                |     |               ")
  print("               /     /                ")
  print("              |     |                 ")
  print("               \     \                ")
  Clear(2)
  SleepEnding()
  
def SleepEnding():
  print("You make your way home and head to bed.".center(200, " "))
  print("")
  print("ACHIEVEMENT GET".center(210))
  print("SLEEP TIGHT".center(210))
  print("")
  print(f"                        {BrightColor.WHITE}▆██▆{Color.OFF}   ".center(200, " "))
  print(f"{Color.RED}     ▄▆▇████████████████████████{Color.OFF}     ".center(200, " "))
  print(f" {BgColor.RED}█▀▀██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀██{BgColor.OFF}".center(200, " "))
  print("                   █  ██                 █  ██                           ".center(200, " "))
  print("                      ██                    ██                           ".center(200, " "))
  Achievements.Unlocked.append("sleepTight")
  Vars.HasSave = True
  Wait(2)
  MainMenuImage()



def TheHouse():
  ToDoor = False
  Clear()
  print("You arrive at a decrepit house with what seems to be a tree growing out of the side".center(200, " "))
  print("It feels eerily familiar".center(200, " "))
  print(f"                     {Color.RED}| \___ |      |/ /{Color.OFF}".center(200, " "))
  print(f"                      {Color.RED}\_   \|      | |{Color.OFF} ".center(200, " "))
  print(f"                        {Color.RED}\__ |      |/{Color.OFF}  ".center(200, " "))
  print(f"                 ████      {Color.RED}\|      |{Color.OFF}   ".center(200, " "))
  print(f"              ██████████    {Color.RED}|      |\__{Color.OFF}".center(200, " "))
  print(f"         __███████████████  {Color.RED}|      |\__{Color.OFF}".center(200, " "))
  print(f"       _|     ████████████  {Color.RED}|      |{Color.OFF}   ".center(200, " "))
  print(f"     _|      ██████████████ {Color.RED}|      |{Color.OFF}   ".center(200, " "))
  print(f"    |     ██████████████████{Color.RED}|      |{Color.OFF}   ".center(200, " "))
  print(f"  ███   ████████████████████████████   ".center(200, " "))
  print(f" ████████████████    *███████████████  ".center(200, " "))
  print(f"█████████████████\    ████████████████ ".center(200, " "))
  print(f"███████████████████\  ████████████████ ".center(200, " "))
  print(f"██████████████████████████████████████ ".center(200, " "))
  print(f"██████████████████████████████████████ ".center(200, " "))
  print(f"██████████████████████████████████████ ".center(200, " "))
  print(f"██████████████████████████████████████ ".center(200, " "))
  print(f"█████████████████/     /██████████████ ".center(200, " "))
  print(f"████████████████/     /███████████████ ".center(200, " "))
  print(f"███████████████/     /████████████████ ".center(200, " "))
  print(f"██████████████/_▁▁▁/██████████████████ ".center(200, " "))
  print(f"                                       ".center(200, " "))
  print(f"                     *                 ".center(200, " "))
  print(f"                /                      ".center(200, " "))
  print(f"                   _                   ".center(200, " "))
  while ToDoor == False:
    print(f"Walk {BrightColor.RED}closer{BrightColor.OFF}?".center(200, " "))
    HouseChoice = input("".rjust(193//2)).lower()
    if HouseChoice == "yes":
      ToDoor = True
  Clear()
  if "itBegins" not in Achievements.Unlocked:
    Achievements.Unlocked.append("itBegins")
    print("ACHIEVEMENT GET".center(210))
    print("IT BEGINS".center(210))
    Clear(1)
  print("You feel drawn to the house".center(210))



def Door():
  doorChoice = ""
  Clear()
  print("As you get closer, you fully realize just how rotted the door is".center(200, " "))
  print("Though, there is a slight reddish color to some of it".center(200, " "))
  print("      _________ ".center(200, " "))
  print("     |         |".center(200, " "))
  print("    /_         |".center(200, " "))
  print(f"             {Color.RED}_|        |{Color.OFF} ".center(200, " "))
  print("   |          | ".center(200, " "))
  print("   |         |  ".center(200, " "))
  print("  |        /    ".center(200, " "))
  print(" |        |_    ".center(200, " "))
  print("|           |   ".center(200, " "))
  print(f"{Color.RED}         |__________|{Color.OFF}    ".center(200, " "))
  print("If there was ever a time to leave, it would be now".center(200, " "))
  print("Leave / Open the door".center(200, " "))
  doorChoice = input("".rjust(193//2)).lower()
  if doorChoice == "leave":
    HomeImage()
  elif doorChoice == "open":
    Clear()
  print("As you go to open the door, it falls to the ground, almost with a splat sound".center(200, " "))
  print("It almost seems to be writhing?".center(200, " "))
  Clear(.125)
  for i in range(5):
    Clear(.75)
    print("      _________ ".center(200, " "))
    print("     |         |".center(200, " "))
    print("    /_         |".center(200, " "))
    print("    _|        | ".center(200, " "))
    print("   |          | ".center(200, " "))
    print("   |         |  ".center(200, " "))
    print("  |        /    ".center(200, " "))
    print(" |        |_    ".center(200, " "))
    print("|           |   ".center(200, " "))
    print("|__________|    ".center(200, " "))
    Clear(.75) 
    print("      ________  ".center(200, " "))
    print("     \        \ ".center(200, " "))
    print("    |          |".center(200, " "))
    print("    /         / ".center(200, " "))
    print("   |          | ".center(200, " "))
    print("   |         |  ".center(200, " "))
    print("  _|       /    ".center(200, " "))
    print(" /         \    ".center(200, " "))
    print("|           |   ".center(200, " "))
    print("|__________|    ".center(200, " "))
    Clear(.75) 
    print("      ________  ".center(200, " "))
    print("     |        | ".center(200, " "))
    print("    |          |".center(200, " "))
    print("    |         | ".center(200, " "))
    print("   /          / ".center(200, " "))
    print("   /        _|  ".center(200, " "))
    print("  \        |    ".center(200, " "))
    print(" |         |    ".center(200, " "))
    print("/           /   ".center(200, " "))
    print("|___________    ".center(200, " "))
  End()
    
    
def End():
  Clear()
  print("Congratulations on completing the demo".center(210))
  NL()
  print("ACHIEVEMENT GET".center(210))
  print("THE END?".center(210))
  Achievements.Unlocked.append("theEnd?")
  Wait(4)
  MainMenuImage()
  
