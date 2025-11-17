class TreeNode:
    def __init__(self, val=0, left=None, right = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class BST:
    def __init__(self ):
        root: TreeNode
        size: int

    def create(self):
        self.root : TreeNode | None = None
        self.size : int= 0
        # print("New tree created")

    
    def search(self, node: TreeNode):
        if(self.root.val == node.val):
            return True
        if(self.root.left == None or self.root.right == None): 
            return False
        
        if(self.root.val < node.val): 
            self.search(node.left)
        else: self.search(node.right)
        
        # else: self.node.right.insert(node)

    def insert(self, key: int):
        self.root = self._insert_helper(self.root, key)
    
    def _insert_helper(self, node: TreeNode | None, key: int) -> TreeNode:

        if node is None:
            self.size += 1
            return TreeNode(key)
        
        if key < node.val:
            node.left = self._insert_helper(node.left, key)
        elif key > node.val:
            node.right = self._insert_helper(node.right, key)

        return node
    
    def search(self, key: int) -> TreeNode | None:
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: TreeNode | None, key: int) -> TreeNode | None:
        if node is None or node.val == key:
            return node

        if key < node.val:
            return self._search_recursive(node.left, key)
        else: 
            return self._search_recursive(node.right, key)



    def destroy(self):
        self.root = None