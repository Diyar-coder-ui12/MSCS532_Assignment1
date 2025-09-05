

def insertion_sort_desc(arr):
    """
    Function to perform Insertion Sort in descending order.

    Parameters:
        arr (list): List of numbers to be sorted.

    Returns:
        list: Sorted list in descending order.
    """
    # Loop through elements starting from index 1 (second element)
    for i in range(1, len(arr)):
        key = arr[i]   # Current element to insert
        j = i - 1      # Index of the previous element

        # Move elements greater than key one position ahead
        # (Descending order means we shift smaller elements to the right)
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at the correct position
        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    # Test Case 1
    numbers1 = [12, 11, 13, 5, 6]
    print("Original:", numbers1)
    print("Sorted (Descending):", insertion_sort_desc(numbers1))

    # Test Case 2: Already sorted in descending order
    numbers2 = [50, 40, 30, 20, 10]
    print("\nOriginal:", numbers2)
    print("Sorted (Descending):", insertion_sort_desc(numbers2))

    # Test Case 3: Sorted in ascending order
    numbers3 = [1, 2, 3, 4, 5]
    print("\nOriginal:", numbers3)
    print("Sorted (Descending):", insertion_sort_desc(numbers3))

    # Test Case 4: Contains duplicate values
    numbers4 = [10, 20, 20, 5, 30, 10]
    print("\nOriginal:", numbers4)
    print("Sorted (Descending):", insertion_sort_desc(numbers4))

    # Test Case 5: Single element
    numbers5 = [99]
    print("\nOriginal:", numbers5)
    print("Sorted (Descending):", insertion_sort_desc(numbers5))

    # Test Case 6: Empty list
    numbers6 = []
    print("\nOriginal:", numbers6)
    print("Sorted (Descending):", insertion_sort_desc(numbers6))
