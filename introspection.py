class Human:
    """Someone we've named via their given_name and family_name."""

    def __init__(self, given_name, family_name):
        """
        :param given_name:
        :param family_name:
        """
        self.given_name = given_name
        self.family_name = family_name

    def __str__(self):
        """Return the Person's formatted name"""
        # Using the f-string syntax (https://peps.python.org/pep-0498/)
        return f"{self.given_name} {self.family_name}"


# Parameters are positional and named.  In the below, I could remove the
# `given_name=' and it would behave the same.  I could not, however, remove the
# `family_name=' while leaving `given_name='.
person = Human(given_name="Jeremy", family_name="Friesen")

# Leverage the __str__ method of Person.
print(person)

# Print a list of the methods and fields.
print(dir(person))
