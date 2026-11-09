class HashTable:
    def __init__(self):
        self._capacity = 16
        self._size = 0
        self._buckets = []

        for i in range(self._capacity):
            self._buckets.append([])

    def _hash(self, key):
        index = 0

        for char in key:
            index = (index * 10 + ord(char)) % self._capacity

        return index

    def set(self, key, value):
        index = self._hash(key)
        bucket = self._buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return bucket[i]
            
        bucket.append((key, value))
        self._size += 1 
        

    def get(self, key, default=None):
        index = self._hash(key)
        bucket = self._buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]

        return default

    def __contains__(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return True
        return False

    def  __len__(self):
        return self._size

    def delete(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                self._size -= 1
                return
        raise KeyError(key)

    def items(self):
        for bucket in self._buckets:
            for tuple in bucket:
                yield tuple

    def values(self):
        for bucket in self._buckets:
            for tuple in bucket:
                yield tuple[1]

    # Resize HashTable 

table = HashTable()

table.set("AAK", 100)
table.set("ABA", 200)
table.set("ABC", 300)



print(list(table.items()))
print(list(table.values()))