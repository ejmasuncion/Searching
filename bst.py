from typing import List

class K_Mer:
    def __init__(self, sequence="", count= 0):
        self.sequence: str = sequence 
        self.count: int = count

class TreeNode:
    def __init__(self, val = K_Mer(), left=None, right = None):
        self.val: K_Mer= val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class BST:
    def __init__(self ):
        root: TreeNode
        size: int

    def create(self):
        self.root : TreeNode | None = TreeNode()
        self.size : int= 0
    
    # def search(self, node: TreeNode):
    #     if(self.root.val.sequence == node.val.sequence):
    #         return self.root.val.count
    #     # if(self.root.left == None or self.root.right == None): 
    #     if(self.root.left == None and self.root.right == None): 
    #         return 0
        
    #     if(self.root.val.sequence < node.val.sequence): 
    #         self.search(node.left)
    #     else: self.search(node.right)
        
        # else: self.node.right.insert(node)

    def insert(self, key: str, new_count: int):
        self.root = self._insert_helper(self.root, key, new_count)
    
    def _insert_helper(self, node: TreeNode | None, key: str, new_count : int) -> TreeNode:

        if node is None:
            self.size += 1
            return TreeNode(K_Mer(key, new_count))
        
        if key < node.val.sequence:
            node.left = self._insert_helper(node.left, key, new_count)
        elif key > node.val.sequence:
            node.right = self._insert_helper(node.right, key, new_count)

        return node
    
    def search(self, key: str) -> TreeNode | None:
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: TreeNode | None, key: str) -> TreeNode | None:
        if node is None:
            return 0

        if node.val.sequence == key:
            return node.val.count

        if key < node.val.sequence:
            return self._search_recursive(node.left, key)
        else: 
            return self._search_recursive(node.right, key)



    def destroy(self):
        self.root = None