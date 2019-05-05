from models.level import Level
from models.position import Position
from models.player import Player

# Step one instantiate level
level = Level("models/map.txt")
p = Position(1, 1)

player = Player(level)

player.move("down")


print(player.position)