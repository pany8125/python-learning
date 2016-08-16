class Parent():
    def print_last_name(self):
        print('Roberts')

class Child(Parent):
    def print_first_name(self):
        print('Bucky')

    #Overwriting
    # def print_last_name(self):
    #     print('Snitzleberg')

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

class Mario():
    def move(self):
        print('I am moving!')

class Shroom():
    def eat_shroom(self):
        print('Now I am big')

class Flower():
    def eat_flower(self):
        print('Now I can fire')

class BigMario(Mario,Shroom,Flower):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()
bm.eat_flower()