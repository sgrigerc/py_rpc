from variants import Variants
class Player:

    def __init__(self, choice=Variants.scissors, name='John'):
        self.choice = choice,
        self.name = name

    # def getChoice(self):
    #     return self.choice
    def whoWins(self, player_1, player_2):
        if player_1.choice == player_2.choice:  # 1
            return print("Ничья")
        elif player_1.choice == Variants.rock.value and player_2.choice == Variants.scissors.value:  # 2
            return print("Выиграл: ", player_1)
        elif player_1.choice == Variants.rock and player_2.choice == Variants.paper:  # 3
            return print("Выиграл: ", player_2)
        elif player_1.choice == Variants.scissors and player_2.choice == Variants.rock:  # 4
            return print("Выиграл: ", player_2)
        elif player_1.choice == Variants.scissors and player_2.choice == Variants.paper:  # 5
            return print("Выиграл: ", player_1)
        elif player_1.choice == Variants.paper and player_2.choice == Variants.rock:  # 6
            return print("Выиграл: ", player_1)
        elif player_1.choice == Variants.paper and player_2.choice == Variants.scissors:  # 7
            return print("Выиграл: ", player_2)
