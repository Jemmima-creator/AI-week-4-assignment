# copilot_sort.py
# Write a Python function that sorts a list of dictionaries by a key

def sort_dict_list_by_key(data, key, reverse=False):
    """
    Sort a list of dictionaries by a given key.
    """
    try:
        return sorted(data, key=lambda item: item.get(key, 0), reverse=reverse)
    except Exception as e:
        print(f"Error: {e}")
        return data


students = [
    {"name": "Alice", "score": 85},
    {"name": "Brian", "score": 90},
    {"name": "Carol", "score": 78},
]

print(sort_dict_list_by_key(students, "score"))

