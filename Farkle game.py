from Farkle import *
from time import sleep
final_score = 0
rounds = 1
playing = True
dice = 6
round_score = 0
sleep(0.1)
while True:
    print(f' total score is: {final_score}')
    playing = True
    if rounds == 10:
        print("end of the game, you made it!")
        print(f'this is your final score!: {final_score}')
        input("press enter to exit: ")
        break
    while playing:
        print(f'current round score {round_score}'
              f'and this is the total score: {final_score}')

        Game = Farkle()
        Values = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        dontfail = True

        roll = Game.dice_roll(dice)
        street = False
        while (1, 2, 3, 4, 5, 6) in roll:
            street = Game.yes_or_no("there is a street, do you want the street?")
            if street == True:
                print("smart choice, restarting round with 2000 score, you must roll one more time")

                round_score += 2000
                street = True
                break
            elif street == False:
                print("i think you meant to say yes?")
        if street == True:
            break

        for i in roll:
            Values[i] += 1


        # check to see if roll/values contains 1, 5, or duplicates, end round if not
        if Game.end_of_game(rounds, Values) == False:
            dice = 6
            rounds += 1
            round_score = 0
            break
        playing = Game.end_of_game(rounds, Values)

        print(f"this is round {rounds}\n")
        print(roll)
        temp_score = 0

        # check om input er valid i forhold til roll
        amount = 0
        try:
            # hent et input fra spilleren


            # loop der får et input der ikke bare gå videre
            while dontfail:
                choice = Game.choice(roll)
                if Game.valid(choice, Values):
                    # hvis muligt, spørg hvor mange de vil have
                    amount = 0
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
                            new_amount = Values.get(choice) - amount
                            new_values = {choice: new_amount}
                            Values.update(new_values)
                            temp_score += Game.new_score(choice, amount)
                            round_score += temp_score
                            dice -= amount
                        else:
                            raise ValueError
                    except ValueError:
                        print("No can do, it has to be a valid amount")
                    except TypeError:
                        print("something went wrong")
                    # tjek om der er flere valid values
                    if Game.end_of_game(rounds, Values) == True:
                        try:
                            for i in range(amount):
                                roll.remove(choice)
                            print(roll)
                            if Game.yes_or_no('Would you like more dice from the current roll?') == True:
                                continue
                            else:
                                break
                        except ValueError:
                            print("something went wrong")
                    else:
                        break
                elif Game.valid(choice, Values) == False:
                    print("i need a number that is in the roll, and a number that is valid, valid numbers are 1 or 5 "
                          "and 2, 3, 4, 6 when there are 3 or more")
                    continue
        except Exception:
            print("something went wrong, try again")

        # tilføj til temp_score(list)

        print(f'this rounds current score is {round_score}\n')
        # input om de vil slå med resterende terninger
        # hvis ja fjern antal valgte terninger og fortsæt med runde
        # hvis nej, og temp_score > 350 runde +1 og alle terninger med igen
        # hvis roll bliver tømt, tilføj 6 nye terninger og giv rolls igen
        if dice == 0:
            print("lucky, you'll get a new round")
            dice = 6
            break
        while True:
            keep_playing = ''
            try:
                keep_playing = str(input(f"do you want to roll the new amount of dice?: {dice}: "))
            except ValueError:
                print("it has to be a yes or a no")
            if keep_playing == 'Yes'.lower() or keep_playing == 'yes'.upper():
                print("let's go")
                break
            else:
                if round_score < 350:
                    print("sorry, you need more than 350 points in a round before quitting "
                          "rolling again")
                    sleep(1)
                else:
                    print("alright, let's roll with 6 new dice")
                    dice = 6
                    rounds += 1
                    final_score += round_score
                    round_score = 0
                break
