import random

#variables
word_list_movies = ["ironman", "ironman2", "ironman3", "hulk", "captainamerica", "titanic", "harrypotter",
"nowyouseeme", "nowyouseeme2", "spectre", "alisencetokill", "theworldisnotenough", "thunderball", "casinoroyale",
"themartian", "gravity", "dieanotherday", "skyfall", "quantumofsolace", "onceuponatimeinhollywood",
"avengers", "joker", "superman", "thedarkknight", "thedarkknightrises", "batmanvssuperman", "aquaman",
"justiceleague", "wonderwoman", "deadpool", "xmen", "logan", "shazam", "hollowman", "hollowman2",
"liveandletdie", "foryoureyesonly", "conjuring", "conjuring2", "annabelle", "annabellecomeshome",
"annabellecreation", "incedious", "incedious2", "incedious3", "borat", "thedictator", "baywatch", "lalaland",
"bladerunner", "citizenkane", "inception", "doctorstrange", "avengersendgame", "civilwar", "avengersinfinitywar",
"shaolinsoccer", "suicidesquad", "snakeundertheeaglesshadow", "charlieandthechocolatefactory"

]



word_list = word_list_movies    # which list will be used, i only have one but you can add more
x = random.randrange(len(word_list))
word = word_list[x]
no_words = len(word)
lives = 5
dashes = no_words * "_"
stupid_fill = "_"
correct_guesses = 0
listy = []
listy2 = []
listyz = []
listyz2 = []
listyx = []
listyx2 = []
breaker = False


#functions
def high_score():
    HighScore = open("high score", "w")
    HighScore.write(str(high_score_streak))
    HighScore.close()



def correct_letter_checker(x):
    global Right_Or_Wrong
    global Right_Or_Wrong2
    global Right_Or_Wrong3
    global place
    global place2
    global place3
    place = word.find(x)
    if place != -1:
        Right_Or_Wrong = True
        place2 = word.find(x, place+1)
        if place2 != -1:
            Right_Or_Wrong2 = True
            place3 = word.find(x, place2+1)
            if place3 != -1:
                Right_Or_Wrong3 = True
            elif place3 == -1:
                Right_Or_Wrong3 = False
        elif place2 == -1:
            Right_Or_Wrong2 = False
    elif place == -1:
        Right_Or_Wrong = False








correct_letter_checker("x")

Right_Or_Wrong = Right_Or_Wrong

place = place



board = """                                  

 Rules:                             |
                                    |
    - The words don't have spaces.
                                    |
    - There may be numbers as well. |

    - If there is a repeat in       |
      characters, you may have to   
      repeat the character again.   |
                                    |  
                                    |    _____________________________________
        """
board_after_1 = """                          
                                    |
                                               |
 Rules:                             |          |
                                    |          |
    - The words don't have spaces.             |
                                    |          |
    - There may be numbers as well. |          |
                                               |
    - If there is a repeat in       |          |
      characters, you may have to              |
      repeat the character again.   |          |
                                    |          |
                                    |    ______|_______________________________
        """

board_after_2 = """                          
                                    |          ___________________
                                               |
 Rules:                             |          |
                                    |          |
    - The words don't have spaces.             |
                                    |          |
    - There may be numbers as well. |          |
                                               |
    - If there is a repeat in       |          |
      characters, you may have to              |
      repeat the character again.   |          |
                                    |    ______|_______________________________
        """
board_after_3 = """                          
                                    |          ___________________
                                               |                  |
 Rules:                             |          |                  |
                                    |          |                  |
    - The words don't have spaces.             |
                                    |          |
    - There may be numbers as well. |          |
                                               |
    - If there is a repeat in       |          |
      characters, you may have to              |
      repeat the character again.   |          |
                                    |          |
                                    |    ______|_______________________________
        """

board_after_4 = """                       
                                    |          ___________________
                                               |                  |
 Rules:                             |          |                  |
                                    |          |                  |
    - The words don't have spaces.             |                  O
                                    |          |                  |
    - There may be numbers as well. |          |                  |
                                               |
    - If there is a repeat in       |          |
      characters, you may have to              |
      repeat the character again.   |          |
                                    |          |
                                    |    ______|_______________________________
        """

board_after_5 = """
                                                ___________________
                                               |                  |
 Rules:                             |          |                  |
                                    |          |                  |
    - The words don't have spaces.             |                  O
                                    |          |                 /|\  
    - There may be numbers as well. |          |                  |
                                               |                 / \     
                                    |          |
                                               |
    You Lose!                       |          |
                                    |    ______|_______________________________
        """


main_board = board





high_score_streak1 = open("high score", "r")
high_score_streak = high_score_streak1.read()
high_score_streak1.close()
print("Hangman!!(Movie Theme!)\n")
print(main_board)
print(f"""\nWord: {dashes}\n Lives: {lives}\n  Streak: {high_score_streak}""")
while True:
    choice = input("Choose A Letter:\n")
    correct_letter_checker(choice)
    if Right_Or_Wrong:
        listy = []
        listy2 = []
        for abdsz in word:
            listy2.append(abdsz)

        for abds in dashes:
            listy.append(abds)

        listy[place] = listy2[place]
        listy2[place] = "_"
        dashes = ""
        dashes = dashes.join(listy)
        word = ""
        word = word.join(listy2)

        if Right_Or_Wrong2:
            listyx = []
            listyx2 = []
            for abdsz in word:
                listyx2.append(abdsz)

            for abds in dashes:
                listyx.append(abds)

            listyx[place2] = listyx2[place2]
            listyx2[place2] = "_"
            dashes = ""
            dashes = dashes.join(listyx)
            word = ""
            word = word.join(listyx2)
            if Right_Or_Wrong3:
                listyz = []
                listyz2 = []
                for abdsz in word:
                    listyz2.append(abdsz)

                for abds in dashes:
                    listyz.append(abds)

                listyz[place3] = listyx2[place3]
                listyz2[place3] = "_"
                dashes = ""
                dashes = dashes.join(listyz)
                word = ""
                word = word.join(listyz2)



        correct_guesses += 1


    if not(Right_Or_Wrong):
        lives -= 1
        if lives == 4:
            main_board = board_after_1
        if lives == 3:
            main_board = board_after_2
        if lives == 2:
            main_board = board_after_3
        if lives == 1:
            main_board = board_after_4
        if lives == 0:
            main_board = board_after_5

    print(main_board)
    print(f"""\nWord: {dashes}\nLives: {lives}\nStreak: {high_score_streak}\n""")
    if lives == 0:
        print("YOU LOSE!")
        main_board = board
        high_score_streak = 0
        high_score()
        break
    count = 0
    for gy in dashes:
        if gy != "_":
            count += 1
        if count == len(word):
            print("YOU WIN!")
            count = 0
            main_board = board
            high_score_streak = int(high_score_streak) + 1
            high_score()
            breaker = True
    if breaker:
        break












