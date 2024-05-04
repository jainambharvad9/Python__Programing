def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
my_list = [1, 3, 5, 7, 9]
target_element = int(input("Enter NUmber"))
result_index = linear_search(my_list, target_element)
if result_index != -1:
    print(f"Element {target_element} found at index {result_index}.")
else:
    print(f"Element {target_element} not found in the list.")
