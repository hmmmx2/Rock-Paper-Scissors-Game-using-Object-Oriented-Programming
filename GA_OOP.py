import random, time
from abc import ABC, abstractmethod

c_list = {                              # character
            '1': '╭(●｀∀´●)╯',
            '2': '(ฅ´ω`ฅ)',
            '3': '(๑•́ ₃•̀๑)',
            '4': '( ´◔ ‸◔`)',
            '5': '(๑￫‿ฺ￩๑)',
            '6': '(╯°Д°)╯︵ ┻━┻',
            '7': 'ㄟ(◑‿◐ )ㄏ',
            '8': '=≡Σ((( つ•̀ω•́)つ',
            '9': '(◕‿◕✿)',
            '10': '(๑＞ ڡ ＜)☆',
            '11': 'Σ( ° △ °|||)︴',
            '12': '（╬￣皿￣）'
        }

choices = ["1", "2", "3"]  # 1=Rock, 2=Scissor, 3=Paper

win = [
    ["1", "2"],
    ["2", "3"],
    ["3", "1"],
]
print(
    "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── \n"
    "─██████──────────██████─██████████████─██████─────────██████████████─██████████████─██████──────────██████─██████████████─ \n"
    "─██░░██──────────██░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██─ \n"
    "─██░░██──────────██░░██─██░░██████████─██░░██─────────██░░██████████─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─██░░██████████─ \n"
    "─██░░██──────────██░░██─██░░██─────────██░░██─────────██░░██─────────██░░██──██░░██─██░░██████░░██████░░██─██░░██───────── \n"
    "─██░░██──██████──██░░██─██░░██████████─██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██░░██──██░░██─██░░██████████─ \n"
    "─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─ \n"
    "─██░░██──██░░██──██░░██─██░░██████████─██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██████──██░░██─██░░██████████─ \n"
    "─██░░██████░░██████░░██─██░░██─────────██░░██─────────██░░██─────────██░░██──██░░██─██░░██──────────██░░██─██░░██───────── \n"
    "─██░░░░░░░░░░░░░░░░░░██─██░░██████████─██░░██████████─██░░██████████─██░░██████░░██─██░░██──────────██░░██─██░░██████████─ \n"
    "─██░░██████░░██████░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──────────██░░██─██░░░░░░░░░░██─ \n"
    "─██████──██████──██████─██████████████─██████████████─██████████████─██████████████─██████──────────██████─██████████████─ \n"
    "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── \n")
time.sleep(1)
print(
    "\n=========================================================================================================================="
    "\n<< RULES OF THE GAME>>\n",
    "1. There are two mode in this game which are one player mode and two player mode.\n",
    "2. One player mode - Player 1 will play with the AI.\n",
    "                   - The score of the AI will be hide while playing the game. It only can check after the game.\n",
    "3. Two player mode - Player 1 and Player 2 will play with different AI.\n",
    "                   - The choice of the AI will show after two player make their choice.\n",
    "4. Player can set the number of rounds that you want to play with AI.\n",
    "5. Player can choose a favourite character to display themselves.\n",
    "6. The player with highest total score are the WINNER.\n",
    "\n==========================================================================================================================\n")

class Welcome(ABC):
    def __init__(self):
        print("\n｡:.ﾟヽ(｡◕‿◕｡)ﾉﾟ.:｡+ﾟ")

    def print_character(self):
        print(
            "\n《 Character 》\n"
            "   1. ╭(●｀∀´●)╯\n"
            "   2. (ฅ´ω`ฅ)\n"
            "   3. (๑•́ ₃•̀๑)\n"
            "   4. ( ´◔ ‸◔`)\n"
            "   5. (๑￫‿ฺ￩๑)\n"
            "   6. (╯°Д°)╯︵ ┻━┻ \n"
            "   7. ㄟ(◑‿◐ )ㄏ\n"
            "   8. =≡Σ((( つ•̀ω•́)つ\n"
            "   9. (◕‿◕✿) \n"
            "   10. (๑＞ ڡ ＜)☆\n"
            "   11. Σ( ° △ °|||)︴\n"
            "   12. （╬￣皿￣）\n"
        )

    @abstractmethod
    def name(self, name):
        pass
    def character(self, num):
        pass

class Player1(Welcome):
    def name(self, name):
        self.name = name
        print("The first player %s is in." % self.name)

    def character(self, num):
        self.num = num
        print("\n%s\nPlayer %s \n" % (c_list[num], player1_name))

class Player2(Welcome):
    def name(self, name):
        self.name = name
        print("The second player %s is in." % self.name)

    def character(self, num):
        self.num = num
        print("\n%s\nPlayer %s \n" % (c_list[num], player2_name))


