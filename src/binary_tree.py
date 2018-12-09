class BinarySearchTree:
    
    def __init__(self, value):
        """
        Parameters
        ----------
        value : str
            The data of the node.
        """
        self.value = value
        self.left_child, self.right_child = None, None
    
    def insert_node(self, value):
        """
        Adds a new node to the tree according the rules:
        
        1. Is the new node value greater or smaller than the current node?
        
        2. If the value of the new node is greater than the current node, go to the right subtree.
           If the current node doesn’t have a right child, insert it there, or else backtrack to step #1.
        
        3. If the value of the new node is smaller than or equal to the current node, go to the left subtree.
           If the current node doesn’t have a left child, insert it there, or else backtrack to step #1.
        
        Parameters
        ----------
        value : str
            The value to be inserted in the node.
        """
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)
    
    def find_node(self, value):
        """
        Searches for a value in the tree according the rules:

        1. We start with the root node as our current node.
           Is the given value smaller than the current node value?
           If yes, then we will search for it on the left subtree.
        
        2. Is the given value greater than the current node value?
           If yes, then we will search for it on the right subtree.
        
        3. If rules #1 and #2 are both false,
           we can compare the current node value and the given value if they are equal.
        
        Parameters
        ----------
        value : str
            The value to be searched in the tree.
        
        Returns
        -------
        bool
            True if found, False otherwise.
        """
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value
    
    def find_nodes(self, value):
        """
        Searches for all values in the tree
        that matches with the given value (full or partial name).

        Parameters
        ----------
        value : str
            The value (full or partial) to be searched in the tree.
        
        Returns
        -------
        tuple
            - A list of patient's name.
            - The length of that list.
        """
        patients = []
        limit = len(value)

        def find(node):
            if node is None:
                return None
            
            if node.value[:limit] == value:
                if value in patients:
                    return None
                patients.append(node.value)
                find(node.left_child)
                find(node.right_child)
            if node.value[:limit] > value:
                find(node.left_child)
            if node.value[:limit] < value:
                find(node.right_child)
        
        find(self)

        return patients, len(patients)