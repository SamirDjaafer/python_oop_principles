class Animal:

    def __init__(self, fur, eye_colour):
        self.fur = fur
        self.eye_colour = eye_colour


    def growl(self, animal):
        return f"Grrrr I see that {animal}"



tiger = Animal("orange stripes", "black")

print(tiger.eye_colour)

print(tiger.growl("gazelle"))

