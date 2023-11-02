from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): 
        # Returns empty BST
        self.root = None

    def is_empty(self): 
        if self.root == None:
            return True
        else:
            return False

    def search(self, key): 
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return False
        else:
            return self.search_helper(self.root, key)
    def search_helper(self, current_node, key):
        if current_node == None:
            return False
        if current_node.key == key:
            return True
        if key > current_node.key:
            return self.search_helper(current_node.right, key)
        if key < current_node.key:
            return self.search_helper(current_node.left, key)

    def insert(self, key, data=None): 
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        new_node = TreeNode(key, data)
        if self.is_empty():
            self.root = new_node
        self.insert_helper(self.root, new_node)

    def insert_helper(self, current_node, new_node):
        if current_node.key == new_node.key:
            current_node.data = new_node.data
        elif new_node.key > current_node.key:
            if current_node.right == None:
                current_node.right = new_node
            else:
                self.insert_helper(current_node.right, new_node)

        elif new_node.key < current_node.key:
            if current_node.left == None:
                current_node.left = new_node
            else:
                self.insert_helper(current_node.left, new_node)

    def find_min(self): 
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        else:
            return self.min_helper(self.root)

    def min_helper(self, current_node):
        if current_node.left == None:
            return ((current_node.key, current_node.data))
        else:
            return self.min_helper(current_node.left)

    def find_max(self): 
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        else:
            return self.max_helper(self.root)
    def max_helper(self, current_node):
        if current_node.right == None:
            return ((current_node.key, current_node.data))
        else:
            return(self.max_helper(current_node.right))
    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.is_empty():
            return None
        else:
            return self.tree_height_helper(self.root)
    def tree_height_helper(self, current_node):

        tree_height_1 = 0
        tree_height_2 = 0

        if current_node.left != None:
            tree_height_1 = 1 + self.tree_height_helper(current_node.left)
        if current_node.right != None:
            tree_height_2 = 1 + self.tree_height_helper(current_node.right)

        if tree_height_1 > tree_height_2:
            return tree_height_1
        else:
            return tree_height_2



    def inorder_list(self): 
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        inlist = []
        self.inorder_list_helper(self.root, inlist)
        return inlist
    def inorder_list_helper(self, node, inlist):
        if node == None:
            return
        else:
            self.inorder_list_helper(node.left, inlist)
            inlist.append(node.key)
            self.inorder_list_helper(node.right, inlist)

    def preorder_list(self):  
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        plist = []
        self.preorder_list_helper(self.root, plist)
        return plist
    def preorder_list_helper(self, node, plist):
        if node == None:
            return
        plist.append(node.key)
        self.preorder_list_helper(node.left, plist)
        self.preorder_list_helper(node.right, plist)

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000) # Don't change this!
        return_list = []
        if not self.is_empty():
            q.enqueue(self.root)
            while q.is_empty() == False:
                node = q.dequeue()
                return_list.append(node.key)
                if node.left != None:
                    q.enqueue(node.left)
                if node.right != None:
                    q.enqueue(node.right)
        return return_list




