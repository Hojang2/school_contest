#!usr/bin/python3
from time import ctime


class Ticket:

    def __init__(self, minutes, zones, cheap_price, expensive_price):
        self.minutes = minutes
        self.zones = zones
        self.cheap_price = cheap_price
        self.expensive_price = expensive_price
        self.return_money = 0
        self.price = None
        self.type = None

    def get_price(self, argument):
        if argument == "Z":
            return self.expensive_price
        elif argument == "R":
            return self.cheap_price
        else:
            print("Wrong ticket type")
            exit()

    def validate_zones(self, zones):
        if self.zones == "*":
            return True
        elif self.zones >= zones:
            return True
        else:
            return False

    def validate_time(self, time):
        if self.minutes >= time:
            return True
        else:
            return False

    def __str__(self):
        return """
        Integrovaný dopravní systém JMK
        Dopravní podnik města Brna, a.s.
        {}
        Tarif platný k 1.9. 2018
        *{} Kč vč. DPH
        {}, přestupní {} min
        {} zóny
        Jízdenku označte ihned
        při nástupu do vozidla
        nebo před nástupem do vlaku
        
        Vráceno: {} Kč
        """.format(ctime(), self.price, self.type, self.minutes, self.zones, self.return_money)


class Automat:

    def __init__(self):
        self.tickets = []
        self.tickets.append(Ticket(15, 2, 5, 20))
        self.tickets.append(Ticket(60, 2, 6, 25))
        self.tickets.append(Ticket(90, 3, 6, 27))
        self.tickets.append(Ticket(90, 4, 8, 34))
        self.tickets.append(Ticket(120, 5, 10, 42))
        self.tickets.append(Ticket(120, 6, 12, 49))
        self.tickets.append(Ticket(150, 7, 14, 56))
        self.tickets.append(Ticket(150, 8, 15, 63))
        self.tickets.append(Ticket(180, 9, 17, 71))
        self.tickets.append(Ticket(180, 10, 19, 78))
        self.tickets.append(Ticket(180, "*", 21, 86))
        # self.tickets.append(Ticket(0, 1, 4, 16))
        # self.tickets.append(Ticket(86400, [100, 101], 22, 90))

    def choose_ticket(self, time, zones, type):
        """Getting only tickets that has wanted time, and zones"""
        tickets = []
        for ticket in self.tickets:
            if ticket.validate_time(time):
                if ticket.validate_zones(zones):
                    tickets.append(ticket)
        return tickets

    def run(self):
        try:
            time = int(input("Select time in minutes: "))
            zones = int(input("select number of zones: "))
            type = input("Standard [Z]/ cheap [R]: ")
        except ValueError:
            print("Some values are not numbers")
            exit()
        tickets = self.choose_ticket(time, zones, type)
        ticket = tickets[0]
        ticket.price = ticket.get_price(type)
        ticket.type = "Základní" if type == "Z" else "Zlevěná"
        coins = [1, 2, 5, 10, 20, 50]
        money = 0
        while money <= ticket.price:  # Runs before the user pays enough for ticket
            try:
                tmp = int(input("throw money: "))
                if tmp in coins:
                    money += tmp
                else:
                    print("coin doesn't exist")
            except ValueError:
                print("Not a number")

        if money > ticket.price:
            ticket.return_money = money - ticket.price

        print(ticket)  # Calls __str__() method of ticket


aut = Automat()
aut.run()
