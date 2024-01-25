"""
merge_sort_linked_list.py

Contains the implementation of a merge sort algorithm for linked lists.

Author: Ray Wang
Created: 1/25/2024
"""

from data_structures.common.node import Node

def merge_sort_linked_list(head, compare_func):
    if head is None or head.next is None:
        return head
    
    # To be implemented