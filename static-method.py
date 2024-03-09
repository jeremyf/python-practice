# This is my notes for https://python-patterns.guide/gang-of-four/abstract-factory/
#
# NOTE: We specifically name what we're importing
from decimal import Decimal

class DecimalFactory(object):
    ##
    # NOTE: The static method is analogous to a class/module method in Ruby.
    #
    # However, unlike Ruby the static method is available to both the instance
    # and the class.  That's super convenient.
    #
    # I cannot declare an instance method that is already declared as a
    # staticmethod; and vice versa I assume.
    #
    # This does make an object easier to understand and steers the developer
    # towards a "concept" having one implementation of a method.
    @staticmethod
    def build(string):
        return Decimal(string.lstrip('$'))

class Loader(object):
    @staticmethod
    def load(string, factory):
        string = string.rstrip(',')  # allow trailing comma
        return [factory.build(item) for item in string.split(',')]

# Create an instance.
f = DecimalFactory()

# Because of the `@staticmethod' I could either pass `f' or `DecimalFactory'.
result = Loader.load('464.80, 993.68', f)
print(result)
