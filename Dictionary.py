import random


class Dictionary:
    def __init__(self, resource_path):
        self.resource_path = resource_path
        self.word_list = self.read_from_file()

    def read_from_file(self):
        try:
            with open(self.resource_path, "r") as resource:
                word_list = []
                for line in resource.readlines():
                    word_list.append(line.replace("\n", ""))
                return word_list
        except OSError:
            print("Plik ze sciezki nie istnieje lub zostal uszkodzony")

    def choose_random_word(self):
        return random.choice(self.word_list)
