from animal_class import Animal

class Dog(Animal):

    def __init__(self, name, fur, eye_colour, pet_id):
        self.name = name
        super().__init__(fur, eye_colour)
        self.__pet_id = pet_id


    def growl(self, animal):
        return f"BARK! I see {animal}"

    def get_pet_id(self):
        return self.__pet_id

    def set_pet_id(self, new_id):
        self.__pet_id = new_id
        return f"congrats, your new pet id is {new_id}"



german_shepherd = Dog("german shepherd", "scruffy", "brown", 1)

print(german_shepherd.growl("samir"))

german_shepherd.set_pet_id(300)

print(german_shepherd.get_pet_id())

