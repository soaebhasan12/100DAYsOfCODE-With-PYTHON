# List Slicing

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print()
print("List Slicing")
print(piano_keys[:5])        # ['a', 'b', 'c', 'd', 'e']
print(piano_keys[2:5])       # ['c', 'd', 'e']
print(piano_keys[2:])        # ['c', 'd', 'e', 'f', 'g']
print(piano_keys[2:5:2])     # ['c', 'e']
print(piano_keys[::-1])      # ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(piano_keys[1:])        # ['b', 'c', 'd', 'e', 'f', 'g']



# Tuple Slicing

piano_tuple = ["sa", "re", "ga", "ma", "pa", "da", "ni", "sa"]
print()
print("Tuple Slicing")
print(piano_tuple[:5])        # ['a', 'b', 'c', 'd', 'e']
print(piano_tuple[2:5])       # ['c', 'd', 'e']
print(piano_tuple[2:])        # ['c', 'd', 'e', 'f', 'g']
print(piano_tuple[2:5:2])     # ['c', 'e']
print(piano_tuple[::-1])      # ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(piano_tuple[1:])        # ['b', 'c', 'd', 'e', 'f', 'g']