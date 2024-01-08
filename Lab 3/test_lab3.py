import lab3
import unittest



class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        print(t)

        #The following check is without using tree as an iterator (which uses inorder traversal)
        #So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")




class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)
        tree_success.print()

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]



        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")
        
class T6_new_insert(unittest.TestCase):
    
    def test_insert(self):
        t = lab3.Tree()
        t.insert(5)
        self.assertTrue(t.contains(5))
        self.assertEqual(t.root.data, 5)

        t.insert(3)
        self.assertTrue(t.contains(3))
        self.assertEqual(t.root.left.data, 3)

        t.insert(7)
        self.assertTrue(t.contains(7))
        self.assertEqual(t.root.right.data, 7)
        
class T7_new_traverse(unittest.TestCase):
    
    def test_traversal(self):
        t = lab3.Tree()
        data = [5, 3, 7, 2, 4, 6, 8]
        for value in data:
            t.insert(value)

        inorder_result = list(t.inorder())
        preorder_result = list(t.preorder())
        postorder_result = list(t.postorder())

        self.assertEqual(inorder_result, [2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(preorder_result, [5, 3, 2, 4, 7, 6, 8])
        self.assertEqual(postorder_result, [2, 4, 3, 6, 8, 7, 5])
        
class T8_find_node(unittest.TestCase):
    
    def test_find_node(self):
        t = lab3.Tree()
        
        self.assertFalse(t.contains(5))

        t.insert(5)
        self.assertTrue(t.contains(5))
        self.assertIsNotNone(t._Tree__find_node(5))

        t.insert(3)
        t.insert(7)

        self.assertTrue(t.contains(3))
        self.assertIsNotNone(t._Tree__find_node(3))

        self.assertTrue(t.contains(7))
        self.assertIsNotNone(t._Tree__find_node(7))

        self.assertFalse(t.contains(10))
        self.assertIsNone(t._Tree__find_node(10))
        
class T9_contains(unittest.TestCase):
    
    def test_contains(self):
        t = lab3.Tree()
        
        self.assertFalse(t.contains(5))

        t.insert(5)
        self.assertTrue(t.contains(5))
        
class T10_find_successor(unittest.TestCase):
    
    def test_find_successor(self):
        t = lab3.Tree()
        data = [5, 3, 7, 2, 4, 6, 8]
        for value in data:
            t.insert(value)

        self.assertEqual(t.find_successor(3).data, 4)
        self.assertEqual(t.find_successor(5).data, 6)
        self.assertEqual(t.find_successor(7).data, 8)

        with self.assertRaises(KeyError):
            # Trying to find the successor of a node that doesn't exist
            t.find_successor(10)
            
class T11_delete(unittest.TestCase):
    
    def test_delete(self):
        t = lab3.Tree()
        t.insert(5)
        t.insert(3)
        t.insert(7)

        self.assertTrue(t.contains(3))
        t.delete(3)
        self.assertFalse(t.contains(3))

        self.assertTrue(t.contains(7))
        t.delete(7)
        self.assertFalse(t.contains(7))

        self.assertTrue(t.contains(5))
        t.delete(5)
        self.assertFalse(t.contains(5))
        self.assertIsNone(t.root)

        with self.assertRaises(KeyError):
            # Trying to delete a node that doesn't exist
            t.delete(10)
                
class T12_empty_tree_errors(unittest.TestCase):
    
    def test_empty(self):
        t = lab3.Tree()
        
        with self.assertRaises(KeyError):
            # Trying to delete a node that doesn't exist
            t.delete(1)
            
        with self.assertRaises(KeyError):
            # Trying to delete a node that doesn't exist
            t.find_successor(1)



if __name__ == '__main__' :
    unittest.main()