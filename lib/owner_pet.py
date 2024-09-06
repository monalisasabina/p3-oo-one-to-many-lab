class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] 
    
    all = []
    
    def __init__(self,name,pet_type,owner = None):
        self.name = name
        self.pet_type =pet_type
        self.owner = owner
        Pet.all.append(self)


    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Invalid pet type.')
        self._pet_type = pet_type     

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception("Object is not of type Owner")
        self._owner = owner
       

class Owner:
    
     def __init__(self,name):
        self.name = name

     def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
     
     def add_pet(self,pet):
         if not isinstance(pet,Pet):
          raise Exception("pet is not of type Pet")
         pet.owner = self

     def get_sorted_pets(self):
         return sorted(self.pets(), key= lambda pet: pet.name)



# Create some owners
owner1 = Owner("Alice")
owner2 = Owner("Bob")

#  Create some pets
pet1 = Pet("Rex", "dog", owner1)
pet2 = Pet("Whiskers", "cat", owner1)
pet3 = Pet("Buddy", "bird", owner2)

# Add pets to the owners
owner1.add_pet(pet1)
owner1.add_pet(pet2)
owner2.add_pet(pet3)

#  Output each owner's pets
print(f"{owner1.name}'s pets: {[pet.name for pet in owner1.pets()]}")
print(f"{owner2.name}'s pets: {[pet.name for pet in owner2.pets()]}")

# Output sorted pets for owner1
print(f"{owner1.name}'s sorted pets: {[pet.name for pet in owner1.get_sorted_pets()]}")        
               


     