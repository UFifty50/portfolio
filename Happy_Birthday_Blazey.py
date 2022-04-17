import time
import datetime

now = datetime.datetime.now()
name = "Blazey"
sleepTime = 0.75
birthday = datetime.datetime(datetime.datetime.now().year, 1, 26)
timeUntilBirthday = birthday - now

def happyBirthday(name):
    if now.month == 1 and now.day == 26:
        print("\n")
        for i in range(2):
            print("Happy Birthday to you!")
            time.sleep(sleepTime)

        print("Happy birthday dear " + name+ "!")
        time.sleep(sleepTime)

        print("Happy Birthday to you!\n")
        time.sleep(sleepTime)

        for i in range(4):
            print("How old are you now?")
            time.sleep(sleepTime)

            print("I'm %d!" % (now.year - 2006))
            time.sleep(sleepTime)
    else:
        print("\nIt isnt your birthday just yet! You still have another %d days to go! " % int(366 + timeUntilBirthday.days))

def printCake():
    if now.month == 1 and now.day == 26:
        print("\n\t  v  v   v    v v  v  ")
        print("\t__|__|___|____|_|__|__")
        print("\t|                    |")
        print("\t|       |    |       |")
        print("\t|       |    |       |")
        print("\t|     \        /     |")
        print("\t|      \______/      |")
        print("\t|____________________|")
        print("\n\tHav sum cake :)")
    else:
        print("\n\t     /~~~~\      ")
        print("\t    /      \_    ")
        print("\t  _/         \   ")
        print("\t_/            \_ ")
        print("\t|               |")
        print("\t|               |")
        print("\t|               |")
        print("\t|_______________|")
        print("\n\tIt may not be your birtday, but you can still have sum volcano cake! :D")
if __name__ == "__main__":
    happyBirthday(name)
    printCake()
    print("\n\nFrom Fifty :3")

    while True:
         if input("\nAgain? (y/n): ") == "y" or "Y":
            happyBirthday(name)
            printCake()
            print("\n\nFrom Fifty :3")
         else:
            print("From Fifty :3")
            break
