def min_edit_distance_optimized(source, target):
    """
    Calculates the Levenshtein distance between two strings 
    using space-optimized Dynamic Programming.
    """
    if len(source) < len(target):
        source, target = target, source

    rows = len(source)
    cols = len(target)

    prev_row = list(range(cols + 1))
    curr_row = [0] * (cols + 1)

    for i in range(1, rows + 1):
        curr_row[0] = i
        for j in range(1, cols + 1):
            cost = 0 if source[i-1] == target[j-1] else 1
            
            curr_row[j] = min(
                prev_row[j] + 1,      # Deletion
                curr_row[j-1] + 1,    # Insertion
                prev_row[j-1] + cost  # Substitution
            )
        prev_row[:] = curr_row

    return prev_row[cols]

if __name__ == "__main__":
    # Example test cases
    s1, s2 = 'intentional', 'execution'
    result = min_edit_distance_optimized(s1, s2)
    print(f"The Edit Distance between '{s1}' and '{s2}' is: {result}")
