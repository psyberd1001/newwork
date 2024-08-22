class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)



Home = House('ЖК Эльбрус', 18)
Home_2 = House('Домик в деревне', 2)
Home.go_to(5)
Home_2.go_to(10)