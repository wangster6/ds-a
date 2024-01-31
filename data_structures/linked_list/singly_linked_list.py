"""
singly_linked_list.py

Contains the implementation of a singly linked list data structure.

Author: Ray Wang
Created: 12/19/2023
"""

from data_structures.common.node import Node
from data_structures.interfaces.linked_list import LinkedList
        
class SinglyLinkedList:
    """
    Class: SinglyLinkedList

    A singly linked list data structure.
    """
    
    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance.
        
        Parameters:
            No parameters.
            
        Returns:
            Nothing returned.
        """
        self.head = None

    def is_empty(self):
        """
        Checks if the list is empty.
        
        Parameters:
            No parameters.
            
        Returns:
            bool: True if the list is empty, False if not empty.
        """
        return self.head is None
    
    def append(self, data):
        """
        Appends a new node with the provided data at the end of the list.
        
        Parameters:
            data: The data to be stored in the node.
            
        Returns:
            Nothing returned.
        """
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next: # traverse through the linked list until we reach the last node
                current = current.next
            current.next = new # append the new node to the end of the linked list

    def prepend(self, data):
        """
        Prepends a new node with the provided data at the front of the list.
        
        Parameters:
            data: The data to be stored in the node.
            
        Returns:
            Nothing returned.
        """
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def delete(self, data):
        """
        Removes the first occurrence of a node with the specified data in the list.
        
        Parameters:
            data: The data to be deleted from the list.
        
        Returns:
            None: None is returned if the list is empty or if no node is found with the specified data.
            deleted: Returns the deleted node if it is found in the list.
        """
        # time complexity: O(1)
        if self.head is None:
            return None # returns None if the list is empty
        
        # time complexity: O(1)
        if self.head.data == data: # checks if the head node of the linked list contains the specified data and should be removed
            deleted = self.head
            self.head = self.head.next
            return deleted
        
        current = self.head
        
        # time complexity: O(n)
        while current.next: # traverse through the linked list until we reach the last node
            if current.next.data == data: # check if the node after the current one contains the specified data and should be removed
                deleted = current.next
                current.next = current.next.next # set the current node's next pointer to point towards the node two places after the current node
                return deleted
            current = current.next
        
        return None # returns None if no node with the specified data is found
    
    def len(self):
        """
        Returns the length of the linked list
        
        Parameters:
            No parameters.
            
        Returns:
            count: Returns the number of nodes in the linked list.
        """
        current = self.head # set current to the head of the list
        count = 0
        while current: # while current is not None (the list is not empty)
            count += 1 # increment count variable
            current = current.next # move current to the next node in the list
            
        return count
    
    def display(self):
        """
        Displays the entire linked list using print.
        
        Parameters:
            No parameters.
            
        Returns:
            Nothing returned.
        """
        current = self.head
        while current: # traverses through the list, printing each node as it is visited
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def iter(self):
        """
        Iterates through the linked list.
        
        Parameters:
            No parameters.
            
        Yields:
            Any: The elements of the linked list, one at a time.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def subset(self, start, end):
        """
        Creates a new linked list that is a subset of the current linked list
        from the specified start index (inclusive) to the specified end index (exclusive).

        Parameters:
            start (int): The starting index of the subset.
            end (int): The ending index (exclusive) of the subset.

        Returns:
            SinglyLinkedList: A new linked list containing the subset of elements.
        """
        if start < 0 or end > self.len() or start >= end:
            raise ValueError("Invalid indices for subset")

        new_list = SinglyLinkedList()
        current = self.head
        index = 0

        while current and index < end:
            if index >= start:
                new_list.append(current.data)
            current = current.next
            index += 1

        return new_list