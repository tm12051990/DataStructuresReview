from typing import Any, Callable, List, Optional

class SinglyLinkedList:
   """Models an unsorted singly linked list"""

   class Node:
       """Each node contains data and a reference to the next node"""

       def __init__(self, data, next_node = None) -> None:
           self._data = data
           self._next = next_node

       def data(self) -> Any:
           return self._data

       def __str__(self) -> str:
           """Return a string representation of the node's data"""
           return str(self._data())

       def __repr__(self) -> str:
           """Return a string representation(internal) of the node's data"""
           return repr(self._data())

       def next(self) -> "SinglyLinkedList.Node":
           """Return the successor of the current node"""
           return self._next

       def has_next(self) -> bool:
           """Check if the node has a successor"""
           return self._next is not None

       def append(self, next_node):
           """Append a node to the current one"""
           self._next = next_node

    # --- SinglyLinkedList Methods ---

   def __init__(self):
       """Initializes a new empty Singly Linked List"""
       self._head = None
       self._size = 0

   def __len__(self):
       """Return the length of the linked list"""
       self._head = None
       self._size = 0

   def __str__(self) -> str:
       values = []
       current = self._head

       while current:
           values.append(str(current.data()))
           current = current.next()
       return " -> ".join(values)

   def __repr__(self) -> str:
       values = []
       current = self._head

       while current:
           values.append(repr(current.value))
           current = current.next()

       return f"SinglyLinkedList({', '.join(values)})"

   def __iter__(self):
       """Iterate over the values in the linked list"""

       current = self._head

       while current:
           data = current.data()
           current = current.next()
           yield data

   def is_empty(self) -> bool:
       """Checks whether the linked list is empty"""
       return self._head is None

   def insert_at_front(self, data: Any) -> None:
       """Insert a new node at the front of the linked list"""

       old_head = self._head
       self._head = SinglyLinkedList.Node(data, old_head)

   def insert_at_back(self, data: Any) -> None:
       """Insert a new node at the back of the linked list"""

       new_node = SinglyLinkedList.Node(data)
       current = self._head

       if current is None:
           self._head = new_node

       else:
           while current.next() is not None:
               current = current.next()
           current.append(new_node)
       
       self._size += 1

   def get(self, index) -> int:
       """Return the value at the given index"""


       if index < 0:
           raise IndexError("Index must be non negative")

       current = self._head
       current_index = 0

       while current_index < index and current is not None:
           current = current.next()
           current_index += 1

           if current is None:
               raise IndexError("Index not found")

       return current.data()

   def _search(self, target: Any) -> Optional["SinglyLinkedList.Node"]:
       """Search for the target within the linked list"""

       current = self._head

       while current is not None:
           if current.data() == target:
               return current
           current = current.next()

       return None

   def search(self, predicate: Callable[..., Any]) -> Optional[Any]:
        """Functional search using a predicate, input parameters for search and return if found"""

        current = self._head

        while current is not None:
            if predicate(current.data()):
                return current.data()
            current = current.next()
        return None
   
   def delete(self, target: Any) -> None:
       """Delete the node from the linked list"""

       current = self._head
       previous = None

       while current is not None:
           if current.data() == target:
               if previous is None:
                   self._head = current.next()
               else:
                   previous.append(current.next())
               return
           previous = current
           current = current.next()
       #If we get here, we haven't found the target
       raise ValueError("No element found with value {target} in the linked list")

   def delete_from_front(self) -> Any:
       """Delete the node at the front of the list and return the data it held"""

       if self.is_empty():
           raise ValueError("Linked List is empty")

       data = self._head.data()
       self._head = self._head.next()

       return data