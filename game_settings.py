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
        self.size = self.screen_width, self.screen_height = 1920, 1080  # temporary
        self.caption = 'Terrible World Simulator'

        self.background_color = (255, 255, 255)

        # we can use the variable to try different speeds
        # by passing it to self.clock.tick()
        self.game_pace = 60
