from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def bfs(root):
    if root is None:
        return

    queue = []

    queue.append(root)

    while(len(queue) > 0):
        item = queue[0]
        print(item.data, end=" ")

        # Pop the first element in the queue (element at back of queue)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

# Inorder without recursion, using stack
def inorder2(root):
    stack = []
    current = root

    while (True):
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            item = stack.pop()
            print(item.data, end=" ")
            current = item.right
        else:
            break
    print()

# Construct binary tree given post_order and in_order
#
# Last value in post_order is the root
# Find index of root in in_order.  Left of root is left-subtree
# Right of root is right-subtree

# Function to search for root value in in_order
def search(arr, start, end, value):
    i = 0
    for i in range(start, end+1):
        if(arr[i] == value):
            break
    return i

def buildTree(In, Post, n):
    postIndex = [n - 1]
    return buildUtil(In, Post, 0, n - 1, postIndex)

def buildUtil(In, Post, inStart, inEnd, postIndex):
    if (inStart > inEnd):
        return None

    # Pick current node from Postorder traversal
    # using postIndex and decrement postIndex
    node = Node(Post[postIndex[0]])
    postIndex[0] -= 1

    # If this node has no children
    # then return
    if (inStart == inEnd):
        return node

    rootIndex = search(In, inStart, inEnd, node.data)

    # Using index in Inorder traversal
    # Construct right (first) and then left subtrees
    node.right = buildUtil(In, Post, rootIndex+1, inEnd, postIndex)
    node.left = buildUtil(In, Post, inStart, rootIndex-1, postIndex)
    return node

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    print("Pre-order traversal: ")
    preorder(root)
    print("", end="\n")
    print("In-order traversal: ")
    inorder(root)
    print("", end="\n")
    print("Post-order traversal: ")
    postorder(root)
    print("", end="\n")
    print("Breadth First Traversal: ")
    bfs(root)
    print("", end="\n")
    print("Inorder without recursion: ")
    inorder2(root)
    print("", end="\n")
    print("="*60, end="\n")

    inTraversal = [4, 8, 2, 5, 1, 6, 3, 7]
    postTraversal = [8, 4, 5, 2, 6, 7, 3, 1]
    n = len(inTraversal)
    root = buildTree(inTraversal, postTraversal, n)
    print(f"Inorder traversal: {inTraversal}")
    print(f"Post Order traversal: {postTraversal}")
    print("Inorder Traversal of the newly constructed tree: ")
    inorder(root)
    print("", end="\n")
    print("Post order Traversal of the newly constructed tree: ")
    postorder(root)
    print("", end="\n")


