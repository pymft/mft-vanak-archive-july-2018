class Player:
    number_of_wins = 0

    def __init__(self, name, money=200):
        print('an object created', name)
        self.name_of_instance = name
        self.health = 100
        self.money = money
        self.is_alive = True


    def hited(self):
        self.health -= 25
        if not self.health > 0:
            self.is_alive = False



john = Player('John')
bob = Player('Bob')
ross = Player('Ross')

print('John ',john.name_of_instance)
print('Bob  ',bob.name_of_instance)
print('Ross ',ross.name_of_instance)

for i in [1, 2, 3, 4]:
    john.hited()
    print(john.health,
          'John is alive : ' ,
          john.is_alive)

# print('John', john.number_of_wins)
# print(john.__dict__)
# john.number_of_wins = 1
# print(john.__dict__)
