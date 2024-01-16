import os
import random

# Booleans
run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

# Game Values
HP = 50
MAXHP = HP
ATK = 4
pot = 0
elix = 0
trimias = 0
x = 0
y = 0

# Map    x = 0     x = 1     x = 2     x = 3     x = 4     x = 5     x = 6
map = [["plains", "plains", "plains", "plains", "forest", "mountain", "cave"],  # y = 0
       ["forest", "forest", "forest", "forest", "forest", "hills", "mountain"],  # y = 1
       ["forest", "fields", "bridge", "plains", "hills", "forest", "hills"],  # y = 2
       ["plains", "shop", "town", "major", "plains", "hills", "mountain"],  # y = 3
       ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain"]  # y = 4
       ]

y_len = len(map) - 1
x_len = len(map[0]) - 1

# Biomes
biomes = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIDGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "major": {
        "t": "MAJOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True},
}

# Mobs
e_list = ["Globurks", "Bosses"]

mobs = {
    "Globurks": {
        "hp": 100,
        "at": 3,
        "to": 5
    },
    "Bosses": {
        "hp": 50,
        "at": 20,
        "to": 500
    }
}


# Cleaning screen
def clear():
    os.system("cls")


# Lines Separators
def draw():
    print("")
    print("~ |------------------------| ~")
    print("")


# Save
def save():
    lst = [name, str(HP), str(ATK), str(pot), str(elix), str(trimias), str(key)]
    with open("load.txt", 'w') as f:
        for item in lst:
            f.write(f'{item}\n')

        # Load


def load() -> list:
    lst = []
    with open("load.txt", 'r') as f:
        for line in f:
            lst.append(line[0:-1])  # deleting "\n" sings
    return lst


# Heal
def heal(amount):
    global HP
    if HP + amount < MAXHP:
        HP += amount
    else:
        HP = MAXHP
    print(name + "'s HP refilled to " + str(HP) + "!")


# Battle
def battle():
    global fight, play, run, HP, pot, elix, trimias, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Boss"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    t = mobs[enemy]["to"]

    while fight:
        global menu
        clear()
        draw()
        print("Defeat the " + enemy + "!")
        draw()
        print(name + "'Has: " + str(HP) + "HP" + str(MAXHP))
        print(enemy + "Has: " + str(hp) + "HP" + str(hpmax))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        print("2 - USE A POTION ( RESTORE 30HP )")
        print("3 - USE AN ELIXIR ( RESTORE 50HP )")
        draw()

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No elixirs!")
            input("> ")

        if HP <= 0:
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print(name, "tried to survive but.. Died..")
            draw()
            print(".1 | Leave The Game.")
            print(".2 | Continue Playing.")
            when_died = input("# ")
            if when_died == "1":
                clear()
                print(" _______ _                 _           __                   _             _               _ ")
                print("|__   __| |               | |         / _|                 | |           (_)             | |")
                print("   | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _  | |")
                print("   | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | | |")
                print("   | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | |_) | | (_| | |_| | | | | | (_| | |_|")
                print("   |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, | (_)")
                print("                                                     | |             __/ |         __/ |    ")
                print("                                                     |_|            |___/         |___/     ")
                print(" -> You left the game successfully.")
                print("")
                quit()
            elif when_died == "2":
                clear()
                fight = False
                menu = True

        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw()
            fight = False
            trimias += t
            print("You've earned " + str(t) + " Trimias !")
            if random.randint(0, 100) < 10:
                pot += 1
                print("You've found a potion!")
            if enemy == "Bosses":
                draw()
                print("Congratulations,", name.title(), "you've finished the game!")
                boss = False
                play = False
                run = False
            input("> ")
            clear()


