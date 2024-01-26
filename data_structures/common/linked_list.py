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
    def is_empty(self) -> bool:
        """
        Checks if the list is empty.
        
        Parameters:
            No parameters.
            
        Returns:
            bool: True if the list is empty, False if not empty.
        """
        pass
    
    @abstractmethod
    def append(self, data) -> None:
        """
        Appends a new node with the provided data at the end of the list.
        
        Parameters:
            data: The data to be stored in the node.
            
        Returns:
            Nothing returned.
        """
        pass
    
    @abstractmethod
    def prepend(self, data) -> None:
        """
        Prepends a new node with the provided data at the front of the list.
        
        Parameters:
            data: The data to be stored in the node.
            
        Returns:
            Nothing returned.
        """
        pass
    
    @abstractmethod
    def delete(self, data) -> Optional[Node]:
        """
        Removes the first occurrence of a node with the specified data in the list.
        
        Parameters:
            data: The data to be deleted from the list.
        
        Returns:
            Optional[Node]: Returns the deleted node if it is found in the list, None otherwise.
        """
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the length of the linked list
        
        Parameters:
            No parameters.
            
        Returns:
            count: Returns the number of nodes in the linked list.
        """
        pass
    
    @abstractmethod
    def display(self) -> None:
        """
        Displays the entire linked list using print.
        
        Parameters:
            No parameters.
            
        Returns:
            Nothing returned.
        """
        pass