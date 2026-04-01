import random
again = "yes"
def game(choice, result):
    print("")
    print("=====Start Game rock, paper, scissors, lizard, spock=====")
    computer_choice = random.choice("rpslc")
    print("--------------------------------")
    print("Your select – ",str.capitalize(choice))
    print("Computer select —",str.capitalize(computer_choice))
    if str.lower(choice) == computer_choice:
        print("Result of game – Draw")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "r" and computer_choice == "p":
        result["computer"]+=1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "r" and computer_choice == "c":
        result["computer"]+=1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "r" and computer_choice == "s":
        result["player"]+=1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "r" and computer_choice == "l":
        result["player"]+=1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "p" and computer_choice == "s":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "p" and computer_choice == "l":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "p" and computer_choice == "r":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "p" and computer_choice == "c":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "s" and computer_choice == "r":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "s" and computer_choice == "c":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "s" and computer_choice == "p":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "s" and computer_choice == "l":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "l" and computer_choice == "s":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "l" and computer_choice == "r":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "l" and computer_choice == "p":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "l" and computer_choice == "c":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "c" and computer_choice == "p":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "c" and computer_choice == "l":
        result["computer"] += 1
        print("------Computer Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "c" and computer_choice == "r":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
    elif str.lower(choice) == "c" and computer_choice == "s":
        result["player"] += 1
        print("------Player Wins------")
        print("Score,Computer", result["computer"], "—", result["player"], "Player")
result = {"computer": 0, "player": 0}
choise = input("Select R/P/S/L/C – ")
game(choise, result)
while again == "yes":
    if result["computer"] != 3 or result["player"] != 3:
        choise = input("Select R/P/S/L/C – ")
        game(choise, result)
    if result["computer"] == 3 or result["player"] == 3:
        if result["computer"] > result["player"]:
            print("Defeat, computer is winner!")
            again = input("Do you want to play again? yes/no: ")
        if result["computer"] < result["player"]:
            print("Victory, you are winner!")
            again = input("Do you want to play again? yes/no: ")
        if again == "yes":
            result = {"computer": 0, "player": 0}
            choise = input("Select R/P/S/L/C – ")
            game(choise, result)
        else:
            print("So good bye!")