class Stats:
    def __init__(self, bulls, cows):
        self.bulls = bulls
        self.cows = cows

    def __str__(self):
        return "Bulls:\t{}\nCows:\t{}".format(self.bulls, self.cows)
