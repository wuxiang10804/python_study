class GameStates():

    def __init__(self):
        """
        initialize statistics
        """
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.score = 0