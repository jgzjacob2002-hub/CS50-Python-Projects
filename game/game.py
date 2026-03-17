import random

while True:
    try:
        nivel = int(input("Level: "))
        aletorio = random.randint(1, nivel)
        if nivel <= 0:
            continue
        else:
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if guess > 0:
                            if guess > aletorio:
                                print("Too large!")
                                continue

                            elif guess < aletorio:
                                print("Too small!")
                                continue

                            elif guess == aletorio:
                                print("Just right!")
                                exit()
                        else:
                            continue
                    except ValueError:
                        continue
    except ValueError:
        continue


