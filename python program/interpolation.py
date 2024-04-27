def interpolation_search(arr, target):
    """
    Perform interpolation search to find the index of the target element in the array.

    Args:
    arr (list): The list to search through (must be sorted in ascending order).
    target: The element to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Estimate the position of the target element
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 13
result_index = interpolation_search(my_list, target_element)
if result_index != -1:
    print(f"Element {target_element} found at index {result_index}.")
else:
    print(f"Element {target_element} not found in the list.")
 
