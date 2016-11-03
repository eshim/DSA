class BSTNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @property
    def isLeaf(self):
        return not self.left and not self.right

    @property
    def height(self):
        if self.isLeaf:
            return 0
        else:
            left_height = self.left.height + 1 if self.left else 0
            right_height = self.right.height + 1 if self.right else 0
            return max([left_height, right_height])



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


    def delete(self, value):
        parent = self.findParent(value)
        node = self.search(value)

        if not node:
            return False

        # if tree is a leaf
        if value == node.value:
            if parent:
                    choice = 'left' if node.value < parent.value else 'right'
            if node.isLeaf:
                if not parent: # if it's the only value in tree
                    node = None
                else:
                    setattr(parent, choice, None)
            else:

                # if only left
                if node.left and not node.right:
                    setattr(parent, choice, node.left)
                    node = None
                #if only right
                elif node.right and not node.left:
                    setattr(parent, choice, node.right)
                    node = None
                # if both children exist
                else:
                    largest_value = node.left
                    while largest_value.right:
                        # find largest value in left subtree
                        largest_value = largest_value.right
                    # set the parent's right pointo of larget_value to None
                    self.findParent(largest_value.value).right = None
                    node.value = largest_value.value
        return True


    def traversePreorder(self):
        # N L R
        yield self.value
        if self.left:
            for value in self.left.traversePreorder():
                yield value
        if self.right:
            for value in self.right.traversePreorder():
                yield value

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
    for i in root.traversePreorder():
        print i

    root.delete(9)
    root.delete(17)
    root.delete(31)
    root.delete(7)
    root.delete(14)
    print '\n'
    for i in root.traversePreorder():
        print i

    print root.height
    # x = root.search(14)
    # y = x.right.value
    # print x.right.value
    # y = 30
    # print x.right.value
    # print root.findParent(7).value




main()