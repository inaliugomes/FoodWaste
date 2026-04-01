from enum import Enum

#Meu classe ENUM para que el utilizado solo puede eligir destas opciones
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
