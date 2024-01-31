"""
linked_list.py

Interface that contains the methods that all linked list implementations must implement.

Author: Ray Wang
Created: 1/26/2024
"""

from abc import ABC, abstractmethod

class LinkedList(ABC):
    """
    Class: LinkedList
    The abstract base class for a linked list data structure.
    """
    
    @abstractmethod
    def __init__(self):
        """
        Initializes a new LinkedList instance.
        
        Parameters:
            No parameters.
            
        Returns:
            Nothing returned.
        """
        pass
    
    @abstractmethod
    def is_empty(self):
        """
        Checks if the list is empty.
        
        Parameters:
            No parameters.
            
        Returns:
            bool: True if the list is empty, False if not empty.
        """
        pass
    
    @abstractmethod
    def append(self, data):
        """
        Appends a new node with the provided data at the end of the list.
        
        Parameters:
            data: The data to be stored in the node.
            
        Returns:
            Nothing returned.
        """
        pass
    
    @abstractmethod
    def prepend(self, data):
        """
        Prepends a new node with the provided data at the front of the list.
        
        Parameters:
            data: The data to be stored in the node.
            
        Returns:
            Nothing returned.
        """
        pass
    
    @abstractmethod
    def delete(self, data):
        """
        Removes the first occurrence of a node with the specified data in the list.
        
        Parameters:
            data: The data to be deleted from the list.
        
        Returns:
            None: None is returned if the list is empty or if no node is found with the specified data.
            deleted: Returns the deleted node if it is found in the list.
        """
        pass
    
    @abstractmethod
    def len(self):
        """
        Returns the length of the linked list
        
        Parameters:
            No parameters.
            
        Returns:
            count: Returns the number of nodes in the linked list.
        """
        pass
    
    @abstractmethod
    def display(self):
        """
        Displays the entire linked list using print.
        
        Parameters:
            No parameters.
            
        Yields:
            Any: The elements of the linked list, one at a time.
        """
        pass
    
    @abstractmethod
    def iter(self):
        """
        Returns an iterator for the linked list.
        
        Parameters:
            No parameters.
            
        Returns:
            Nothing returned.
        """
        pass
    
    @abstractmethod
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
        pass