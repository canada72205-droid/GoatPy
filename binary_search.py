def binary_search(sequence, item):
    low = 0
    high = len(sequence) - 1
    
    
    target = item.strip().lower()

    while low <= high:
        mid = (low + high) // 2
        
        
        midpoint_value = sequence[mid].name.lower()

        if midpoint_value == target:
            return sequence[mid] 
            
       
        if midpoint_value > target:
            high = mid - 1
        else:
            low = mid + 1

    return None
