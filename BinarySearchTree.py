class BSTNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @property
    def isLeaf(self):
        return not self.left and not self.right

    def insert(self, value):
        # small to the left, big to the right
        # if it's already in the tree, don't do anything
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, value):
        # Return the first matching node if you find it, none otherwise
        node = None
        if value == self.value:
            node = self
        elif value < self.value:
            if self.left:
                node = self.left.search(value)
        elif value > self.value:
            if self.right:
                node = self.right.search(value)
        return node

    def findParent(self, value):
        # Find parent node for the node with data matching the given value
        if value == self.value:
            return None
        elif value < self.value:
            if not self.left:
                return None
            elif value == self.left.value:
                return self
            else:
                return self.left.findParent(value)
        elif value > self.value:
            if not self.right:
                return None
            elif value == self.right.value:
                return self
            else:
                return self.right.findParent(value)


    # def delete(self, value):
    #     root = self.findParent(value)
    #     node = self.search(value)
    #     # if tree is JUST a leaf
    #     if value == node.value:
    #         if node.isLeaf:
    #             node == None

    #     # if only left
    #     if node.left and not node.right:
    #         parent.left = node.left
    #         node = None
    #     #if only right
    #     if node.right and not node.left:
    #         parent.right = node.right
    #         node = None


    #     node = self.search(value)
    #     if node

    def traversePreorder(self):
        # N L R
        yield self.value
        if self.left:
            for value in self.left.traversePreorder():
                yield value
        if self.right:
            self.right.traversePreorder()

    def traversePostorder(self):
        # L R N
        if self.left:
            for value in self.left.traversePostorder():
                yield value
        if self.right:
            for value in self.right.traversePostorder():
                yield value
        yield self.value

    def traverseInorder(self):
        # L N R
        if self.left:
            for value in self.left.traverseInorder():
                yield value
        yield self.value
        if self.right:
            for value in self.right.traverseInorder():
                yield value


def main():
    root = BSTNode(23)
    root.insert(14)
    root.insert(31)
    root.insert(7)
    root.insert(17)
    root.insert(9)
    # import pdb;pdb.set_trace()
    # root.traversePreorder()
    # root.traversePostorder()
    # for i in root.traverseInorder():
    #     print i
    print root.search(14).value
    print root.findParent(7).value



main()