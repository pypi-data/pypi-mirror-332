def unique_elements(lst):
    """Returns a list of unique elements while preserving the order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def flatten_list(nested_list):
    """Flattens a nested list."""
    return [item for sublist in nested_list for item in sublist]


def reverse_string(s):
    """Returns the reversed version of a string."""
    return s[::-1]
