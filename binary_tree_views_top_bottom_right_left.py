from queue import Queue


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.position = 0


def get_level_hash_map(root_node):
    """
    creates a hash map in which
    key is the tree level and
    value is the corresponding nodes in that level
    :param root_node:
    :return: dict
    """
    level = 0
    hash_map = {level: [root_node.value]}
    nodes_queue = Queue()
    nodes_queue.put(root_node)

    while nodes_queue.qsize():

        node = nodes_queue.get()
        # if node is None:
        #     continue

        # parent_level = node.position
        child_level = node.position + 1

        for child in [node.left, node.right]:
            if child is None:
                continue
            child.position = child_level
            if child_level in hash_map:
                hash_map[child_level].append(child.value)
            else:
                hash_map[child_level] = [child.value]
            nodes_queue.put(child)

    return hash_map


def get_horizontal_distance_hash_map(root_node):
    """
    creates a hash map in which
    key is the horizontal distance and
    value is the corresponding nodes in that distance
    :param root_node:
    :return: dict
    """
    distance = 0
    hash_map = {distance: [root_node.value]}
    nodes_queue = Queue()
    nodes_queue.put(root_node)

    while nodes_queue.qsize():

        node = nodes_queue.get()
        # if node is None:
        #     continue

        parent_distance = node.position

        if node.left:
            left_child = node.left
            left_distance = parent_distance - 1
            left_child.position = left_distance
            if left_distance in hash_map:
                hash_map[left_distance].append(left_child.value)
            else:
                hash_map[left_distance] = [left_child.value]
            nodes_queue.put(left_child)

        if node.right:
            right_child = node.right
            right_distance = parent_distance + 1
            right_child.position = right_distance
            if right_distance in hash_map:
                hash_map[right_distance].append(right_child.value)
            else:
                hash_map[right_distance] = [right_child.value]
            nodes_queue.put(right_child)

    return hash_map


def top_view(root_node):
    hash_map = get_horizontal_distance_hash_map(root_node)
    return [hash_map[key][0] for key in sorted(hash_map.keys())]


def bottom_view(root_node):
    hash_map = get_horizontal_distance_hash_map(root_node)
    return [hash_map[key][-1] for key in sorted(hash_map.keys())]


def left_view(root_node):
    hash_map = get_level_hash_map(root_node)
    return [hash_map[key][0] for key in sorted(hash_map.keys())]


def right_view(root_node):
    hash_map = get_level_hash_map(root_node)
    return [hash_map[key][-1] for key in sorted(hash_map.keys())]


if __name__ == "__main__":
    """ Create following Binary Tree  
             1  
            / \  
            2  3  
             \  
               4  
             /  \  
            5     6  
                  \  
                   7 
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.left = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    print(f"Top view:\n{top_view(root)}\n"
          f"Bottom view:\n{bottom_view(root)}\n\n"
          f"Left View:\n{left_view(root)}\n"
          f"Right View:\n{right_view(root)}\n")


# OUTPUT :
# ==================
#
# Top view:
# [2, 1, 3, 7]
# Bottom view:
# [5, 4, 6, 7]
#
# Left View:
# [1, 2, 4, 5, 7]
# Right View:
# [1, 3, 4, 6, 7]

