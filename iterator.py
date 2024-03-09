# some_primes = [2, 3, 5]
# for prime in some_primes:
#     print(prime)

# Dictionary in Python
d = {'H': 1.008, 'He': 4.003, 'Li': 6.94}
print(d)
for symbol, weight in d.items():
    print(symbol, weight)

# This is analogous to Ruby's #each_with_object({})
print({symbol: weight for symbol, weight in d.items() if weight > 5})

# Analogous to #each_with_object([])
print(list(symbol for symbol, weight in d.items() if weight > 5))
