class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):

        if self.open_seats() > 0:
            self.passengers.append(name)
            print("Add with success")
        else:
            print("Não deu para adicionar")

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def exibir_resultado(self):
        print(self.passengers)
        print(len(self.passengers))
        print(self.capacity)


flight = Flight(3)

pessoas = ["Sancho","Augusto", "Art", "Tok"]
for name in pessoas:
    flight.add_passenger(name)


flight.exibir_resultado()




'''people = ["Sancho", "Augusto", "Arruda", "Caires"]
for person in people:
    if flight.add_passenger(person):
        print("Added {} to flight sucessfully.".format(person))
    else:
        print("No avaible seats for {} ".format(person))'''