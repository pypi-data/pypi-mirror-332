# Example usage:
mapping = {
    (0, 0): "a",
    (0, 1): "b",
    (1, 0): "c",
    (1, 1): "d",
}
shape = (2, 2)
result = nested_list_from_mapping(mapping, shape, default_value="x")
print(result)  # Output: [['a', 'b'], ['c', 'd']]
