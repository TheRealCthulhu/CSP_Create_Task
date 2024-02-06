Unlocked = []
def AchievementDisplay():
  if "drivenToMadness" not in Unlocked:
    print("\033[1m" +"???" + "\033[0m")
    print("???")
  else:
    print("\033[1m" + "Driven to Madness" + "\033[0m")
    print("That's a lot of driving.")