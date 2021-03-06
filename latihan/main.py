from Cat import *
from Snake import *

animal = Animal()
animal.setName("Buddy")
animal.setHasTail(False)
animal.setSkinType("Feather")
animal.setFoodType("Omnivore")

cat1 = Cat()
cat1.setName("Molly")
cat1.setHasTail(True)
cat1.setSkinType("Hair")
cat1.setFoodType("Carnivore")
cat1.setBreed("Persian")
cat1.setColor("White")

snake1 = Snake()
snake1.setName("Barbara")
snake1.setHasTail(True)
snake1.setSkinType("Scale")
snake1.setFoodType("Carnivore")
snake1.setLength(5.5)
snake1.setIsVenom(True)

print("-> Animal")
print("Name\t: " + animal.getName())
print("Tail\t: " + ("Yes" if animal.getHasTail() else "No"))
print("Skin\t: " + animal.getSkinType())
print("Type\t: " + animal.getFoodType())
animal.sleep()
animal.eat()

print("-> Cat")
print("Name\t: " + cat1.getName())
print("Tail\t: " + ("Yes" if cat1.getHasTail() else "No"))
print("Skin\t: " + cat1.getSkinType())
print("Type\t: " + cat1.getFoodType())
print("Breed\t: " + cat1.getBreed())
print("Color\t: " + cat1.getColor())
cat1.sleep()
cat1.eat()

print("-> Snake")
print("Name\t: " + snake1.getName())
print("Tail\t: " + ("Yes" if snake1.getHasTail() else "No"))
print("Skin\t: " + snake1.getSkinType())
print("Type\t: " + snake1.getFoodType())
print("Length\t: " + str(snake1.getLength()))
print("Venom\t: " + ("Yes" if snake1.getIsVenom() else "No"))
snake1.sleep()
snake1.eat()
