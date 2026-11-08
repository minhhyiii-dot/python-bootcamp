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

    def set(key, value):
        HashTable._hash(key) = 

table = HashTable()

print(table._capacity)
print(table._hash("FPT"))