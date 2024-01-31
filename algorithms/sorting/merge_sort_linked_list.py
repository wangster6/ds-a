"""
merge_sort_linked_list.py

Contains the implementation of a merge sort algorithm for linked lists.

Author: Ray Wang
Created: 1/25/2024
"""

from data_structures.common.node import Node
from data_structures.interfaces.linked_list import LinkedList
from data_structures.linked_list.singly_linked_list import SinglyLinkedList
from functools import cmp_to_key

def merge_sort_linked_list(list: LinkedList, compare_func):
    """
    Sorts the provided linked list using the merge sort algorithm.
    
    Parameters:
        list: The linked list to be sorted.
        compare_func: The function used to compare two elements in the list.
    
    Returns:
        LinkedList: The sorted linked list.
    """
    if list.is_empty():
        list.display() 
        print("List: ", list)
        return list

    if list.len() == 1:
        print("List: ", list)
        print("List length: ", list.len())
        print("List has one element.")
        return list

    # Split the list into two halves
    mid = find_middle(list)
    mid_idx = find_middle_index(list)
    left_list = list.subset(0, mid_idx)
    right_list = list.subset(mid_idx + 1, list.len())
    mid.next = None

    # Recursively sort the two halves
    left_sorted = merge_sort_linked_list(left_list, compare_func)
    right_sorted = merge_sort_linked_list(right_list, compare_func)

    # Merge the two sorted halves
    merged_list = merge(left_sorted, right_sorted, compare_func)

    return merged_list

def find_middle(list: LinkedList):
    """
    Finds the middle node of the linked list.
    
    Parameters:
        list: The linked list to find the middle node of.
    
    Returns:
        Node: The middle node of the linked list.
    """
    slow_ptr = list.head
    fast_ptr = list.head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr

def find_middle_index(list: LinkedList):
    """
    Finds the middle node of the linked list.
    
    Parameters:
        list: The linked list to find the middle node of.
    
    Returns:
        Node: The middle node of the linked list.
    """
    slow_ptr = list.head
    fast_ptr = list.head
    index = 0

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        index += 1

    return index
    # middle = list.len() // 2
    # current = list.head
    
    # while middle > 0:
    #     current = current.next
    #     middle -= 1
    
    # return current

def merge(left: LinkedList, right: LinkedList, compare_func):
    result = LinkedList()
    dummy = Node(None)
    result.prepend(dummy)
    current = dummy
    
    left_current = left.iter()
    right_current = right.iter()

    while left_current is not None and right_current is not None:
        if compare_func(left_current.data, right_current.data) <= 0:
            current.next = left_current
            left_current = left_current.next
        else:
            current.next = right_current
            right_current = right_current.next
        current = current.next

    # Append the rest of the remaining elements from left and right
    current.next = left_current or right_current

    return result