import pygame


class Update:
    def __init__(self, settings):
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.settings = settings

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()
