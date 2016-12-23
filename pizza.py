#!/usr/bin/python


class Am_I_A_Pizza_Or_Burger:
    def __init__(self):
        self.whatAmI = 'pizza'


    def am_I_a_burger(self):
        if self.whatAmI == 'burger':
            return True
        else:
            return False

    def am_I_a_pizza(self):
        if self.whatAmI == 'pizza':
            return True
        else:
            return False

    def amIaSportsCar(self):
        if self.whatAmI == 'sportscar':
            return True

        return False

if __name__ == '__main__':
            whatami = Am_I_A_Pizza_Or_Burger()
            print(whatami.am_I_a_burger()        )
            print(whatami.am_I_a_pizza()        )
            print(whatami.amIaSportsCar()        )

