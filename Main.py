import sys
import StaticImages
from os import system
from colorist import Color, BrightColor 
print(f"This is a {Color.RED}Red Test{Color.OFF} I hope it {BrightColor.YELLOW}works!{BrightColor.OFF}")
tert = input("test")
system('cls')
StaticImages.MainMenuImage()
tret = input(" ")
sys.exit()