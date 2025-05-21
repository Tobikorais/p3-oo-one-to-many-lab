from lib.owner import Owner
from lib.pet import Pet

def test_owner_init():
    """Test Owner class initialization"""
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_init():
    """Test Pet class initialization"""
    pet = Pet("Buddy", "dog")
    assert pet.name == "Buddy"
    assert pet.pet_type == "dog"
    assert pet.owner is None

def test_add_pet():
    """Test adding a pet to an owner"""
    owner = Owner("John")
    pet = Pet("Buddy", "dog")
    owner.add_pet(pet)
    assert pet.owner == owner
    assert pet in owner.pets()

def test_get_sorted_pets():
    """Test getting sorted pets by name"""
    owner = Owner("John")
    pet1 = Pet("Charlie", "dog", owner)
    pet2 = Pet("Buddy", "dog", owner)
    pet3 = Pet("Max", "dog", owner)
    sorted_pets = owner.get_sorted_pets()
    assert [pet.name for pet in sorted_pets] == ["Buddy", "Charlie", "Max"]