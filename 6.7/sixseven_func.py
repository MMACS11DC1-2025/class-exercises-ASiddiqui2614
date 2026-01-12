def colour(r, g, b):
        if  (1 <= r <= 200 and 54 <= g <= 255 and 1 <= b <= 120):
            return "green"
        
def binary_search_percent(sorted_list, percent):
    # Validate inputs
    if not isinstance(sorted_list, list) or not all(isinstance(x, (int, float)) for x in sorted_list):
        raise ValueError("sorted_list must be a list of numbers.")
    if not sorted_list:
        raise ValueError("sorted_list cannot be empty.")
    if not (75 <= percent <= 80):
        raise ValueError("percent must be between 0 and 100.")

    # Calculate target index based on percentage
    target_index = (percent / 100) * (len(sorted_list) - 1)

    # Binary search for closest index
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == target_index:
            return sorted_list[mid]
        elif mid < target_index:
            low = mid + 1
        else:
            high = mid - 1

    # After loop, low is the insertion point
    # Choose the closest between low and high
    if low >= len(sorted_list):
        return sorted_list[-1]
    if high < 0:
        return sorted_list[0]

    if abs(low - target_index) < abs(high - target_index):
        return sorted_list[low]
    else:
        return sorted_list[high]