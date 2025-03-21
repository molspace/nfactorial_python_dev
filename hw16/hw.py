from typing import List, Any, Dict, Set, Generator

class StaticArray:
    def __init__(self, capacity: int):
        """
        Initialize a static array of a given capacity.
        """
        self.capacity = capacity
        self.array = [None] * capacity

    def set(self, index: int, value: int) -> None:
        """
        Set the value at a particular index.
        """
        self.array[index] = value

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        return self.array[index]

class DynamicArray:
    def __init__(self):
        """
        Initialize an empty dynamic array.
        """
        self.array = []

    def append(self, value: int) -> None:
        """
        Add a value to the end of the dynamic array.
        """
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        """
        Insert a value at a particular index.
        """
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        """
        Delete the value at a particular index.
        """
        self.array.pop(index)

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        return self.array[index]

class Node:
    def __init__(self, value: int):
        """
        Initialize a node.
        """
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None
        self.tail = None
        self.node_count = 0

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = Node(value)
        if self.node_count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.node_count += 1

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.node_count == 0:
                self.tail = new_node
        else:
            cur_node = self.head
            for _ in range(position - 1):
                cur_node = cur_node.next
            new_node.next = cur_node.next
            cur_node.next = new_node
            if new_node.next is None:
                self.tail = new_node
        self.node_count += 1
                
    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        if self.head is None:
            return None
        if self.head.value == value:
            self.head = self.head.next
            self.node_count -= 1
            if self.head is None:
                self.tail = None
            return None

        cur_node = self.head
        while cur_node.next:
            if cur_node.next.value == value:
                cur_node.next = cur_node.next.next
                self.node_count -= 1
                if cur_node.next is None:
                    self.tail = cur_node
                return None                
            cur_node = cur_node.next

    def find(self, value: int) -> Node:
        """
        Find a node with a specific value.
        """
        cur_node = self.head
        while cur_node:
            if cur_node.value == value:
                return cur_node
            cur_node = cur_node.next
        return None

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        return self.node_count

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.size() == 0

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        all_elements = []
        cur_node = self.head
        while cur_node:
            all_elements.append(cur_node.value)
            cur_node = cur_node.next
        print(all_elements)
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        if self.is_empty() or self.size() == 1:
            return None

        prev_node = None
        cur_node = self.head
        self.tail = self.head

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def get_head(self) -> Node:
        """
        Returns the head node of the linked list.
        """
        return self.head
    
    def get_tail(self) -> Node:
        """
        Returns the tail node of the linked list.
        """
        return self.tail

class DoubleNode:
    def __init__(self, value: int, next_node = None, prev_node = None):
        """
        Initialize a double node with value, next, and previous.
        """
        self.value = value
        self.next = next_node
        self.prev = prev_node
    
class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None
        self.node_count = 0

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = DoubleNode(value)
        if self.node_count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.node_count += 1

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        new_node = DoubleNode(value)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.node_count == 0:
                self.tail = new_node
        elif position == self.node_count:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            cur_node = self.head
            for _ in range(position - 1):
                cur_node = cur_node.next
            new_node.next = cur_node.next
            new_node.prev = cur_node
            cur_node.next.prev = new_node
            cur_node.next = new_node
        self.node_count += 1

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        cur_node = self.head
        while cur_node:
            if cur_node.value == value:
                prev_node = cur_node.prev
                next_node = cur_node.next

                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node

                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node

                self.node_count -= 1
                return None
            cur_node = cur_node.next

    def find(self, value: int) -> DoubleNode:
        """
        Find a node with a specific value.
        """
        cur_node = self.head
        while cur_node:
            if cur_node.value == value:
                return cur_node
            cur_node = cur_node.next
        return None

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        return self.node_count

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.size() == 0

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        all_elements = []
        cur_node = self.head
        while cur_node:
            all_elements.append(cur_node.value)
            cur_node = cur_node.next
        print(all_elements)
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        if self.is_empty() or self.size() == 1:
            return None

        cur_node = self.head
        self.tail = self.head

        while cur_node:
            cur_node.prev, cur_node.next = cur_node.next, cur_node.prev
            if cur_node.prev is None:
                self.head = cur_node
            cur_node = cur_node.prev
    
    def get_head(self) -> DoubleNode:
        """
        Returns the head node of the linked list.
        """
        return self.head
    
    def get_tail(self) -> DoubleNode:
        """
        Returns the tail node of the linked list.
        """
        return self.tail

