# Binary Tree Lab — Depth and Ancestors

Implements two classic binary tree algorithms in `binary_tree_lab.py`.

## Problems

### 1. Maximum Depth

`max_depth(root: Optional[TreeNode]) -> int`

Returns the number of nodes along the longest path from the root down to
the farthest leaf.

**Approach:** Recursive. An empty subtree (`None`) has depth 0. Any other
node's depth is `1 + max(depth of left subtree, depth of right subtree)` —
the node itself, plus whichever side goes deeper.

### 2. Lowest Common Ancestor (BST)

`lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode`

Returns the deepest node that has both `p` and `q` as descendants (a node
counts as its own descendant).

**Approach:** Iterative, using the BST ordering property rather than a
general tree search. Starting at the root:
- If both `p` and `q` are smaller than the current node's value, the LCA
  must be further down the left subtree.
- If both are larger, the LCA must be further down the right subtree.
- Otherwise — one is smaller and one is larger (or one equals the current
  node) — the current node is where `p` and `q`'s paths split, making it
  the LCA.

This is faster than a general LCA algorithm (O(h) where h is tree height,
vs. searching the whole tree) because it takes advantage of BST ordering
to know which direction to go without checking both subtrees.

## Running the Tests

```bash
python binary_tree_tests.py
```

All test cases (balanced tree, left-skewed tree, single node, empty tree
for `max_depth`; standard case, deep nodes, and one-node-is-ancestor for
`lowest_common_ancestor`) pass.