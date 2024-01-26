"""
merge_sort_linked_list.py

Contains the implementation of a merge sort algorithm for linked lists.

Author: Ray Wang
Created: 1/25/2024
"""

from data_structures.common.node import Node
from data_structures.interfaces.linked_list import LinkedList
from data_structures.linked_list.singly_linked_list import SinglyLinkedList

def merge_sort_linked_list(list: LinkedList, compare_func):
    """
    Sorts the provided linked list using the merge sort algorithm.
    
    Parameters:
        list: The linked list to be sorted.
        compare_func: The function used to compare two elements in the list.
    
    Returns:
        LinkedList: The sorted linked list.
    """
    if list.is_empty:
        return list

    # Split the list into two halves
    mid = find_middle(list)
    left_list = list.copy()
    right_list = mid.next.copy()
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
    middle = list.len() // 2
    current = list.head
    
    while middle > 0:
        current = current.next
        middle -= 1
    
    return current

def merge(left: LinkedList, right: LinkedList, compare_func):
    """
    Merges the two provided linked lists into a single linked list.
    
    Parameters:
        left: The left linked list.
        right: The right linked list.
        compare_func: The function used to compare two elements in the list.
    
    Returns:
        LinkedList: The merged linked list.
    """
    result = LinkedList()
    current = result.head

    while left.head is not None and right.head is not None:
        if compare_func(left.head.data, right.head.data) <= 0:
            current.next = left.head
            left.head = left.head.next
        else:
            current.next = right.head
            right.head = right.head.next
        current = current.next

    # One of the lists has ended, just append the rest of the other list
    current.next = left.head if left.head is not None else right.head

    return result