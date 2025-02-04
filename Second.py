def find_second_highest(nums):
    # Remove duplicates and sort the list in descending order
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)

    # Check if there are at least two elements
    if len(unique_nums) < 2:
        return "No second highest element exists."
    else:
        return unique_nums[1]  # Return the second highest element