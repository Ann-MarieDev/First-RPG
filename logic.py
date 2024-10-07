"""
---------------
FIRST RPG
Logic
By Ann-MarieDev
---------------
"""
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


