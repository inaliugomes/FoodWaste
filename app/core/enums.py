from enum import Enum

#Enum class so the user can only choose from these options
class FoodNameEnum(str,Enum):
    lechuga = "Lechuga"
    tomate = "Tomate"
    cebolla = "Cebolla"
    arroz = "Arroz"
    alubias = "Alubias"
    tiras = "Tiras"
    pollo = "Pollo"

class CategoryEnum(str,Enum):
    verdura = "Verdura"
    pollo = "Pollo"
    organico = "Organico"
