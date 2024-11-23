# Define Hash Map class
class CreateHashMap:
    # Create hash table
    def __init__(self, starting_size=20):
        self.list = []
        for i in range(starting_size):
            self.list.append([])

    # Method to insert package to hash table
    def ht_insert(self, key, package):
        bucket = hash(key) % len(self.list)
        bucket_items = self.list[bucket]

        # Check if key exists and update if it does
        # O(N) runtime
        for val in bucket_items:
            if val[0] == key:
                val[1] = package
                return True

        # If key does not exist, append package to end of buckets
        key_val = [key, package]
        bucket_items.append(key_val)
        return True

    # Search for package in hash table
    def ht_search(self, key):
        bucket = hash(key) % len(self.list)
        bucket_items = self.list[bucket]
        for vals in bucket_items:
            if key == vals[0]:
                return vals[1]

        return None  # Result if search finds no match

    # Remove package from hash table
    def ht_remove(self, key):
        bucket = hash(key) % len(self.list)
        target = self.list[bucket]

        if key in target:
            target.remove(key)
