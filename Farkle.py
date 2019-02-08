from random import randint
from time import sleep

class Farkle:

    def dice_roll(self, dice):
        self.roll = []
        for i in range(dice):
            self.roll.append(randint(1, 6))
        return self.roll

    def new_score(self, choice, amount):
        score = 0
        x = amount
        if amount >= 3:
            x -= 2
        if choice == 1:
            if amount < 3:
                score += 100 * x
            elif amount >= 3:
                score += 1000 * x
        elif choice == 2:
            score += 200 * x
        elif choice == 3:
            score += 300 * x
        elif choice == 4:
            score += 400 * x
        elif choice == 5:
            if amount < 3:
                score += 50 * x
            elif amount >= 3:
                score += 500 * x
        elif 6 == choice:
            score += 600 * x
        return score

    def valid(self, choice, dictionary):
        # needs a dict of key, values to check from
        p = dictionary.get(choice)
        if choice in (1, 5) and p > 0:
            return True
        elif choice in (2, 3, 4, 6) and p > 2:
            return True
        else:
            return False

    def valid_amount(self, amount, choice, dictionary):
        p = dictionary.get(choice)
        if amount > p:
            return False
        elif amount <= 0:
            return False
        else:
            return True

    def end_of_game(self, rounds, dictionary):
        playing_new = True
        for k, v in dictionary.items():
            p = dictionary.get(k)
            if k in (1, 5) and p < 1:
                rounds += 1
                playing_new = False
            elif k in (2, 3, 4, 6) and p < 3:
                rounds += 1
                playing_new = False
            elif k in (1, 5) and p >= 1:
                playing_new = True
                break
            elif k in (2, 3, 4, 6) and p >= 3:
                playing_new = True
                break
        if playing_new == False:
            sleep(0.1)
            return False
        return playing_new

    def choice(self, roll):
        while True:
            try:
                choice = int(input("which dice do you want?: >>>"))
                break
            except ValueError:
                print("i need a number ")
                print(roll)
        return int(choice)

    def yes_or_no(self, tekst):
        while True:
            tjek = ''
            try:
                tjek = str(input(f'{tekst}:' ))
            except ValueError:
                print("it has to be a yes or a no")
            if tjek == 'Yes'.lower() or tjek == 'yes'.upper():
                return True
            else:
                return False

