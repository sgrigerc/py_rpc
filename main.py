# Импорт файлов и классов из них
from player import Player
from variants import Variants

# Создаем объекты на основе класса Player
player1 = Player(Variants.rock, "Mona")

# При создании можем не передавать значения или же
# можем передать выбор (камень, ножницы или бумага), а также имя
player2 = Player(Variants.scissors, "Hine")

# далее через объект можем обратить к функции whoWins
# и мы узнаем кто победил

print(player1.whoWins(player1, player2))

