# Bilal Sayed C950 HashTable.py


# class to make hash table data structure
class HashTable:
    index = 0

    def __init__(self, length):
        self.array = [None] * length

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.array):
            raise StopIteration
        index = self.index
        self.index += 1
        return int(self.array[index][0][0])

    def __str__(self):
        return str(self.array) + '\n'

    # method to hash key
    def __hash(self, key):
        length = len(self.array)
        index = int(key) % length
        return index

    # add key value pair to hash table
    def set(self, key, value):
        index = self.__hash(key)
        self.array[index] = []
        self.array[index].append(key)
        self.array[index].append(value)

    # get value using key
    def get(self, key):
        index = self.__hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            return self.array[index][1]
