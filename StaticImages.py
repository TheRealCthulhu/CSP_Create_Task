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

def HomeImage():
  Clear()
  print("                 ████                 ")
  print("              ██████████              ")
  print("           ████████████████           ")
  print("        ██████████████████████        ")
  print("      ██████████████████████████      ")
  print("    ██████████████████████████████    ")
  print("  ██████████████████████████████████  ")
  print(" ████████████████|▔▔|████████████████ ")
  print("█████████████████|▁▁|█████████████████")
  print("██████████████████████████████████████")
  print("██████████████████████████████████████")
  print("██████████████████████████████████████")
  print("██████████████████████████████████████")
  print("██████████████████████████████████████")
  print("████████████████      ████████████████")
  print("████████████████    * ████████████████")
  print("████████████████      ████████████████")
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
  print(f"                        {Color.WHITE}▆██▆{Color.OFF}   ".center(200, " "))
  print(f"{Color.RED} ▄▆▇████████████████████████{Color.OFF}     ".center(200, " "))
  print(f" {BgColor.RED}█▀▀██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀██{BgColor.OFF}".center(200, " "))
  print(" █  ██                 █  ██                           ")
  print("    ██                    ██                           ")
  Achievements.Unlocked.append("sleepTight")
  Vars.HasSave = True
  Wait(2)
  MainMenuImage()









