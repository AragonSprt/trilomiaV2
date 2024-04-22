import os, random

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

HP = 50
HPMAX = 50
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

        #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
map = [["plains",   "plains",   "plains",   "plains",   "forest", "mountain",       "cave"],    # y = 0
       ["forest",   "forest",   "forest",   "forest",     "shop",    "hills",   "mountain"],    # y = 1
       ["forest",   "fields",   "bridge",   "plains",    "hills",   "forest",      "hills"],    # y = 2
       ["plains",     "shop",     "town",    "mayor",   "plains",    "hills",   "mountain"],    # y = 3
       ["plains",   "fields",   "fields",   "plains",    "hills", "mountain",   "mountain"]]    # y = 4

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
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
        "t": "BRIGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "mayor": {
        "t": "MAYOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,
    }
}

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Orc": {
        "hp": 35,
        "at": 5,
        "go": 18
    },
    "Slime": {
        "hp": 30,
        "at": 2,
        "go": 12
    },
    "Dragon": {
        "hp": 100,
        "at": 8,
        "go": 100
    }
}


def clear():
    os.system("cls")


def draw():
    print("")
    print("~ |------------------------| ~")
    print("")


def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()


def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(name + "'s HP refilled to " + str(HP) + "!")


def battle():
    global fight, play, run, HP, pot, elix, gold, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print("You are now in combat, defeat the " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print(".1 | ATTACK")
        if pot > 0:
            print(".2 | USE POTION (RESTORE 30HP)")
        if elix > 0:
            print(".3 | USE ELIXIR (RESTORE 50HP)")
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
                print("You don't have any potions left!")
            input("> ")

        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("You don't have any elixirs left!")
            input("> ")

        if HP <= 0:
            clear()
            fight = False
            play = False
            run = False
            draw()
            print("On this heavenly ground fell our strong and defeated" + name + "... Might he someday get up and heal from his injuries ?")
            print("")
            print("")
            print(" _______ _                 _           __                   _             _               _ ")
            print("|__   __| |               | |         / _|                 | |           (_)             | |")
            print("   | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _  | |")
            print("   | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | | |")
            print("   | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | |_) | | (_| | |_| | | | | | (_| | |_|")
            print("   |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, | (_)")
            print("                                                     | |             __/ |         __/ |    ")
            print("                                                     |_|            |___/         |___/     ")
            print(" -> You unfortunately died..")
            print()
            quit()

        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw()
            fight = False
            gold += g
            print("You've found " + str(g) + " gold!")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                draw()
                print("CONGRATULATIONS DEAR TRAVELER, YOU HAVE MY RESPECT FOR EVER AND EVER!")
                print("")
                print("")
                print(" _______ _                 _           __                   _             _               _ ")
                print("|__   __| |               | |         / _|                 | |           (_)             | |")
                print("   | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _  | |")
                print("   | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | | |")
                print("   | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | |_) | | (_| | |_| | | | | | (_| | |_|")
                print("   |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, | (_)")
                print("                                                     | |             __/ |         __/ |    ")
                print("                                                     |_|            |___/         |___/     ")
                print("")
                print(" -> You successfully beated the dragon, I can't congrat you more! Please have a wonderful life and take care of you if we don't see each other again <3")
                boss = False
                play = False
                run = False
            quit()


def shop():
    global buy, gold, pot, elix, ATK

    while buy:
        clear()
        draw()
        print("Welcome to the shop traveller, what would you like to do ?")
        draw()
        print("TRIMIAS: " + str(gold))
        print("POTIONS LEFT: " + str(pot))
        print("ELIXIRS LEFT: " + str(elix))
        print("DAMAGE POINTS: " + str(ATK))
        draw()
        print(".1 | BUY A POTION (30HP) - 5 TRIMIAS")
        print(".2 | BUY ELIXIR (50HP) - 8 TRIMIAS")
        print(".3 | UPGRADE WEAPON (+2ATK) - 10 TRIMIAS")
        print(".4 | LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if gold >= 5:
                pot += 1
                gold -= 5
                print("You've bought a potion!")
            else:
                print("You don't have enough trimias!")
            input("> ")
        elif choice == "2":
            if gold >= 8:
                elix += 1
                gold -= 8
                print("You've bought an elixir!")
            else:
                print("You don't have enough trimias!")
            input("> ")
        elif choice == "3":
            if gold >= 10:
                ATK += 2
                gold -= 10
                print("Congrats, you've upgraded your weapon!")
            else:
                print("You don't have enough trimias!")
            input("> ")
        elif choice == "4":
            buy = False


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



while run:
    while menu:
        clear()
        print("__          __  _                            _______      _______   _ _                 _          _____  _____   _____ ")
        print("\ \        / / | |                          |__   __|    |__   __| (_) |               (_)        |  __ \|  __ \ / ____|")
        print(" \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___      | |_ __ _| | ___  _ __ ___  _  __ _   | |__) | |__) | |  __ ")
        print("  \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \     | | '__| | |/ _ \| '_ ` _ \| |/ _` |  |  _  /|  ___/| | |_ |")
        print("   \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) |    | | |  | | | (_) | | | | | | | (_| |  | | \ \| |    | |__| |")
        print("    \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/     |_|_|  |_|_|\___/|_| |_| |_|_|\__,_|  |_|  \_\_|     \_____|                -by Aragon")
        print("")
        draw()
        print("")
        print(".1 | New Save File")
        print(".2 | Load A Save File")
        print(".3 | Prologue")
        print(".4 | Leave The Game")
        print("")
        draw()

        if rules:
            print("I'm the creator of this game and the rules are that you explore as much as you want.")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("For your adventure in Trilomia, please choose a name for a strong hero like you > ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print("Hey", name, "a save file is found. Have a great time playing :)")
                    input("Press enter to continue...")
                    menu = False
                    play = True
                else:
                    print("Your save file is corrupted! I'm sorry but.. You'll need to restart your adventure :()")
                    input("> ")
            except OSError:
                print("There was no loadable save file found!")
                input("> ")
        elif choice == "3":
            clear()
            draw()
            input("Once upon a time, there was a young and strong hero, his name was Dragolio and he had the life power that allowed him to take care of the world and kill the Globurks who were created by Herloon, the evil itself. Dragolio was really good at his job but one  day, Herloon decided to try to take the control of the world and started an assault on Trilomia ! Dragolio, distraught by what was happening struggled to fight every Globurks by himself, with no help and eventually fallen in the darkness after days and days of intensive fights... But 100 years after, another hero named ... woke up and the attributed mission it got was to find this old legend Dragolio or something like that..")
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
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) < 30:
                    fight = True
                    battle()

        if play:
            draw()
            print("YOU ARE IN THE: " + biom[map[y][x]]["t"])
            draw()
            print("HERO'S NAME: " + name)
            print("HEAL POINTS: " + str(HP) + "/" + str(HPMAX))
            print("DAMAGE POINTS: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("TRIMIAS: " + str(gold))
            print("COORD:", x, y)
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
            if pot > 0:
                print(".5 | USE A POTION (RESTORE 30HP)")
            if elix > 0:
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
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print("You don't have any potions left!")
                input("> ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                else:
                    print("You don't have any elixirs left!")
                input("> ")
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