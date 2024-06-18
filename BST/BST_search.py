class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def BST_search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return BST_search(root.right, key)
    return BST_search(root.left, key)

def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    key = 6
    result = BST_search(root, key)
    if result:
        print(f"Key {key} is found in the BST")
    else:
        print(f"Key {key} is not found in the BST")

if __name__ == "__main__":
    main()