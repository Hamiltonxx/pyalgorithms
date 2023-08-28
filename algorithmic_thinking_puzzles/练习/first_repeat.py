def find_first_repeated_element(arr):
    seen = set()

    for element in arr:
        if element in seen:
            return element
        seen.add(element)

    return None  # No repeated element found

# Example usage
arr = [3, 2, 1, 2, 2, 3]
first_repeated = find_first_repeated_element(arr)
if first_repeated is not None:
    print("First repeated element:", first_repeated)
else:
    print("No repeated element found")