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
    
#---------------CLASSES---------------

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
        
#Weapon Class
class weapon:
    def __init__(self, name, damage, weight, weapon_class):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.weapon_class = weapon_class
        
#Clothes/Armor
class weapon:
    def __init__(self, name, defense, weight, type, color):
        self.name = name
        self.defense = defense
        self.weight = weight
        self.type = type
        self.color = color

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
#---------------VARIABLES---------------
"""
Weapon classes:
- Worst
- Bad
- Good
- Best
- Legendary
"""
worst = "WEAPON CLASS: Worst"
bad = "WEAPON CLASS: Bad"
good = "WEAPON CLASS: Good"
best = "WEAPON CLASS: Best"
legendary = "WEAPON CLASS: Legendary"

#---------------WEAPONS---------------
#Copy n paste: weapon("",,,),
#weapon(Name,  Damage, Weight,  Weapon Class),
weapons = [
    #---------------Worst---------------
    weapon("Baloon Sword", 0.5, 0.2, worst),
    weapon("Plastic Sword", 1, 0.5, worst),
    weapon("Clown Hammer", 0.5, 1, worst),
    weapon("Broken Pencil", 0, 0.1, worst),
    #---------------Bad---------------
    weapon("Sling Shot", 0, 4, bad),
    weapon("Piñata Stick", 2, 2, bad),
    weapon("Wooden Sword", 4, 2.0, bad),
    weapon("Holy Water", 5, 1, bad),
    #---------------Good---------------
    #---------------Best---------------
    #---------------Legendary---------------
]




#---------------STARTER ITEMS---------------






