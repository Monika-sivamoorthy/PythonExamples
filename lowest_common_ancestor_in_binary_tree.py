class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lowest_common_ancestor(node, element1, element2):
    if node is None:
        return None

    if node.value in [element1, element2]:
        return node.value

    left_lca = lowest_common_ancestor(node.left, element1, element2)
    right_lca = lowest_common_ancestor(node.right, element1, element2)

    if left_lca and right_lca:
        return node.value

    return left_lca if left_lca else right_lca


if __name__ == "__main__":
    """
    Input tree
           1
        /     \
       2        3
     /   \     /  \
    4     5   6    7
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    lca = lowest_common_ancestor(root, 3, 6)
    print(f"Method 1 : \n{lca}\n")

    # Method 2: Constructing binary tree from given input array
    # Note: This works only for complete or full binary tree
    input_arr = [1, 2, 3, 4, 5, 6, 7]
    node_hash = {}
    len_arr = len(input_arr)
    tree = len_arr // 2 - 1
    for index in range(len_arr - 1, -1, -1):
        if index > tree:
            node_hash[index] = Node(input_arr[index])
        else:
            node_hash[index] = Node(input_arr[index], node_hash[2 * index + 1], node_hash[2 * index + 2])
    lca = lowest_common_ancestor(node_hash[0], 3, 6)
    print(f"Method 2 : \n{lca}\n")


# OUTPUT:
# ==================
#
# Method 1 :
# 3
#
# Method 2 :
# 3
