from colorist import Color, BrightColor
from GeneralFunctions import Clear
import Vars








def MainMenuImage():
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
    print(f"{BrightColor.BLACK}Continue{BrightColor.OFF}".center(210," "))
    print(f"{BrightColor.GREEN}New Game{BrightColor.OFF}".center(210," "))
    print(f"{BrightColor.BLACK}Achievements{BrightColor.OFF}".center(210," "))
    print(f"{Color.RED}Exit{Color.OFF}".center(210," "))
  elif Vars.HasSave == True:
    print(f"{BrightColor.GREEN}Continue{BrightColor.OFF}".center(210," "))
    print(f"{BrightColor.GREEN}New Game{BrightColor.OFF}".center(210," "))
    print(f"{BrightColor.BLACK}Achievements{BrightColor.OFF}".center(210," "))
    print(f"{Color.RED}Exit{Color.OFF}".center(210," "))
  Option = input("".rjust(193//2)).lower()
  if Option == "exit":
    Clear()
    print("Are you sure? Yes/No".center(210, " "))
    Exit = input("".rjust(193//2)).lower()









