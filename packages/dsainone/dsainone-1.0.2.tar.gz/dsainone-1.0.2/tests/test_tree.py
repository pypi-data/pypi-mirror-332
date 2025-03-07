from dsainone.tree import AVLTree

def test_avl_insert():
    tree = AVLTree()
    root = None
    root = tree.insert(root, 10)
    root = tree.insert(root, 20)
    assert root.key == 10

test_avl_insert()
