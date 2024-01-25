"""
singly_linked_list.py

Contains the implementation of a singly linked list data structure.

Author: Ray Wang
Created: 12/19/2023
"""

from data_structures.common.node import Node  
        
# class to manage the linked list
class SinglyLinkedList:
    def __init__(self):
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
    
    def __len__(self):
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