def search_element(data_structure, element):
    if isinstance(data_structure, str):
        if element in data_structure:
            position = data_structure.index(element)
            print(f"Element '{element}' found at position {position} in the string.")
        else:
            print(f"Element '{element}' not found in the string.")
    elif isinstance(data_structure, (list, tuple)):
        if element in data_structure:
            position = data_structure.index(element)
            print(f"Element '{element}' found at position {position} in the data structure.")
        else:
            print(f"Element '{element}' not found in the data structure.")
    elif (data_structure, dict):
        if element in data_structure:
            position = list(data_structure.keys()).index(element)
            print(f"Element '{element}' found at position {position} in the dictionary.")
        else:
            print(f"Element '{element}' not found in the dictionary.")
    else:
        print("Invalid data structure!")

# Example usage
my_string = "Hello, World!"
search_element(my_string, "W")

my_list = [1, 2, 3, 4, 5]
search_element(my_list, 3)

my_tuple = (1, 2, 3, 4, 5)
search_element(my_tuple, 3)

# my_set = {1, 2, 3, 4, 5}
# search_element(my_set, 3)

my_dict = {"a": 1, "b": 2, "c": 3}
search_element(my_dict, "b")
