import pygame


class Update:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()