class Game:
    def round(self):
        global rounds
        while True:
            player = input("\nHow many rounds do you want to play? \nEnter:")
            try:
                rounds = int(player)
            except ValueError:
                print("Error, this is not a number")
            else:
                break
        return rounds

class Win_Lose(Game):
    def win_loose_1_player(self):
        global totalscore_p1
        global totalscore_AI
        score = 100 / rounds

        if [player1_choice, computer_choice] in win:
            print("\nPlayer %s WIN !!!!!" % player1_name)
            totalscore_p1 += score
        elif player1_choice == computer_choice:
            print("No one win.")
        else:
            print("\n🤖 AI WIN !!!!!")
            totalscore_AI += score

        return totalscore_p1, totalscore_AI

    def win_loose_2_player(self):
        global totalscore_p1
        global totalscore_p2
        score = 100 / rounds

        if [player1_choice, computer_choice_1] in win:
            print("\n%s Player %s WIN !!!!!" % (c_list[cha_p1], player1_name))
            totalscore_p1 += score
        elif [computer_choice_1, player1_choice] in win:
            print("\n%s Player %s LOSE..." % (c_list[cha_p1], player1_name))
        elif player1_choice == computer_choice_1:
            print("No one win between Player 1 and AI.")

        if [player2_choice, computer_choice_2] in win:
            print("\n%s Player %s WIN !!!!!" % (c_list[cha_p2], player2_name))
            totalscore_p2 += score
        elif [computer_choice_2, player2_choice] in win:
            print("\n%s Player %s LOSE..." % (c_list[cha_p2], player2_name))
        elif player2_choice == computer_choice_2:
            print("No one win between %s Player %s and 🤖 AI." % (c_list[cha_p2], player2_name))

        return totalscore_p1, totalscore_p2

class Final(Game):
    def final_win_p1(self):
        if totalscore_p1 > totalscore_AI:
            print("\n------------------------------------------------------------------------\n",
                  "THE WINNER IS %s PLAYER %s!!!!!!!!!" % (c_list[cha_p1], player1_name),
                  "\n------------------------------------------------------------------------\n")
        elif totalscore_p1 == totalscore_AI:
            print("\n------------------------------------------------------------------------\n",
                  "No one win between %s Player %s and 🤖 AI." % (c_list[cha_p1], player1_name),
                  "\n------------------------------------------------------------------------\n")
        elif totalscore_p1 < totalscore_AI:
            print("\n------------------------------------------------------------------------\n",
                  "THE WINNER IS 🤖 AI!!!!!!!!!",
                  "\n------------------------------------------------------------------------\n")

    def final_win_p2(self):
        if totalscore_p1 > totalscore_p2:
            print("\n------------------------------------------------------------------------\n",
                  "THE WINNER IS %s PLAYER %s!!!!!!!!!" % (c_list[cha_p1], player1_name),
                  "\n------------------------------------------------------------------------\n")
        elif totalscore_p1 == totalscore_p2:
            print("\n------------------------------------------------------------------------\n",
                  "No one win between %s Player %s and %s player %s." % (c_list[cha_p1], player1_name, c_list[cha_p2], player2_name),
                  "\n------------------------------------------------------------------------\n")
        else:
            print("\n------------------------------------------------------------------------\n",
                  "THE WINNER IS %s PLAYER %s!!!!!!!!!" % (c_list[cha_p2], player2_name),
                  "\n------------------------------------------------------------------------\n")


class Score_AI:

    def __init__(self, scoreAi):
        self.__scoreAi = scoreAi

    def get_score_Ai(self):
        return self.__scoreAi

    def set_score_Ai(self, scoreAi):
        self.__scoreAi = scoreAi


class Score_Player:
    def __init__(self, totalscore_p1, totalscore_p2):
        self._totalscore_p1 = totalscore_p1
        self._totalscore_p2 = totalscore_p2

    def display_score_P1(self):
        print(f"\n 《PLAYER 1》           《AI》     "
              f"\n:::::::::::::      :::::::::::::\n"
              f" Score: {self._totalscore_p1:.0f}%       Score: <PRIVATE>"
              f"\n:::::::::::::      :::::::::::::\n")

    def display_score_p2(self):
        print(f"\n 《PLAYER 1》        《PLAYER 2》   "
              f"\n:::::::::::::      :::::::::::::\n"
              f" Score: {self._totalscore_p1:.0f}%       Score: {self._totalscore_p2:.0f}%"
              f"\n:::::::::::::      :::::::::::::\n")


