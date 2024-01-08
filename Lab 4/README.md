This Lab is very similar to the prior yet the new task is to create a Red-Black tree with all methods implemented. RB Tree methods are very similar to those of Binary Search Trees, with some added functionality. The largest concern with Red-Black Trees is that they must not violate the principles of the tree:
1. Every Node is red or black.
2. Every leaf node is black.
3. If a node is red, both its children are black.
4. Every simple path from a node to a descendant leaf contains the same number of black nodes.
This requires the addition of left and right rotate methods as well as an RB Insertion Fix-up method to fix the tree after each element is inserted and RB Deletion Fix-up to fix when elements are deleted.
