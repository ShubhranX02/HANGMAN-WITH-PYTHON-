import random

#variables
word_list_movies = ["ironman", "hulk", "captain/america", "titanic", "harry/potter",
"now/you/see/me", "spectre", "a/lisence/to/kill", "the/world/is/not/enough", "thunder/ball", "casino/royale",
"the/martian", "gravity", "die/another/day", "skyfall", "quantum/of/solace", "once/upon/a/time/in/hollywood",
"avengers", "joker", "superman", "the/dark/knight", "the/dark/knight/rises", "batman/vs/superman", "aquaman",
"justice/league", "wonder/woman", "deadpool", "x/men", "logan", "shazam", "hollow/man",
"live/and/let/die", "for/your/eyes/only", "conjuring", "annabelle", "annabelle/comes/home",
"annabelle/creation", "incedious", "borat", "the/dictator", "baywatch", "lalaland",
"blade/runner", "citizen/kane", "inception", "doctor/strange", "avengers/endgame", "civil/war",
"avengers/infinity/war",
"shaolin/soccer", "suicide/squad", "snake/under/the/eagles/shadow", "charlie/and/the/chocolate/factory"

]



word_list = word_list_movies    # which list will be used, i only have one but you can add more
x = random.randrange(len(word_list))
word = word_list[x]
no_words = len(word)
lives = 7
dashes = no_words * "_"
stupid_fill = "_"
correct_guesses = 0
word_save = word
listy = []
listy2 = []
listyz = []
listyz2 = []
listyx = []
listyx2 = []
listyy = []
listyy2 = []
listyf = []
listyf2 = []
hehe = []
hehe2 = []
ghg = 0
breaker = False
words_done = []
county = -1

#functions
def high_score():
    HighScore = open("high score", "w")
    HighScore.write(str(high_score_streak))
    HighScore.close()



