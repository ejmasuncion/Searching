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
        self.root: TreeNode = None
        self.size: int = 0

    def create(self, node: TreeNode, size: int):
        self.root : TreeNode | None = TreeNode(node)
        self.size : int= size
  

    def insert(self, key: str, new_count: int):
        if(self.root is None): 
            print("Establishing root")
            self.root = TreeNode(K_Mer(key, 1))
            return
        self.root = self._insert_helper(self.root, key, new_count)
    
    def _insert_helper(self, node: TreeNode | None, key: str, new_count : int) -> TreeNode:
        # if (node is not None):
        #     print(f"Current Node: {node.val.sequence}")

        if (node is None ):
            self.size += 1
            print(f"Inserting new node {key}")
            print(f"------------------------")
            return TreeNode(K_Mer(key, new_count))

        print(f"Comparing {node.val.sequence} to {key}...")
        if (node.val.sequence == key):
            node.val.count += 1
            print(f"Increasing {key} to {node.val.count}")
            print(f"------------------------")

            return node
        
        if key < node.val.sequence:
            print("going left")
            node.left = self._insert_helper(node.left, key, new_count)
        elif key > node.val.sequence:
            print("going right")
            node.right = self._insert_helper(node.right, key, new_count)

        return node
    
    def search(self, key: str) -> int | None:
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: TreeNode | None, key: str) -> int | None:
        if node is None:
            return 0
        elif node.val.sequence == key:
            return node.val.count

        if key < node.val.sequence:
            return self._search_recursive(node.left, key)
        else: 
            return self._search_recursive(node.right, key)


    def inorder_traversal(self):
        nodes = []
        self._inorder(self.root, nodes)
        print(f"Inorder Traversal: ")
        for node in nodes:
            print(f"sequence: {node.sequence}: {node.count}")
    
    def _inorder(self, node, nodes):
        if node:
            self._inorder(node.left, nodes)
            nodes.append(node.val)
            self._inorder(node.right, nodes)


    def destroy(self):
        self.root = None
        self.size = 0