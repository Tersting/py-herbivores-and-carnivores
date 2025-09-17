from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, Hidden: "
                f"{self.hidden}}}")

    @staticmethod
    def check_alive(herbivore: Herbivore) -> None:
        if herbivore.health <= 0:
            for element in Animal.alive:
                if element.name == herbivore.name:
                    Animal.alive.remove(element)


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
                Animal.check_alive(herbivore)
