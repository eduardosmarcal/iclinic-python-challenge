from binary_tree import BinarySearchTree

class Dataset:

    def __init__(self):
        self.dataset = None

    def load(self, file):
        """
        Loads a file containing patient names
        and creates a list with this patient names.

        Parameters
        ----------
        file : str
            The file path.
        
        Returns
        -------
        list
            A list of patient names.
        """
        with open(file) as file:
            self.dataset = [line.strip() for line in file]

        return self.dataset
    
    def as_binary_search_tree(self):
        """
        Creates a binary tree from a list of patients name.

        Returns
        -------
        BinaryTree
            A binary tree of patient names.
        """
        root = self.get_root()
        bst = BinarySearchTree(root)

        for patient in self.dataset:
            bst.insert_node(patient)

        return bst
    
    def get_root(self):
        """
        Gets the patient's name that corresponds to the middle element of the ascending sorted dataset
        and removes it from the original dataset.

        Returns
        -------
        str
            A patient's name.
        """
        sorted_dataset = sorted(self.dataset)
        sorted_middle = round(len(sorted_dataset)/2)
        root_name = sorted_dataset[sorted_middle]
        
        self.dataset.remove(root_name)

        return root_name