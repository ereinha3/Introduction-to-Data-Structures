import lab1
import unittest

class T0_TestingEnqueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")

class T1_TestingStack(unittest.TestCase):

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")


class T2_TestingPalindrome(unittest.TestCase):

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

class T3_TestingDequeue(unittest.TestCase):

    def test_basic_dequeue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        d1 = q.dequeue()
        d2 = q.dequeue()

        self.assertEqual(d1, 1)
        self.assertEqual(d2, 2)
        print("\n")
        
class T4_TestingPop(unittest.TestCase):

    def test_basic_pop(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Stack()
        q.push(1)
        q.push(2)
        q.push(3)
        q.push(4)
        p1 = q.pop()
        p2 = q.pop()

        self.assertEqual(p1, 4)
        self.assertEqual(p2, 3)
        print("\n")
        
class T5_Test1(unittest.TestCase):

    def test1(self):
        # testing the basic enqueue operation
        print("\n")
        s_arr = [["Hello", False], ["ni t I N", True], ["&$(^^)$&", False], ["My gym", True], ["12TENET12", False], ["63488436", True]]
        for ele in s_arr:
            self.assertEqual(lab1.isPalindrome(ele[0]), ele[1])
        print("\n")
        
class T6_EC_test(unittest.TestCase):

    def test1(self):
        # testing the basic enqueue operation
        print("\n")
        s_arr = [["Hello", False], ["ni t I N", True], ["&$(^^)$&", False], ["My gym", True], ["12TENET12", False], ["63488436", True]]
        for ele in s_arr:
            print("the sting being tested is ", ele[0])
            self.assertEqual(lab1.isPalindromeEC(ele[0]), ele[1])
        print("\n")
        
class T7_TSQ(unittest.TestCase):
    def test_enqueue(self):
        print("\n")
        q = lab1.TwoStackQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual('[1, 2, 3, 4]', str(q))
        d1 = q.dequeue()
        d2 = q.dequeue()

        self.assertEqual(d1, 1)
        self.assertEqual(d2, 2)
        print("\n")
        
        

if __name__ == '__main__':
    unittest.main()
