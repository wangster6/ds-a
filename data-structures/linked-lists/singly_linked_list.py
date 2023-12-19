"""
singly_linked_list.py

Contains the implementation of a sinlgy linked list data structure.

Author: Ray Wang
Created: 12/19/2023
"""

# class to represent a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
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
        if self.head is None:
            return None # returns None if the list is empty
        
        current = self.head
        if current.data == data: # checks if the head node of the linked list contains the specified data and should be removed
            deleted = current
            self.head = current.next
            return deleted
        
        while current.next: # traverse through the linked list until we reach the last node
            if current.next.data == data: # check if the node after the current one contains the specified data and should be removed
                deleted = current.next
                current.next = current.next.next # set the current node's next pointer to point towards the node two places after the current node
                return deleted
            current = current.next
        
        return None # returns None if no node with the specified data is found
    
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