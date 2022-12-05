import threading
import random
from Room import Room


class RoomManager:
    def __init__(self):
        self.waiting_for_rival = []
        self.key_generator = self.__genereate_active_room_key__()
        self.room_list = []

    def room_key_generator(self):
        for i in range(0, 5000):
            yield i

    def subscript_waiting(self, id):
        self.waiting_for_rival.append(id)

    def __genereate_active_room_key__(self):
        def give_me_id(self, addr_user):
            key = ""
            flag = True
            while flag:
                for x in range(4):
                    key += str(random.randint(0, 9))
                if key in self.dict_of_id.keys():
                    key = ""
                else:
                    flag = False
                    self.dict_of_id[id] = addr_user
            return id

    def pair(self):
        if len(self.waiting_for_rival) % 2 == 0 and len(self.waiting_for_rival) != 0:
            id1 = self.waiting_for_rival.pop(0)
            id2 = self.waiting_for_rival.pop(0)
            key = self.key_generator
            room = Room(id1, id2, key)
            self.room_list.append(room)
            return key
