from typing import List, Any, Dict, Set, Generator

class StaticArray:
    def __init__(self, capacity: int):
        """
        Initialize a static array of a given capacity.
        """

    def set(self, index: int, value: int) -> None:
        """
        Set the value at a particular index.
        """

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """

class DynamicArray:
    def __init__(self):
        """
        Initialize an empty dynamic array.
        """

    def append(self, value: int) -> None:
        """
        Add a value to the end of the dynamic array.
        """

    def insert(self, index: int, value: int) -> None:
        """
        Insert a value at a particular index.
        """

    def delete(self, index: int) -> None:
        """
        Delete the value at a particular index.
        """

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """

class Node:
    def __init__(self, value: int):
        """
        Initialize a node.
        """

class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """

    def find(self, value: int) -> Node:
        """
        Find a node with a specific value.
        """

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
    
    def get_head(self) -> Node:
        """
        Returns the head node of the linked list.
        """
    
    def get_tail(self) -> Node:
        """
        Returns the tail node of the linked list.
        """

class DoubleNode:
    def __init__(self, value: int, next_node = None, prev_node = None):
        """
        Initialize a double node with value, next, and previous.
        """

class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """

    def find(self, value: int) -> DoubleNode:
        """
        Find a node with a specific value.
        """

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
    
    def get_head(self) -> DoubleNode:
        """
        Returns the head node of the linked list.
        """
    
    def get_tail(self) -> DoubleNode:
        """
        Returns the tail node of the linked list.
        """

class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """

    def enqueue(self, value: int) -> None:
        """
        Add a value to the end of the queue.
        """

    def dequeue(self) -> int:
        """
        Remove a value from the front of the queue and return it.
        """

    def peek(self) -> int:
        """
        Peek at the value at the front of the queue without removing it.
        """

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """

class TreeNode:
    def __init__(self, value: int):
        """
        Initialize a tree node with value.
        """

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """

    def insert(self, value: int) -> None:
        """
        Insert a node with a specific value into the binary search tree.
        """

    def delete(self, value: int) -> None:
        """
        Remove a node with a specific value from the binary search tree.
        """

    def search(self, value: int) -> TreeNode:
        """
        Search for a node with a specific value in the binary search tree.
        """

    def inorder_traversal(self) -> List[int]:
        """
        Perform an in-order traversal of the binary search tree.
        """
    
    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty.
        """

    def height(self) -> int:
        """
        Returns the height of the tree.
        """

    def preorder_traversal(self) -> List[int]:
        """
        Perform a pre-order traversal of the tree.
        """

    def postorder_traversal(self) -> List[int]:
        """
        Perform a post-order traversal of the tree.
        """

    def level_order_traversal(self) -> List[int]:
        """
        Perform a level order (breadth-first) traversal of the tree.
        """

    def minimum(self) -> TreeNode:
        """
        Returns the node with the minimum value in the tree.
        """

    def maximum(self) -> TreeNode:
        """
        Returns the node with the maximum value in the tree.
        """
    
    def is_valid_bst(self) -> bool:
        """
        Check if the tree is a valid binary search tree.
        """

def insertion_sort(lst: List[int]) -> List[int]:
    pass

def selection_sort(lst: List[int]) -> List[int]:
    pass

def bubble_sort(lst: List[int]) -> List[int]:
    pass

def shell_sort(lst: List[int]) -> List[int]:
    pass

def merge_sort(lst: List[int]) -> List[int]:
    pass

def quick_sort(lst: List[int]) -> List[int]:
    pass
