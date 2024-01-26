"""
test_merge_sort_linked_list.py

Contains the test cases for the merge sort algorithm for linked lists.

Author: Ray Wang
Created: 1/25/2024
"""

import unittest
from data_structures.common.node import Node
from data_structures.interfaces.linked_list import LinkedList
from data_structures.linked_list.singly_linked_list import SinglyLinkedList
from algorithms.sorting.merge_sort_linked_list import merge_sort_linked_list

class TestMergeSortLinkedList(unittest.TestCase):
    """
    Tests for the merge_sort_linked_list function.
    """
    
    def setUp(self):
        """
        Initializes a new SinglyLinkedList instance for each test.
        """
        self.list: LinkedList = SinglyLinkedList()
    
    def tearDown(self):
        """
        Cleans up after each test.
        """
        del self.list
    
    def test_empty_list(self):
        """
        Tests sorting an empty list.
        """
        sorted_list = merge_sort_linked_list(self.list, lambda x, y: x - y)
        self.assertTrue(sorted_list.is_empty())
    
    def test_single_node(self):
        """
        Tests sorting a list with a single node.
        """
        self.list.append(1)
        result = merge_sort_linked_list(self.list, lambda x, y: x - y)
        self.assertEqual(list(result), [1])

    def test_sorted_list(self):
        """
        Tests sorting a list with multiple nodes.
        """
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        result = merge_sort_linked_list(self.list, lambda x, y: x - y)
        self.assertEqual(list(result), [1, 2, 3])