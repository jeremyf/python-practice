class Dog:
    # This initializer shows three defaults:
    #
    # 1. Calling a static method (e.g. `Dog.default_theme()')
    # 2. Having a default named parameter (e.g. "Border Collie")
    # 3. Or specifying `None' and using an `or' operator.
    def __init__(self, name=Dog.default_name(), breed="Border Collie", color=None):
        """The dogs name and breed"""
        self.name = name
        self.breed = breed
        self.color = color or "color unknown"

    @staticmethod
    def default_name():
        """Return a common dog name."""
        return("Fido")

lacey = Dog(name="Lacey", color="black and white")
print(f'{lacey.name} is a {lacey.color} {lacey.breed}')

default = Dog()
print(f'{default.name} is a {default.color} {default.breed}')
