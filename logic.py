"""
---------------
FIRST RPG
Logic
By Ann-MarieDev
---------------
"""
#Imports:
import json

#---------------Test if logic.py is working on main.py---------------
def test_logic():
    print("logic.py is working")
    
#---------------VARIABLES---------------
"""
Weapon classes:
- Worst
- Bad
- Good
- Best
- Legendary
"""
worst_weapon = "WEAPON CLASS: Worst"
bad_weapon = "WEAPON CLASS: Bad"
good_weapon = "WEAPON CLASS: Good"
best_weapon = "WEAPON CLASS: Best"
legendary_weapon = "WEAPON CLASS: Legendary"

"""
Clothing/Armor classes:
- Worst
- Bad
- Good
- Best
- Legendary
""" 
worst_armor = "ARMOR CLASS: Worst"
bad_armor = "ARMOR CLASS: Bad"
good_armor = "ARMOR CLASS: Good"
best_armor = "ARMOR CLASS: Best"
legendary_armor = "ARMOR CLASS: Legendary"

#---------------CLASSES---------------
#Inventory Class
class inventory:
    def __init__(self) -> None:
        pass
    
#Character Class
class character:
    def __init__(self, name, age, health, power, hair_color, skin_color, eye_color):
        self.name = name
        self.age = age
        self.health = health
        self.power = power
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
#        self.inventory = inventory
        
#Weapon Class
class weapon:
    def __init__(self, name, damage, weight, weapon_class):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.weapon_class = weapon_class
        
#Clothes/Armor Class
class clothes:
    def __init__(self, name, defense, weight, armor_class):
        self.name = name
        self.defense = defense
        self.weight = weight
        self.armor_class = armor_class

#Spells Class
class spells:
    def __init__(self) -> None:
        pass

#---------------FUNCTIONS---------------
#Inventory functions
def add_item():
    pass

def remove_item():
    pass

#---------------CHARACTERS---------------
#--Main Characters--
#Nala
main_char = character("Nala", 16, 100, 3, "orange", "tan", "green")
#Orlando
main_char_two = character("Orlando", 17, 100, 5, "brown", "tan", "brown")

#--Enemies--
#Alice
enemy_one = character("Alice", 17, 100, 5, "blonde", "pale", "blue")

#--Side Characters/NPC's--

#---------------WEAPONS---------------
#Copy n paste: weapon("",,,),
#weapon(Name,  Damage, Weight,  Weapon Class),
weapons = [
    #---------------Worst---------------
    weapon("Balloon Sword", 0.5, 0.2, worst_weapon),
    weapon("Plastic Sword", 1, 0.5, worst_weapon),
    weapon("Clown Hammer", 0.5, 1, worst_weapon),
    weapon("Broken Pencil", 0, 0.1, worst_weapon),
    #---------------Bad---------------
    weapon("Sling Shot", 0, 4, bad_weapon),
    weapon("Piñata Stick", 2, 2, bad_weapon),
    weapon("Wooden Sword", 4, 2, bad_weapon),
    weapon("Holy Water", 5, 1, bad_weapon),
    weapon("Wooden Bow", 6, 2, bad_weapon),
    #---------------Good---------------
    weapon("Stone Sword", 7, 5, good_weapon),
    weapon("Stone Staff", 8, 4, good_weapon),
    weapon("Strong Bow", 10, 4, good_weapon),
    weapon("War Hammer", 11, 6, good_weapon),
    #---------------Best---------------
    weapon("Metal Sword", 18, 6, best_weapon),
    weapon("Metal Bow", 18, 7, best_weapon),
    weapon("Jumbo Hammer", 20, 15, best_weapon),
    weapon("Katana", 20, 4, best_weapon),
    #---------------Legendary---------------
    weapon("Legendary Sword", 40, 10, legendary_weapon),
    weapon("Legendary Bow", 45, 10, legendary_weapon)
]
#Use a json file??? Lets try it
wepon_json = []
#---------------CLOTHES/ARMOR---------------
#Copy n paste: clothes("",,,,),
#clothes(name, defense, weight, armor_class, color)
clothing = [
    clothes("Chain Link Armor", 4, 25, worst_armor),
    clothes("Wizard Cloak", 5, 4, worst_armor),
]


#---------------STARTER ITEMS---------------






