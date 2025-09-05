# Insertion Sort in Descending Order
# Author: [Your Name]
# Course: MSCS532 - Assignment 1
# Description: This program implements the Insertion Sort algorithm
#              that sorts a list in monotonically decreasing order.

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
    # Sample input list
    numbers = [12, 11, 13, 5, 6]

    # Print the original list
    print("Original:", numbers)

    # Sort the list in descending order
    sorted_numbers = insertion_sort_desc(numbers)

    # Print the sorted result
    print("Sorted (Descending):", sorted_numbers)