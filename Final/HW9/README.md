# Minimum Edit Distance (Levenshtein Distance)

This repository contains an optimized Python implementation of the Minimum Edit Distance algorithm. 

### Features
* **Space Optimized:** Uses only $O(min(n, m))$ space by maintaining only two rows of the dynamic programming table.
* **Time Complexity:** $O(n \times m)$ where $n$ and $m$ are the lengths of the strings.

### Usage
```python
distance = min_edit_distance_optimized('intentional', 'execution')
print(f"Distance: {distance}")
