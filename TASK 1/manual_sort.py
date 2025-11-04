
# 1.  Write a Python function to sort a list of dictionaries by a specific key.

# manual_sort.py

def sort_dict_list(data, key):
    """
    Sorts a list of dictionaries by a specified key in ascending order.
    :param data: list of dictionaries
    :param key: key to sort by
    :return: sorted list
    """
    # Simple manual sort using sorted() and lambda
    sorted_list = sorted(data, key=lambda x: x[key])
    return sorted_list


# Example data
students = [
    {"name": "Alice", "score": 85},
    {"name": "Brian", "score": 90},
    {"name": "Carol", "score": 78}
]

# Run the function
result = sort_dict_list(students, "score")
print(result)

