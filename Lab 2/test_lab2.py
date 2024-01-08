import unittest
import pqueue
import mheap

class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(3)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")

    def test_1_pq_peek_empty(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(3)
        self.assertEqual(pq.peek(), None)
        print("\n")


class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(3)
        pq.insert(1)
        pq.insert(14)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 14)
        print("\n")

class T3_max_heap_build(unittest.TestCase):
    # Test Case: Check that build_heap() properly builds a max heap

    def test_1_max_heap_build(self):
        max_heap = mheap.max_heap(3)
        max_heap.build_heap()
        max_heap.insert(1)
        # print(max_heap.get_heap())
        max_heap.insert(4)
        max_heap.insert(2)
        self.assertEqual(max_heap.get_heap(), [4, 1, 2])

class T4_max_heap_full_insert(unittest.TestCase):
    # Test Case: Check that an IndexError is raised when inserting to a full heap

    def test_1_max_heap_full_insert(self):
        max_heap = mheap.max_heap(3)
        max_heap.insert(1)
        max_heap.insert(2)
        max_heap.insert(3)
        with self.assertRaises(IndexError):
            max_heap.insert(4)

class T5_heap_sort(unittest.TestCase):
    # Test Case: Check that a KeyError is raised when extract_max() is called on an empty heap

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [5, 3, 17, 10, 84, 19, 6, 22, 9]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 5, 6, 9, 10, 17, 19, 22, 84])
        print("\n")

class T6_pqueue_object_validity(unittest.TestCase):
    # Test Case: Check that an object of pqueue is still a valid maximum heap
    # after calling insert() and extract max() on the same pqueue object.

    def test_1_pqueue_object_validity(self):
        pq = pqueue.pqueue(3)
        pq.insert(1)
        pq.insert(3)
        pq.insert(2)
        pq.extract_max()
        pq.insert(4)
        self.assertEqual(pq.get_pqueue(), [4, 1, 2])

class T7_max_heap_sort(unittest.TestCase):
    # Test Case: Check the heap_sort function on an unsorted list

    def test_1_max_heap_sort(self):
        to_sort_list = [10, 24, 3, 57, 4, 67, 37, 87, 7]
        sorted_list = mheap.heap_sort(to_sort_list)
        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])

class T8_pqueue_empty_is_empty(unittest.TestCase):
    # Test Case: Check if a newly created priority queue is empty

    def test_1_pqueue_empty_is_empty(self):
        pq = pqueue.pqueue(5)
        self.assertTrue(pq.is_empty())

class T9_pqueue_not_empty_is_empty(unittest.TestCase):
    # Test Case: Check if a priority queue is not empty after inserting elements

    def test_1_pqueue_not_empty_is_empty(self):
        pq = pqueue.pqueue(5)
        pq.insert(1)
        self.assertFalse(pq.is_empty())

class T10_pqueue_insert_max(unittest.TestCase):
    # Test Case: Check if inserting a maximum element results in it being at the top

    def test_1_pqueue_insert_max(self):
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(5)
        pq.insert(2)
        self.assertEqual(pq.peek(), 5)

class T11_pqueue_insert_multiple_max(unittest.TestCase):
    # Test Case: Check if inserting multiple maximum elements results in them being at the top

    def test_1_pqueue_insert_multiple_max(self):
        pq = pqueue.pqueue(5)
        pq.insert(5)
        pq.insert(5)
        pq.insert(5)
        self.assertEqual(pq.peek(), 5)

class T12_pqueue_extract_all(unittest.TestCase):
    # Test Case: Check if extracting all elements from the priority queue results in an empty queue

    def test_1_pqueue_extract_all(self):
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        self.assertTrue(pq.is_empty())

    
    
if __name__ == '__main__':
    unittest.main()