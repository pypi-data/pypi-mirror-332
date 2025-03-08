def calculate_median(numbers):
    """
    Calculates the median of a list of numbers.

    The median is the value separating the higher half from the lower half
    of a data sample. If the list length is odd, the middle element is returned.
    If the list length is even, the average of the two middle elements is returned.

    Args:
        numbers (list of float): A list of numerical values.

    Returns:
        float: The median value of the list.

    Raises:
        ValueError: If the input list is empty.
    """
    # Check if the input list is empty and raise an error if it is
    if not numbers:
        raise ValueError("The input list cannot be empty.")

    # Sort the list to find the median
    sorted_numbers = sorted(numbers)

    # Calculate the length of the list
    n = len(sorted_numbers)

    # If the length is odd, return the middle element
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        # If the length is even, return the average of the two middle elements
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2

    return median