from src.colors import White
import json

class Settings:
    ''' place to organize the games settings we might want to mess around with '''

    def __init__(self, tws):
        ''' tws will be 'self' from the main game loop
        this will give us access to everything
         in the loop we allow it to with 'self'
        '''

        self.game_loop = tws

        # screen dimentions
        # Display vars

        settings_json = self.read_json()
        self.size = self.screen_width, self.screen_height = settings_json["screen_width"], settings_json["screen_height"]  # temporary
        self.caption = 'Terrible World Simulator'

        self.background_color = White

        # we can use the variable to try different speeds
        # by passing it to self.clock.tick()
        self.game_pace = 60

    def read_json(self) -> {str, int}:
        with open("./src/settings.json") as settings:
            data = json.load(settings)
            return data
