import random
list_of_question = [
 "Ты когда-то прогуливал уроки?",
 "Что ты любишь делать больше всего?",
 "Ты когда-то не платил за какую-небудь покупку?",
 "Кого ты любишь больше всего из родителей?",
 "Какие компьютерные игры ты любишь?"
 ]
list_of_action = [
 "Прыгни 100 раз",
 "Съешь 3 яблока",
 "Отожмись 50 раз",
 "Подтянись 20 раз",
 "Выпей 1л воды"
 ]
gamer_list = []
def gamers(list):
     while True:
         name = input("Enter a Player name – ")
         if 0 < len(name) <= 2:
             continue
         list.append(str.capitalize(name))
         if len(list)>=2:
             need_next_player = input("More players? – Y/N ")
             if need_next_player == str.lower("y") or need_next_player == str.lower("yes"):
                 continue
             else:
                 break
gamers(gamer_list)
print(gamer_list)
def game(list_of_question, list_of_action, *args):
     while True:
         next_step = None
         for gamer in args:
             print(gamer)
             user_choise = input("Question or Action? ")
             if user_choise == str.lower("q") or user_choise == str.lower("question"):
                 question_index = random.randint(0, len(list_of_question)-1)
                 print(list_of_question[question_index])
                 list_of_question.pop(question_index)
             elif user_choise == str.lower("a") or user_choise == str.lower("action"):
                 action_index = random.randint(0,len(list_of_action)-1)
                 print(list_of_action[action_index])
                 list_of_action.pop(action_index)
             else:
                 while user_choise != str.lower("q") or user_choise != str.lower("question") or user_choise != str.lower("a") or user_choise != str.lower("action"):
                     print("Try again!")
                     user_choise = input("Question or Action? ")
                     if user_choise == str.lower("q") or user_choise == str.lower("question"):
                         question_index = random.randint(0, len(list_of_question) - 1)
                         print(list_of_question[question_index])
                         list_of_question.pop(question_index)
                         break
                     elif user_choise == str.lower("a") or user_choise == str.lower("action"):
                         action_index = random.randint(0, len(list_of_action) - 1)
                         print(list_of_action[action_index])
                         list_of_action.pop(action_index)
                         break
             if args[-1] == gamer:
                break

         next_step=input("Next player? – Y/N ")

         if next_step == str.lower("y") or next_step == str.lower("yes"):
            continue
         else:
            print("Game is over")
            break
         if next_step == str.lower('y') or next_step == str.lower('yes'):
            pass
         else:
            break
         select = input("New round? – Y/N ")
         if select == str.lower("y") or select == str.lower("yes"):
            continue
         else:
            break
game(list_of_question,list_of_action, *gamer_list)

list_of_heroes = ["Halk", "Spider Man", "Iron Man", "Wolverine", "Captain America"]
list_of_players = []
players_name = input("Enter a Player name – ")
list_of_players.append(str.capitalize(players_name))
print("More?")
more = input("Y/N - ")
while str.capitalize(more) == "Y" or str.capitalize(more) == "Yes":
    if str.capitalize(more) == "Y" or str.capitalize(more) == "Yes":
        players_name = input("Enter a Player name – ")
        list_of_players.append(str.capitalize(players_name))
        if len(list_of_players) == 5:
            break
        print("More?")
        more = input("Y/N - ")
    else:
        break
print(list_of_players)
players = len(list_of_players)
for a in range(players):
    hero_index = random.randint(0, len(list_of_heroes) - 1)
    print(list_of_players[0], "-", list_of_heroes[hero_index], "\n",)
    list_of_heroes.pop(hero_index)
    list_of_players.pop(0)

random_name = []
name_for_list = input("Enter something - ")
random_name.append(name_for_list)
more_names = input("More names? Y/N - ")
while str.capitalize(more_names) == "Y" or str.capitalize(more_names) == "Yes":
    name_for_list = input("Enter something - ")
    random_name.append(name_for_list)
    more_names = input("More names? Y/N - ")
    random_name_index = random.randint(0, len(random_name) - 1)