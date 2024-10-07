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
        
#Clothes/Armor Class
class weapon:
    def __init__(self, name, defense, weight, type, color):
        self.name = name
        self.defense = defense
        self.weight = weight
        self.type = type
        self.color = color
        
#Inventory Class
class inventory:
    def __init__(self) -> None:
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
    weapon("Wooden Sword", 4, 2, bad),
    weapon("Holy Water", 5, 1, bad),
    weapon("Wooden Bow", 6, 2, bad),
    #---------------Good---------------
    weapon("Stone Sword", 7, 5, good),
    weapon("Stone Staff", 8, 4, good),
    weapon("Strong Bow", 10, 4, good),
    weapon("War Hammer", 11, 6, good,),
    #---------------Best---------------
    weapon("Metal Sword", 18, 6, best),
    weapon("Metal Bow", 18, 7, best),
    weapon("Jumbo Hammer", 20, 15, best),
    weapon("Katana", 20, 4, best),
    #---------------Legendary---------------
    weapon("Legendary Sword", 40, 10, legendary),
    weapon("Legendary Bow", 45, 10, legendary)
]

#---------------STARTER ITEMS---------------






