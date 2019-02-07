from Farkle import *

final_score = 0
rounds = 1
playing = True
dice = 6
round_score = 0
while playing:

    Game = Farkle()
    Values = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    dontfail = True

    roll = Game.dice_roll(dice)

    for i in roll:
        Values[i] += 1

    # check to see if roll/values contains 1, 5, or duplicates, end round if not
    Game.end_og_game(rounds, Values)
    playing = Game.end_og_game(rounds, Values)

    print(f"this is round {rounds}\n")
    print(roll)
    temp_score = 0
    # hent et input fra spilleren
    choice = int
    while True:
        try:
            choice = int(input("which dice do you want?: >>>"))
            break
        except ValueError:
            print("i need a number ")
            print(roll)
    # check om input er valid i forhold til roll
    amount = int
    try:

        if Game.valid(choice, Values) == True:
            while dontfail:

                # hvis muligt, spørg hvor mange de vil have
                amount = int
                try:
                    amount = int(input("how many do you want?: "))
                except ValueError:
                    print("It has to be a number that is in the roll")
                except TypeError:
                    print("only numbers")
                try:
                    if Game.valid_amount(amount, choice, Values) == True:
                        print(amount)
                        amount = amount
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("No can do, it has to be a valid amount")
                except TypeError:
                    print("something went wrong")
    except Exception:
        print("something went wrong, try again")

    # tilføj til temp_score(list)
    temp_score += Game.new_score(choice, amount)
    round_score += temp_score
    dice -= amount
    print(f'this rounds current score is {round_score}')
    input("await")
    play = True
    # input om de vil slå med resterende terninger
    # hvis ja fjern antal valgte terninger og fortsæt med runde
    # hvis nej, og temp_score > 350 runde +1 og alle terninger med igen
    # hvis roll bliver tømt, tilføj 6 nye terninger og giv rolls igen
    while True:
        keep_playing = str
        try:
            keep_playing = str(input(f"do you want to roll the new amount of dice?{dice}: "))
        except ValueError:
            print("it has to be a yes or a no")
        if keep_playing == 'Yes'.lower() or keep_playing == 'yes'.upper():
            print("let's go")

            break
        else:
            print("alright, let's roll with 6 new dice")
            if round_score < 350:
                print("sorry, you need more than 350 points in a round before quitting")
                play = True
            else:
                print("alright, let's roll with 6 new dice")
                dice = 6
                rounds += 1
                final_score += temp_score
                round_score = 0
                play = False
            break



