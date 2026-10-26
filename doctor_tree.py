
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def find_doctor(self, node, name):
        if node is None:
            return None

        if node.name == name:
            return node

        left_result = self.find_doctor(node.left, name)
        if left_result is not None:
            return left_result

        return self.find_doctor(node.right, name)

    def insert(self, parent_name, employee_name, side):
        if side not in ("left", "right"):
            print("Error: Side must be left or right.")
            return False

        if self.root is None:
            print("Error: The tree has no root doctor.")
            return False

        parent = self.find_doctor(self.root, parent_name)

        if parent is None:
            print(f"Error: Parent doctor '{parent_name}' not found.")
            return False

        if self.find_doctor(self.root, employee_name) is not None:
            print(f"Error: Doctor '{employee_name}' already exists.")
            return False

        if getattr(parent, side) is not None:
            print(f"Error: {side.upper()} side of {parent_name} is occupied.")
            return False

        setattr(parent, side, DoctorNode(employee_name))
        print(f"{employee_name} added to the {side.upper()} of {parent_name}.")
        return True

    def preorder(self, node):
        if node is None:
            return []

        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


if __name__ == "__main__":
    print("========== DOCTOR REPORTING TREE ==========")

    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    assert tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    assert tree.insert("Dr. Croft", "Dr. Phan", "left")
    assert tree.insert("Dr. Phan", "Dr. Carson", "right")
    assert tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("\nPreorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    assert tree.preorder(tree.root) == [
        "Dr. Croft", "Dr. Phan", "Dr. Morgan",
        "Dr. Carson", "Dr. Goldsmith"
    ]
    assert tree.inorder(tree.root) == [
        "Dr. Morgan", "Dr. Phan", "Dr. Carson",
        "Dr. Croft", "Dr. Goldsmith"
    ]
    assert tree.postorder(tree.root) == [
        "Dr. Morgan", "Dr. Carson", "Dr. Phan",
        "Dr. Goldsmith", "Dr. Croft"
    ]

    print("\n========== EDGE CASE TESTS ==========")

    assert not tree.insert("Dr. Unknown", "Dr. Smith", "left")
    assert not tree.insert("Dr. Croft", "Dr. Smith", "middle")
    assert not tree.insert("Dr. Croft", "Dr. Smith", "left")
    assert not tree.insert("Dr. Croft", "Dr. Phan", "right")

    assert tree.preorder(None) == []
    assert tree.inorder(None) == []
    assert tree.postorder(None) == []

    empty_tree = DoctorTree()
    assert not empty_tree.insert("Nobody", "Dr. Smith", "left")

    print("\nAll DoctorTree tests passed!")
