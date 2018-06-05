import names
from datetime import datetime
from datetime import timedelta
from random import randrange


class Hotel:
    def __init__(self):
        self.rooms = {}
        for x in range(100):
            beds = randrange(4) + 1
            price = 10 * (randrange(10) + 1)
            seeview = randrange(2)

            booked_for = randrange(20)
            booked = []
            for y in range(booked_for):
                booked.append(str(datetime.now() + timedelta(days=randrange(y + 1)))[:10])

            name = names.get_first_name(gender='female')

            self.rooms[x] = [beds, price, seeview, booked, name]


    def if_available_date(self, des_date):
        available_rooms = []
        for x in self.rooms:
            if des_date not in self.rooms[x][3]:
                available_rooms.append(self.rooms[x][4])
        return available_rooms



if __name__ == '__main__':
    hotel = Hotel()
    print(hotel.if_available_date('2018-06-09'))