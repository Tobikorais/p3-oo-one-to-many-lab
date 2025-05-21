from lib.pet import Pet  # Import the Pet class

class Owner:
    def __init__(self, name):
        # Initialize the Owner with a name
        self.name = name

    def pets(self):
        # Returns a list of all pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Checks if the pet is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        # Returns a sorted list of pets by their names
        return sorted(self.pets(), key=lambda pet: pet.name)
