"""Here the main game runs"""
import pygame
from pygame.locals import *
import os
import settings
import time

from models.level import Level
from models.position import Position
from models.player import Player
from models.gatekeeper import GateKeeper
from models.item import Item
from controllers.keyboard import KeyboardInputs
from views.update import Update
from settings import Settings


def run_game():
    pygame.init()
    pygame.display.set_caption("McGyver")

    mcsettings = Settings()
    level = Level("models/map.txt")
    item = Item(level)
    position = Position(1, 1)
    player = Player(level, mcsettings)
    gatekeeper = GateKeeper(level)

    print("Player initial position =", player.position)
    chk_event = KeyboardInputs(player)
    updater = Update(mcsettings, level, player)
    updater.update_screen()

    running_state = True
    while running_state:
        chk_event.check_events()
        player.pickup_item()
        updater.update_player()
        updater.update_gatekeeper()
        updater.update_item()
        player.check_victory_condition()
        if updater.ending_display():
            continue
        else:
            while True:
                chk_event.check_events()


if __name__ == "__main__":
    run_game()
