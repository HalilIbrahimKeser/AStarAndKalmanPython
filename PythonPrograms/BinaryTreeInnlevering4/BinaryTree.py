from PythonPrograms.BinaryTreeInnlevering4.BinaryTreeNode import BinaryTreeNode


class BinaryTree:
    def __init__(self, data=None):
        self._root = None
        if isinstance(data, BinaryTreeNode):
            self._root = data

    def findLeftMost(self, treenode):
        left = treenode.left
        if left is None:
            return treenode
        return self.findLeftMost(left)

    def findMin(self):
        return self.findLeftMost(self._root)

    def findRightMost(self, treenode):
        right = treenode.right
        if right is None:
            return treenode
        return self.findRightMost(right)

    def findMax(self):
        return self.findRightMost(self._root)

    def find(self, key, treenode=None):
        if treenode is None:
            treenode = self._root
        if treenode is None:
            return None
        elif treenode.value > key:
            if treenode.left:
                return self.find(key, treenode.left)
        elif treenode.value < key:
            if treenode.right:
                return self.find(key, treenode.right)
        elif treenode.value == key:
            return treenode
        else:
            raise KeyError("Key not found")

    def _getnodes(self, current=None, treenode=None, value=None):
        if current is not None and treenode is not None:
            return current, treenode
        if value is None:
            if treenode is None:
                raise Exception("Attempt to insert an empty space into Binary Tree")
            else:
                if treenode.value is None:
                    raise Exception("Attempt to insert an Node into Binary Tree with no key value")
        else:
            if treenode is not None:
                if treenode.value is not None:
                    raise Exception("Key inconsistency detected")
            else:
                treenode = BinaryTreeNode(value)
        if current is None:
            current = self._root
        return current, treenode

    def insert(self, current = None, treenode = None, value = None):
        if current == None:
            current = self._root
        # Checking consistency ...
        current, treenode = self._getnodes(current, treenode, value)
        if current != None:
            if treenode.value < current.value:
                treenode.level += 1
                if current.left is None:
                    current.left = treenode
                else:
                    self.insert(current.left, treenode)
            elif treenode.value > current.value:
                treenode.level += 1
                if current.right is None:
                    current.right = treenode
                else:
                    self.insert(current.right, treenode)
            else:
                if self._root == None:
                    treenode.level = 0
                    self._root = treenode
                else:
                    raise Exception("Duplicate key: " + treenode.value)
        else: # If empty tree, the first node entered is the root
            self._root = treenode
        return treenode

    def deleteMin(self):
        # if self._root.left == None:
        #    return self._deleteRoot()
        parent = self._root
        while True:
            # If a left branch exists - find the smallest item
            current = parent.left
            if current:
                if current.left is None:
                    if current.right is not None:
                        parent.left = current.right
                        return current
                    else:
                        parent.left = None
                        return current
                else:
                    parent = current
            # If no left branch exists, the root item is the smallest in the tree
            else:
                self._root = parent.right
                return self._root

    def deleteMax(self):
        # if self._root.left == None:
        #    return self._deleteRoot()
        parent = self._root
        while True:
            current = parent.right
            if current.right is None:
                if current.left is not None:
                    parent.right = current.left
                    return current
                else:
                    parent.right = None
                    return current
            else:
                parent = current

    '''       
    def delete(self, key):
        node = self.find(key)
        delnode = node
        if not node.left and not node.right:
            node = None
        elif node.right:
            temptree = BinaryTree(node.right)
            mintempnode = temptree.deleteMin()
            node.value = mintempnode.value
        elif node.left:
            node = node.left  
        return delnode
    '''

    def delete(self, key):
        #
        # Finding node ... with parent reference ...
        # Need the parent reference to update tree references
        parent = self._root
        current = parent
        while True:
            if key < current.value:
                parent = current
                current = parent.left
            elif key > current.value:
                parent = current
                current = parent.right
            elif key == current.value:
                node = current
                break
            else:
                return None
        # using a shallow copy of the original node to maintain deleted node while reassigning it
        import copy
        delnode = copy.copy(node)
        # If node has no children, we need to update the parent reference
        if not node.left and not node.right:
            if parent.left == node:
                parent.left = None
            if parent.right == node:
                parent.right = None
            if node == self._root:
                self._root = None
            node = None
        elif node.right:
            if node.right.left is None:
                node.value = node.right.value
                node.right = node.right.right
            else:
                temptree = BinaryTree(node.right)
                mintempnode = temptree.deleteMin()
                node.value = mintempnode.value
        elif node.left:
            if parent.left == node:
                parent.left = node.left
            elif parent.right == node:
                parent.right = node.left
        return delnode



