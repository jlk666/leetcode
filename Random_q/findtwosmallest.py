def find_two_smallest(lst):
    def recurse(sublist):
        n = len(sublist)
        if n == 1:
            return (sublist[0], float('inf'))  # Only one element, second smallest is infinity
        elif n == 2:
            return (min(sublist), max(sublist))  # Two elements, directly return min and max

        # Split the list into two halves
        mid = n // 2
        left = recurse(sublist[:mid])
        right = recurse(sublist[mid:])

        # Combine the results
        # Determine the two smallest elements from left and right
        smallest = min(left[0], right[0])
        if smallest == left[0]:
            second_smallest = min(left[1], right[0])
        else:
            second_smallest = min(left[0], right[1])

        return (smallest, second_smallest)

    # Start the recursion from the entire list
    return recurse(lst)

# Example usage:
lst = [4, 66, 7, 1, 3434, 5]
smallest, second_smallest = find_two_smallest(lst)
print("The two smallest numbers are:", smallest, "and", second_smallest)
