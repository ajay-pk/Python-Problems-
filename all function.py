# all(iterable)

    # Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True

Examples:

# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))

output -

True
False
False
False
True
