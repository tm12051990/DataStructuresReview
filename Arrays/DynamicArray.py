from array import array

class DynamicArray:

    def __init__ (self, initial_capacity: 'l', typecode: str = 'l'):
        self._array = [0] * initial_capacity
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def __len__ (self) -> int:
        """Returns the number of elements in the array."""

        return self._size

    def __getitem__ (self, index):
        """Returns the element at the specified index."""

        if index < 0 or index >= self._size:
            raise ValueError("Index out of bounds")

        return self._array(index)

    def __repr__ (self) -> str:
        """Return the string representation of the dynamic array."""

        return str(self._array[:self._size])

    def __iter__ (self):

        """Iterate over the elements in the array."""

        for i in range(self._size):
            yield self._array[i]

    def _is_full(self) -> bool:
        """Check if the array is full."""

        return self._size >= self._capacity

    def _double_size(self):
        """Double the size of the array when it is full."""

        assert(self._size == self._capacity)
        old_array = self._array
        self._capacity *= 2
        self._array = [0] * self._capacity
        for i in range(self._size):
            self._array[i] = old_array[i]

    def _halve_size(self):
        """Halve the size of the array when it is less than a quarter full."""

        assert(self._capacity > 1 and self._size < self._capacity // 4)
        old_array = self._array
        self._capacity //= 2
        self._array = [0] * self._capacity
        for i in range(self._size):
            self._array[i] = old_array[i]

    def is_empty(self) -> bool:
        """Checks if the array is empty."""

        return self._size == 0

    def append(self, value: int | float):
        """Appends a value to the end of the dynamic array."""

        if self._is_full():
            self._double_size()
        self._array[self._size] = value
        self._size += 1

    def insert(self, value: int | float, index: int):
        """Inserts a value at the specified index in the dynamic array."""

        if index < 0 or index > self._size:
            raise ValueError("Index out of bounds")

        if self._is_full():
            self._double_size()

        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = value
        self._size += 1


    def find(self, target: int | float) -> int | None:
        """Find the value in the array and return its index if found, otherwise return None."""

        if self.is_empty():
            return None

        for i in range(self._size):
            if self._array[i] == target:
                return i
        return None

    def delete(self, target: int | float) -> None:
        """Deletes target from the array"""

        index = self.find(target)

        if index is None:
            raise ValueError("Target not found in the array")

        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1

        if self._capacity > 1 and self._size <= self._capacity // 4:
            self._halve_size()