# Shop
def shop():
    global buy, trimias, pot, elix, ATK

    while buy:
        clear()
        draw()
        print("Welcome to the shop!")
        draw()
        print("TRIMIAS: " + str(trimias))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("ATTACK: " + str(ATK))
        draw()
        print("1 - BUY POTION (30HP) - 5 TRIMIAS")
        print("2 - BUY ELIXIR (MAXHP) - 8 TRIMIAS")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 TRIMIAS")
        print("4 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if trimias >= 5:
                pot += 1
                trimias -= 5
                print("You've bought a potion!")
            else:
                print("You don't have enough gold!")
            input("> ")
        elif choice == "2":
            if trimias >= 8:
                elix += 1
                trimias -= 8
                print("You've bought an elixir!")
            else:
                print("You don't have enough gold!")
            input("> ")
        elif choice == "3":
            if trimias >= 10:
                ATK += 2
                trimias -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False


# Mayor
def mayor():
    global speak, key

    while speak:
        clear()
        draw()
        print("Hello there, " + name + "!")
        if ATK < 10:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            key = False
        else:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            key = True

        draw()
        print(".1 | LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            speak = False


# Cave
def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        if key:
            print(".1 | USE KEY")
        print(".2 | TURN BACK")
        draw()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False


# Game itself
while run:
    while menu:
        clear()
        print(
            "__          __  _                            _______      _______   _ _                 _          _____  _____   _____ ")
        print(
            "\ \        / / | |                          |__   __|    |__   __| (_) |               (_)        |  __ \|  __ \ / ____|")
        print(
            " \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___      | |_ __ _| | ___  _ __ ___  _  __ _   | |__) | |__) | |  __ ")
        print(
            "  \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \     | | '__| | |/ _ \| '_ ` _ \| |/ _` |  |  _  /|  ___/| | |_ |")
        print(
            "   \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) |    | | |  | | | (_) | | | | | | | (_| |  | | \ \| |    | |__| |")
        print(
            "    \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/     |_|_|  |_|_|\___/|_| |_| |_|_|\__,_|  |_|  \_\_|     \_____|                -by Aragon")
        print("")
        draw()
        print("")
        print(".1 | New Save File")
        print(".2 | Load A Save File")
        print(".3 | Prologue")
        print(".4 | Leave The Game")
        print("")
        draw()

        choice = input("# ")

        if choice == "1":
            clear()
            draw()
            name = input("For your adventure in Trilomia, please choose a name for a strong hero like you > ")
            menu = False
            play = True
        elif choice == '2':
            name, HP, ATK, pot, elix, trimias, key = load()
            print("Hey", name, "a save file is found. Have a great time playing :)")
            input("Press enter to continue...")
            menu = False
            play = True

        elif choice == "3":
            clear()
            draw()
            input(
                "Once upon a time, there was a young and strong hero, his name was Dragolio and he had the life power that allowed him to take care of the world and kill the Globurks who were created by Herloon, the evil itself. Dragolio was really good at his job but one  day, Herloon decided to try to take the control of the world and started an assault on Trilomia ! Dragolio, distraught by what was happening struggled to fight every Globurks by himself, with no help and eventually fallen in the darkness after days and days of intensive fights... But 100 years after, another hero named ... woke up and the attributed mission it got was to find this old legend Dragolio or something like that..")
        elif choice == "4":
            clear()
            print(" _______ _                 _           __                   _             _               _ ")
            print("|__   __| |               | |         / _|                 | |           (_)             | |")
            print("   | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _  | |")
            print("   | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | | |")
            print("   | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | |_) | | (_| | |_| | | | | | (_| | |_|")
            print("   |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, | (_)")
            print("                                                     | |             __/ |         __/ |    ")
            print("                                                     |_|            |___/         |___/     ")
            print(" -> You left the game successfully.")
            print("")
            quit()

    while play:
        save()  # autosave
        clear()

        if not standing:
            if biomes[map[y][x]]["e"] and random.randint(0, 100) < 30:
                pass

        if play:
            draw()
            print("YOU ARE IN THE: " + biomes[map[y][x]]["t"])
            draw()
            print("HERO'S NAME: " + name.title())
            print("HEAL POINTS: " + str(HP) + "/" + str(MAXHP))
            print("DAMAGE POINTS: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("TRIMIAS: " + str(trimias))
            print("COORDINATES:", x, y)
            draw()
            print(".0 | SAVE AND QUIT")
            if y > 0:
                print(".1 | GO TO THE NORTH")
            if x < x_len:
                print(".2 | GO TO THE EAST")
            if y < y_len:
                print(".3 | GO TO THE SOUTH")
            if x > 0:
                print(".4 | GO TO THE WEST")
            print(".5 | USE A POTION (RESTORE 30HP)")
            print(".6 | USE AN ELIXIR (RESTORE 50HP)")
            if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
                print(".7 | ENTER")
            draw()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                heal(30)
                standing = True
            elif dest == "6":
                heal(50)
                standing = True
            elif dest == "7":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()
            else:
                standing = True
