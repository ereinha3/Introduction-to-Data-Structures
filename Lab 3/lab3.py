from unittest.mock import NonCallableMagicMock


class Node(object):
    def __init__(self, data=None):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """
    This class represents the standard implementation of a binary search tree.

    Attributes
    -----------------------
        root - the root of the binary tree

    Methods
    -----------------------
        print - prints data of nodes in order, low->high
        insert - takes in an integer data value and creates and inserts a node with that data value
        min - returns the minimum value of the tree
        max - returns the maximum value of the tree
        contains - returns a boolean corresponding to whether that node is in the tree
        inorder - executes an in-order traversal
        preorder - executes a pre-order traversal
        postorder - executes a post-order traversal
        find_successor - finds the successor node of the given data input
        delete - deletes the node corresponding to the inputed data from the tree
    Errors Raised
    -----------------------
        KeyError - raised if find_successor or delete are called on an empty tree
    """
    # Binary Search Tree
    # class constants
    # Correspond to a number that will be inputted to dictate traversal type
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        """Initialize a binary tree.

        root: root of the tree"""
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        '''
        Prints elements from lowest data value to highest starting at a given node
        curr_node = starting node for printing order
        '''
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        """Insert an element into the tree.

        data = number corresponding to where the newly created node should be placed within the tree"""
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        node = self.root
        curr = None
        # Iterate until leaf node is found where new_node should be inserted left or right
        while node != None:
            curr = node
            if data < node.data:
                node = node.left
            else:
                node = node.right
        new_node = Node(data)
        new_node.parent = curr
        # Insert new node by setting parents child to be this node and this nodes parent to the leaf
        if curr == None:
            self.root = new_node
        elif data > curr.data:
            curr.right = new_node
        else:
            curr.left = new_node

    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        if self.isEmpty():
            return None
        return self.__min(self.root).data
    
    def __min(self, node):
        '''
        Returns the minimum of the subtree with the given node as the root
        node = root node of subtree'''
        while node.left != None:
            node = node.left
        return node
        

    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.isEmpty():
            return None
        return self.__max(self.root).data
                    
    def __max(self, node):
        '''
        Returns the maximum of the subtree with the given node as the root
        node = root node of subtree'''
        while node.right != None:
            node = node.right
        return node

    def __find_node(self, data):
        '''
        Iteratoes over the tree to return the node whose data value is equal to the inputted data value
        data = data value searched for in the tree'''
        # returns the node with that particular data value else returns None
        if self.isEmpty():
            return None
        # Going down the tree in accordance to relative values of node.data until match is found
        else:
            curr = self.root
            while curr != None and curr.data != data:
                if data < curr.data:
                    curr = curr.left
                else:
                    curr = curr.right
        # If no match is found curr will be done, else it will be the node
        return curr

    def contains(self, data):
        '''
        Looks throughout the tree to see if a node exists whose data value equals the inputted data value.
        data = data value searched for in the tree'''
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        return self.__find_node(data) != None

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        
        #Yield data of the correct node/s
        if curr_node != None:
            if traversal_type == Tree.PREORDER:
                yield curr_node.data
            for data in self.__traverse(curr_node.left, traversal_type):
                yield data
            if traversal_type == Tree.INORDER:
                yield curr_node.data
            for data in self.__traverse(curr_node.right, traversal_type):
                yield data
            if traversal_type == Tree.POSTORDER:
                yield curr_node.data

    def find_successor(self, data):
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None
        # KeyErrors raised if empty tree or node is not found in tree
        node = self.__find_node(data)
        if node == None:
            raise KeyError
        else:
            # If there is a right node, find the minimum of the right childs subtree
            if node.right != None:
                return self.__min(node.right)
            # Otherwise, keep looking at parents until a parent is found whose child is a left child
            else:
                parent = node.parent
                while parent!=None and node==parent.right:
                    node = parent
                    parent = parent.parent
                return parent

    def transplant(self, u, v):
        '''
        Helper function to swap values as needed by delete
        Used from textbook
        '''
        # Swaps the parents of two nodes so that u can be deleted
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
            
    def isEmpty(self):
        #Function to check if the tree is empty
        return self.root == None



    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None
        # KeyError raised on empty tree or node not found
        if self.isEmpty():
            raise KeyError
        node = self.__find_node(data)
        if node == None:
            raise KeyError
        # This is all from the book
        # In the case that no children exist, it will try to swap the node with its right child
        if node.left == None:
            self.transplant(node, node.right)
        # If only left child exists or prior swap fails, swap with left child
        elif node.right == None:
            self.transplant(node, node.left)
        # Otherwise, keep iterating over until the successor is the nodes right child and then swap the two and all corresponding attributes to delete the node
        else:
            y = self.__min(node.right)
            if y != node.right:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y


