try:
    # The code we want to execute.  Analogous to a `begin' in Ruby.
    a = int(input("Enter an integer: "))
except (ValueError):
    # Analogous to the `rescue' of a Ruby block
    print("Enter a valid integer")
else:
    print(a)
    # The "happy path"; simply assumed to be part of the `begin' block.
finally:
    # Analogous to the `ensure' in Ruby.
    print("Thank you and good-bye.")
