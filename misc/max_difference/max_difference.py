def max_difference(numbers):
    """
    The idea is to shift the index and precalculate the right max
    so as we shift we calculate the left max and used the pre
    calculated right one.

    >>> max_difference([1, 3, -3])
    6
    >>> max_difference([1 ,-5 ,6,  8, 1])
    7
    """
    # Calculate right maxes O(n)
    right_maxes = [] # Reversed list of maxes
    current_right_max = numbers[-1]
    for element in reversed(numbers):
        if element > current_right_max:
            current_right_max = element
        right_maxes.append(element)
    
    # Calculate left_max while finding the max difference O(n)
    left_max = numbers[0]
    max_difference = 0
    for index in range(len(numbers) - 1):
        if numbers[index] > left_max:
            left_max = numbers[index]
        difference =  abs(left_max - right_maxes[len(numbers) - 2 - index])
        if difference > max_difference:
            max_difference = difference

    return max_difference