class Rock(Game):
    def display(self):
        print("888888888888888888888888888888888 \n"
              "888888888888888888888888888888888 \n"
              "888888888888888888888888888888888 \n"
              "888888888888888888888888888888888 \n"
              "888888888888888888888888888888888 \n"
              "888888888888888888888888888888888 \n"
              "88888888888888888____888888888888 \n"
              "8888888888888888______888___88888 \n"
              "8888888888_____8______88_____8888 \n"
              "8888___88______8______8______8888 \n"
              "888_____8______8______8______8888 \n"
              "888_____8______8______8______8888 \n"
              "888_____8______8______8______8888 \n"
              "888_____8____88888888888888888888 \n"
              "8_8_____8___88________________888 \n"
              "8_8_____8__88__________________88 \n"
              "8__888888_888_________888_______8 \n"
              "8_________88________8___________8 \n"
              "8____________8888888____________8 \n"
              "88_____________88_______________8 \n"
              "88_______________88_____________8 \n"
              "888______________8_____________88 \n"
              "888_______________8___________888 \n"
              "88888_____________8__________8888 \n"
              "888888_____________________888888 \n"
              "888888____________________8888888 \n")

class Scissor(Game):
    def display(self):
        print("888888888888888888888888888888888 \n"
              "88888888888888888____88888____888 \n"
              "8888888888888888______888_____888 \n"
              "8888888888888888______888_____888 \n"
              "8888888888888888______888_____888 \n"
              "8888888888888888______88_____8888 \n"
              "8888888888888888______88_____8888 \n"
              "8888888888888888______88_____8888 \n"
              "8888888888_____8______88_____8888 \n"
              "8888___88______8______8_____88888 \n"
              "888_____8______8______8_____88888 \n"
              "888_____8______8______8_____88888 \n"
              "888_____8______8______8_____88888 \n"
              "888_____8____88888888888888888888 \n"
              "8_8_____8___88________________888 \n"
              "8_8_____8__88__________________88 \n"
              "8__888888_888_________888_______8 \n"
              "8_________88________8___________8 \n"
              "8____________8888888____________8 \n"
              "88_____________88_______________8 \n"
              "88_______________88_____________8 \n"
              "888______________8_____________88 \n"
              "888_______________8___________888 \n"
              "88888_____________8__________8888 \n"
              "888888_____________________888888 \n")

class Paper(Game):
    def display(self):
        print("88888888888888888____888888888888888888 \n"
              "8888888888888888______88____88888888888 \n"
              "8888888888888888______8______8888888888 \n"
              "8888888888____88______8______8888888888 \n"
              "888888888______8______8______8888888888 \n"
              "888888888______8______8______8888888888 \n"
              "888888888______8______8______8888888888 \n"
              "888888888______8______8______8888888888 \n"
              "8888___88______8______8______8888888888 \n"
              "888_____8______8______8______8888888888 \n"
              "888_____8______8______8______8888888888 \n"
              "888_____8______8______8______8888__8888 \n"
              "888_____8______8______8______888____888 \n"
              "88___________________________88_____888 \n"
              "8____________________________8______888 \n"
              "8____________________________8_____8888 \n"
              "8_____________________888__________8888 \n"
              "8___________________8_____________88888 \n"
              "8________________8________________88888 \n"
              "88______________8_______________8888888 \n"
              "88______________8_______________8888888 \n"
              "888______________8______________8888888 \n"
              "888_______________8____________88888888 \n"
              "88888_____________8__________8888888888 \n"
              "888888_____________________888888888888 \n"
              "888888____________________8888888888888 \n")

result = Win_Lose()
final_r = Final()

