from typing import Optional


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Returns the maximum depth of a binary tree — the number of nodes
    along the longest path from the root down to the farthest leaf.

    Recursive idea: an empty tree has depth 0. Any other node's depth
    is 1 (itself) plus whichever of its two subtrees is deeper.
    """
    # Base case: an empty subtree contributes no depth.
    if root is None:
        return 0

    # Recurse into both subtrees, then take the deeper one and add 1
    # for the current node itself.
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Returns the lowest common ancestor (LCA) of nodes p and q in a
    Binary Search Tree (BST).

    Uses the BST ordering property instead of general tree search:
      - If both p and q are smaller than the current node's value,
        the LCA must be in the left subtree.
      - If both are larger, the LCA must be in the right subtree.
      - Otherwise (one is smaller, one is larger, or one equals the
        current node), the current node is the split point — and
        therefore the LCA.
    """
    current = root

    while current:
        if p.val < current.val and q.val < current.val:
            # Both target nodes are in the left subtree — go left.
            current = current.left
        elif p.val > current.val and q.val > current.val:
            # Both target nodes are in the right subtree — go right.
            current = current.right
        else:
            # p and q split here (or one of them IS current) —
            # this is the lowest common ancestor.
            return current

    # Should not be reached if p and q are guaranteed to exist in the tree.
    return current