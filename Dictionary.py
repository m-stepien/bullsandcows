import random


class Dictionary:
    def __init__(self, dificulty_level, resource_path="resource/dictionary.txt"):
        self.resource_path = resource_path
        self.word_list = self.read_from_file()
        self.dificulty_level = dificulty_level
        self.filter_dictionary = {
            "easy": lambda: [x for x in self.word_list if len(x) < 5],
            "medium": lambda: [x for x in self.word_list if 5 <= len(x) <= 8],
            "hard": lambda: [x for x in self.word_list if len(x) >= 9]
        }

    def read_from_file(self):
        try:
            with open(self.resource_path, "r") as resource:
                word_list = []
                for line in resource.readlines():
                    word_list.append(line.replace("\n", ""))
                return word_list
        except OSError:
            print("Plik ze sciezki nie istnieje lub zostal uszkodzony")

    def get_filter_word_list(self):
        return self.filter_dictionary[self.dificulty_level]()

    def choose_random_word(self):
        return random.choice(self.word_list)
