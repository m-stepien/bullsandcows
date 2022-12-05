import random


class IdGenerator:
    def __init__(self):
        self.dict_of_id = dict()

    def give_me_id(self, addr_user):
        id = ""
        flag = True
        while flag:
            for x in range(12):
                id += str(random.randint(0, 9))
            if id in self.dict_of_id.keys():
                id = ""
            else:
                flag = False
                self.dict_of_id[id] = addr_user
        return id

