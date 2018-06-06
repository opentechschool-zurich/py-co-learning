import names
from datetime import datetime
from datetime import timedelta
from random import randrange
import os, json

def JSON_write(config, to_file):

    with open(to_file, 'w') as f:
        json.dump(config, f)

def JSON_update(config, to_file):

    with open(to_file, 'a') as f:
        json.dump(config, f)

def JSON_read(from_file):

    with open(from_file, 'r') as f:
        config = json.load(f)
        f.close()
        return config

# added id to the Room class
class Room:
    def __init__(self, id, be, pr, se, bo, ro):
        self.id = id
        self.beds = be
        self.price = pr
        self.seeview = se
        self.booked = bo
        self.room_name = ro

# would rename to create_random rooms, renmaed hotel to hotel_rooms
def create_hotel(total_rooms):
    hotel_rooms = {}
    for x in range(total_rooms):
        id = x
        beds = randrange(4)+1
        price = 10 * (randrange(10)+1)
        seeview = randrange(2)

        booked_for = randrange(20)
        booked = []
        for i in range(booked_for): # better use i and not x again like in parent loop
            booked.append(str(datetime.now()+timedelta(days=randrange(i+1)))[:10])

        name = names.get_first_name(gender='female')

        hotel_rooms[id] = Room(id, beds, price, seeview, booked, name)

    return hotel_rooms

class Hotel(object):

    __save_path = os.path.join(os.getcwd(), 'hotel_storage.json')

    def __init__(self, name, price_cat, location):
        self.name = name
        self.price_cat = price_cat
        self.location = location
        self.rooms = {}

    def init_random_hotel(self):
        self.rooms = create_hotel(total_rooms=100)

    def load_config(self):
        if os.path.isfile(self.__save_path):
            dict = JSON_read(self.__save_path)
            for key in dict:
                setattr(self, key, dict[key])
        else:
            print("Folder Setting File does not exist")

    def write_config(self):
        config_dict = self.__dict__
        JSON_write(config_dict, self.__save_path)

# Test code

Ho = Hotel('Ibis', 'Top-Class', 'Berlin Mitte')
Ho.init_random_hotel()

# works great, but an Object Rooms can not be written as json
#

Ho.write_config()   # does not work, let's discuss why

# the idea to make a class for the rooms is cool too



# def conv_to_dic(obj):
#     dict_ex = {}
#     for x in obj:
#         dict_ex[x] = [obj[x].beds, obj[x].price, obj[x].seeview, obj[x].booked, obj[x].room_name]
#
#     return dict_ex

# if __name__ == '__main__':
#     hotel = create_hotel()
#
#     print('The name of room is {}'.format(hotel[10].room_name))
#     dic_hotel = hotel
#
#     for x in (dic_hotel):
#         print('hotel {} properties are {}'.format(x, dic_hotel[x]))

