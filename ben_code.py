import json

"""
---------------
FIRST RPG
Logic
By Ann-MarieDev
---------------
"""
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
weapon_classes = [worst_weapon, bad_weapon, good_weapon, best_weapon, legendary_weapon]
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
    def __init__(self, name, age, health, power, hair_color, skin_color, eye_color, inventory):
        self.name = name
        self.age = age
        self.health = health
        self.power = power
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.inventory = inventory
        
#Weapon Class
class weapon:
    def __init__(self, name, damage, weight, weapon_class):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.weapon_class = weapon_class
        
    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return self.name
        
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
main_char = character("Nala", 16, 100, 3, "orange", "tan", "green", [])
#Orlando
main_char_two = character("Orlando", 17, 100, 5, "brown", "tan", "brown", [])

#--Enemies--
#Alice
enemy_one = character("Alice", 17, 100, 5, "blonde", "pale", "blue", [])

#--Side Characters/NPC's--

#---------------WEAPONS---------------
#Copy n paste: weapon("",,,),
#weapon(Name,  Damage, Weight,  Weapon Class),
# Function to load weapons from a JSON file
weapons = []  # Initialize an empty list for weapons
with open("weapons.json", 'r') as file:
    data = json.load(file)  # Load the JSON data
    
    for weapon_name, weapon_info in data.items():
        # Create a weapon instance using the data from the JSON
        wclass = weapon_classes[weapon_info['weapon_class']]
        new_weapon = weapon(
            name=weapon_name.title(),  # Capitalize the weapon name
            damage=weapon_info['damage'],
            weight=weapon_info['weight'],
            weapon_class=wclass,
        )
        weapons.append(new_weapon)  # Append the weapon instance to the list
        

#---------------CLOTHES/ARMOR---------------
#Copy n paste: clothes("",,,,),
#clothes(name, defense, weight, armor_class, color)
clothing = [
    clothes("Chain Link Armor", 4, 25, worst_armor),
    clothes("Wizard Cloak", 5, 4, worst_armor),
    clothes("",0,0,0,),
]


#---------------STARTER ITEMS---------------