def correct_letter_checker(x):
    global Right_Or_Wrong
    global Right_Or_Wrong2
    global Right_Or_Wrong3
    global Right_Or_Wrong4
    global Right_Or_Wrong5
    global place
    global place2
    global place3
    global place4
    global place5
    place = word.find(x)
    if place != -1:
        Right_Or_Wrong = True
        place2 = word.find(x, place+1)
        if place2 != -1:
            Right_Or_Wrong2 = True
            place3 = word.find(x, place2+1)
            if place3 != -1:
                Right_Or_Wrong3 = True
                place4 = word.find(x)
                if place4 != -1:
                    Right_Or_Wrong4 = True
                    place5 = word.find(x)
                    if place5 != -1:
                        Right_Or_Wrong5 = True
                        place4 = word.find(x)
                    elif place5 == -1:
                        Right_Or_Wrong5 = False
                elif place4 == -1:
                    Right_Or_Wrong4 = False
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
    - The spaces are slashes.
                                    |
                                    |

    
    
                                    |
                                    |  
                                    |    _____________________________________
        """
board_after_1 = """                          
                                    |
                                               |
 Rules:                             |          |
                                    |          |
    - The spaces are slashes.                  |
                                    |          |
                                    |          |
                                               |
                                               |
                                               |
                                    |          |
                                    |          |
                                    |    ______|_______________________________
        """

board_after_2 = """                          
                                    |          ___________________
                                               |
 Rules:                             |          |
                                    |          |
    - The spaces are slashes.                  |
                                    |          |
                                    |          |
                                               |
                                               |
                                    |          |
                                    |          |
                                    |    ______|_______________________________
        """
board_after_3 = """                          
                                    |          ___________________
                                               |                  |
 Rules:                             |          |                  |
                                    |          |                  |
    - The spaces are slashes.                              |
                                    |          |
                                    |          |
                                               |
                                    |          | 
                                               |
                                    |          |
                                    |          |
                                    |    ______|_______________________________
        """

board_after_4 = """                       
                                    |          ___________________
                                               |                  |
 Rules:                             |          |                  |
                                    |          |                  |
    - The spaces are slashes.                  |                  O
                                    |          |                  |
                                    |          |                  |
                                    |          |
                                               |
                                    |          |
                                    |          |
                                    |          |
                                    |    ______|_______________________________
        """

board_after_5 = """
                                                ___________________
                                               |                  |
 Rules:                             |          |                  |
                                    |          |                  |
    - The spaces are slashes.                  |                  O
                                    |          |                 /|\  
                                    |          |                  |
                                               |                       
                                    |          |
                                               |
                                    |          |
                                    |    ______|_______________________________
        """
board_after_6 = """
                                                ___________________
                                               |                  |
 Rules:                             |          |                  |
                                    |          |                  |
    - The spaces are slashes.                  |                  O
                                    |          |                 /|\  
                                    |          |                  |
                                               |                 /      
                                    |          |
                                               |
                                    |          |
                                    |    ______|_______________________________
        """
board_after_7 = """
                                                ___________________
                                               |                  |
 Rules:                             |          |                  |
                                    |          |                  |
    - The spaces are slashes.                  |                  O
                                    |          |                 /|\  
                                    |          |                  |
                                               |                 / \     
                                    |          |
                                               |
    You Lose!                       |          |
                                    |    ______|_______________________________
        """


main_board = board



while ghg < 5:
    hehe = []
    hehe2 = []
    correct_letter_checker("/")
    for fds in word:
        hehe2.append(fds)

    for fabds in dashes:
        hehe.append(fabds)

    hehe[place] = hehe2[place]
    hehe2[place] = "_"
    dashes = ""
    dashes = dashes.join(hehe)
    word = ""
    word = word.join(hehe2)
    ghg += 1

hehe =[]
hehe2 = []

for ipo in word:
    hehe.append(ipo)
for iso in word_save:
    hehe2.append(iso)
for dr in range(len(word_save)):
    county += 1
    if dr != "/":
        hehe[county] = hehe2[county]

word = ""
word = word.join(hehe)
hehe =[]
hehe2 = []

high_score_streak1 = open("high score", "r")
high_score_streak = high_score_streak1.read()
high_score_streak1.close()
print("Hangman!!(Movie Theme!)\n")
print(main_board)
print(f"""\nWord: {dashes}\n Lives: {lives}\n  Streak: {high_score_streak}""")

while True:
    choice = input("Choose A Letter:\n")
    words_done.append(choice)
    correct_letter_checker(choice)
    if Right_Or_Wrong:
        listy = []
        listy2 = []
        for abdsz in word:
            listy2.append(abdsz)

        for abds in dashes:
            listy.append(abds)

        listy[place] = listy2[place]
        if listy[place] != "_":
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
            if listyx[place2] != "_":
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
                if listyz[place3] != "_":
                    listyz2[place3] = "_"
                dashes = ""
                dashes = dashes.join(listyz)
                word = ""
                word = word.join(listyz2)
                if Right_Or_Wrong4:
                    listyy = []
                    listyy2 = []
                    for abdsz in word:
                        listyy2.append(abdsz)

                    for abds in dashes:
                        listyy.append(abds)

                    listyy[place4] = listyy2[place4]
                    if listyy[place4] != "_":
                        listyy2[place4] = "_"
                    dashes = ""
                    dashes = dashes.join(listyy)
                    word = ""
                    word = word.join(listyy2)
                    if Right_Or_Wrong5:
                        listyf = []
                        listyf2 = []
                        for abdsz in word:
                            listyf2.append(abdsz)

                        for abds in dashes:
                            listyf.append(abds)

                        listyf[place5] = listyf2[place5]
                        if listyf[place5] != "_":
                            listyf2[place5] = "_"
                        dashes = ""
                        dashes = dashes.join(listyf)
                        word = ""
                        word = word.join(listyf2)




        correct_guesses += 1


    if not(Right_Or_Wrong):
        lives -= 1
        if lives == 6:
            main_board = board_after_1
        if lives == 5:
            main_board = board_after_2
        if lives == 4:
            main_board = board_after_3
        if lives == 3:
            main_board = board_after_4
        if lives == 2:
            main_board = board_after_5
        if lives == 1:
            main_board = board_after_6
        if lives == 0:
            main_board = board_after_7

    print(main_board)
    print(f"""\nWord: {dashes}\nLives: {lives}\nStreak: {high_score_streak}\n""")
    print(f"Words Done: {words_done}")
    if lives == 0:
        print("\nYOU LOSE!\n")
        print(f"It Was {word_save}")
        main_board = board
        high_score_streak = 0
        high_score()
        break
    count = 0
    for gy in dashes:
        if gy != "_":
            count += 1
        if count == len(word):
            print("\nYOU WIN!")
            count = 0
            main_board = board
            high_score_streak = int(high_score_streak) + 1
            high_score()
            breaker = True
    if breaker:
        break












