class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.owner = owner
        self.pet_type = pet_type
        self.all.append(self)
    @property
    def pet_type(self ):
        return self._pet_type
    @pet_type.setter
    def pet_type(self,pet_type ):
        if(not pet_type in self.PET_TYPES):
            raise Exception("invalide pet type")
        self._pet_type = pet_type
         


class Owner:
    def __init__(self, name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if(not isinstance(pet,Pet)):
            raise Exception("invalid pet")
        pet.owner = self
    def get_sorted_pets(self):
        return sorted([*self.pets()], key=lambda pet:pet.name)
    
