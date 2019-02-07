from random import randint


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
        if 1 == choice:
            if amount < 3:
                score += 100 * x
            elif amount >= 3:
                score += 1000 * x
        elif 2 == choice:
            score += 200 * x
        elif 3 == choice:
            score += 300 * x
        elif 4 == choice:
            score += 400 * x
        elif 5 == choice:
            if amount < 3:
                score += 50 * x
            elif amount >= 3:
                score += 500 * x
        elif 6 == choice:
            score += 600 * x
        return score


    def score(self, choice):
        score = 0
        x = len(choice)
        if len(choice) > 3:
            x = len(choice) - 3
        if 1 in choice:
            if len(choice) < 3:
                score += 100 * len(choice)
            elif (choice) > 3:
                score += 1000 * x
        elif 2 in choice:
            score += 200 * x
        elif 3 in choice:
            score += 300 * x
        elif 4 in choice:
            score += 400 * x
        elif 5 in choice:
            if len(choice) < 3:
                score += 50 * len(choice)
            elif len(choice) > 3:
                score += 5 * x
        elif 6 in choice:
            score += 600 * x
        return score

    def valid(self, choice, dictionary):
        # needs a dict of key, values to check from
        p = dictionary.get(choice)
        if choice == 1 or 5:
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

    def end_og_game(self, rounds, dictionary):
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
            print("there is no valid choices")
            return False
        return playing_new