# Run code
time.sleep(1)
while True:
    # Reset score
    score_Ai1 = 0
    score_Ai2 = 0
    s = Score_AI(0)
    totalscore_p1 = 0
    totalscore_p2 = 0
    totalscore_AI = 0

    while True:
        # Choosing mode
        mode = input("\nMode:\n1. One Player\n2. Two Player\nPlease choose one of the mode:")
        if mode == '1' or mode == '2':
            break

    # 1 Player Mode
    if mode == '1':
        # Enter player name
        player1_name = input("\n< PLAYER 1 >\nPlease key in your name:")
        y = Player1()
        y.name(player1_name)

        # Select player character
        y.print_character()
        while True:
            cha_p1 = input("Select your character:")
            if cha_p1 in c_list:
                break
            else:
                print("x")
        y.character(cha_p1)

        # Choice by player
        for x in range(result.round()):
            while True:
                n = x + 1
                print(f"\n==========\n"
                      f" Rounds {n}"
                      f"\n==========")
                player1_choice = input(
                    "\n < Player %s >\nKey in the number \n1. Rock\n2. Scissor\n3. Paper\nEnter here:" % player1_name)
                if player1_choice in choices:
                    break
                else:
                    print("Oops, please key in the given input.")
            if player1_choice == "1":
                choose = Rock()
                choose.display()
            elif player1_choice == "2":
                choose = Scissor()
                choose.display()
            else:
                choose = Paper()
                choose.display()

            # Choice by computer
            computer_choice = random.randint(1, 3)
            computer_choice = str(computer_choice)
            time.sleep(1)
            print("Computer Choice: ")
            if computer_choice == "1":
                choose = Rock()
                choose.display()
            elif computer_choice == "2":
                choose = Scissor()
                choose.display()
            else:
                choose = Paper()
                choose.display()


            # Determine who win
            result.win_loose_1_player()
            s.set_score_Ai(totalscore_AI)
            sp = Score_Player(totalscore_p1=totalscore_p1, totalscore_p2=totalscore_p2)
            sp.display_score_P1()

        # The winner of this game
        time.sleep(1)
        final_r.final_win_p1()

        # Checking AI score
        while True:
            check = input("Check Ai score? (y/n):")
            if check == "y":
                print(f"AI Score: {totalscore_AI:.0f}%")
                break
            elif check == "n":
                print("You have chosen no to see the AI Score")
                break
            else:
                print("this is not a y/n")
                continue


    # 2 Player Mode
    else:
        # Enter player 1 name
        player1_name = input("\n< PLAYER 1 >\nPlease key in your name:")
        y = Player1()
        y.name(player1_name)

        # Select player character
        y.print_character()
        while True:

            cha_p1 = input("Select your character:")
            if cha_p1 in c_list:
                break
            else:
                print("x")
        y.character(cha_p1)

        # Enter player 2 name
        player2_name = input("\n< PLAYER 2 >\nPlease key in your name:")
        y = Player2()
        y.name(player2_name)

        # Select player 2 character
        y.print_character()
        while True:
            cha_p2 = input("Select your character:")
            if cha_p2 in c_list:
                break
            else:
                print("x")
        y.character(cha_p2)

        for x in range(result.round()):
            while True:
                n = x + 1
                print(f"\n==========\n"
                      f" Rounds {n}"
                      f"\n==========")

                # Choice by player 1
                player1_choice = input(
                    "\n < Player %s >\nKey in the number \n1. Rock\n2. Scissor\n3. Paper\nEnter here:" % player1_name)
                if player1_choice in choices:
                    break
                else:
                    print("Oops, please key in the given input.")
            if player1_choice == "1":
                choose = Rock()
                choose.display()
            elif player1_choice == "2":
                choose = Scissor()
                choose.display()
            else:
                choose = Paper()
                choose.display()

            while True:
                # Choice by player 2
                player2_choice = input(
                    "\n < Player %s >\nKey in the number \n1. Rock\n2. Scissor\n3. Paper\nEnter here:" % player2_name)
                if player2_choice in choices:
                    break
                else:
                    print("Oops, please key in the given input.")
            if player2_choice == "1":
                choose = Rock()
                choose.display()
            elif player2_choice == "2":
                choose = Scissor()
                choose.display()
            else:
                choose = Paper()
                choose.display()

            # Choice by computer for player 1
            computer_choice_1 = random.randint(1, 3)
            computer_choice_1 = str(computer_choice_1)
            time.sleep(1)
            print("Computer Choice (P1):\n")

            if computer_choice_1 == "1":
                choose = Rock()
                choose.display()
            elif computer_choice_1 == "2":
                choose = Scissor()
                choose.display()
            else:
                choose = Paper()
                choose.display()

            # Choice by computer for player 2
            computer_choice_2 = random.randint(1, 3)
            computer_choice_2 = str(computer_choice_2)
            time.sleep(1)
            print("Computer Choice (P2):\n")

            if computer_choice_2 == "1":
                choose = Rock()
                choose.display()
            elif computer_choice_2 == "2":
                choose = Scissor()
                choose.display()
            else:
                choose = Paper()
                choose.display()

            # Determine who win
            time.sleep(1)
            result.win_loose_2_player()
            sp = Score_Player(totalscore_p1=totalscore_p1, totalscore_p2=totalscore_p2)
            sp.display_score_p2()

        # The winner of this game
        time.sleep(1)
        final_r.final_win_p2()


    # Continue game or not
    ask = input("\nContinue the game[Press 1] or exit[Any key]: ")
    if ask == "1":
        print("Enjoy")
        continue
    else:
        print("\nThank you for playing this game.\nWish you have a nice day.")
        break
