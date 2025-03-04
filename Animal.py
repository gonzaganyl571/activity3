class Animal:
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    def _make_sound(self):
        return f"{self._name} says {self._sound}"

class Cat(Animal):
    def bark(self):
        return self._make_sound()

Cat = Cat("Jessica", "meow")
print(Cat.bark())
