from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # Dictionary to store key -> list of (value, timestamp) pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))  # Append the value and timestamp to the list for the given key

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""  # If the key is not in the store, return an empty string
        
        values = self.store[key]
        # Use binary search to find the rightmost timestamp <= the given timestamp
        l, r = 0, len(values) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        if r == -1:
            return ""  # If no valid timestamp is found, return an empty string
        
        return values[r][0]  # Return the value at the found position

a = TimeMap()

# Given test case
operations = ["TimeMap", "set", "get", "get", "set", "get", "get"]
inputs = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

# To store the results of operations
results = []

for i, operation in enumerate(operations):
    if operation == "TimeMap":
        # Initialize the TimeMap
        a = TimeMap()
        results.append(None)
    elif operation == "set":
        # Set the key-value pair
        a.set(*inputs[i])
        results.append(None)
    elif operation == "get":
        # Get the value at the given timestamp
        result = a.get(*inputs[i])
        results.append(result)

print(results)
