###
#A character have attributes, which are Strength - Agility - Intellignece - Wisdom. 
#The values of these attributes can be from 1 to 20. 
#
#
#
###

from abc import ABC, abstractmethod

class Character():
    def __init__(self, name: str, strength: int, agility:int, intelligence:int, wisdom:int):
        self.name = name
        self.__strength = min(max(1, strength), 20)
        self.__agility = min(max(1, agility), 20)
        self.__intelligence = min(max(1, intelligence), 20)
        self.__wisdom = min(max(1, wisdom), 20)
        
    def strength(self):
        return self.__strength
    
    def starter_health_points(self):
        return self.__strength
    
    def agility(self):
        return self.__agility
    
    def starter_defense_score(self):
        return self.__agility
    
    def healing_rate(self):
        return self.starter_health_points/4
    
    def intelligence(self):
        return self.__intelligence
    