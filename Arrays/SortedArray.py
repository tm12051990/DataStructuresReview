from multiprocessing import Value
from array import array
from module1 import DynamicArray

class SortedArray:

    def __init__(self, max_size: int, typecode: str = 'l'):
        self._array = [0] * max_size
        self._max_size = max_size
        self._size = 0

    def __len__(self) -> int:
        """Returns the number of elements in the array."""
        return self._size 

    def __getitem__(self, index):
        """Returns the element at the specified index."""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]
    
    def __repr__(self) -> str:
        """Return the string representation of the sorted array."""
        return str(self._array[:self._size])

    def __iter__(self):
        """Iterate over the elements in the array."""

        for i in range(self._size):
            yield self._array[i]

    def insert(self, value: int | float):
        """Inserts a value into the sorted array"""
        if self._size >= self._max_size:
            raise ValueError("Array is full")

        # Find the correct position to insert the value

        for i in range(self._size, 0, -1):

            if self._array[i - 1] <= value:
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self._array[i-1]

        # If array is empty, insert the value at index 0
        self._array[0] = value
        self._size += 1

    def linear_search(self, target: int | float) -> int | None:
        """Search for the value using linear search algorithm and return its index if found, otherwise return None."""
        for i in range(self._size):
            if self._array[i] == target:
                return i
            elif self._array[i] > target:
                return None
        return None

    def binary_search(self, target: int | float) -> int | None:
        """Search for the value using binary search algorithm and return its index if found, otherwise return None."""
        left = 0
        right = self._size - 1

        while left <= right:
            mid = (left + right) // 2
            if self._array[mid] == target:
                return mid
            elif self._array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def delete(self, target: int | float) -> None:
        """Deletes the first occurrence of the target value from the array."""
        index = self.binary_search(target)

        if index is None:
            raise ValueError("Value not found in the array")

        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1



if __name__ == "__main__":
    arr = DynamicArray(20)

    arr.append(20)
    arr.append(10)
    arr.append(5)
    arr.insert(3, 2)

    print(arr)

    arr.delete(20)

    print(arr)