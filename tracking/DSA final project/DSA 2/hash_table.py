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
        

table = HashTable()

print(table._capacity)
print(table._hash("FPT"))


table.set("AAK", 100)
table.set("ABA", 200)
table.set("AAK", 300)

print(table._buckets[9])
print(table._size)