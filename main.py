class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.final = []

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Printing In-Order Tree OR NORMAL PRINT!
    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

    # Printing Pre-Order Traversal
    def print_preorder(self):
        if self.data:
            print(self.data)
            final_list.append(self.data)
            if self.left:
                self.left.print_preorder()
            if self.right:
                self.right.print_preorder()


if __name__ == "__main__":
    final_list = []
    root = Tree(27)
    root.insert(14)
    root.insert(10)
    root.insert(19)
    root.insert(35)
    root.insert(31)
    root.insert(42)

    # root.print()
    print(root.print_preorder())
    print(final_list)