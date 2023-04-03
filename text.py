# intro
import sys
import time

a = 2
b = 0.2
c = 0.08

def intro():
    time.sleep(a)
    print("Crowhat Studios Presents")
    time.sleep(a)
    print()
    print()
    print()
    print("Reaver")
    time.sleep(a)
    print()
    print()
    print()
    time.sleep(a)
    print("When an asteroid fall into the heart of Ravenfall, an outer god crawled out from it and cursing the world, sending demons and monsters on a rampage")
    time.sleep(a)
    print()
    print()
    time.sleep(a)
    print("Many stood up to these monsters, monsters that reaped all innocents.")
    time.sleep(b)
    print()
    time.sleep(a)
    print("You are the Raven, Lilith")
    time.sleep(a)
    print()
    time.sleep(a)
    print("The great fog comes, signaling the hunt. You pack your gun and katana and set out to reap the monsters")
    time.sleep(a)
    print()
    print("Your boots clicking on the stone pavement of Ravenfall, it was cold, high gothic buildings always looming over and the moon hardly gave light")
    time.sleep(a)
    print()
    print("Three different monsters approach you")
    time.sleep(c)
    print("1: Fight all three")
    time.sleep(c)
    print("2: Flee")
    time.sleep(c)
    print("3: Use your smoke bomb to limit their vision and pick them off one by one")
    time.sleep(b)

    firstPath = input("Which choice? 1/2/3:")
    time.sleep(c)
    if firstPath == "1":
        time.sleep(c)
        print()
        path1()
    elif firstPath == "2":
        time.sleep(c)
        print()
        path2()
    elif firstPath == "3":
        time.sleep(b)
        print()
        path3()
# Paths

def path1():

    print("You died!")



def path2():
    print("You are a coward, a hunter never runs")
    print("Game over!")


def path3():
    print("You throw down your smoke bomb, the monsters confused and you slit and stab their throat and all three are dead")
    time.sleep(b)
    print("You are met by a man named Ray, a skilled hunter from a place called the nightmares. He askes for your aid in battle and finally destroy the outer god.")
    time.sleep(b)
    battle_help = input("Do you wish to help? [Y/N]")
    time.sleep(a)
    if battle_help == "Y" or battle_help == "y":
        print("You accept and fight alongside the hunter. ")
        time.sleep(b)
        print("Together with Ray you go through the hordes of monsters and demons, killing them one by one and finally facing the outer god")
        time.sleep(b)
        print("You and Ray head straight towards the being, determined to finally end this cursed nightmare. ")
        time.sleep(b)
        print("The sound of screaming and the smell of blood filled the air")
        time.sleep(b)
        print("Ray is injured.")
        time.sleep(b)

        injury_help = input("Do you wish to help? [Y/N]")
        if injury_help == "Y" or injury_help == "y":
            print()
        elif injury_help == "N" or injury_help == "n":
            print()
        time.sleep(c)
        if battle_help == "Y" or battle_help == "y":
            time.sleep(b)
            print("You helped Ray get back on his feet and together you fought against the being and won the fight, ending the nightmare. ")
            time.sleep(b)
            print("You finally are free from this cursed world and you take a deep breathe. ")
            time.sleep(a)
            print("The End")
            time.sleep(a)
            print("Thank you for Playing")
            time.sleep(c)
            battle_help()
    elif battle_help == "N" or battle_help == "n":
        time.sleep(c)
        print("You refused, and could not win alone and died")
        battle_help()

    elif battle_help == "N" or battle_help == "n":
        time.sleep(c)
        print("You refuse and walk away, you prefer to work alone. ")





print("┌──═━┈━═──┐")
print("   Reaver ")
print("└──═━┈━═──┘")
time.sleep(a)

print("You are Lilith, a young and skilled hunter from a city called Ravenfall, Plunder the world and destroy all the evil sent by the outer god")
time.sleep(a)
print("__________________________________________________________________________________________________________________________________________")
startGame = input("Start the game?  (Y/N):")
if startGame == 'n' or startGame == 'N':
    print("That is a shame :(")

elif startGame == "y" or startGame == "Y":
    time.sleep(a)
    intro()