class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.queue = []
        self.size = 0

    def enqueue(self, value: int) -> None:
        """
        Add a value to the end of the queue.
        """
        self.queue.append(value)
        self.size += 1

    def dequeue(self) -> int:
        """
        Remove a value from the front of the queue and return it.
        """
        if self.is_empty():
            return None
        self.size -= 1
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Peek at the value at the front of the queue without removing it.
        """
        return self.queue[0]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        return self.size == 0

class TreeNode:
    def __init__(self, value: int):
        """
        Initialize a tree node with value.
        """
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        # pretty print the node
        return f"TreeNode(value={self.value}, left={self.left}, right={self.right})"

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None
        self.node_count = 0

    def insert(self, value: int) -> None:
        """
        Insert a node with a specific value into the binary search tree.
        """
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
        else:
            cur_node = self.root
            while cur_node:
                if value < cur_node.value:
                    if not cur_node.left:
                        cur_node.left = new_node
                        break
                    cur_node = cur_node.left
                else:
                    if not cur_node.right:
                        cur_node.right = new_node
                        break
                    cur_node = cur_node.right
        self.node_count += 1

    def delete(self, value: int) -> None:
        """
        Remove a node with a specific value from the binary search tree.
        """
        self.root = self._delete_helper(self.root, value)

    def _delete_helper(self, node: TreeNode, value: int) -> TreeNode:
        if not node:
            return None
        if value < node.value:
            node.left = self._delete_helper(node.left, value)
        elif value > node.value:
            node.right = self._delete_helper(node.right, value)
        # if node found
        else:
            # if no children
            if not node.left and not node.right:
                return None
            # if one child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # if two children (find successor)
            successor = self._minimum_helper(node.right)
            node.value = successor.value
            node.right = self._delete_helper(node.right, successor.value)
        return node
            
    def search(self, value: int) -> TreeNode:
        """
        Search for a node with a specific value in the binary search tree.
        """
        cur_node = self.root
        while cur_node:
            if value == cur_node.value:
                return cur_node
            elif value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return None

    def inorder_traversal(self) -> List[int]:
        """
        Perform an in-order traversal of the binary search tree.
        """
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node: TreeNode, result: List[int]) -> None:
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
    
    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """
        return self.node_count

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty.
        """
        return self.size() == 0
    
    def height(self) -> int:
        """
        Returns the height of the tree.
        """
        return self._height_helper(self.root)

    def _height_helper(self, node: TreeNode) -> int:
        if not node:
            return 0
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        return max(left_height, right_height) + 1

    def preorder_traversal(self) -> List[int]:
        """
        Perform a pre-order traversal of the tree.
        """
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node: TreeNode, result: List[int]) -> None:
        if node:
            result.append(node.value)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def postorder_traversal(self) -> List[int]:
        """
        Perform a post-order traversal of the tree.
        """
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node: TreeNode, result: List[int]) -> None:
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.value)

    def level_order_traversal(self) -> List[int]:
        """
        Perform a level order (breadth-first) traversal of the tree.
        """
        if not self.root:
            return []
        queue = Queue()
        queue.enqueue(self.root)
        result = []
        while not queue.is_empty():
            node = queue.dequeue()
            result.append(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return result

    def minimum(self) -> TreeNode:
        """
        Returns the node with the minimum value in the tree.
        """
        return self._minimum_helper(self.root)

    def _minimum_helper(self, node: TreeNode) -> TreeNode:
        if not node:
            return None
        while node.left:
            node = node.left
        return node

    def maximum(self) -> TreeNode:
        """
        Returns the node with the maximum value in the tree.
        """
        return self._maximum_helper(self.root)

    def _maximum_helper(self, node: TreeNode) -> TreeNode:
        if not node:
            return None
        while node.right:
            node = node.right
        return node
    
    def is_valid_bst(self) -> bool:
        """
        Check if the tree is a valid binary search tree.
        """
        return self._is_valid_bst_helper(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_helper(self, node: TreeNode, min_val: float, max_val: float) -> bool:
        if not node:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self._is_valid_bst_helper(node.left, min_val, node.value) and
                self._is_valid_bst_helper(node.right, node.value, max_val))

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def selection_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def bubble_sort(lst: List[int]) -> List[int]:
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted = False
    return lst

def shell_sort(lst: List[int]) -> List[int]:
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    pivot = lst.pop()
    left = []
    right = []
    for x in lst:
        if x > pivot:
            right.append(x)
        else:
            left.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)
