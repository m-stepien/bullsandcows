class Stats:
    def __init__(self, bulls, cows):
        self._bulls = bulls
        self._cows = cows

    def get_bulls(self):
        return self._bulls

    def get_cows(self):
        return self._cows

    def __str__(self):
        return "Bulls: {}\nCows: {}".format(self._bulls, self._cows)
